import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Jay Shahapurakar | AI Engineer", page_icon="🚀", layout="wide")

# --- ASSETS & ANIMATIONS ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load animations
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie_ai = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_26ewjioz.json")
lottie_contact = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_u25cckyh.json")

# --- CSS STYLING ---
st.markdown("""
<style>
    .main-header {font-size: 2.5rem; color: #4CAF50;}
    .sub-header {font-size: 1.5rem; color: #555;}
    .card {background-color: #f9f9f9; padding: 20px; border-radius: 10px; margin-bottom: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4140/4140048.png", width=100)
    st.title("Jay Shahapurakar")
    st.write("AI Engineer | Data Scientist")
    
    selected = st.radio(
        "Navigate to:",
        ["Home", "About Me", "Projects", "Experience", "Education", "Contact"],
        index=0
    )
    
    st.markdown("---")
    st.write("📍 Belgaum, Karnataka")
    
    # Resume Download
    try:
        with open("resume.pdf", "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
        st.download_button(
            label="📄 Download CV",
            data=pdf_bytes,
            file_name="Jay_Shahapurakar_Resume.pdf",
            mime="application/pdf"
        )
    except FileNotFoundError:
        pass # Handle gracefully if file not found

# --- PAGE: HOME ---
if selected == "Home":
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h1 class='main-header'>Hi, I'm Jay! 👋</h1>", unsafe_allow_html=True)
        st.write("### AI Engineer & Data Scientist")
        st.write(
            """
            I build scalable ML pipelines and solve real-world problems with predictive modeling.
            Currently bridging the gap between complex data and actionable insights at **GTechnoHubb Solutions**.
            """
        )
        st.write("🚀 **Specialized in:** Python, Deep Learning (CNN/LSTM), and Full-Stack AI Deployment.")
    with col2:
        st_lottie(lottie_coding, height=300, key="coding")

# --- PAGE: ABOUT ME ---
if selected == "About Me":
    st.header("🧠 About Me & Skills")
    st.write("I am a Data Scientist skilled in analytical thinking, machine learning, and end-to-end model development.")
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Languages & Core")
        st.markdown("Example of my core stack:")
        st.code("import pandas as pd\nimport numpy as np\n# Python & SQL Expert", language="python")
        
    with col2:
        st.subheader("ML & Deep Learning")
        st.markdown("Libraries I use daily:")
        st.code("import tensorflow as tf\nfrom sklearn import svm\n# OpenCV, Keras, SBERT", language="python")

    with col3:
        st.subheader("Deployment & Tools")
        st.markdown("How I ship code:")
        st.code("$ git push origin main\n# Docker, Flask, AWS", language="bash")

# --- PAGE: PROJECTS ---
if selected == "Projects":
    st.header("💻 Featured Projects")
    st.write("Here are some of the impactful projects I've built.")
    
    # Project 1
    with st.container():
        col_text, col_viz = st.columns([2, 1])
        with col_text:
            st.subheader("1. AI ATS Resume Scanner")
            st.write("**Tech Stack:** Django, SBERT, SpaCy, PDFPlumber")
            st.write("""
            Built a full-stack system that uses semantic matching to score resumes against job descriptions.
            - ✅ Weighted ATS scoring and automated PDF reports.
            - ✅ Solved the 'keyword stuffing' problem using semantic embeddings.
            """)
            st.markdown("[View Code >](#)")
        with col_viz:
            st.info("Impact: Automated hiring workflows.")
            
    st.markdown("---")

    # Project 2
    with st.container():
        col_text, col_viz = st.columns([2, 1])
        with col_text:
            st.subheader("2. Anomaly Detection System (CCTV)")
            st.write("**Tech Stack:** CNN + LSTM, OpenCV")
            st.write("""
            A hybrid deep learning pipeline for video-based anomaly detection (fire, accidents, robbery).
            - ✅ Achieved **92% accuracy** in detecting suspicious movements.
            - ✅ Real-time frame processing optimized for speed.
            """)
            st.markdown("[View Code >](#)")
        with col_viz:
            st.success("Acc: 92% | Speed: Real-time")

    st.markdown("---")

    # Project 3
    with st.container():
        col_text, col_viz = st.columns([2, 1])
        with col_text:
            st.subheader("3. Credit Card Default Prediction")
            st.write("**Tech Stack:** XGBoost, Flask API")
            st.write("""
            Predictive model for credit defaults deployed via REST API.
            - ✅ Improved system responsiveness by **8%**.
            - ✅ Deployed for real-time inference.
            """)
            st.markdown("[View Code >](#)")
        with col_viz:
            st.warning("Acc: 84% | Status: Deployed")

# --- PAGE: EXPERIENCE ---
if selected == "Experience":
    st.header("💼 Work Experience")
    
    st.markdown("#### **AI Engineer** | GTechnoHubb Solutions")
    st.caption("04/2025 – Present | Bengaluru, Karnataka")
    st.write("- Building production ML/DL models and real-time inference pipelines.")
    st.write("- Designing ML pipelines including preprocessing, training, and evaluation.")
    
    st.markdown("---")
    
    st.markdown("#### **Data Science Intern** | NullClass")
    st.caption("12/2024 – 04/2025")
    st.write("- Contributed to data preparation, tuning, and validation.")
    st.write("- Improved ML model accuracy significantly through hyperparameter tuning.")
    
    st.markdown("---")
    
    st.markdown("#### **Machine Learning Intern** | Eysec Cyber Security")
    st.caption("08/2023 – 09/2023")
    st.write("- Improved ML accuracy from 80% to 87.58% through tuning.")
    st.write("- Performed EDA and feature extraction.")

# --- PAGE: EDUCATION ---
if selected == "Education":
    st.header("🎓 Education")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Bachelor of Engineering (CS)")
        st.write("**MMEC**")
        st.write("2020 - 2024")
        st.write("Result: **78%**")
    
    with col2:
        st.subheader("PUC (PCMCS)")
        st.write("**MM Integrated PU College**")
        st.write("2018 - 2020")
        st.write("Belgaum, Karnataka")
        
    st.markdown("---")
    st.subheader("📜 Certifications")
    st.write("- **Data Analysis with Python** (Pandas, NumPy, Matplotlib)")
    st.write("- **Certificate of Training:** ML model development & EDA")

# --- PAGE: CONTACT ---
if selected == "Contact":
    st.header("📬 Get In Touch")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("Feel free to reach out for collaborations or job opportunities.")
        st.write("📧 **Email:** jayshahapurakar@gmail.com")
        st.write("📱 **Phone:** 8296597356")
        st.write("🔗 **LinkedIn:** [Jay Shahapurakar](www.linkedin.com/in/jay-shahapurakar)")
        st.write("🐙 **GitHub:** [Jay Shahapurakar](https://github.com/Legit18Im/Jay-Shahapurakar)")
    
    with col2:
        st_lottie(lottie_contact, height=200)
        
    st.markdown("---")
    
    # Contact Form (Functional)
    st.write("### Send me a message")
    contact_form = """
    <form action="https://formsubmit.co/jayshahapurakar@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required style="width: 100%; padding: 8px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 4px;">
        <input type="email" name="email" placeholder="Your email" required style="width: 100%; padding: 8px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 4px;">
        <textarea name="message" placeholder="Your message here" required style="width: 100%; padding: 8px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 4px;"></textarea>
        <button type="submit" style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)