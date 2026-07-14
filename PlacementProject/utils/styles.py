def load_css(theme):

    return f"""
<style>

/* Background */

.stApp {{
    background: {theme['bg']};
}}

/* Hide Streamlit Branding */

#MainMenu {{
    visibility:hidden;
}}

footer {{
    visibility:hidden;
}}

header {{
    visibility:hidden;
}}

/* Cards */

.card {{

background:{theme['card']};

padding:25px;

border-radius:20px;

box-shadow:
0 10px 25px rgba(0,0,0,.08);

margin-bottom:20px;

}}

/* Titles */

.big-title {{

font-size:42px;

font-weight:700;

color:{theme['primary']};

}}

.sub-title {{

font-size:18px;

color:gray;

}}

/* Metric */

.metric {{

font-size:28px;

font-weight:bold;

color:{theme['text']};

}}

</style>
"""