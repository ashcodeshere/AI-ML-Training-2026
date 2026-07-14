import plotly.graph_objects as go
import streamlit as st



def render_gauge(probability,dark_mode=False):

    percentage = probability * 100


    fig = go.Figure(
        go.Indicator(

            mode="gauge+number",

            value=percentage,

            number={
                "suffix":"%",
                "font":{
                    "size":40
                }
            },

            title={
                "text":"Placement Probability",
                "font":{
                    "size":24
                }
            },


            gauge={

                "axis":{
                    "range":[0,100]
                },


                "bar":{
                    "color":"#10B981"
                },


                "steps":[

                    {
                        "range":[0,50],
                        "color":"#FEE2E2"
                    },


                    {
                        "range":[50,68],
                        "color":"#FEF3C7"
                    },


                    {
                        "range":[68,100],
                        "color":"#D1FAE5"
                    }

                ],


                "threshold":{

                    "line":{
                        "color":"red",
                        "width":4
                    },

                    "value":68

                }

            }
        )
    )



    fig.update_layout(

        height=350,

        margin=dict(
            l=20,
            r=20,
            t=70,
            b=20
        ),


        paper_bgcolor="rgba(0,0,0,0)",

        font={
            "color": "white" if dark_mode else "#1F2937"
        }

    )



    st.plotly_chart(
        fig,
        use_container_width=True
    )