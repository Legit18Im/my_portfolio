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

# --- CUSTOM CSS ANIMATIONS ---
st.markdown("""
<style>
    /* 1. Global Font */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        scroll-behavior: smooth;
    }

    /* 2. Fade In Animation for the whole page */
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    .main {
        animation: fadeIn 1s ease-in-out;
    }

    /* 3. Card Styling with Hover Animation */
    .stExpander {
        border: none !important;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        border-radius: 10px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .stExpander:hover {
        transform: scale(1.01);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    /* 4. Project Cards Styling */
    .project-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #2E86C1;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
        margin-bottom: 20px;
    }
    .project-card:hover {
        transform: translateY(-5px);
    }

    /* 5. Badges */
    .badge {
        background-color: #e3f2fd;
        color: #1565c0;
        padding: 5px 12px;
        border-radius: 15px;
        font-size: 0.85em;
        font-weight: 600;
        margin-right: 5px;
        display: inline-block;
        border: 1px solid #bbdefb;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR (Static Profile Info) ---
with st.sidebar:
    # Profile Pic
    try:
        image = Image.open("profile-pic.png")
        st.image(image, width=150)
    except FileNotFoundError:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150)

    st.markdown("### Jay Shahapurakar")
    st.markdown("**AI Engineer @ Trainee**")
    st.caption("📍 Belgaum, Karnataka, India")
    
    st.markdown("---")
    
    # Social Icons
    st.markdown("""
    <div style="display: flex; gap: 10px; margin-bottom: 20px;">
        <a href="https://www.linkedin.com/in/jay-shahapurakar" target="_blank">
            <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" width="100" />
        </a>
        <a href="https://github.com/Legit18Im/Jay-Shahapurakar" target="_blank">
            <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" width="90" />
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Download Resume
    try:
        with open("resume.pdf", "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
        st.download_button(
            label="📄 Download Resume PDF",
            data=pdf_bytes,
            file_name="Jay_Shahapurakar_Resume.pdf",
            mime="application/pdf"
        )
    except FileNotFoundError:
        st.warning("⚠️ resume.pdf not found")

    st.markdown("---")
    st.info("ℹ️ **Navigation:** Scroll down to see my Projects, Experience, and Skills.")

# ==========================================
# SECTIONS START HERE (Vertical Flow)
# ==========================================

# --- 1. HERO SECTION ---
col1, col2 = st.columns([1.5, 1])
with col1:
    st.title("Jay Shahapurakar")
    st.markdown("#### 🚀 Building Intelligent Systems with AI & Deep Learning")
    st.write("""
    I am an **AI Engineer** specializing in **Computer Vision** and **Predictive Modeling**. 
    My work bridges the gap between raw data and actionable business insights, utilizing modern pipelines like **CI/CD**, **Azure ML**, and **GPU Acceleration**.
    """)
    st.markdown("---")
    # Quick Stats
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric(label="Experience", value="4+ Roles")
    with c2:
        st.metric(label="Projects", value="Full Stack AI")
    with c3:
        st.metric(label="Top Grade", value="Grade A (VTU)")
    
    st.info("💡 **Open to Work:** Data Scientist, ML Engineer, AI Engineer.")

with col2:
    if lottie_hero:
        st_lottie(lottie_hero, height=350)

st.write("---")

# --- 2. SKILLS & TECH STACK ---
st.header("🛠 Technical Proficiency")
st.markdown("My toolkit for building scalable AI solutions.")

sc1, sc2 = st.columns(2)
with sc1:
    st.subheader("Languages & Tools")
    st.markdown("![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)")
    st.markdown("![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white)")
    st.markdown("![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)")
    st.markdown("![Azure](https://img.shields.io/badge/Azure%20ML-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)")
    
with sc2:
    st.subheader("AI Frameworks")
    st.markdown("![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)")
    st.markdown("![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)")
    st.markdown("![Hadoop](https://img.shields.io/badge/Hadoop-66CCFF?style=for-the-badge&logo=apachehadoop&logoColor=white)")

st.write("---")

# --- 3. EXPERIENCE TIMELINE ---
st.header("🚀 Professional Experience")
st.write("A chronological view of my career journey.")

# 1. GTechnoHubb
with st.expander("📍 **AI Engineer | GTechnoHubb Solutions** (Apr 2025 - Present)", expanded=True):
    st.write("**Bengaluru, Karnataka**")
    st.markdown("- Building and deploying **production-grade ML/DL models**.")
    st.markdown("- Designing end-to-end ML pipelines covering preprocessing, training, and evaluation.")
    st.markdown("- Implementing real-time inference systems using Flask.")

# 2. Labmentix
with st.expander("📍 **Data Analyst Intern | Labmentix** (Mar 2025 - Apr 2025)", expanded=True):
    st.write("**Bengaluru, Karnataka / Remote**")
    st.markdown("- Worked on large-scale **Data Integration** and analysis.")
    st.markdown("- Utilized **Convolutional Neural Networks (CNN)** for image data processing.")

# 3. NullClass
with st.expander("📍 **Data Science Intern | NullClass** (Dec 2024 - Mar 2025)"):
    st.write("**Dharmapuri, Tamil Nadu**")
    st.markdown("- Specialized in **Deep Learning** and **GPU Computing**.")
    st.markdown("- Built pipelines using **PySpark** and performed advanced Feature Engineering.")

# 4. Internship Studio
with st.expander("📍 **Data Scientist | Internship Studio** (Aug 2024 - Nov 2024)"):
    st.write("**Pune, Maharashtra**")
    st.markdown("- Developed **Financial Risk Models** using Statistical Modeling.")
    st.markdown("- Managed databases using **SQL** and optimized data queries.")

# 5. Eysec
with st.expander("📍 **Machine Learning Intern | Eysec Cyber Security** (Aug 2023 - Sep 2023)"):
    st.write("**Belgaum**")
    st.markdown("- Improved model accuracy from **80% to 87.58%**.")
    st.markdown("- Performed EDA to identify security threats.")

st.write("---")

# --- 4. FEATURED PROJECTS ---
st.header("💻 Featured Projects")

# Project 1
st.markdown('<div class="project-card">', unsafe_allow_html=True)
p1_col1, p1_col2 = st.columns([3, 1])
with p1_col1:
    st.subheader("1. AI ATS Resume Scanner & Ranker")
    st.markdown('<span class="badge">Django</span> <span class="badge">NLP (SBERT)</span> <span class="badge">spaCy</span>', unsafe_allow_html=True)
    st.write("A semantic search engine that scores resumes against Job Descriptions. Unlike simple keyword matchers, this understands context.")
    st.markdown("**Impact:** Automated PDF reporting and weighted ATS scoring.")
    st.link_button("View Code", "https://github.com/Legit18Im/AI-ATS-Resume-Scanner")
with p1_col2:
    st.image("https://cdn-icons-png.flaticon.com/512/2910/2910791.png", width=120)
st.markdown('</div>', unsafe_allow_html=True)

# Project 2
st.markdown('<div class="project-card">', unsafe_allow_html=True)
p2_col1, p2_col2 = st.columns([3, 1])
with p2_col1:
    st.subheader("2. Video Anomaly Detection (CCTV)")
    st.markdown('<span class="badge">Computer Vision</span> <span class="badge">CNN+LSTM</span> <span class="badge">OpenCV</span>', unsafe_allow_html=True)
    st.write("Real-time detection of fire, accidents, and robbery. Optimized for GPU inference.")
    st.markdown("**Impact:** 92% Accuracy with 15% efficiency gain via frame-skipping.")
    st.link_button("View Code", "https://github.com/Legit18Im/Jay-Shahapurakar")
with p2_col2:
    st.image("https://cdn-icons-png.flaticon.com/512/3067/3067303.png", width=120)
st.markdown('</div>', unsafe_allow_html=True)

# Project 3
st.markdown('<div class="project-card">', unsafe_allow_html=True)
st.subheader("3. Credit Risk Financial Model")
st.markdown('<span class="badge">XGBoost</span> <span class="badge">Finance</span> <span class="badge">SQL</span>', unsafe_allow_html=True)
st.write("Developed a statistical model at **Internship Studio** to predict loan defaults, significantly lowering financial risk.")
st.link_button("View Code", "https://github.com/Legit18Im/Credit-Risk-Financial-Model/tree/main")
st.markdown('</div>', unsafe_allow_html=True)

st.write("---")

# --- 5. EDUCATION & CERTS ---
st.header("🎓 Education & Certifications")
e_col1, e_col2 = st.columns(2)

with e_col1:
    st.subheader("Education")
    st.markdown("**B.E. Computer Science**")
    st.write("Visvesvaraya Technological University")
    st.write("📅 2021 - 2024")
    st.success("Result: Grade A")
    
    st.markdown("**B.E. Computer Science**")
    st.write("Maratha Mandal Engineering College")
    st.write("📅 2020 - 2024")
    st.info("Result: Grade 7.5")

with e_col2:
    st.subheader("Certifications")
    st.info("✅ **Data Science Training** (NullClass)")
    st.info("✅ **Certified Data Scientist** (Internship Studio)")
    st.info("✅ **Data Analysis with Python** (Cognitive Class)")

st.write("---")

# --- 6. CONTACT FOOTER ---
st.header("📬 Get in Touch")
contact_col1, contact_col2 = st.columns([2, 1])

with contact_col1:
    st.write("I am open to full-time opportunities in Data Science & AI. Feel free to reach out!")
    st.markdown("**📧 Email:** jayshahapurakar@gmail.com")
    
    st.write("OR Send a message directly:")
    contact_form = """
    <form action="https://formsubmit.co/jayshahapurakar@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 5px;">
        <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 5px;">
        <textarea name="message" placeholder="Your Message" required style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 5px;"></textarea>
        <button type="submit" style="background-color: #2E86C1; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">Send Message</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

with contact_col2:
    if lottie_contact:
        st_lottie(lottie_contact, height=250)