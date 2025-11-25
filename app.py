import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Jay Shahapurakar | AI Engineer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ASSETS & ANIMATIONS ---
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

lottie_hero = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie_contact = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_u25cckyh.json")

# --- CUSTOM CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        scroll-behavior: smooth;
    }
    
    /* Fade In Animation */
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    .main { animation: fadeIn 0.8s ease-in-out; }

    /* Project Cards */
    .project-card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #2E86C1;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 25px;
        transition: transform 0.3s ease;
    }
    .project-card:hover { transform: translateY(-5px); }

    /* Badges */
    .badge {
        background-color: #e3f2fd;
        color: #1565c0;
        padding: 5px 12px;
        border-radius: 15px;
        font-size: 0.8em;
        font-weight: 600;
        margin-right: 5px;
        display: inline-block;
        border: 1px solid #bbdefb;
    }
    
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: 600;
        border: 1px solid #2E86C1;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    try:
        image = Image.open("profile-pic.png")
        st.image(image, width=150)
    except FileNotFoundError:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150)

    st.markdown("### Jay Shahapurakar")
    st.markdown("**AI Engineer @ Trainee**")
    st.caption("📍 Belgaum, Karnataka, India")
    st.markdown("---")
    
    st.markdown("""
    <div style="display: flex; gap: 10px; margin-bottom: 20px;">
        <a href="https://www.linkedin.com/in/jay-shahapurakar" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" width="100" /></a>
        <a href="https://github.com/Legit18Im/Jay-Shahapurakar" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" width="90" /></a>
    </div>
    """, unsafe_allow_html=True)
    
    try:
        with open("resume.pdf", "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
        st.download_button(label="📄 Download Resume PDF", data=pdf_bytes, file_name="Jay_Shahapurakar_Resume.pdf", mime="application/pdf")
    except:
        st.warning("⚠️ resume.pdf not found")

    st.markdown("---")
    st.info("Scroll down to explore my portfolio.")

# --- HERO SECTION ---
col1, col2 = st.columns([1.5, 1])
with col1:
    st.title("Jay Shahapurakar")
    st.markdown("#### 🚀 Transforming Data into Intelligent Systems")
    st.write("""
    I am an **AI Engineer** with deep expertise in **Computer Vision**, **NLP**, and **Generative AI**. 
    Beyond coding, I specialize in **Prompt Engineering** and **AI-Assisted Development**, leveraging LLMs to accelerate build times and optimize workflows.
    """)
    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    with c1: st.metric("Experience", "4+ Roles")
    with c2: st.metric("Projects", "Full Stack AI")
    with c3: st.metric("Education", "Grade A (VTU)")

with col2:
    if lottie_hero: st_lottie(lottie_hero, height=320)

st.write("---")

# --- TECHNICAL SKILLS (Updated with Prompt Engineering) ---
st.header("🛠 Technical Proficiency")

tab1, tab2, tab3 = st.tabs(["🔹 AI & Generative AI", "🔹 Data Engineering & Cloud", "🔹 Development & Tools"])

with tab1:
    st.subheader("Artificial Intelligence")
    st.markdown("""
    - **Generative AI:** Prompt Engineering, LLM Integration, RAG (Retrieval-Augmented Generation)
    - **Deep Learning:** CNN, RNN, LSTM, Transfer Learning (ResNet, YOLO)
    - **NLP:** Transformers (BERT/SBERT), spaCy, Text Preprocessing, NER
    - **Computer Vision:** OpenCV, Image Processing, Object Detection [cite: 7]
    """)

with tab2:
    st.subheader("Big Data & Cloud")
    st.markdown("""
    - **Cloud Platforms:** Microsoft Azure ML, AWS (Basics) [cite: 58]
    - **Big Data:** Apache Spark (PySpark), Hadoop Ecosystem, Hive
    - **Pipelines:** ETL Processes, Data Integration, CI/CD Pipelines [cite: 5]
    - **Databases:** SQL (PostgreSQL, MySQL), NoSQL Basics [cite: 58]
    """)

with tab3:
    st.subheader("Development")
    st.markdown("""
    - **Languages:** Python (Advanced), SQL, C++ [cite: 58]
    - **Web Frameworks:** Flask, Django, Streamlit, FastAPI [cite: 58]
    - **Tools:** Docker, Git/GitHub, VS Code, Jupyter, Power BI [cite: 58]
    - **AI Workflow:** AI-Assisted Coding, Rapid Prototyping
    """)

st.write("---")

# --- PROFESSIONAL EXPERIENCE ---
st.header("🚀 Professional Experience")

with st.expander("📍 **AI Engineer | GTechnoHubb Solutions** (Apr 2025 - Present)", expanded=True):
    st.write("**Bengaluru, Karnataka**")
    st.markdown("""
    - 🛠 **End-to-End Development:** Designing and deploying production-grade ML/DL models[cite: 62].
    - 🚀 **Pipeline Optimization:** Implementing real-time inference pipelines using **Flask** and **Docker**[cite: 63].
    - 📊 **Model Monitoring:** Collaborating with cross-functional teams to improve model accuracy[cite: 64].
    """)

with st.expander("📍 **Data Analyst Intern | Labmentix** (Mar 2025 - Apr 2025)", expanded=True):
    st.write("**Bengaluru / Remote**")
    st.markdown("""
    - 🔍 **Large-Scale Analysis:** Performed data integration and quality checks on complex datasets[cite: 20, 21].
    - 🖼 **Computer Vision:** Applied **Convolutional Neural Networks (CNN)** for image classification tasks.
    - 📈 **Optimization:** Assisted in optimizing SQL queries for faster analytics dashboards.
    """)

with st.expander("📍 **Data Science Intern | NullClass** (Dec 2024 - Mar 2025)"):
    st.write("**Dharmapuri, Tamil Nadu**")
    st.markdown("""
    - ⚡ **GPU Computing:** Utilized GPU acceleration for training Deep Learning models[cite: 5].
    - 🛠 **Feature Engineering:** Developed robust pipelines using **PySpark** for big data processing[cite: 15].
    - 🎯 **Impact:** Instrumental in enhancing model accuracy through hyperparameter tuning.
    """)

with st.expander("📍 **Data Scientist | Internship Studio** (Aug 2024 - Nov 2024)"):
    st.write("**Pune, Maharashtra**")
    st.markdown("""
    - 💳 **Risk Modeling:** Developed a **Financial Risk Model** that lowers default rates for credit institutions[cite: 16].
    - 📉 **Statistical Analysis:** Applied advanced statistical methods to identify key risk indicators.
    - 🗄 **Data Management:** Managed large financial datasets using SQL and Pandas.
    """)

with st.expander("📍 **ML Intern | Eysec Cyber Security** (Aug 2023 - Sep 2023)"):
    st.write("**Belgaum**")
    st.markdown("""
    - 🛡 **Security AI:** Applied ML to identify patterns in security threat data[cite: 33].
    - 📈 **Performance Boost:** Tuned models to improve accuracy from **80% to 87.58%**[cite: 38].
    - 🔍 **EDA:** Performed rigorous Exploratory Data Analysis to clean and prep security logs[cite: 33].
    """)

st.write("---")

# --- FEATURED PROJECTS ---
st.header("💻 Featured Projects")

# Project 1
st.markdown('<div class="project-card">', unsafe_allow_html=True)
p1_col1, p1_col2 = st.columns([3, 1])
with p1_col1:
    st.subheader("1. AI ATS Resume Scanner & Ranker")
    st.markdown('<span class="badge">Django</span> <span class="badge">SBERT</span> <span class="badge">Named Entity Recognition</span>', unsafe_allow_html=True)
    st.write("A semantic search engine designed to solve the 'Keyword Stuffing' problem in recruitment.")
    st.markdown("""
    - **Semantic Matching:** Uses **Cosine Similarity** on SBERT vectors to understand context, not just keywords[cite: 80].
    - **Entity Extraction:** Implemented **NER (spaCy)** to automatically extract Skills, Education, and Experience[cite: 81].
    - **Full-Stack:** Built with Django and generates automated PDF compatibility reports[cite: 83].
    """)
    st.link_button("View Code", "https://github.com/Legit18Im/Jay-Shahapurakar")
with p1_col2:
    st.image("https://cdn-icons-png.flaticon.com/512/2910/2910791.png", width=120)
st.markdown('</div>', unsafe_allow_html=True)

# Project 2
st.markdown('<div class="project-card">', unsafe_allow_html=True)
p2_col1, p2_col2 = st.columns([3, 1])
with p2_col1:
    st.subheader("2. Video Anomaly Detection (CCTV)")
    st.markdown('<span class="badge">Computer Vision</span> <span class="badge">ConvLSTM</span> <span class="badge">Real-time Inference</span>', unsafe_allow_html=True)
    st.write("An automated surveillance system to detect accidents, fire, and robbery in real-time video feeds.")
    st.markdown("""
    - **Architecture:** Utilized **ConvLSTM** to capture both spatial (image) and temporal (time) dependencies[cite: 90].
    - **Optimization:** Implemented frame-skipping techniques to improve processing speed by **15%**[cite: 92].
    - **Accuracy:** Achieved **92% accuracy** with reduced false positives in varying lighting conditions[cite: 91].
    """)
    st.link_button("View Code", "https://github.com/Legit18Im/Jay-Shahapurakar")
with p2_col2:
    st.image("https://cdn-icons-png.flaticon.com/512/3067/3067303.png", width=120)
st.markdown('</div>', unsafe_allow_html=True)

# Project 3
st.markdown('<div class="project-card">', unsafe_allow_html=True)
st.subheader("3. Credit Risk Financial Model")
st.markdown('<span class="badge">XGBoost</span> <span class="badge">SMOTE</span> <span class="badge">Statistical Modeling</span>', unsafe_allow_html=True)
st.write("A robust classification system to predict potential credit card defaulters.")
st.markdown("""
    - **Class Imbalance:** Handled skewed datasets using **SMOTE (Synthetic Minority Over-sampling Technique)**.
    - **Feature Engineering:** Analyzed demographic and behavioral data to identify key risk factors[cite: 86].
    - **Performance:** Optimized **ROC-AUC Score** to minimize financial risk for lenders[cite: 85].
    """)
st.link_button("View Code", "https://github.com/Legit18Im/Jay-Shahapurakar")
st.markdown('</div>', unsafe_allow_html=True)

st.write("---")

# --- EDUCATION ---
st.header("🎓 Education & Certifications")
c1, c2 = st.columns(2)
with c1:
    st.subheader("Education")
    st.markdown("**B.E. Computer Science** | VTU (2021-2024)")
    st.success("Result: Grade A [cite: 41]")
    st.markdown("**B.E. Computer Science** | Maratha Mandal (2020-2024)")
    st.info("Result: Grade 7.5 [cite: 42, 43]")
with c2:
    st.subheader("Certifications")
    st.markdown("✅ **Certified Data Scientist** (Internship Studio) [cite: 7]")
    st.markdown("✅ **Data Science Training** (NullClass) [cite: 8]")
    st.markdown("✅ **Data Analysis with Python** (Cognitive Class) [cite: 9]")

# --- FOOTER ---
st.write("---")
st.caption("🚀 Portfolio built with Python, Streamlit, and Prompt Engineering.")
st.header("📬 Get in Touch")
st.write("Open to Full-Time Roles. Let's Connect!")
st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/jay-shahapurakar) &nbsp; [![Email](https://img.shields.io/badge/Email-Me-red?style=for-the-badge&logo=gmail)](mailto:jayshahapurakar@gmail.com)")