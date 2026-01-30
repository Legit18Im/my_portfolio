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
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif;
    scroll-behavior: smooth;
}

.stApp {
    background: radial-gradient(circle at top left, #1a202c, #0d1117);
    color: #e2e8f0;
}

:root {
    --primary: #00ADB5;
    --secondary: #393E46;
    --text: #EEEEEE;
}

h1, h2, h3 { color: var(--primary) !important; font-weight: 700; }
a { color: var(--primary) !important; text-decoration: none; transition: 0.3s; }
a:hover { color: #00FFF5 !important; }

.glass-card {
    background: rgba(30, 41, 59, 0.4);
    backdrop-filter: blur(10px);
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

::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: #0f172a; }
::-webkit-scrollbar-thumb { background: #334155; border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: var(--primary); }

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

.stButton>button {
    background: linear-gradient(135deg, #00ADB5 0%, #007f85 100%);
    color: white;
    border: none;
    padding: 12px 24px;
    font-weight: 600;
    border-radius: 8px;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### ⚡ Navigator")
    st.markdown("""
    <a href="#jay-shahapurakar">🏠 Home</a><br>
    <a href="#technical-proficiency">🛠 Skills</a><br>
    <a href="#professional-experience">🚀 Experience</a><br>
    <a href="#featured-projects">💻 Projects</a><br>
    <a href="#get-in-touch">📬 Contact</a>
    """, unsafe_allow_html=True)

    st.markdown("---")

    try:
        with open("resume.pdf", "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
        st.download_button(
            label="📄 Download Resume",
            data=pdf_bytes,
            file_name="Jay_Shahapurakar_Resume.pdf",
            mime="application/pdf"
        )
    except:
        st.warning("⚠️ resume.pdf not found")

# ==========================================
# HERO SECTION
# ==========================================
col1, col2 = st.columns([1.3, 1])

with col1:
    st.markdown('<span class="tech-badge">AI Engineer</span><span class="tech-badge">GenAI Systems</span>', unsafe_allow_html=True)
    st.title("Jay Shahapurakar")
    st.markdown("#### **AI & Machine Learning Engineer**")

    st.write("""
    I architect **production-grade AI systems** across **Machine Learning, Computer Vision, and Generative AI**.
    My focus is on building **scalable ML pipelines**, decision-intelligence systems, and deploying models that
    solve real-world business problems.
    """)

    st.markdown('<a href="#get-in-touch"><button>Hire Me</button></a>', unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-top: 25px;">
        <a href="https://www.linkedin.com/in/jay-shahapurakar" target="_blank">LinkedIn</a> •
        <a href="https://github.com/Legit18Im/Jay-Shahapurakar" target="_blank">GitHub</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    try:
        image = Image.open("profile-pic.png")
        st.markdown('<div class="profile-pic-container">', unsafe_allow_html=True)
        st.image(image, width=320)
        st.markdown('</div>', unsafe_allow_html=True)
    except:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=250)

st.write("---")

# --- SKILLS ---
st.header("🛠 Technical Proficiency")

tab1, tab2, tab3 = st.tabs(["**AI & GenAI**", "**Big Data & Cloud**", "**Development**"])

with tab1:
    st.markdown("""
    <div class="glass-card">
        <ul>
            <li><b>Machine Learning:</b> Regression, Classification, Feature Engineering, Model Evaluation</li>
            <li><b>Deep Learning:</b> CNNs, ConvLSTM, Transfer Learning</li>
            <li><b>Generative AI:</b> Prompt Engineering, RAG Pipelines, LLM Integration</li>
            <li><b>NLP:</b> SBERT, Semantic Search, Text Processing</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <div class="glass-card">
        <ul>
            <li><b>Cloud:</b> Azure ML, AWS (Foundations)</li>
            <li><b>Big Data:</b> PySpark, Hadoop, Hive</li>
            <li><b>MLOps:</b> MLflow, Model Versioning, CI/CD</li>
            <li><b>Databases:</b> PostgreSQL, MySQL</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown("""
    <div class="glass-card">
        <ul>
            <li><b>Languages:</b> Python, SQL, C++</li>
            <li><b>Frameworks:</b> Flask, Django, FastAPI, Streamlit</li>
            <li><b>Tools:</b> Git, GitHub, Docker, Power BI</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- EXPERIENCE ---
st.write("---")
st.header("🚀 Professional Experience")

def experience_card(role, company, date, loc, desc):
    st.markdown(f"""
    <div class="glass-card" style="border-left:4px solid #00ADB5;">
        <h4>{role}</h4>
        <p style="color:#94a3b8;"><b>{company}</b> • {date} • <i>{loc}</i></p>
        <p>{desc}</p>
    </div>
    """, unsafe_allow_html=True)

experience_card(
    "AI Engineer", "GTechnoHubb Solutions", "Apr 2025 – Present", "Bengaluru",
    "Developing and deploying end-to-end machine learning pipelines, integrating models with APIs, and building scalable AI-driven systems aligned with business requirements."
)

experience_card(
    "Data Analyst Intern", "Labmentix", "Mar 2025 – Apr 2025", "Bengaluru",
    "Worked on large-scale data analysis and image-based ML workflows using convolutional neural networks."
)

experience_card(
    "Data Science Intern", "NullClass", "Dec 2024 – Mar 2025", "Dharmapuri",
    "Improved classification model accuracy from 56% to 96% through feature engineering, experimentation, and hyperparameter tuning."
)

experience_card(
    "Data Scientist", "Internship Studio", "Aug 2024 – Nov 2024", "Pune",
    "Developed financial risk models using statistical and machine learning techniques and optimized SQL-based data workflows."
)

experience_card(
    "Machine Learning Intern", "Eysec Cyber Security", "Aug 2023 – Sep 2023", "Belgaum",
    "Performed exploratory data analysis and improved model accuracy from 80% to 87.58% for cybersecurity-related ML models."
)

# --- PROJECTS ---
st.write("---")
st.header("💻 Featured Projects")

def project_card_pro(title, tech_stack, description, link, icon):
    st.markdown(f"""
    <div class="glass-card">
        <div style="display:flex; justify-content:space-between;">
            <h3>{title}</h3>
            <span style="font-size:1.5em;">{icon}</span>
        </div>
        <p style="color:#00ADB5;"><b>{tech_stack}</b></p>
        <p>{description}</p>
        <a href="{link}" target="_blank">
            <button style="background:transparent;border:1px solid #00ADB5;color:#00ADB5;padding:8px 16px;border-radius:6px;">
                View Source Code ➔
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    project_card_pro(
        "AI-Driven Real Estate Investment Recommendation System",
        "Scikit-Learn • Random Forest • Streamlit • MLflow",
        "Designed a decision-support system that predicts long-term property valuation and classifies assets into actionable investment verdicts using regression and risk-aware classification models.",
        "https://huggingface.co/spaces/your-username/real-estate-advisor",
        "🏠"
    )

    project_card_pro(
        "SBERT-Based Resume Intelligence & Matching Engine",
        "Django • SBERT • NLP",
        "Built a semantic resume–job matching system using embedding-based similarity search, improving matching relevance by ~30% over keyword-based approaches.",
        "https://github.com/Legit18Im/Jay-Shahapurakar",
        "📄"
    )

with c2:
    project_card_pro(
        "Real-Time Video Anomaly Detection Pipeline",
        "ConvLSTM • OpenCV • Deep Learning",
        "Implemented a real-time video anomaly detection pipeline achieving 92% accuracy at 20+ FPS for surveillance and safety monitoring.",
        "https://github.com/Legit18Im/Jay-Shahapurakar",
        "📹"
    )

    project_card_pro(
        "Credit Risk Scoring & Default Prediction Engine",
        "XGBoost • SMOTE • Machine Learning",
        "Developed and deployed credit risk prediction models on large-scale financial datasets, optimizing ROC-AUC and exposing inference via REST APIs.",
        "https://github.com/Legit18Im/Jay-Shahapurakar",
        "💳"
    )

# --- CONTACT ---
st.write("---")
st.header("📬 Get in Touch")

c1, c2 = st.columns([1.5, 1])

with c1:
    st.markdown("""
    <div class="glass-card" style="text-align:center;">
        <h3>📧 jayshahapurakar@gmail.com</h3>
    </div>
    """, unsafe_allow_html=True)

with c2:
    if lottie_contact:
        st_lottie(lottie_contact, height=200)

st.markdown("<center><p style='color:#555;'>Built with Python & Streamlit • © 2025 Jay Shahapurakar</p></center>", unsafe_allow_html=True)
