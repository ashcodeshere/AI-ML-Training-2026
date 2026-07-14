import streamlit as st
import joblib

from components.sidebar import render_sidebar
from components.input_form import render_input_form
from components.prediction_card import render_prediction_card
from components.gauge import render_gauge
from components.radar_chart import render_radar_chart
from components.score_cards import (
    calculate_scores,
    render_score_cards
)

from utils.theme import LIGHT, DARK
from utils.styles import load_css


# =====================================================
# Page Configuration
# =====================================================

st.set_page_config(
    page_title="Student Placement Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)



# =====================================================
# Sidebar + Theme
# =====================================================

dark_mode = render_sidebar()

theme = DARK if dark_mode else LIGHT


st.markdown(
    load_css(theme),
    unsafe_allow_html=True
)



# =====================================================
# Load ML Model
# =====================================================

@st.cache_resource
def load_model():
    from pathlib import Path
    try:
        BaseDir=Path(__file__).parent
        model_path=BaseDir/"placement_model.pkl"
        model = joblib.load(model_path)

        return model

    except Exception as e:
        st.error(
            "❌ Unable to load trained model."
        )
        st.exception(e)

        st.stop()



model = load_model()



# =====================================================
# Header
# =====================================================

st.markdown(
    """
    <div class="big-title">
    🎓 Student Placement Predictor
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <div class="sub-title">
    AI-powered student placement probability analysis
    </div>
    """,
    unsafe_allow_html=True
)



st.write("")



# =====================================================
# Top Dashboard Cards
# =====================================================

col1,col2,col3 = st.columns(3)


with col1:

    st.markdown(
        """
        <div class="card">

        ### 📚 Academic Analysis

        CGPA

        Attendance

        Academic Performance

        </div>
        """,
        unsafe_allow_html=True
    )



with col2:

    st.markdown(
        """
        <div class="card">

        ### 💻 Technical Skills

        Coding

        Communication

        Aptitude

        </div>
        """,
        unsafe_allow_html=True
    )



with col3:

    st.markdown(
        """
        <div class="card">

        ### 🚀 Career Profile

        Projects

        Internships

        Certifications

        </div>
        """,
        unsafe_allow_html=True
    )



st.divider()



# =====================================================
# Input Section
# =====================================================

st.subheader(
    "📝 Student Information"
)


input_data = render_input_form()



st.write("")



# =====================================================
# Prediction Button
# =====================================================

predict_button = st.button(
    "🚀 Predict Placement",
    use_container_width=True
)



if predict_button:


    with st.spinner(
        "Analyzing student profile..."
    ):

        placed_index = list(model.classes_).index(1)

        probability = model.predict_proba(
            input_data
        )[0][placed_index]


    st.divider()



    # ---------------------------------------------
    # Prediction + Gauge
    # ---------------------------------------------

    st.subheader(
        "🎯 Prediction Result"
    )


    result_col1,result_col2 = st.columns(
        [1,1]
    )


    with result_col1:

        render_prediction_card(
            probability
        )


    with result_col2:

        render_gauge(
            probability,
            dark_mode
        )



    st.divider()



    # ---------------------------------------------
    # Score Cards
    # ---------------------------------------------

    st.subheader(
        "📈 Student Profile Overview"
    )


    academic_score, skill_score, experience_score = calculate_scores(

        cgpa=input_data["cgpa"][0],

        tenth_percentage=input_data["tenth_percentage"][0],

        twelfth_percentage=input_data["twelfth_percentage"][0],

        coding=input_data["coding_skill_rating"][0],

        communication=input_data["communication_skill_rating"][0],

        aptitude=input_data["aptitude_skill_rating"][0],

        projects=input_data["projects_completed"][0],

        internships=input_data["internships_completed"][0],

        certifications=input_data["certifications_count"][0],

        hackathons=input_data["hackathons_participated"][0]

    )


    render_score_cards(

        academic_score,

        skill_score,

        experience_score

    )



    st.divider()



    # ---------------------------------------------
    # Radar Chart
    # ---------------------------------------------

    st.subheader(
        "🕸️ Skill Profile Analysis"
    )


    render_radar_chart(

        coding=input_data["coding_skill_rating"][0],

        communication=input_data["communication_skill_rating"][0],

        aptitude=input_data["aptitude_skill_rating"][0],

        projects=input_data["projects_completed"][0],

        internships=input_data["internships_completed"][0],

        certifications=input_data["certifications_count"][0],

        dark_mode=dark_mode

    )



# =====================================================
# Footer
# =====================================================

st.divider()


st.caption(
    """
    Built with Python • Streamlit • Scikit-Learn • Plotly
    
    Built by Anshul Ahluwalia
    
    Student Placement Predictor v2.0
    """
)



# Download Report in pdf/word