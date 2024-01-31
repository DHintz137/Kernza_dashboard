def Flax(number):
    return f"{'rgba(188, 155, 27, '}{number}{')'}"

def Olive(number):
    return f"{'rgba(106, 133, 29, '}{number}{')'}"

def Aqua(number):
    return f"{'rgba(65, 196, 209, '}{number}{')'}"

def Red(number):
    return f"{'rgba(214, 83, 58, '}{number}{')'}"

def Purple(number):
    return f"{'rgba(88, 90, 223, '}{number}{')'}"

import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.graph_objects as go


# Initialize Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.Div([
        html.Div([
            html.Label('Clean Conversion Loss:', style={'fontSize': 18, 'marginRight': '10px'}),
            dcc.Slider(
                id='scale_a_slider',
                min=0,
                max=0.9,
                step=0.1,
                value=0.2,
                marks={i: {'label': str(i), 'style': {'fontSize': 18}} for i in range(0, 2)},
            ),
            html.Div(id='scale_a_value', style={'fontSize': 18, 'marginTop': '10px'})
        ], style={'padding': '10px', 'width': '50%', 'display': 'inline-block'}),
        html.Div([
            html.Label('De-Hulling Conversion Loss:', style={'fontSize': 18, 'marginRight': '10px'}),
            dcc.Slider(
                id='scale_b_slider',
                min=0,
                max=0.9,
                step=0.1,
                value=0.2,
                marks={i: {'label': str(i), 'style': {'fontSize': 18}} for i in range(0, 2)},
            ),
            html.Div(id='scale_b_value', style={'fontSize': 18, 'marginTop': '10px'})
        ], style={'padding': '10px', 'width': '50%', 'display': 'inline-block'})
    ]),
    dcc.Graph(id='sunburst_chart', style={'height': '90vh'})
], style={'height': '100vh', 'display': 'flex', 'flexDirection': 'column'})

# Callback to update Sunburst chart and slider values
@app.callback(
    [Output('sunburst_chart', 'figure'),
     Output('scale_a_value', 'children'),
     Output('scale_b_value', 'children')],
    [Input('scale_a_slider', 'value'),
     Input('scale_b_slider', 'value')]
)

def update_content(DH_Loss, CL_Loss):
    DH_mult = (1-DH_Loss)
    DH_CL_mult = (1-DH_Loss) * (1-CL_Loss)
    # Update Sunburst chart
    ###########################################
    ## 2023 ##
    #tier4 = # * conversion
    yr23_CV_CL_H = 159600 * DH_mult
    yr23_CV_CL_D = 18000
    yr23_CV_UL_H = 177510 * DH_CL_mult
    yr23_OG_UL_H = 66000 * DH_CL_mult
    yr23_OG_CL_NS = 700
    yr23_OG_US_NS = 3000
    yr23_TR_UL_H = 23075 * DH_CL_mult
    yr23_TR_US_NS = 9800
    yr23_ROC_US_NS = 20000
    yr23_ROC_CL_NS = 8000
    yr23_US_UL_H = 14900 * DH_CL_mult
    yr23_US_US = 50
    #tier 3 = tier 4s
    yr23_CV_CL = yr23_CV_CL_H + yr23_CV_CL_D 
    yr23_CV_UL = yr23_CV_UL_H
    yr23_OG_UL = yr23_OG_UL_H
    yr23_OG_CL = yr23_OG_CL_NS
    yr23_OG_US = yr23_OG_US_NS
    yr23_TR_UL = yr23_TR_UL_H
    yr23_TR_US = yr23_TR_US_NS
    yr23_ROC_US = yr23_ROC_US_NS
    yr23_ROC_CL = yr23_ROC_CL_NS
    yr23_US_UL = yr23_US_UL_H
    yr23_US_US = yr23_US_US
    # tier 2
    yr23_CV = yr23_CV_CL + yr23_CV_UL
    yr23_OG = yr23_OG_UL + yr23_OG_CL + yr23_OG_US
    yr23_TR = yr23_TR_UL + yr23_TR_US
    yr23_ROC = yr23_ROC_US + yr23_ROC_CL
    yr23_US = yr23_US_UL + yr23_US_US
    # tier 1
    yr23 = yr23_CV + yr23_OG + yr23_TR + yr23_ROC + yr23_US 
    ###########################################
    ## 2022 ##
    #tier 4 * loss conversion
    yr22_CV_CL_H = 107327 * DH_mult
    yr22_CV_CL_D = 88000 
    yr22_CV_UL_H = 39800 * DH_CL_mult
    yr22_CV_US_H = 1500 * DH_mult
    yr22_CV_US_NS = 1300
    yr22_OG_UL_H = 68800 * DH_CL_mult
    yr22_OG_US_NS = 17000
    yr22_OG_CL_H = 3700 * DH_mult
    yr22_ROC_UL_H = 24000 * DH_CL_mult
    yr22_US_UL_H = 10000 * DH_CL_mult
    #tier 3
    yr22_CV_CL = yr22_CV_CL_H + yr22_CV_CL_D #conventional
    yr22_CV_UL = yr22_CV_UL_H 
    yr22_CV_US = yr22_CV_US_H + yr22_CV_US_NS
    yr22_OG_UL = yr22_OG_UL_H #organic
    yr22_OG_US = yr22_OG_US_NS
    yr22_OG_CL = yr22_OG_CL_H
    yr22_ROC_UL = yr22_ROC_UL_H #ROC
    yr22_US_UL = yr22_US_UL_H #unspecified
    # tier 2
    yr22_CV = yr22_CV_CL + yr22_CV_UL + yr22_CV_US
    yr22_OG = yr22_OG_UL + yr22_OG_US + yr22_OG_CL
    yr22_ROC = yr22_ROC_UL
    yr22_US = yr22_US_UL
    # tier 1
    yr22 = yr22_CV + yr22_OG + yr22_ROC + yr22_US 
    ###########################################
    ## 2021 ##
    #tier 4 * loss conversion
    yr21_CV_CL_H = 1600 * DH_mult
    yr21_CV_CL_D = 33000
    yr21_CV_UL_H = 22730 * DH_CL_mult
    yr21_OG_UL_H = 40000 * DH_CL_mult
    yr21_OG_CL_H = 4000 * DH_CL_mult
    #tier 3
    yr21_CV_CL = yr21_CV_CL_H + yr21_CV_CL_D #conventional
    yr21_CV_UL = yr21_CV_UL_H
    yr21_OG_UL = yr21_OG_UL_H
    yr21_OG_CL = yr21_OG_CL_H
    # tier 2
    yr21_CV = yr21_CV_CL + yr21_CV_UL
    yr21_OG = yr21_OG_UL + yr21_OG_CL
    # tier 1
    yr21 = yr21_CV + yr21_OG
    ###########################################
    ## 2020 ##
    #tier 4 * loss conversion
    yr20_OG_UL_H = 3750 * DH_CL_mult
    #tier 3
    yr20_OG_UL = yr20_OG_UL_H
    # tier 2
    yr20_OG = yr20_OG_UL
    # tier 1
    yr20 = yr20_OG
    ###########################################
    ## 2019 ##
    #tier 4 * loss conversion
    yr19_OG_UL_H = 8750 * DH_CL_mult
    #tier 3
    yr19_OG_UL = yr19_OG_UL_H
    # tier 2
    yr19_OG = yr19_OG_UL
    # tier 1
    yr19 = yr19_OG
    ###########################################
    ## TOTAL ##
    yr_Total = yr19 + yr20 + yr21 + yr22 + yr23 
    ##############################################

    fig = go.Figure(
    go.Sunburst(   #   |-Total-||----------------2023------------2023---------2023--------------2023------------2023---------2023------------2023------------2023------------2023---------2023------------2023-----------2023------------2023---------2023------------2023-----------2023------------2023---------2023----------------2023------------2023---------2023--------------2023---------2023-------------2023---------2023---------2023-------------2023---------2023------------2023------------2023----------2023------------2023----------2023------2023----------2023------2023----------2023------2023----------2023------2023----------2023------2023----------2023---------2023----------2023---------2023----------2023---------2023-----| |-----------2022---------------2022--------------2022--------------2022--------------2022--------------2022------------2022-------------2022-------------2022-------------2022-------------2022------------2022-----------2022-----------2022-----------2022----------2022-----------2022-----------2022-------------2022-----------2022-----------2022-----------2022--------2022-----------2022-------2022----------2022-------2022----------2022-------2022----------2022-------2022----------2022-------2022------------2022----------2022-------2022------------2022----------2022------------2022----------2022-------------2022----------2022-------------2022----------2022-------------2022----------2022-------------2022----------2022-------------2022----------2022-------------2022----------2022-------------2022----------2022-------------2022----------2022-------------2022----------2022-------------2022----------2022-------------2022----------2022-------------2022----------2022-------------2022----------2022-------------2022----------2022-------------2022----------2022--------------|  |-----------2021---------2021--------2021--------2021--------2021--------2021--------2021--------2021--------2021--------2021--------2021--------2021--------2021--------2021--------2021--------2021--------2021--------2021--------2021--------2021--------2021--------2021--------2021-------------2021-------------2021-------------2021-------------2021-------------2021-------------2021-------------2021-------------2021-------------2021-------------2021-------------2021-------------2021-------------2021-------------2021-------------2021-------------2021-------------2021-------------2021-------------2021-------------2021-------------2021-------------2021-------------2021-------------2021-------------2021----| |---2020------2020-----2020-----2020-----2020-----2020-----2020-----2020-----2020-----2020-----2020-----2020-----2020-||--2019-----2019-----2019-----2019-----2019-----2019-----2019-----2019-----2019-----2019-----2019-----2019-----2019-----2019-|
        labels=       [  "Total",   "2023",   "Conventional",     "Organic",     "Transitional",        "ROC",      "Unspecified",              "Clean",        "Unclean",      "Unclean\u200B",  "Unspecified\u200B",       "Clean\u200B",             "Unclean\u200B\u200B",          "Unspecified\u200B\u200B",     "Unspecified\u200B\u200B\u200B",          "Clean\u200B\u200B",                 "Unclean\u200B\u200B\u200B",    "Unspecified\u200B\u200B\u200B\u200B",                            "Hulled",        "De-Hulled",        "Hulled\u200B",       "Hulled\u200B\u200B",                      "NS",       "NS\u200B",      "Hulled\u200B\u200B\u200B",              "NS\u200B\u200B",                   "NS\u200B\u200B\u200B",      "NS\u200B\u200B\u200B\u200B",        "Hulled\u200B\u200B\u200B\u200B",        "2022",   "Conventional\u200B",    "Organic\u200B",       "ROC\u200B",        "Unspecified\u200B\u200B\u200B\u200B\u200B",     "Clean\u200B\u200B\u200B",   "Unclean\u200B\u200B\u200B\u200B",      "Unspecified\u200B\u200B\u200B\u200B\u200B\u200B",      "Unclean\u200B\u200B\u200B\u200B\u200B",      "Unspecified\u200B\u200B\u200B\u200B\u200B\u200B\u200B",    "Clean\u200B\u200B\u200B\u200B",       "Unclean\u200B\u200B\u200B\u200B\u200B\u200B",    "Unclean\u200B\u200B\u200B\u200B\u200B\u200B\u200B",    "Hulled\u200B\u200B\u200B\u200B\u200B",            "De-Hulled\u200B",  "Hulled\u200B\u200B\u200B\u200B\u200B\u200B",                      "NS\u200B\u200B\u200B\u200B\u200B",    "Hulled\u200B\u200B\u200B\u200B\u200B\u200B\u200B",       "Hulled\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B",                           "NS\u200B\u200B\u200B\u200B\u200B\u200B",   "Hulled\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B",      "Hulled\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B",    "Hulled\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B",       "2021",  "Conventional\u200B\u200B",    "Organic\u200B\u200B",    "Unclean\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B",       "Clean\u200B\u200B\u200B\u200B\u200B",      "Unclean\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B",     "Clean\u200B\u200B\u200B\u200B\u200B\u200B",    "Hulled\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B",                     "De-Hulled\u200B\u200B",      "Hulled\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B",   "Hulled\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B",  "Hulled\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B",   "2020",      "Organic\u200B\u200B\u200B",   "Unclean\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B",  "Hulled\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B",   "2019",     "Organic\u200B\u200B\u200B\u200B",     "Unclean\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B",      "Hulled\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B"],
        parents=      [       "",  "Total",           "2023",        "2023",             "2023",       "2023",             "2023",       "Conventional",   "Conventional",            "Organic",            "Organic",           "Organic",                    "Transitional",                     "Transitional",                               "ROC",                        "ROC",                              "Unspecified",                            "Unspecified",                             "Clean",             "Clean",             "Unclean",            "Unclean\u200B",       "Unspecified\u200B",    "Clean\u200B",           "Unclean\u200B\u200B",      "Unspecified\u200B\u200B",         "Unspecified\u200B\u200B\u200B",               "Clean\u200B\u200B",             "Unclean\u200B\u200B\u200B",       "Total",                 "2022",             "2022",            "2022",                                             "2022",          "Conventional\u200B",                "Conventional\u200B",                                   "Conventional\u200B",                              "Organic\u200B",                                              "Organic\u200B",                    "Organic\u200B",         "Unspecified\u200B\u200B\u200B\u200B\u200B",                                            "ROC\u200B",                 "Clean\u200B\u200B\u200B",    "Clean\u200B\u200B\u200B",             "Unclean\u200B\u200B\u200B\u200B",       "Unspecified\u200B\u200B\u200B\u200B\u200B\u200B",     "Unspecified\u200B\u200B\u200B\u200B\u200B\u200B",                        "Unclean\u200B\u200B\u200B\u200B\u200B",      "Unspecified\u200B\u200B\u200B\u200B\u200B\u200B\u200B",                                  "Clean\u200B\u200B\u200B\u200B",                             "Unclean\u200B\u200B\u200B\u200B\u200B\u200B\u200B",                                 "Unclean\u200B\u200B\u200B\u200B\u200B\u200B",      "Total",                      "2021",                   "2021",                                   "Conventional\u200B\u200B",                  "Conventional\u200B\u200B",                                                "Organic\u200B\u200B",                           "Organic\u200B\u200B",                           "Unclean\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B",       "Clean\u200B\u200B\u200B\u200B\u200B",                                                       "Clean\u200B\u200B\u200B\u200B\u200B",                                "Unclean\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B",                                                         "Clean\u200B\u200B\u200B\u200B\u200B\u200B",  "Total",                           "2020",                                             "Organic\u200B\u200B\u200B",                                     "Unclean\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B",  "Total",                                "2019",                                               "Organic\u200B\u200B\u200B\u200B",                                         "Unclean\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B"],
        values=       [ yr_Total,     yr23,          yr23_CV,       yr23_OG,            yr23_TR,     yr23_ROC,            yr23_US,           yr23_CV_CL,       yr23_CV_UL,           yr23_OG_UL,          yr23_OG_US,           yr23_OG_CL,                        yr23_TR_UL,                         yr23_TR_US,                         yr23_ROC_US,                  yr23_ROC_CL,                                 yr23_US_UL,                               yr23_US_US,                        yr23_CV_CL_H,        yr23_CV_CL_D,          yr23_CV_UL_H,               yr23_OG_UL_H,             yr23_OG_US_NS,    yr23_OG_CL_NS,                   yr23_TR_UL_H,                  yr23_TR_US_NS,                           yr23_ROC_US_NS,                    yr23_ROC_CL_NS,                          yr23_US_UL_H,            yr22,                 yr22_CV,           yr22_OG,          yr22_ROC,                                            yr22_US,                    yr22_CV_CL,                          yr22_CV_UL,                                             yr22_CV_US,                                   yr22_OG_UL,                                                    yr22_OG_US,                         yr22_OG_CL,                                        yr22_US_UL ,                                             yr22_ROC_UL,                             yr22_CV_CL_H,                 yr22_CV_CL_D,                                  yr22_CV_UL_H,                                           yr22_CV_US_NS,                                          yr22_CV_US_H,                                                   yr22_OG_UL_H,                                                yr22_OG_US_NS,                                                    yr22_OG_CL_H,                                                                    yr22_ROC_UL_H,                                                                  yr22_US_UL_H,       yr21,                       yr21_CV,                  yr21_OG,                                                   yr21_CV_UL,                                  yr21_CV_CL,                                                           yr21_OG_UL,                                      yr21_OG_CL,                                                                       yr21_CV_UL_H,                                 yr21_CV_CL_D,                                                                                yr21_CV_CL_H,                                                                                   yr21_OG_UL_H,                                                                                        yr21_OG_CL_H,     yr20,                          yr20_OG,                                                              yr20_OG_UL,                                                                                              yr20_OG_UL_H,     yr19,                               yr19_OG,                                                                      yr19_OG_UL,                                                                                                        yr19_OG_UL_H],
        branchvalues="total",
        textfont_size=16,
        insidetextfont=dict(color='black'),  # Set font color for text inside segments
        outsidetextfont=dict(color='black'), # Set font color for text outside segments
        marker=dict(
            colors=[ # 69 total 
                "rgba(255, 255, 255, 1)",  # Total
                Olive(1),  
                Olive(1),  # 
                Olive(1), #3
                Olive(1),  
                Olive(1),  # 
                Olive(1),  # 6
                Olive(1),  
                Olive(1),  # 
                Olive(1), #9
                Olive(1),  
                Olive(1),  # 
                Olive(1), #12
                Olive(1),  
                Olive(1),  # 
                Olive(1), #15
                Olive(1),  
                Olive(1),  # 
                Olive(1),  #18
                Olive(1),  
                Olive(1),  # 
                Olive(1), #21
                Olive(1),  
                Olive(1),  # 
                Olive(1), #24
                Olive(1),  #25
                Olive(1),  
                Olive(1), # adjust numbering by +1 hereafter 
                Olive(1), #27
                Flax(1),  
                Flax(1), 
                Flax(1),  #30
                Flax(1),  
                Flax(1),  
                Flax(1), #33
                Flax(1),  
                Flax(1),  
                Flax(1), #36
                Flax(1),  
                Flax(1),  
                Flax(1), #39
                Flax(1),  
                Flax(1), 
                Flax(1),  #42
                Flax(1),  
                Flax(1),  
                Flax(1), #45
                Flax(1),  
                Flax(1),  
                Flax(1), #48
                Flax(1),  #49
                Flax(1),  
                Red(1),  
                Red(1), #52
                Red(1),  
                Red(1),  
                Red(1), #55
                Red(1),  
                Red(1), 
                Red(1), #58
                Red(1),  
                Red(1),  
                Red(1),  #61
                Red(1),  
                Aqua(1),  
                Aqua(1), #64
                Aqua(1),  
                Aqua(1),  
                Purple(1), #67
                Purple(1),  
                Purple(1), #69
                Purple(1)
    ],
                pattern=dict(
                    shape=[     "",        "",            "/",         "x",              ".",      "\\",              "|",               "",               "",                   "",                   "",                 "",                               "",                                  "",                               "",                       "",                                        "",                                      "",                               "",                "",                 "",                         "",                        "",              "",                "",                            "",                                "",                          "",                                      "",          "",                   "/",                 "x",              "\\",                                                  "|",                          "",                                  "",                                                   "",                                           "",                                                            "",                                 "",                                                  "",                                                      "",                                         "",                          "",                                            "",                                                       "",                                                    "",                                                            "",                                                           "",                                                                "",                                                                   "",                                                                            "",       "",                        "/",                       "x",                                                          "",                                          "",                                                                    "",                                              "",                                                                                  "",                                          "",                                                                                            "",                                                                                             "",                                                                                                  "",       "",                             "x",                                                                      "",                                                                                                         "",       "",                                "x",                                                                               "",                                                                                                                   ""], 
                    solidity=0.9
                )
            ),
        )
    )
    fig.update_layout(
        margin=dict(t=50, l=0, r=0, b=0)
    )
    # Update slider values
    scale_a_text = f"Current value: {DH_Loss}"
    scale_b_text = f"Current value: {CL_Loss}"

    return fig, scale_a_text, scale_b_text

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

#http://127.0.0.1:8050/