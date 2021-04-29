import pandas as pd
from utils import _spectrum_generator
from utils import _get_scan_polarity
import uuid
import subprocess


def perform_feature_finding(filename, params, timeout=90):
    """
    Do stuff for feature finding
    """

    if params["type"] == "Test":
        return _test_feature_finding(filename)

    if params["type"] == "Trivial":
        return _trivial_feature_finding(filename)

    if params["type"] == "TidyMS":
        return _tidyms_feature_finding(filename)

    if params["type"] == "MZmine2":
        return _mzmine_feature_finding(filename, params["params"], timeout=timeout)
    
    if params["type"] == "Dinosaur":
        return _dinosaur_feature_finding(filename, timeout=timeout)

    if params["type"] == "MSQL":
        return _msql_feature_finding(filename, params["params"])
    

def _test_feature_finding(filename):
    features_df = pd.DataFrame()
    features_df["mz"] = [100]
    features_df["rt"] = [0.2]
    features_df["i"] = [1000]

    return features_df

def _trivial_feature_finding(filename):
    min_rt = 0
    max_rt = 1000000
    min_mz = 0
    max_mz = 2000

    all_mz = []
    all_i = []
    all_rt = []

    for spec in _spectrum_generator(filename, min_rt, max_rt):
        scan_polarity = _get_scan_polarity(spec)

        if spec.ms_level == 1:
            rt = spec.scan_time_in_minutes()

            try:
                # Filtering peaks by mz
                peaks = spec.reduce(mz_range=(min_mz, max_mz))

                # Sorting by intensity
                peaks = peaks[peaks[:,1].argsort()]
                peaks = peaks[-2:]

                mz, intensity = zip(*peaks)

                all_mz += list(mz)
                all_i += list(intensity)
                all_rt += len(mz) * [rt]
            except:
                pass

    features_df = pd.DataFrame()
    features_df['mz'] = all_mz
    features_df['i'] = all_i
    features_df['rt'] = all_rt

    features_df = features_df.sort_values(by=['i'])
    features_df = features_df.head(50)

    return features_df

# TODO: 
def _tidyms_feature_finding(filename):
    import tidyms as ms

    ms_data = ms.MSData(filename,
                     ms_mode="centroid",
                     instrument="orbitrap",
                     separation="uplc")
    
    roi, feature_data = ms_data.detect_features()

    print(feature_data)

    features_df = pd.DataFrame()
    features_df['mz'] = feature_data['mz']
    features_df['i'] = feature_data['area']
    features_df['rt'] = feature_data['rt'] / 60

    print(features_df)

    return features_df

# TODO: 
def _mzmine_feature_finding(filename, parameters, timeout=90):
    import xmltodict
    import os

    batch_base = "feature_finding/batch_files/Generic_Batchbase.xml"

    batch_xml = xmltodict.parse(open(batch_base).read())

    all_batch_steps = batch_xml["batch"]["batchstep"]

    ##Setting input files
    for batch_step in all_batch_steps:
        if batch_step["@method"] == "net.sf.mzmine.modules.rawdatamethods.rawdataimport.RawDataImportModule":
            #Found loading module
            batch_step["parameter"]["file"] = [os.path.abspath(filename)]

        if batch_step["@method"] == "io.github.mzmine.modules.io.rawdataimport.RawDataImportModule":
            #Found loading module
            batch_step["parameter"]["file"] = [os.path.abspath(filename)]

    output_prefix = os.path.abspath(os.path.join("temp", "feature-finding", "{}_{}".format(os.path.basename(filename), str(uuid.uuid4()).replace("-", "")  )))
    output_prefix = output_prefix.replace(".", "_")
    output_ms2_csv = output_prefix + "_quant.csv"
    output_ms2_mgf = output_prefix + ".mgf"
    filled_batch = output_prefix + "_filled_batch.xml"

    # Subsituting inputs and outputs
    batch_text = xmltodict.unparse(batch_xml, pretty=True)
    batch_text = batch_text.replace("GNPSEXPORTPREFIX", output_prefix)
    batch_text = batch_text.replace("FEATUREFINDING_PPMTOLERANCE", str(parameters["feature_finding_ppm"]))
    batch_text = batch_text.replace("FEATUREFINDING_NOISELEVEL", str(parameters["feature_finding_noise"]))
    batch_text = batch_text.replace("FEATUREFINDING_MINABSOLUTEHEIGHT", str(float(parameters["feature_finding_noise"]) * 3.0 ))
    
    batch_text = batch_text.replace("FEATUREFINDING_MINPEAKDURATION", str(parameters["feature_finding_min_peak_rt"]))
    batch_text = batch_text.replace("FEATUREFINDING_MAXPEAKDURATION", str(parameters["feature_finding_max_peak_rt"]))

    batch_text = batch_text.replace("FEATUREFINDING_RTTOLERANCE", str(parameters["feature_finding_rt_tolerance"]))
    
    with open(filled_batch, "w") as o:
        o.write(batch_text)
    
    # Figuring out how to launch MZmine via script
    mzmine_script_path = os.path.join("feature_finding/mzmine2/MZmine-2.53-Linux", "startMZmine_Linux.sh")
    if not os.path.exists(mzmine_script_path):
        mzmine_script_path = os.path.join("feature_finding/mzmine2/MZmine-2.53-Linux", "startMZmine-Linux")
        
    cmd = "export JAVA_OPTS='-Xmx4096m' && {} {}".format(mzmine_script_path, filled_batch)
    print(cmd)
    _call_feature_finding_tool(cmd, timeout=timeout)
    

    mzmine_features_df = pd.read_csv(output_ms2_csv)

    features_df = pd.DataFrame()
    features_df['mz'] = mzmine_features_df['row m/z']
    features_df['i'] = mzmine_features_df['{} Peak area'.format(os.path.basename(filename))]
    features_df['rt'] = mzmine_features_df['row retention time']

    return features_df

