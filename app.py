import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Researcher Profile | Cesky Nengudza",
    page_icon="📊",
    layout="centered"
)

# Header
st.title("Cesky Fhulufhelo Nengudza")
st.subheader("Applied Mathematics • Data Analytics • Research")

st.write(
    """
    I am an applied mathematics researcher with a strong analytical background and
    a passion for transforming complex data into meaningful insights. My work
    combines mathematical theory, statistical modelling, and computational tools
    to address real-world challenges.
    """
)

st.divider()

# Research Focus
st.header("🔬 Research Focus")
st.markdown("""
- Data-driven decision making  
- Statistical modelling and inference  
- Machine learning for social and economic data  
- Numerical methods for scientific problems  
- Applied analytics with real-world datasets  
""")

# Interactive chart: Research focus areas
focus_data = pd.DataFrame({
    "Area": [
        "Data Analytics",
        "Statistical Modelling",
        "Machine Learning",
        "Numerical Methods",
        "Social Impact Analytics"
    ],
    "Emphasis Level": [5, 4, 3, 4, 5]
})

st.subheader("Research Focus Emphasis")
st.bar_chart(focus_data.set_index("Area"))

st.divider()

# Academic Background
st.header("🎓 Academic Background")
st.markdown("""
**Bachelor of Science in Applied Mathematics**  
Walter Sisulu University  

Key academic areas:
- Linear Regression and Multivariate Distributions  
- Numerical Analysis and Differential Equations  
- Time Series and Stochastic Processes  
- Machine Learning Fundamentals  
""")

st.divider()

# Research & Projects
st.header("📈 Research & Selected Work")
st.markdown("""
**Crime Data Analytics and Gender-Based Violence (GBV)**  
- Investigated the role of data analytics in understanding crime patterns  
- Applied multiple linear regression techniques to real South African datasets  
- Focused on analytical insights that support evidence-based interventions  

**Computational Mathematics Projects**
- Finite difference methods for solving partial differential equations  
- Numerical solutions to heat, Laplace, and wave equations  
""")

st.divider()

# Skills section with interactive sliders
st.header("🛠 Technical Skills (Self-Assessed)")

python_level = st.slider("Python", 0, 5, 4)
r_level = st.slider("R", 0, 5, 4)
cpp_level = st.slider("C++", 0, 5, 3)
java_level = st.slider("Java", 0, 5, 3)
stats_level = st.slider("Statistical Modelling", 0, 5, 5)

skills_df = pd.DataFrame({
    "Skill": ["Python", "R", "C++", "Java", "Statistical Modelling"],
    "Proficiency": [
        python_level,
        r_level,
        cpp_level,
        java_level,
        stats_level
    ]
})

st.subheader("Skills Proficiency Overview")
st.line_chart(skills_df.set_index("Skill"))

st.divider()

# Professional Interests
st.header("🌍 Professional Interests")
st.markdown("""
- Research in applied mathematics and data science  
- Data analytics for social impact  
- Quantitative research and modelling  
""")

st.divider()

# Contact
st.header("📬 Contact")
st.markdown("""
📧 Email: ceskyakeelah@gmail.com  
📍 South Africa  
""")

st.caption("© 2026 | Researcher Profile – Cesky F. Nengudza")
