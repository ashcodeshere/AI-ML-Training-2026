import streamlit as st


def render_sidebar():

    # -----------------------------
    # Header
    # -----------------------------
    st.sidebar.title("🎓 Placement Predictor")

    st.sidebar.caption(
        "AI Powered Student Placement Analytics"
    )


    # -----------------------------
    # Theme Selector
    # -----------------------------
    st.sidebar.subheader("🎨 Appearance")

    theme_choice = st.sidebar.selectbox(
        "Select Theme",
        ["Light", "Dark"]
    )

    dark_mode = theme_choice == "Dark"


    st.sidebar.divider()


    # -----------------------------
    # Model Performance
    # -----------------------------
    st.sidebar.subheader(
        "📊 Model Performance"
    )


    col1, col2 = st.sidebar.columns(2)


    with col1:
        st.metric(
            label="Accuracy",
            value="88.6%"
        )


    with col2:
        st.metric(
            label="ROC-AUC",
            value="91.1%"
        )


    st.sidebar.metric(
        label="Decision Threshold",
        value="0.68"
    )


    st.sidebar.divider()


    # -----------------------------
    # Model Configuration
    # -----------------------------
    st.sidebar.subheader(
        "⚙️ Model Configuration"
    )


    st.sidebar.write(
        "**Algorithm**"
    )

    st.sidebar.code(
        "Logistic Regression"
    )


    st.sidebar.write(
        "**GridSearchCV Best Parameters**"
    )


    st.sidebar.json(
        {
            "C": 10,
            "penalty": "l2",
            "solver": "liblinear",
            "class_weight": "None"
        }
    )


    st.sidebar.divider()


    # -----------------------------
    # Features Used
    # -----------------------------
    st.sidebar.subheader(
        "🧠 Prediction Features"
    )


    features = [
        "📚 Academic Performance",
        "💻 Technical Skills",
        "🚀 Projects & Internships",
        "🏆 Certifications & Hackathons",
        "🌍 Background Information"
    ]


    for feature in features:
        st.sidebar.write(feature)


    st.sidebar.divider()


    # -----------------------------
    # Technology Stack
    # -----------------------------
    st.sidebar.subheader(
        "🛠 Technology Stack"
    )


    st.sidebar.write(
        """
        🐍 Python

        🎈 Streamlit

        🤖 Scikit-Learn

        📊 Plotly

        💾 Joblib
        """
    )


    st.sidebar.divider()


    # -----------------------------
    # About Section
    # -----------------------------
    st.sidebar.info(
        """
This dashboard predicts student placement probability using a trained Logistic Regression model.

The model uses preprocessing pipelines, feature scaling, encoding, and optimized hyperparameters.
"""
    )


    # -----------------------------
    # Footer
    # -----------------------------
    st.sidebar.caption(
        "🚀 Placement Predictor v2.0"
    )


    return dark_mode