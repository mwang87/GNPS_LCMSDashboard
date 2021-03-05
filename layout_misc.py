# Dash imports

import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output, State
import dash_daq as daq

# Plotly Imports
import plotly.express as px
import plotly.graph_objects as go

EXAMPLE_DASHBOARD = [
    dbc.CardHeader(html.H5("Example Exploration Dashboards")),
    dbc.CardBody(
        [
            html.H5("Basic Examples - LC/MS Metabolomics"),
            html.Hr(),

            html.A("LCMS Multiple m/z XIC for QC Files", href="/?usi=mzspec%3AMSV000085852%3AQC_0&xicmz=271.0315%3B278.1902%3B279.0909%3B285.0205%3B311.0805%3B314.1381&xic_tolerance=0.5&xic_norm=No&show_ms2_markers=True&ms2_identifier="),
            html.Br(),
            html.A("LCMS Side By Side Visualization", href='/?usi=mzspec%3AMSV000085852%3AQC_0&usi2=mzspec%3AMSV000085852%3AQC_1&xicmz=271.0315%3B278.1902%3B279.0909%3B285.0205%3B311.0805%3B314.1381%3B833.062397505189&xic_tolerance=0.5&xic_rt_window=&xic_norm=False&xic_file_grouping=FILE&show_ms2_markers=True&ms2_identifier=MS2%3A2277&show_lcms_2nd_map=True&map_plot_zoom=%7B"xaxis.range%5B0%5D"%3A+3.2846848333333334%2C+"xaxis.range%5B1%5D"%3A+3.5981121270270275%2C+"yaxis.range%5B0%5D"%3A+815.4334319736646%2C+"yaxis.range%5B1%5D"%3A+853.5983309206755%7D'),
            html.Br(),
            html.A("LCMS XIC by Formula - QC Amitryptiline", href='/?usi=mzspec%3AMSV000085852%3AQC_0&usi2=&xicmz=&xic_formula=C20H23N&xic_tolerance=0.01&xic_ppm_tolerance=20&xic_tolerance_unit=Da&xic_rt_window=&xic_norm=False&xic_file_grouping=FILE&xic_integration_type=AUC&show_ms2_markers=True&ms2_identifier=None&show_lcms_2nd_map=False&map_plot_zoom=%7B"autosize"%3A+true%7D&polarity_filtering=None&polarity_filtering2=None&tic_option=TIC'),
            html.Br(),
            html.A("LCMS auto zoomed by URL", href='/?xicmz=271.0315%3B278.1902%3B279.0909%3B285.0205%3B311.0805%3B314.1381&xic_formula=&xic_peptide=&xic_tolerance=0.5&xic_ppm_tolerance=10&xic_tolerance_unit=Da&xic_rt_window=&xic_norm=False&xic_file_grouping=FILE&xic_integration_type=AUC&show_ms2_markers=True&ms2_identifier=None&show_lcms_2nd_map=False&map_plot_zoom=%7B"xaxis.range%5B0%5D"%3A+3.225196497160058%2C+"xaxis.range%5B1%5D"%3A+3.4834247492797554%2C+"yaxis.range%5B0%5D"%3A+521.8432333663449%2C+"yaxis.range%5B1%5D"%3A+615.6041749343235%7D&polarity_filtering=None&polarity_filtering2=None&tic_option=TIC&overlay_usi=None&overlay_mz=row+m%2Fz&overlay_rt=row+retention+time&overlay_color=&overlay_size=&feature_finding_type=Off#{"usi":%20"mzspec:MSV000085852:QC_0",%20"usi2":%20""}'),
            html.Br(),
            html.A("LCMS auto zoomed by scan in USI", href="/?usi=mzspec:MSV000085852:QC_0:scan:2277"),
            html.Br(),
            html.Br(),

            html.H5("Various Vendor Examples - LC/MS Metabolomics"),
            html.Hr(),
            
            html.A("Thermo Q Exactive LCMS mzML", href="/?usi=mzspec%3AMSV000084951%3AAH22&xicmz=870.9543493652343&xic_tolerance=0.5&xic_norm=False&show_ms2_markers=True&ms2_identifier=None"),
            html.Br(),
            html.A("Thermo Q Exactive LCMS RAW", href="/?usi=mzspec%3AMSV000086206%3Araw/raw/S_N1.raw&xic_tolerance=0.5&xic_norm=False&show_ms2_markers=True&ms2_identifier=None"),
            html.Br(),
            html.A("Thermo Lumos LCMS RAW", href="/?usi=mzspec:MSV000086729:raw/raw/Identification/UP_Fusion_AcX_SAT_ob_pool_1_NOlist.raw"),
            html.Br(),
            html.A("Sciex LCMS", href="/?usi=mzspec%3AMSV000085042%3AQC1_pos-QC1&xicmz=&xic_tolerance=0.5&xic_norm=False&show_ms2_markers=True&ms2_identifier=None"),
            html.Br(),
            html.A("Bruker LCMS", href="/?usi=mzspec%3AMSV000086015%3AStdMix_02__GA2_01_55623&xicmz=&xic_tolerance=0.5&xic_norm=False&show_ms2_markers=True&ms2_identifier=None"),
            html.Br(),
            html.A("Bruker LCMS - PA14 rhlR", href="/?usi=mzspec:MSV000083500:ccms_peak/9177.mzML"),
            html.Br(),
            html.A("Waters LCMS", href="/?usi=mzspec%3AMSV000084977%3AOEPKS7_B_1_neg&xicmz=&xic_tolerance=0.5&xic_norm=False&show_ms2_markers=True&ms2_identifier=None"),
            html.Br(),
            html.A("Agilent LCMS", href="/?usi=mzspec:MSV000084060:KM0001"),
            html.Br(),
            html.A("Agilent LCMS CDF", href="/?usi=mzspec:MSV000086521:raw/ORSL13CM.CDF"),
            html.Br(),
            html.A("Shimadzu LCMS", href="/?usi=mzspec%3AMSV000081501%3Accms_peak%2FAA+BPM+D7+1_Seg1Ev1.mzML"),
            html.Br(),
            html.Br(),

            html.H5("Basic Examples - LC/MS Proteomics"),
            html.Hr(),

            html.A("Thermo LCMS - Orbitrap Elite - Proteomics - Pandey Draft Proteome - mzML from MassIVE", href="/?usi=mzspec:MSV000079514:Adult_CD4Tcells_bRP_Elite_28_f01"),
            html.Br(),
            html.A("Thermo LCMS - Orbitrap Velos - Proteomics - Pandey Draft Proteome - RAW from PRIDE via PX", href="/?usi=mzspec:PXD000561:Adult_Adrenalgland_bRP_Velos_1_f07.raw"),
            html.Br(),
            html.A("Thermo LCMS - Q Exactive HF - Proteomics - TMT10Plex - RAW from MassIVE via PX", href="/?usi=mzspec:PXD022935:21720-TMT-Fra-1-1.raw"),
            html.Br(),
            html.A("Thermo LCMS - Q Exactive - Proteomics - Deep Proteome - mzML from MassIVE", href='/?xicmz=&xic_formula=&xic_peptide=&xic_tolerance=0.5&xic_ppm_tolerance=10&xic_tolerance_unit=Da&xic_rt_window=&xic_norm=False&xic_file_grouping=FILE&xic_integration_type=AUC&show_ms2_markers=True&ms2_identifier=None&show_lcms_2nd_map=False&map_plot_zoom=%7B"autosize"%3A+true%7D&polarity_filtering=None&polarity_filtering2=None&tic_option=TIC&overlay_usi=mzspec%3AGNPS%3ATASK-5ecfcf81cb3c471698995b194d8246a0-f.benpullman%2F_cluster%2Ffeatures%2F29_tissues_colon_01308_H02_P013387_B00_N16_R1.tsv&overlay_mz=m%2Fz&overlay_rt=Retention+time&overlay_color=&overlay_size=&overlay_filter_column=&overlay_filter_value=&feature_finding_type=Off#%7B"usi":%20"mzspec:MSV000083508:01308_H02_P013387_B00_N16_R1%5Cn",%20"usi2":%20""%7D'),
            html.Br(),
            html.A("Thermo LCMS - Q Exactive - Proteomics - mzXML from MassIVE, imported from PRIDE", href='/?usi=mzspec:PXD002854:20150414_QEp1_LC7_GaPI_SA_Serum_DT_03_150416181741.mzXML:scan:2308:[+314.188]-QQKPGQAPR/2'),
            html.Br(),
            html.Br(),

            html.H5("Different Data Sources Examples - LC/MS Metabolomics"),
            html.Hr(),

            html.A("LCMS from Metabolights", href="/?usi=mzspec:MTBLS1124:QC07.mzML"),
            html.Br(),
            html.A("LCMS from Metabolomics Workbench that include MS/MS", href="/?usi=mzspec:ST000763:20160411_MB_CS00000074-1_P.mzXML"),
            html.Br(),
            html.A("Thermo LCMS from GNPS Analysis Classical Molecular Networking Task", href="/?usi=mzspec:GNPS:TASK-5ecfcf81cb3c471698995b194d8246a0-f.MSV000085444/ccms_peak/peak/Hui_N1_fe.mzML#%7B%7D"),
            html.Br(),
            html.Br(),

            html.H5("Basic Examples - GC/MS Metabolomics"),
            html.Hr(),

            html.A("Thermo GCMS", href="/?usi=mzspec:MSV000086150:BA1.mzML"),
            html.Br(),
            html.A("GCMS in CDF Format", href="/?usi=mzspec:GNPS:TASK-ce31b7fdd01244dbb31478147889de1e-f.aaksenov/GC_data/Sterols_data/Samples/0104006.cdf"),
            html.Br(),
            html.Br(),

            html.H5("Advanced Examples - LC/MS Metabolomics"),
            html.Hr(),

            html.A("Multiple Files to show comparison", href="/?usi=mzspec%3AMSV000085618%3Accms_peak%2FBLANK_P2-F-1_01_13263.mzML%3Ascan%3A1%0Amzspec%3AMSV000085618%3Accms_peak%2FED103_P1-D-8_01_3762.mzML%3Ascan%3A1%0Amzspec%3AMSV000085618%3Accms_peak%2FED104_P1-D-9_01_3763.mzML%3Ascan%3A1%0Amzspec%3AMSV000085618%3Accms_peak%2FED105_P1-A-1_01_3781.mzML%3Ascan%3A1%0A&usi2=mzspec%3AMSV000085618%3Accms_peak%2FED24_P1-B-2_01_2171.mzML%3Ascan%3A1%0Amzspec%3AMSV000085618%3Accms_peak%2FED25_P1-B-3_01_2172.mzML%3Ascan%3A1%0Amzspec%3AMSV000085618%3Accms_peak%2FED26_P1-B-4_01_2173.mzML%3Ascan%3A1%0Amzspec%3AMSV000085618%3Accms_peak%2FED36_P1-C-3_01_2181.mzML%3Ascan%3A1%0Amzspec%3AMSV000085618%3Accms_peak%2FED37_P1-C-4_01_2182.mzML%3Ascan%3A1%0Amzspec%3AMSV000085618%3Accms_peak%2FED38_P1-C-5_01_2183.mzML%3Ascan%3A1%0Amzspec%3AMSV000085618%3Accms_peak%2FSJ-123_P1-A-6_01_13658.mzML%3Ascan%3A1&xicmz=799.437&xic_formula=&xic_peptide=&xic_tolerance=0.5&xic_ppm_tolerance=10&xic_tolerance_unit=ppm&xic_rt_window=2.5&xic_norm=False&xic_file_grouping=MZ&xic_integration_type=AUC&show_ms2_markers=True&ms2_identifier=None&show_lcms_2nd_map=False&map_plot_zoom=%7B%22autosize%22%3A+true%7D&polarity_filtering=None&polarity_filtering2=None&tic_option=TIC"),
            html.Br(),
            html.A("LCMS with Feature Finding Overlay from FBMN", href="/?usi=mzspec:GNPS:TASK-ddd650381cef4bcfad4b068e9400c8d7-f.MSV000085444/ccms_peak/peak/Hui_N1_fe.mzML&overlay_usi=mzspec:GNPS:TASK-ddd650381cef4bcfad4b068e9400c8d7-quantification_table_reformatted/"),
            html.Br(),
            html.A("LCMS with Feature Finding Overlay from FBMN with Sizing of highlight", href="/?usi=mzspec:GNPS:TASK-bc7e7e3d61714464a6b47d247933040e-f.MSV000085444/ccms_peak/peak/Hui_N1.mzML&overlay_usi=mzspec:GNPS:TASK-bc7e7e3d61714464a6b47d247933040e-quantification_table_reformatted/&overlay_size=Hui_N1.mzML%20Peak%20area#%7B%7D"),
            html.Br(),
            html.A("LCMS with MZMine2 Feature Finding Active", href='/?usi=mzspec%3AMSV000085852%3AQC_0&usi2=&xicmz=271.0315%3B278.1902%3B279.0909%3B285.0205%3B311.0805%3B314.1381&xic_formula=&xic_peptide=&xic_tolerance=0.5&xic_ppm_tolerance=10&xic_tolerance_unit=Da&xic_rt_window=&xic_norm=False&xic_file_grouping=FILE&xic_integration_type=AUC&show_ms2_markers=True&ms2_identifier=None&show_lcms_2nd_map=False&map_plot_zoom=%7B"autosize"%3A+true%7D&polarity_filtering=None&polarity_filtering2=None&tic_option=TIC&overlay_usi=None&overlay_mz=row+m%2Fz&overlay_rt=row+retention+time&overlay_color=&overlay_size=&feature_finding_type=MZmine2'),
            html.Br(),
            html.A("LCMS with MZMine2 Feature Finding Parameters Set", href='/?xicmz=482.123497282169&xic_formula=&xic_peptide=&xic_tolerance=0.5&xic_ppm_tolerance=10&xic_tolerance_unit=ppm&xic_rt_window=&xic_norm=False&xic_file_grouping=FILE&xic_integration_type=AUC&show_ms2_markers=True&ms2_identifier=MS2%3A3065&show_lcms_2nd_map=True&map_plot_zoom=%7B"autosize"%3A+true%7D&polarity_filtering=None&polarity_filtering2=None&tic_option=TIC&overlay_usi=None&overlay_mz=row+m%2Fz&overlay_rt=row+retention+time&overlay_color=&overlay_size=&overlay_hover=&overlay_filter_column=&overlay_filter_value=&feature_finding_type=MZmine2&feature_finding_ppm=10&feature_finding_noise=100000&feature_finding_min_peak_rt=0.02&feature_finding_max_peak_rt=2&feature_finding_rt_tolerance=0.1#%7B"usi":%20"mzspec:GNPS:TASK-5844c6bea85442b0a998f4d558caa310-f.daniel/Exampel_FBMN_Nissel/mzml/S_N1.mzML%5Cnmzspec:GNPS:TASK-5844c6bea85442b0a998f4d558caa310-f.daniel/Exampel_FBMN_Nissel/mzml/S_N2.mzML%5Cnmzspec:GNPS:TASK-5844c6bea85442b0a998f4d558caa310-f.daniel/Exampel_FBMN_Nissel/mzml/S_N3.mzML",%20"usi2":%20"mzspec:GNPS:TASK-5844c6bea85442b0a998f4d558caa310-f.daniel/Exampel_FBMN_Nissel/mzml/S_P1.mzML%5Cnmzspec:GNPS:TASK-5844c6bea85442b0a998f4d558caa310-f.daniel/Exampel_FBMN_Nissel/mzml/S_P2.mzML%5Cnmzspec:GNPS:TASK-5844c6bea85442b0a998f4d558caa310-f.daniel/Exampel_FBMN_Nissel/mzml/S_P3.mzML"%7D'),

        ]
    )
]


SYCHRONIZATION_MODAL = [
    dbc.Modal(
        [
            dbc.ModalHeader("Sychronization Options"),
            dbc.ModalBody([
                dbc.Row([
                        dbc.Col(
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Session ID", addon_type="prepend"),
                                    dbc.Input(id='sychronization_session_id', placeholder="Enter Session ID", value=""),
                                ],
                                className="mb-3",
                            ),
                        ),
                    ]
                ),
                dbc.Row([
                        dbc.Col(
                            dbc.Button("Save Session", block=True, id="sychronization_save_session_button"),
                        ),
                        dbc.Col(
                            dbc.Button("Load Session", block=True, id="sychronization_load_session_button"),
                        ),
                    ]
                ),
                html.Hr(),
                html.H5("Dashboard Sychronization Type"),
                dbc.Row([
                    dbc.Col(
                        dcc.Dropdown(
                            id='synchronization_type',
                            options=[
                                {'label': 'MANUAL (Default)', 'value': 'MANUAL'},
                                {'label': 'COLLAB (Bidirectional sync)', 'value': 'COLLAB'},
                                {'label': 'LEADER', 'value': 'LEADER'},
                                {'label': 'FOLLOWER', 'value': 'FOLLOWER'},
                            ],
                            searchable=False,
                            clearable=False,
                            value="MANUAL",
                            style={
                                "width":"100%"
                            }
                        ),
                    ),
                    dbc.Col(
                        dbc.Button("Set Synchronization", block=True, id="sychronization_set_type_button"),
                    )
                ]),
                html.Hr(),
                dbc.InputGroup(
                    [
                        dbc.InputGroupAddon("Leader Session Token", addon_type="prepend"),
                        dbc.Input(id='synchronization_leader_token', placeholder="Enter Token", value=""),
                    ],
                    className="mb-3",
                ),
                dbc.Row([
                        dbc.Col(
                            dbc.Button("Get New Token", block=True, id="synchronization_leader_newtoken_button"),
                        ),
                        dbc.Col(
                            dbc.Button("Check Token", block=True, id="synchronization_leader_checktoken_button"),
                        ),
                    ]
                ),
                html.Br(),
                html.Div(id="sychronization_output1"),
                html.Div(id="sychronization_output2"),
                html.Br(),
                html.Div(id="sychronization_teaching_links"),
            ]),
            dbc.ModalFooter(
                dbc.Button("Close", id="sychronization_options_modal_close", className="ml-auto")
            ),
        ],
        id="sychronization_options_modal",
        size="xl",
    )
]