# TODO: 
def _openms_feature_finding(filename):
    return None


def _dinosaur_feature_finding(filename, timeout=90):
    import os

    output_folder = os.path.abspath(os.path.join("temp", "feature-finding"))
    output_filename = "{}_{}".format(os.path.basename(filename), str(uuid.uuid4()).replace("-", ""))

    dinosaur_script_path = "feature_finding/dinosaur/Dinosaur-1.2.0.free.jar"
    cmd = "java -Xmx4096m -jar {} --verbose --profiling --concurrency=8 --maxCharge=2 --nReport=0 --outName={} --outDir={} {}".format(dinosaur_script_path, output_filename, output_folder, filename)
    print(cmd)
    _call_feature_finding_tool(cmd, timeout=timeout)

    temp_features_df = pd.read_csv(os.path.join(output_folder, output_filename + ".features.tsv"), sep='\t')

    features_df = pd.DataFrame()
    features_df['mz'] = temp_features_df['mz']
    features_df['i'] = temp_features_df['intensitySum']
    features_df['rt'] = temp_features_df['rtApex']
    
    return features_df

def _msql_feature_finding(filename, params):
    msql_statement = params["msql_statement"]

    min_rt = 0
    max_rt = 1000000
    min_mz = 0
    max_mz = 2000

    all_mz = []
    all_i = []
    all_rt = []
    all_scan = []

    ms2_highlight = float(msql_statement.split("=")[-1])
    min_mz = ms2_highlight - 0.5
    max_mz = ms2_highlight + 0.5

    for spec in _spectrum_generator(filename, min_rt, max_rt):
        scan_polarity = _get_scan_polarity(spec)

        if spec.ms_level == 2:
            rt = spec.scan_time_in_minutes()
            prec_mz = spec.selected_precursors[0]["mz"]

            try:
                # Filtering peaks by mz
                peaks = spec.reduce(mz_range=(min_mz, max_mz))

                if len(peaks) > 0:
                    all_mz.append(prec_mz)
                    all_i.append(0)
                    all_rt.append(rt)
                    all_scan.append(spec.ID)
            except:
                pass

    features_df = pd.DataFrame()
    features_df['mz'] = all_mz
    features_df['i'] = all_i
    features_df['rt'] = all_rt
    features_df['scan'] = all_scan




    return features_df

def _call_feature_finding_tool(cmd, timeout=90):
    """This calls the feature finding tool but also does proper cleanup by killing all child processes

    Args:
        cmd ([type]): [description]
        timeout (int, optional): [description]. Defaults to 90.
    """

    try:
        p = subprocess.Popen([cmd], shell=True)
        p.wait(timeout=timeout)
        return 0
    except subprocess.TimeoutExpired:
        # Killing off child and all other children
        import psutil
        parent_pid = p.pid
        parent = psutil.Process(parent_pid)
        for child in parent.children(recursive=True):
            child.kill()
        parent.kill()

    return 1

