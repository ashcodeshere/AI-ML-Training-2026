import streamlit as st


THRESHOLD = 0.68


def get_confidence(probability):

    if probability >= 0.90:
        return "★★★★★ Very High"

    elif probability >= 0.80:
        return "★★★★ High"

    elif probability >= 0.70:
        return "★★★ Moderate"

    elif probability >= 0.60:
        return "★★ Low"

    else:
        return "★ Very Low"



def render_prediction_card(probability):

    prediction = (
        "PLACED"
        if probability >= THRESHOLD
        else
        "NOT PLACED"
    )


    confidence = get_confidence(probability)


    probability_percentage = probability * 100


    # -------------------------
    # Success Card
    # -------------------------

    if prediction == "PLACED":

        card_color = "#10B981"

        icon = "✅"

        message = """
        The student has a high probability
        of getting placed.
        """


    else:

        card_color = "#EF4444"

        icon = "❌"

        message = """
        The placement probability is below
        the required threshold.
        """



    st.markdown(
        f"""
        <div style="
        background:{card_color};
        padding:30px;
        border-radius:25px;
        color:white;
        text-align:center;
        box-shadow:0 10px 30px rgba(0,0,0,0.25);
        ">

        <h1>
        {icon} {prediction}
        </h1>


        <h3>
        Placement Probability
        </h3>


        <h1>
        {probability_percentage:.2f}%
        </h1>


        <hr>


        <h3>
        Confidence
        </h3>


        <h2>
        {confidence}
        </h2>


        <p>
        Threshold : {THRESHOLD*100:.0f}%
        </p>


        <p>
        {message}
        </p>


        </div>
        """,
        unsafe_allow_html=True
    )


    return prediction, confidence