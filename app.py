import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Jay Shahapurakar | AI Engineer",
    page_icon="⚡",
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

# --- PREMIUM CSS STYLING (Dark Mode & Glassmorphism) ---
st.markdown("""
<style>
    /* 1. GOOGLE FONTS */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
        scroll-behavior: smooth;
    }

    /* 2. BACKGROUND GRADIENT (Deep Professional Dark) */
    .stApp {
        background: radial-gradient(circle at top left, #1a202c, #0d1117);
        color: #e2e8f0;
    }

    /* 3. NEON ACCENT COLORS */
    :root {
        --primary: #00ADB5;
        --secondary: #393E46;
        --text: #EEEEEE;
    }

    h1, h2, h3 { color: var(--primary) !important; font-weight: 700; }
    a { color: var(--primary) !important; text-decoration: none; transition: 0.3s; }
    a:hover { color: #00FFF5 !important; }

    /* 4. GLASSMORPHISM CARDS */
    .glass-card {
        background: rgba(30, 41, 59, 0.4);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, border-color 0.3s ease;
    }
    .glass-card:hover {
        transform: translateY(-5px);
        border-color: var(--primary);
        box-shadow: 0 10px 30px rgba(0, 173, 181, 0.2);
    }

    /* 5. CUSTOM SCROLLBAR */
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: #0f172a; }
    ::-webkit-scrollbar-thumb { background: #334155; border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: var(--primary); }

    /* 6. PROFILE PIC GLOW */
    .profile-pic-container {
        display: flex;
        justify-content: center;
        padding: 20px;
    }
    .profile-pic {
        border-radius: 50%;
        border: 3px solid var(--primary);
        box-shadow: 0 0 25px rgba(0, 173, 181, 0.4);
        transition: transform 0.5s ease;
    }
    .profile-pic:hover {
        transform: scale(1.05);
        box-shadow: 0 0 40px rgba(0, 173, 181, 0.6);
    }

    /* 7. TECH BADGES */
    .tech-badge {
        background-color: rgba(0, 173, 181, 0.1);
        color: #00ADB5;
        border: 1px solid rgba(0, 173, 181, 0.3);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.85em;
        font-weight: 500;
        margin: 4px;
        display: inline-block;
    }

    /* 8. BUTTONS */
    .stButton>button {
        background: linear-gradient(135deg, #00ADB5 0%, #007f85 100%);
        color: white;
        border: none;
        padding: 12px 24px;
        font-weight: 600;
        border-radius: 8px;
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(0, 173, 181, 0.4);
        color: white;
    }
    
    /* 9. EXPANDER CLEANUP */
    .streamlit-expanderHeader {
        background-color: rgba(255,255,255,0.02);
        border-radius: 8px;
        color: #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### ⚡ Navigator")
    
    st.markdown("""
    <div style="padding: 10px 0;">
        <a href="#jay-shahapurakar">🏠 Home</a><br>
        <a href="#technical-proficiency">🛠 Skills</a><br>
        <a href="#professional-experience">🚀 Experience</a><br>
        <a href="#featured-projects">💻 Projects</a><br>
        <a href="#get-in-touch">📬 Contact</a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Resume Download
    try:
        with open("resume.pdf", "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
        st.download_button(label="📄 Download Resume", data=pdf_bytes, file_name="Jay_Shahapurakar_Resume.pdf", mime="application/pdf")
    except:
        st.warning("⚠️ resume.pdf not found")

# ==========================================
# HERO SECTION
# ==========================================
col1, col2 = st.columns([1.3, 1])

with col1:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<span class="tech-badge">Open to Work</span>', unsafe_allow_html=True)
    st.title("Jay Shahapurakar")
    st.markdown("#### **AI Engineer & Data Scientist**")
    
    st.write("""
    I architect intelligent systems using **Deep Learning**, **Computer Vision**, and **Generative AI**. 
    Bridging the gap between complex algorithms and scalable business solutions using **Azure**, **AWS**, and **CI/CD** pipelines.
    """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # CTA Buttons
    b1, b2 = st.columns([1, 2])
    with b1:
        st.markdown('<a href="#get-in-touch"><button style="background:#00ADB5;color:white;border:none;padding:10px 25px;border-radius:8px;font-weight:bold;cursor:pointer;">Hire Me</button></a>', unsafe_allow_html=True)
    
    # Socials
    st.markdown("""
    <div style="margin-top: 25px; display: flex; align-items: center; gap: 15px;">
        <a href="https://www.linkedin.com/in/jay-shahapurakar" target="_blank">
            <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" height="35" />
        </a>
        <a href="https://github.com/Legit18Im/Jay-Shahapurakar" target="_blank">
            <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" height="35" />
        </a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    try:
        image = Image.open("profile-pic.png")
        st.markdown('<div class="profile-pic-container">', unsafe_allow_html=True)
        st.image(image, width=320)
        st.markdown('</div>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=250)

st.write("---")

# --- SKILLS ---
st.header("🛠 Technical Proficiency")

tab1, tab2, tab3 = st.tabs(["**AI & GenAI**", "**Big Data & Cloud**", "**Development**"])

with tab1:
    st.markdown("""
    <div class="glass-card">
        <h4>🤖 Artificial Intelligence</h4>
        <ul>
            <li><b>Generative AI:</b> Prompt Engineering, RAG Pipelines, LLM Integration</li>
            <li><b>Deep Learning:</b> CNN, LSTM, Transfer Learning (YOLO, ResNet)</li>
            <li><b>NLP:</b> SBERT, spaCy, Transformers (HuggingFace)</li>
            <li><b>Computer Vision:</b> OpenCV, Real-time Object Detection</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <div class="glass-card">
        <h4>☁️ Cloud & Infrastructure</h4>
        <ul>
            <li><b>Cloud:</b> Microsoft Azure ML, AWS (Basics)</li>
            <li><b>Big Data:</b> PySpark, Hadoop Ecosystem, Hive</li>
            <li><b>DevOps:</b> CI/CD Pipelines, Docker Containerization</li>
            <li><b>Databases:</b> PostgreSQL, MySQL, NoSQL</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown("""
    <div class="glass-card">
        <h4>💻 Core Engineering</h4>
        <ul>
            <li><b>Languages:</b> Python (Expert), SQL, C++</li>
            <li><b>Frameworks:</b> Flask, Django, Streamlit, FastAPI</li>
            <li><b>Tools:</b> Git/GitHub, VS Code, Jupyter, Power BI</li>
            <li><b>Workflow:</b> AI-Assisted Coding, Agile Methodology</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- EXPERIENCE ---
st.write("---")
st.header("🚀 Professional Experience")

# Custom HTML timeline feel
def experience_card(role, company, date, loc, desc):
    st.markdown(f"""
    <div class="glass-card" style="border-left: 4px solid #00ADB5;">
        <h4 style="margin-bottom: 5px;">{role}</h4>
        <p style="color: #94a3b8; margin-bottom: 10px;"><b>{company}</b> • {date} • <i>{loc}</i></p>
        <p>{desc}</p>
    </div>
    """, unsafe_allow_html=True)

# 1. GTechnoHubb
experience_card(
    "AI Engineer", "GTechnoHubb Solutions", "Apr 2025 - Present", "Bengaluru",
    "Building production-grade ML/DL models. Designing end-to-end ML pipelines covering preprocessing, training, and evaluation. Implementing real-time inference systems using Flask."
)

# 2. Labmentix
experience_card(
    "Data Analyst Intern", "Labmentix", "Mar 2025 - Apr 2025", "Bengaluru",
    "Worked on large-scale Data Integration and analysis. Utilized Convolutional Neural Networks (CNN) for image data processing."
)

# 3. NullClass
experience_card(
    "Data Science Intern", "NullClass", "Dec 2024 - Mar 2025", "Dharmapuri",
    "Specialized in Deep Learning and GPU Computing. Built pipelines using PySpark and performed advanced Feature Engineering."
)

# 4. Internship Studio
experience_card(
    "Data Scientist", "Internship Studio", "Aug 2024 - Nov 2024", "Pune",
    "Developed Financial Risk Models using Statistical Modeling. Managed databases using SQL and optimized data queries."
)

# 5. Eysec
experience_card(
    "Machine Learning Intern", "Eysec Cyber Security", "Aug 2023 - Sep 2023", "Belgaum",
    "Improved model accuracy from 80% to 87.58%. Performed EDA to identify security threats."
)

# --- PROJECTS ---
st.write("---")
st.header("💻 Featured Projects")

def project_card_pro(title, tech_stack, description, link, img_icon):
    st.markdown(f"""
    <div class="glass-card">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h3 style="margin: 0;">{title}</h3>
            <span style="font-size: 1.5em;">{img_icon}</span>
        </div>
        <p style="color: #00ADB5; font-weight: 600; margin-top: 5px;">{tech_stack}</p>
        <p>{description}</p>
        <a href="{link}" target="_blank">
            <button style="background: transparent; border: 1px solid #00ADB5; color: #00ADB5; padding: 8px 16px; border-radius: 6px; cursor: pointer; transition: 0.3s;">
                View Source Code ➔
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    project_card_pro(
        "AI ATS Resume Scanner",
        "Django • SBERT • NLP",
        "A semantic search engine designed to solve 'Keyword Stuffing'. Uses Cosine Similarity on SBERT vectors to understand resume context. Generates PDF reports.",
        "https://github.com/Legit18Im/Jay-Shahapurakar",
        "📄"
    )
    project_card_pro(
        "Credit Risk Model",
        "XGBoost • SMOTE • AWS",
        "Financial default predictor utilizing SMOTE for class imbalance. Optimized ROC-AUC score to minimize financial risk for lenders.",
        "https://github.com/Legit18Im/Jay-Shahapurakar",
        "💳"
    )

with c2:
    project_card_pro(
        "CCTV Anomaly Detection",
        "ConvLSTM • OpenCV • Real-Time",
        "Automated surveillance system to detect accidents & fire. Achieved 92% accuracy with 15% efficiency gain via frame skipping.",
        "https://github.com/Legit18Im/Jay-Shahapurakar",
        "📹"
    )

# --- EDUCATION & CERTIFICATIONS ---
st.write("---")
st.header("🎓 Education & Certifications")

col_edu, col_cert = st.columns(2)

with col_edu:
    st.subheader("Education")
    st.markdown("""
    <div class="glass-card">
        <h5>B.E. Computer Science</h5>
        <p><b>Visvesvaraya Technological University</b></p>
        <p style="font-size: 0.9em; color: #aaa;">2021 - 2024 • Grade A</p>
        <hr style="border-color: rgba(255,255,255,0.1);">
        <h5>B.E. Computer Science</h5>
        <p><b>Maratha Mandal Engineering College</b></p>
        <p style="font-size: 0.9em; color: #aaa;">2020 - 2024 • Grade 7.5</p>
    </div>
    """, unsafe_allow_html=True)

with col_cert:
    st.subheader("Certifications")
    st.markdown("""
    <div class="glass-card">
        <p>✅ <b>Certified Data Scientist</b> <br><span style="font-size:0.8em; color:#aaa;">Internship Studio</span></p>
        <p>✅ <b>Data Science Training</b> <br><span style="font-size:0.8em; color:#aaa;">NullClass</span></p>
        <p>✅ <b>Data Analysis with Python</b> <br><span style="font-size:0.8em; color:#aaa;">Cognitive Class</span></p>
    </div>
    """, unsafe_allow_html=True)

# --- CONTACT ---
st.write("---")
st.header("📬 Get in Touch")

c1, c2 = st.columns([1.5, 1])
with c1:
    st.write("I am currently open to full-time opportunities in Data Science & AI. Whether you have a question or just want to say hi, I'll try my best to get back to you!")
    st.markdown("""
    <a href="mailto:jayshahapurakar@gmail.com" style="text-decoration: none;">
        <div class="glass-card" style="text-align: center; border: 1px solid #00ADB5;">
            <h3>📧 jayshahapurakar@gmail.com</h3>
        </div>
    </a>
    """, unsafe_allow_html=True)

with c2:
    if lottie_contact:
        st_lottie(lottie_contact, height=200)

st.markdown("<center><p style='color: #555; margin-top: 50px;'>Built with Python, Streamlit & AI • © 2025 Jay Shahapurakar</p></center>", unsafe_allow_html=True)