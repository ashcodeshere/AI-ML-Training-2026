import streamlit as st


def calculate_scores(
    cgpa,
    tenth_percentage,
    twelfth_percentage,
    coding,
    communication,
    aptitude,
    projects,
    internships,
    certifications,
    hackathons
):

    # Academic Score
    academic_score = (
        (cgpa / 10) * 40 +
        (tenth_percentage / 100) * 30 +
        (twelfth_percentage / 100) * 30
    )


    # Skill Score
    skill_score = (
        ((coding + communication + aptitude) / 15)
        * 100
    )


    # Experience Score
    experience_score = (
        (
            min(projects,5) / 5 * 35
            +
            min(internships,3) / 3 * 35
            +
            min(certifications,5) / 5 * 20
            +
            min(hackathons,5) / 5 * 10
        )
    )


    return (
        round(academic_score,1),
        round(skill_score,1),
        round(experience_score,1)
    )



def render_score_cards(
    academic_score,
    skill_score,
    experience_score
):


    col1,col2,col3 = st.columns(3)



    with col1:

        st.markdown(
            f"""
            <div class="card">

            <h3>📚 Academic Score</h3>

            <h1>{academic_score}%</h1>

            </div>
            """,
            unsafe_allow_html=True
        )



    with col2:

        st.markdown(
            f"""
            <div class="card">

            <h3>💻 Skill Score</h3>

            <h1>{skill_score}%</h1>

            </div>
            """,
            unsafe_allow_html=True
        )



    with col3:

        st.markdown(
            f"""
            <div class="card">

            <h3>🚀 Experience Score</h3>

            <h1>{experience_score}%</h1>

            </div>
            """,
            unsafe_allow_html=True
        )