SPECTRUM_DETAILS_MODAL = [
    dbc.Modal(
        [
            dbc.ModalHeader("Spectrum Details as XML"),
            dbc.ModalBody([
                dcc.Loading(
                    id="spectrum_details_area",
                    children=[html.Div([html.Div(id="loading-output-1035")])],
                    type="default",
                ),
            ]),
            dbc.ModalFooter(
                dbc.Button("Close", id="spectrum_details_modal_close", className="ml-auto")
            ),
        ],
        id="spectrum_details_modal",
        size="xl",
    ),
]


ADVANCED_VISUALIZATION_MODAL = [
    dbc.Modal(
        [
            dbc.ModalHeader("Advanced Visualization Modal"),
            dbc.ModalBody([
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.FormGroup(
                                [
                                    dbc.Label("Heatmap Color", width=4.8, style={"width":"150px"}),
                                    dcc.Dropdown(
                                        id='map_plot_color_scale',
                                        options=[
                                            {'label': 'Hot_r', 'value': 'Hot_r'},
                                            {'label': 'Blues', 'value': 'Blues'},
                                            {'label': 'Sunsetdark', 'value': 'Sunsetdark'},
                                            {'label': 'Viridis', 'value': 'Viridis'},
                                            {'label': 'Greys', 'value': 'Greys'},
                                              
                                        ],
                                        searchable=False,
                                        clearable=False,
                                        value="Hot_r",
                                        style={
                                            "width":"60%"
                                        }
                                    )
                                ],
                                row=True,
                                className="mb-3",
                                style={"margin-left": "4px"}
                        )),
                        dbc.Col()
                    ]
                ),
                html.Hr(),

                dbc.Row([
                    dbc.Col(
                        dbc.FormGroup(
                            [
                                dbc.Label("LCMS Quantization Map Level", width=4.8, style={"width":"250px"}),
                                dcc.Dropdown(
                                    id='map_plot_quantization_level',
                                    options=[
                                        {'label': 'Low', 'value': 'Low'},
                                        {'label': 'Medium', 'value': 'Medium'},
                                        {'label': 'High', 'value': 'High'},
                                    ],
                                    searchable=False,
                                    clearable=False,
                                    value="Medium",
                                    style={
                                        "width":"60%"
                                    }
                                )  
                            ],
                            row=True,
                            className="mb-3",
                            style={"margin-left": "4px"}
                    )),
                ]),
                html.Hr(),
                dbc.Row([
                    dbc.Col(
                        dbc.InputGroup(
                            [
                                dbc.InputGroupAddon("RT Range", addon_type="prepend"),
                                dbc.Input(id='map_plot_rt_min', placeholder="Enter Min RT", value=""),
                                dbc.Input(id='map_plot_rt_max', placeholder="Enter Max RT", value=""),
                            ],
                            className="mb-3",
                            style={"margin-left": "4px"}
                    )),
                ]),
                dbc.Row([
                    dbc.Col(
                        dbc.InputGroup(
                            [
                                dbc.InputGroupAddon("m/z Range", addon_type="prepend"),
                                dbc.Input(id='map_plot_mz_min', placeholder="Enter Min m/z", value=""),
                                dbc.Input(id='map_plot_mz_max', placeholder="Enter Max m/z", value=""),
                            ],
                            className="mb-3",
                            style={"margin-left": "4px"}
                    )),
                ]),
                dbc.Button("Update Map Plot Ranges", block=True, id="map_plot_update_range_button"),
            ]),
            dbc.ModalFooter(
                dbc.Button("Close", id="advanced_visualization_modal_close", className="ml-auto")
            ),
        ],
        id="advanced_visualization_modal",
        size="lg",
    ),
]


ADVANCED_IMPORT_MODAL = [
    dbc.Modal(
        [
            dbc.ModalHeader("GNPS Dashboard Settings as JSON"),
            dbc.ModalBody([
                dbc.Row([
                    dbc.Col([
                        html.H5("Current Settings"),
                        dbc.Textarea(id="setting_json_area", className="mb-3", placeholder="JSON Settings", rows="20"),
                        dcc.Upload(
                            id='upload-settings-json',
                            children=html.Div([
                                'Paste settings or Drag and Drop file with existing settings',
                                html.A(' or Select Files')
                            ]),
                            style={
                                'width': '95%',
                                'height': '60px',
                                'lineHeight': '60px',
                                'borderWidth': '1px',
                                'borderStyle': 'dashed',
                                'borderRadius': '5px',
                                'textAlign': 'center',
                                'margin': '10px'
                            },
                            multiple=False
                        ),
                        html.Br(),
                        dbc.Button("Import These JSON Settings", block=True, id="advanced_import_update_button"),
                        html.Br(),
                        html.A(
                            dbc.Button("Download Settings as File", block=True),
                            id="advanced_import_download_button",
                            target="_blank",
                            href="/settingsdownload"
                        ),
                    ]),
                    dbc.Col([
                        html.H5("Settings History"),
                        dbc.Textarea(id="setting_json_area_history", className="mb-3", placeholder="JSON History Settings", rows="20"),
                        html.Br(),
                        html.A(
                            dbc.Button("Link to Analysis History Replay", block=True),
                            id="advanced_import_history_link",
                            target="_blank",
                            href="/"
                        ),
                    ])
                ]),
            ]),
            dbc.ModalFooter(
                dbc.Button("Close", id="advanced_import_modal_close", className="ml-auto")
            ),
        ],
        id="advanced_import_modal",
        size="xl",
    ),
]

ADVANCED_REPLAY_MODAL = [
    dbc.Modal(
        [
            dbc.ModalHeader("GNPS Dashboard Replay"),
            dbc.ModalBody([
                dbc.Row([
                    dbc.Col([
                        html.H5("Previous Replay JSON"),
                        dbc.Textarea(id="replay_json_area_previous", className="mb-3", placeholder="Replay JSON Settings", rows="20"),
                        html.Div(id="replay_summary")
                    ]),
                    dbc.Col([
                        html.H5("Next Replay JSON"),
                        dbc.Textarea(id="replay_json_area", className="mb-3", placeholder="Replay JSON Settings", rows="20"),
                        html.A(
                            dbc.Button("Link to this Replay", block=True),
                            id="advanced_import_replay_link",
                            target="_blank",
                            href="/"
                        ),
                    ])
                ])
            ]),
            dbc.ModalFooter(
                dbc.Button("Close", id="advanced_replay_modal_close", className="ml-auto")
            ),
        ],
        id="advanced_replay_modal",
        size="xl",
    ),
]