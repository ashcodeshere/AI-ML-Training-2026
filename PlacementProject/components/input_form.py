import streamlit as st
import pandas as pd


def render_input_form():


    st.markdown(
        """
        <div class="card">

        ## 📊 Academic Performance

        </div>
        """,
        unsafe_allow_html=True
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        cgpa = st.slider(
            "📈 CGPA",
            min_value=0.0,
            max_value=10.0,
            value=8.0,
            step=0.01
        )


    with col2:

        tenth_percentage = st.slider(
            "📚 10th Percentage",
            min_value=0.0,
            max_value=100.0,
            value=75.0,
            step=0.1
        )


    with col3:

        twelfth_percentage = st.slider(
            "📚 12th Percentage",
            min_value=0.0,
            max_value=100.0,
            value=75.0,
            step=0.1
        )


    col4, col5, col6 = st.columns(3)


    with col4:

        backlogs = st.number_input(
            "⚠️ Backlogs",
            min_value=0,
            max_value=20,
            value=0
        )


    with col5:

        study_hours = st.slider(
            "📖 Study Hours / Day",
            0.0,
            15.0,
            4.0,
            0.1
        )


    with col6:

        attendance = st.slider(
            "🕒 Attendance %",
            0.0,
            100.0,
            75.0,
            0.1
        )



    sleep_hours = st.slider(
        "😴 Sleep Hours",
        0.0,
        12.0,
        7.0,
        0.1
    )



    st.divider()



    # -------------------------------
    # Skills Section
    # -------------------------------


    st.markdown(
        """
        <div class="card">

        ## 💻 Skills & Experience

        </div>
        """,
        unsafe_allow_html=True
    )


    col1,col2,col3 = st.columns(3)


    with col1:

        coding_skill = st.slider(
            "💻 Coding Skill",
            1,
            5,
            3
        )


    with col2:

        communication_skill = st.slider(
            "🗣 Communication Skill",
            1,
            5,
            3
        )


    with col3:

        aptitude_skill = st.slider(
            "🧠 Aptitude Skill",
            1,
            5,
            3
        )


    col4,col5,col6 = st.columns(3)


    with col4:

        projects = st.number_input(
            "🚀 Projects Completed",
            0,
            20,
            2
        )


    with col5:

        internships = st.number_input(
            "💼 Internships Completed",
            0,
            10,
            1
        )


    with col6:

        hackathons = st.number_input(
            "🏆 Hackathons Participated",
            0,
            20,
            0
        )


    certifications = st.number_input(
        "📜 Certifications Count",
        0,
        20,
        2
    )



    stress_level = st.slider(
        "😰 Stress Level",
        1,
        10,
        5
    )



    st.divider()



    # -------------------------------
    # Background Section
    # -------------------------------


    st.markdown(
        """
        <div class="card">

        ## 🌍 Background Information

        </div>
        """,
        unsafe_allow_html=True
    )


    col1,col2,col3 = st.columns(3)


    with col1:

        gender = st.selectbox(
            "👤 Gender",
            [
                "Female",
                "Male"
            ]
        )


    with col2:

        branch = st.selectbox(
            "🏫 Branch",
            [
                "CE",
                "CSE",
                "ECE",
                "IT",
                "ME"
            ]
        )


    with col3:

        part_time_job = st.selectbox(
            "🧑‍💼 Part Time Job",
            [
                "No",
                "Yes"
            ]
        )



    col4,col5,col6 = st.columns(3)


    with col4:

        family_income = st.selectbox(
            "💰 Family Income",
            [
                "Low",
                "Medium",
                "High"
            ]
        )


    with col5:

        city_tier = st.selectbox(
            "🏙 City Tier",
            [
                "Tier 1",
                "Tier 2",
                "Tier 3"
            ]
        )


    with col6:

        internet_access = st.selectbox(
            "🌐 Internet Access",
            [
                "No",
                "Yes"
            ]
        )


    extracurricular = st.selectbox(
        "🎯 Extracurricular Involvement",
        [
            "Low",
            "Medium",
            "High"
        ]
    )


    st.write("")


    return pd.DataFrame({

        "gender":[gender],

        "branch":[branch],

        "cgpa":[cgpa],

        "tenth_percentage":[tenth_percentage],

        "twelfth_percentage":[twelfth_percentage],

        "backlogs":[backlogs],

        "study_hours_per_day":[study_hours],

        "attendance_percentage":[attendance],

        "projects_completed":[projects],

        "internships_completed":[internships],

        "coding_skill_rating":[coding_skill],

        "communication_skill_rating":[communication_skill],

        "aptitude_skill_rating":[aptitude_skill],

        "hackathons_participated":[hackathons],

        "certifications_count":[certifications],

        "sleep_hours":[sleep_hours],

        "stress_level":[stress_level],

        "part_time_job":[part_time_job],

        "family_income_level":[family_income],

        "city_tier":[city_tier],

        "internet_access":[internet_access],

        "extracurricular_involvement":[extracurricular]

    })