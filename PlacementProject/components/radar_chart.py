import plotly.graph_objects as go
import streamlit as st


def render_radar_chart(
    coding,
    communication,
    aptitude,
    projects,
    internships,
    certifications,
    dark_mode=False
):

    categories = [
        "Coding",
        "Communication",
        "Aptitude",
        "Projects",
        "Internships",
        "Certifications"
    ]


    values = [
        coding,
        communication,
        aptitude,
        projects,
        internships,
        certifications
    ]


    # Normalize experience values
    # because projects/internships/certifications
    # have different scales

    normalized_values = [

        coding,

        communication,

        aptitude,

        min(projects,5),

        min(internships,5),

        min(certifications,5)

    ]


    # close radar loop

    normalized_values.append(
        normalized_values[0]
    )

    categories.append(
        categories[0]
    )



    text_color = (
        "#F8FAFC"
        if dark_mode
        else
        "#1F2937"
    )



    fig = go.Figure()



    fig.add_trace(

        go.Scatterpolar(

            r=normalized_values,

            theta=categories,

            fill="toself",

            name="Student Profile",

            line=dict(
                color="#2563EB",
                width=3
            ),

            fillcolor="rgba(37,99,235,0.35)"

        )

    )



    fig.update_layout(

        polar=dict(

            bgcolor="rgba(0,0,0,0)",


            radialaxis=dict(

                visible=True,

                range=[0,5],

                color=text_color

            ),


            angularaxis=dict(

                color=text_color

            )

        ),


        showlegend=False,


        title={

            "text":"🕸️ Skill Profile",

            "x":0.5,

            "font":{

                "size":22,

                "color":text_color

            }

        },


        height=450,


        margin=dict(

            l=50,

            r=50,

            t=80,

            b=40

        ),


        paper_bgcolor="rgba(0,0,0,0)"

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )