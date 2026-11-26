import os
import base64
import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Sanjukta Mandal | Data Analyst & Python Developer",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- CUSTOM CSS (DARK MINIMAL PRO THEME) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap');

    /* Hide default Streamlit UI */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header[data-testid="stHeader"] {display: none;}

    /* Base App Styling */
    html, body, .stApp {
        background-color: #09090b;
        color: #f4f4f5;
        font-family: 'Inter', sans-serif;
        scroll-behavior: smooth;
    }

    .block-container {
        max-width: 1120px;
        padding-top: 1.5rem;
        padding-bottom: 4rem;
    }

    h1, h2, h3, h4 {
        font-family: 'Plus Jakarta Sans', sans-serif;
        letter-spacing: -0.02em;
    }

    /* Sticky Glass Navbar */
    .navbar {
        position: sticky;
        top: 12px;
        z-index: 999;
        display: flex;
        justify-content: center;
        align-items: center;
        width: fit-content;
        margin-left: auto;
        padding: 14px 28px;
        background: rgba(18, 18, 22, 0.78);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        margin-bottom: 3.5rem;
    }
    .nav-brand {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-weight: 800;
        font-size: 1.1rem;
        color: #ffffff;
        text-decoration: none;
        letter-spacing: -0.02em;
    }
    .nav-brand span {
        color: #a855f7;
    }
    .nav-links {
        display: flex;
        gap: 28px;
    }
    .nav-links a {
        color: #a1a1aa;
        text-decoration: none;
        font-size: 0.9rem;
        font-weight: 500;
        transition: color 0.2s ease;
    }
    .nav-links a:hover {
        color: #ffffff;
    }

    /* Availability Badge */
    .status-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(168, 85, 247, 0.1);
        border: 1px solid rgba(168, 85, 247, 0.3);
        color: #d8b4fe;
        padding: 6px 14px;
        border-radius: 999px;
        font-size: 0.82rem;
        font-weight: 500;
        margin-bottom: 1.2rem;
    }
    .status-dot {
        width: 8px;
        height: 8px;
        background-color: #22c55e;
        border-radius: 50%;
        box-shadow: 0 0 8px #22c55e;
    }

    /* Hero Typography */
    .hero-title {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 3.6rem;
        font-weight: 800;
        line-height: 1.08;
        margin-bottom: 1.2rem;
        color: #ffffff;
    }
    .gradient-text {
        background: linear-gradient(90deg, #c084fc 0%, #818cf8 50%, #38bdf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-subtitle {
        font-size: 1.12rem;
        line-height: 1.7;
        color: #a1a1aa;
        margin-bottom: 1.8rem;
    }

    /* Buttons */
    .btn-row {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        margin-top: 1rem;
    }
    .btn-primary {
        background: linear-gradient(135deg, #9333ea 0%, #6366f1 100%);
        color: #ffffff !important;
        padding: 11px 22px;
        border-radius: 10px;
        font-weight: 600;
        font-size: 0.92rem;
        text-decoration: none;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .btn-primary:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(147, 51, 234, 0.35);
    }
    .btn-secondary {
        background: #18181b;
        color: #e4e4e7 !important;
        border: 1px solid #27272a;
        padding: 11px 22px;
        border-radius: 10px;
        font-weight: 500;
        font-size: 0.92rem;
        text-decoration: none;
        transition: border-color 0.2s ease, background 0.2s ease;
    }
    .btn-secondary:hover {
        border-color: #a855f7;
        background: #202025;
    }

    /* Section Headers */
    .section-eyebrow {
        font-family: 'JetBrains Mono', monospace;
        color: #a855f7;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 0.35rem;
    }
    .section-heading {
        font-size: 2.1rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 1.5rem;
    }

    /* Stat / Highlight Cards */
    .stat-card {
        background: #111114;
        border: 1px solid #222228;
        border-radius: 14px;
        padding: 20px 22px;
        text-align: left;
    }
    .stat-number {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 1.5rem;
        white-space: nowrap;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 4px;
    }
    .stat-label {
        font-size: 0.85rem;
        color: #a1a1aa;
    }

    /* Tech Stack Pills */
    .tech-group-title {
        font-size: 0.85rem;
        color: #71717a;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 10px;
        font-weight: 600;
    }
    .tech-pill {
        display: inline-block;
        background: #141418;
        border: 1px solid #27272a;
        color: #d4d4d8;
        padding: 7px 14px;
        border-radius: 8px;
        font-size: 0.86rem;
        font-family: 'JetBrains Mono', monospace;
        margin: 0 8px 8px 0;
        transition: all 0.2s ease;
    }
    .tech-pill:hover {
        border-color: #a855f7;
        color: #ffffff;
        background: rgba(168, 85, 247, 0.1);
    }

    /* Project Cards */
    .project-card {
        background: #111114;
        border: 1px solid #222228;
        border-radius: 16px;
        padding: 26px;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
        margin-bottom: 18px;
    }
    .project-card:hover {
        transform: translateY(-4px);
        border-color: rgba(168, 85, 247, 0.55);
        box-shadow: 0 12px 32px rgba(0, 0, 0, 0.45);
    }
    .project-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 12px;
    }
    .project-badge {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72rem;
        padding: 4px 10px;
        border-radius: 999px;
        background: rgba(168, 85, 247, 0.14);
        color: #d8b4fe;
        border: 1px solid rgba(168, 85, 247, 0.28);
    }
    .project-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 10px;
    }
    .project-desc {
        font-size: 0.93rem;
        color: #a1a1aa;
        line-height: 1.6;
        margin-bottom: 18px;
    }
    .tag-row {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        margin-bottom: 18px;
    }
    .mini-tag {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.74rem;
        color: #a1a1aa;
        background: #1c1c22;
        padding: 4px 9px;
        border-radius: 6px;
    }
    .card-link {
        color: #c084fc !important;
        text-decoration: none;
        font-size: 0.88rem;
        font-weight: 600;
        margin-right: 18px;
    }
    .card-link:hover {
        text-decoration: underline;
    }

    /* Timeline Cards */
    .timeline-item {
        border-left: 2px solid #27272a;
        padding-left: 22px;
        padding-bottom: 24px;
        position: relative;
    }
    .timeline-item::before {
        content: "";
        position: absolute;
        left: -6px;
        top: 6px;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: #a855f7;
        box-shadow: 0 0 10px rgba(168, 85, 247, 0.8);
    }
    .timeline-date {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.8rem;
        color: #a855f7;
        margin-bottom: 4px;
    }
    .timeline-role {
        font-size: 1.1rem;
        font-weight: 700;
        color: #ffffff;
    }
    .timeline-org {
        font-size: 0.92rem;
        color: #a1a1aa;
        margin-bottom: 8px;
    }
    .timeline-desc {
        font-size: 0.9rem;
        color: #d4d4d8;
        line-height: 1.6;
    }

    /* Contact Form Styling */
    .contact-form input, .contact-form textarea {
        width: 100%;
        padding: 12px 15px;
        margin-bottom: 14px;
        background-color: #141418;
        border: 1px solid #27272a;
        border-radius: 10px;
        color: #f4f4f5;
        font-family: 'Inter', sans-serif;
        font-size: 0.92rem;
        outline: none;
        transition: border-color 0.2s ease;
    }
    .contact-form input:focus, .contact-form textarea:focus {
        border-color: #a855f7;
    }
    .contact-form button {
        background: linear-gradient(135deg, #9333ea 0%, #6366f1 100%);
        color: #ffffff;
        border: none;
        padding: 12px 26px;
        border-radius: 10px;
        font-weight: 600;
        font-size: 0.95rem;
        cursor: pointer;
        width: 100%;
        transition: opacity 0.2s ease;
    }
    .contact-form button:hover {
        opacity: 0.92;
    }

    /* Streamlit Expander Dark Override */
    div[data-testid="stExpander"] {
        background-color: #111114;
        border: 1px solid #222228;
        border-radius: 12px;
        margin-bottom: 10px;
    }

    hr {
        border: none;
        border-top: 1px solid #1e1e24;
        margin: 3.5rem 0;
    }
    /* Hero Profile Card */
    .profile-card {
        background: linear-gradient(145deg, #141419 0%, #0d0d11 100%);
        border: 1px solid rgba(168, 85, 247, 0.25);
        border-radius: 20px;
        padding: 28px;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5), 0 0 40px rgba(168, 85, 247, 0.08);
        position: relative;
        overflow: hidden;
    }
    .profile-card::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #9333ea, #6366f1, #38bdf8);
    }
    .profile-top {
        display: flex;
        align-items: center;
        gap: 16px;
        margin-bottom: 22px;
    }
    .avatar-ring {
        width: 56px;
        height: 56px;
        border-radius: 16px;
        background: linear-gradient(135deg, #9333ea 0%, #4f46e5 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-weight: 800;
        font-size: 1.3rem;
        color: #ffffff;
        box-shadow: 0 8px 20px rgba(147, 51, 234, 0.35);
    }
    .profile-name {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 1.2rem;
        font-weight: 700;
        color: #ffffff;
        margin: 0;
    }
    .profile-role {
        font-size: 0.85rem;
        color: #a1a1aa;
        margin: 2px 0 0 0;
    }
    .info-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 12px;
        margin-bottom: 20px;
    }
    .info-box {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 12px;
        padding: 12px 14px;
    }
    .info-label {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: #71717a;
        margin-bottom: 4px;
    }
    .info-value {
        font-size: 0.88rem;
        font-weight: 600;
        color: #e4e4e7;
    }
    .focus-banner {
        background: rgba(168, 85, 247, 0.08);
        border: 1px solid rgba(168, 85, 247, 0.2);
        border-radius: 12px;
        padding: 12px 16px;
        font-size: 0.85rem;
        color: #d8b4fe;
        line-height: 1.5;
    }
    /* Clickable Profile Avatar */
    .profile-avatar-img {
        width: 68px;
        height: 68px;
        border-radius: 16px;
        object-fit: cover;
        border: 2px solid #a855f7;
        box-shadow: 0 8px 20px rgba(147, 51, 234, 0.35);
        cursor: pointer;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .profile-avatar-img:hover {
        transform: scale(1.06);
        box-shadow: 0 0 24px rgba(168, 85, 247, 0.65);
    }

    /* WhatsApp-style Fullscreen Photo Modal */
    .photo-modal {
        display: none;
        position: fixed;
        inset: 0;
        z-index: 99999;
        align-items: center;
        justify-content: center;
        background: rgba(0, 0, 0, 0.85);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
    }
    .photo-modal:target {
        display: flex;
    }
    .photo-modal-backdrop {
        position: absolute;
        inset: 0;
        cursor: default;
    }
    .photo-modal-content {
        position: relative;
        z-index: 2;
        text-align: center;
    }
    .photo-modal-content img {
        max-width: 380px;
        width: 85vw;
        max-height: 80vh;
        object-fit: cover;
        border-radius: 18px;
        border: 2px solid rgba(168, 85, 247, 0.6);
        box-shadow: 0 24px 60px rgba(0, 0, 0, 0.8);
    }
    .photo-modal-close {
        position: absolute;
        top: -14px;
        right: -14px;
        width: 36px;
        height: 36px;
        border-radius: 50%;
        background: #18181b;
        border: 1px solid #3f3f46;
        color: #ffffff !important;
        font-size: 1.4rem;
        line-height: 34px;
        text-align: center;
        text-decoration: none !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
    }
    .photo-modal-close:hover {
        background: #9333ea;
        border-color: #a855f7;
    }
    /* Publications & Patents Cards */
    .pub-card {
        background: #111114;
        border: 1px solid #222228;
        border-radius: 14px;
        padding: 22px 24px;
        margin-bottom: 14px;
        transition: border-color 0.2s ease, transform 0.2s ease;
    }
    .pub-card:hover {
        border-color: rgba(168, 85, 247, 0.5);
        transform: translateX(4px);
    }
    .pub-meta {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 8px;
    }
    .pub-type {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72rem;
        padding: 3px 10px;
        border-radius: 999px;
        background: rgba(56, 189, 248, 0.12);
        color: #7dd3fc;
        border: 1px solid rgba(56, 189, 248, 0.28);
    }
    .pub-type.patent {
        background: rgba(168, 85, 247, 0.14);
        color: #d8b4fe;
        border: 1px solid rgba(168, 85, 247, 0.28);
    }
    .pub-year {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.78rem;
        color: #71717a;
    }
    .pub-title {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 1.08rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 6px;
    }
    .pub-desc {
        font-size: 0.88rem;
        color: #a1a1aa;
        line-height: 1.6;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- NAVBAR ---
st.markdown("""
<div class="navbar">
    <div class="nav-links">
        <a href="#about">About</a>
        <a href="#skills">Skills</a>
        <a href="#projects">Projects</a>
        <a href="#publications">Publications</a>
        <a href="#experience">Experience</a>
        <a href="#education">Education</a>
        <a href="#contact">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown('<div id="home"></div>', unsafe_allow_html=True)
hero_left, hero_right = st.columns([1.35, 1], gap="large")

with hero_left:
    st.markdown("""
    <div class="status-badge">
        <span class="status-dot"></span>
        Open to Data Analyst & Python Opportunities
    </div>
    <div class="hero-title">
        Hi, I'm Sanjukta.<br>
        <span class="gradient-text">Data & Python Developer</span>
    </div>
    <p class="hero-subtitle">
        I transform raw data and complex engineering ideas into interactive dashboards,
        statistical models, and clean Python applications—combining analytical rigor with
        hands-on prototyping.
    </p>
    <div class="btn-row">
        <a href="#projects" class="btn-primary">View Featured Work</a>
        <a href="https://github.com/msanjukta" target="_blank" class="btn-secondary">GitHub</a>
        <a href="https://www.linkedin.com/in/sanjukta245" target="_blank" class="btn-secondary">LinkedIn</a>
        <a href="#contact" class="btn-secondary">Contact</a>
    </div>
    """, unsafe_allow_html=True)

    # Optional automatic Resume download button (activates if resume.pdf is in the folder)
    if os.path.exists("resume.pdf"):
        st.markdown("<br>", unsafe_allow_html=True)
        with open("resume.pdf", "rb") as pdf_file:
            st.download_button(
                label="Download Resume (PDF)",
                data=pdf_file,
                file_name="Sanjukta_Mandal_Resume.pdf",
                mime="application/pdf",
            )

with hero_right:
    avatar_html = '<div class="avatar-ring">SM</div>'
    modal_html = ""
    for img_name, mime in [("profile.jpg", "jpeg"), ("profile.jpeg", "jpeg"), ("profile.png", "png")]:
        if os.path.exists(img_name):
            with open(img_name, "rb") as f:
                img_b64 = base64.b64encode(f.read()).decode()
            img_src = f"data:image/{mime};base64,{img_b64}"
            avatar_html = (
                f'<a href="#profile-modal" title="View profile photo" style="text-decoration:none;">'
                f'<img src="{img_src}" class="profile-avatar-img" alt="Sanjukta Mandal">'
                f'</a>'
            )
            modal_html = (
                f'<div id="profile-modal" class="photo-modal">'
                f'  <a href="#_" class="photo-modal-backdrop"></a>'
                f'  <div class="photo-modal-content">'
                f'    <a href="#_" class="photo-modal-close">×</a>'
                f'    <img src="{img_src}" alt="Sanjukta Mandal">'
                f'  </div>'
                f'</div>'
            )
            break

    st.markdown(f"""
    <div class="profile-card">
        <div class="profile-top">
            {avatar_html}
            <div>
                <div class="profile-name">Sanjukta Mandal</div>
                <div class="profile-role">Data Analyst & Python Developer</div>
            </div>
        </div>
        <div class="info-grid">
            <div class="info-box">
                <div class="info-label">Location</div>
                <div class="info-value">West Bengal, India</div>
            </div>
            <div class="info-box">
                <div class="info-label">EDUCATION</div>
                <div class="info-value">B.Tech CSE (AI & ML)</div>
            </div>
            <div class="info-box">
                <div class="info-label">Core Stack</div>
                <div class="info-value">Python • Pandas • SQL • Advance Excel</div>
            </div>
            <div class="info-box">
                <div class="info-label">Availability</div>
                <div class="info-value" style="color:#4ade80;">● Open to Work</div>
            </div>
        </div>
        <div class="focus-banner">
            <strong>Current Focus:</strong> Exploring Data Analytics and AI/ML fundamentals alongside coordinating AICTE IDEA Lab workshops and IIC documentation.
        </div>
    </div>
    {modal_html}
    """, unsafe_allow_html=True)

# --- HIGHLIGHTS / METRICS ROW ---
st.markdown("<br>", unsafe_allow_html=True)
s1, s2, s3, s4 = st.columns(4)
with s1:
    st.markdown('<div class="stat-card"><div class="stat-number">Python</div><div class="stat-label">Data Pipelines & Dashboards</div></div>', unsafe_allow_html=True)
with s2:
    st.markdown('<div class="stat-card"><div class="stat-number">Excel</div><div class="stat-label">Advanced Formulas, Pivot Tables & Dashboards</div></div>', unsafe_allow_html=True)
with s3:
    st.markdown('<div class="stat-card"><div class="stat-number">Paper & Patent</div><div class="stat-label">Published Indian Patents & Research Papers</div></div>', unsafe_allow_html=True)
with s4:
    st.markdown('<div class="stat-card"><div class="stat-number">MS Office</div><div class="stat-label">Documentation, Reporting & Presentations</div></div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- ABOUT & WHAT I DO ---
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow">01 / About</div>', unsafe_allow_html=True)
st.markdown('<div class="section-heading">What I Do</div>', unsafe_allow_html=True)

about_left, about_right = st.columns([1.15, 1], gap="large")

with about_left:
    st.markdown("""
    <p style="color:#d4d4d8; line-height:1.8; font-size:1rem;">
        I am a <strong>B.Tech CSE (AI & ML) student</strong> and an aspiring <strong>Data Analyst</strong> currently building my skills in Python, Excel, and data visualization. Alongside my coursework, I actively contribute to campus innovation as an <strong>AICTE IDEA Lab Ambassador</strong> and <strong>IIC Innovation Ambassador</strong>—handling technical workshops, documentation, and collaborative research. I am eager to learn, grow, and apply my skills to real-world opportunities.
    </p>
    """, unsafe_allow_html=True)

with about_right:
    with st.expander("Data Analytics & Interactive Dashboards", expanded=True):
        st.write("Designing end-to-end analytical web apps using Python, Pandas, Plotly, and Streamlit with live REST API integration.")
    with st.expander("Rapid Prototyping & Technical Training"):
        st.write("Hands-on experience with Arduino/IoT, digital fabrication workflows, and coordinating multi-week technical internships.")

st.markdown("<hr>", unsafe_allow_html=True)

# --- SKILLS SECTION ---
st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow">02 / Tech Stack</div>', unsafe_allow_html=True)
st.markdown('<div class="section-heading">Tools & Technologies</div>', unsafe_allow_html=True)

sk1, sk2, sk3 = st.columns(3)
with sk1:
    st.markdown('<div class="tech-group-title">Data & Analytics</div>', unsafe_allow_html=True)
    for item in ["Python", "Pandas", "Streamlit", "SQL", "Excel"]:
        st.markdown(f'<span class="tech-pill">{item}</span>', unsafe_allow_html=True)

with sk2:
    st.markdown('<div class="tech-group-title">Development & Version Control</div>', unsafe_allow_html=True)
    for item in ["Git", "GitHub", "VS Code", "Java", "DBMS"]:
        st.markdown(f'<span class="tech-pill">{item}</span>', unsafe_allow_html=True)

with sk3:
    st.markdown('<div class="tech-group-title">Prototyping & Design</div>', unsafe_allow_html=True)
    for item in ["Arduino Uno", "IoT", "Blender 3D", "3D Printing", "CO2 Laser"]:
        st.markdown(f'<span class="tech-pill">{item}</span>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- PROJECTS SECTION ---
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow">03 / Selected Work</div>', unsafe_allow_html=True)
st.markdown('<div class="section-heading">Featured Projects</div>', unsafe_allow_html=True)

projects = [
    {
        "title": "Weather Analytics & Live Rainfall Dashboard",
        "status": "Live on GitHub",
        "desc": "Interactive real-time weather and rainfall monitoring platform fetching live meteorological data via the Open-Meteo API, complete with hourly trends and 7-day forecasts.",
        "tags": ["Python", "Streamlit", "Pandas", "Plotly", "REST API"],
        "code": "https://github.com/msanjukta/Weather-Analytics-Dashboard",
    },
    {
        "title": "Behavioral Finance & PLS-SEM Analysis",
        "status": "Research",
        "desc": "Quantitative econometric study examining investment behavior, job security, and retirement anxiety across public and private sector bank employees using PLS-SEM path modeling.",
        "tags": ["PLS-SEM", "Econometrics", "Statistical Modeling", "Excel"],
        "code": "https://github.com/msanjukta",
    },
    {
        "title": "Patent Specifications & Smart Systems R&D",
        "status": "Technical R&D",
        "desc": "Engineered system architectures, prior-art analyses, and technical specifications for predictive laser optics compensation, hybrid 3D print heads, and smart safety devices.",
        "tags": ["System Design", "Prior-Art Search", "CAD/Diagrams", "R&D"],
        "code": "https://github.com/msanjukta",
    },
    {
        "title": "Python Automation & CLI Applications",
        "status": "Completed",
        "desc": "Collection of modular Python tools including a menu-driven banking/ATM simulator, automated student report card generator, and procedural 3D geometry scripts in Blender.",
        "tags": ["Python", "Data Structures", "Blender Python", "CLI"],
        "code": "https://github.com/msanjukta",
    },
]

row1 = st.columns(2, gap="medium")
for idx, col in enumerate(row1):
    p = projects[idx]
    tags_html = "".join([f'<span class="mini-tag">{t}</span>' for t in p["tags"]])
    with col:
        st.markdown(f"""
        <div class="project-card">
            <div>
                <div class="project-header">
                    <span class="project-badge">{p["status"]}</span>
                </div>
                <div class="project-title">{p["title"]}</div>
                <div class="project-desc">{p["desc"]}</div>
            </div>
            <div>
                <div class="tag-row">{tags_html}</div>
                <a class="card-link" href="{p["code"]}" target="_blank">View Repository →</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

row2 = st.columns(2, gap="medium")
for idx, col in enumerate(row2):
    p = projects[idx + 2]
    tags_html = "".join([f'<span class="mini-tag">{t}</span>' for t in p["tags"]])
    with col:
        st.markdown(f"""
        <div class="project-card">
            <div>
                <div class="project-header">
                    <span class="project-badge">{p["status"]}</span>
                </div>
                <div class="project-title">{p["title"]}</div>
                <div class="project-desc">{p["desc"]}</div>
            </div>
            <div>
                <div class="tag-row">{tags_html}</div>
                <a class="card-link" href="{p["code"]}" target="_blank">View Repository →</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- RESEARCH PAPERS & PATENTS ---
st.markdown('<div id="publications"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow">04 / Research & IP</div>', unsafe_allow_html=True)
st.markdown('<div class="section-heading">Papers & Patents</div>', unsafe_allow_html=True)

tab_papers, tab_patents = st.tabs(["📄 Research Papers", "💡 Patents"])

with tab_papers:
    papers = [
        {
            "title": "EEG Signal Processing and Classification for Assistive Multi-DOF Robotic Control",
            "type": "Conference Paper • ACMESGA 2K26 (CRC Press)",
            "year": "Apr 2026",
            "desc": "Presented at the 2nd International Conference on Advances in Communication, Medical Electronics and Smart Grid Automation (ACMESGA 2K26), JIS College of Engineering, Kalyani.",
            "tags": ["EEG Signal Processing", "Brain-Computer Interface", "Assistive Robotics", "Classification"],
            "link": "",
        },
        {
            "title": "Involuntary Drainage Cleaning System",
            "type": "Journal Paper • JETIR (Vol. 12, Issue 6) • ID: JETIR2506130",
            "year": "Jun 2025",
            "desc": "Published in JETIR (ISSN: 2349-5162). Designed a solar-powered 12V DC rotary drainage cleaner with dual metallic blades, an NE555 timer circuit, and an LM311 charging comparator for automated urban sanitation.",
            "tags": ["Automation", "Mechatronics", "Solar Power", "JETIR"],
            "link": "http://www.jetir.org/view?paper=JETIR2506130",
        },
        {
            "title": "Electricity Generation from Plants",
            "type": "Journal Paper • IJCRT (Vol. 13, Issue 5) • ID: IJCRT2505623",
            "year": "May 2025",
            "desc": "Published in IJCRT (ISSN: 2320-2882). Modeled electrochemical ion flow in living-plant fuel cells using Zn–Cu electrodes in aloe vera leaves, demonstrating 60.4% efficiency at a 1 kΩ load vs. 2.67% at 1 MΩ.",
            "tags": ["Renewable Energy", "Bio-Electricity", "Electrochemistry", "IJCRT"],
            "link": "https://ijcrt.org/viewpaperforall.php?paper=IJCRT2505623",
        },
    ]

    for paper in papers:
        tags_html = "".join([f'<span class="mini-tag">{t}</span>' for t in paper["tags"]])
        link_html = f'<a class="card-link" href="{paper["link"]}" target="_blank">Read Paper</a>' if paper["link"] else ""
        st.markdown(f"""
        <div class="pub-card">
            <div class="pub-meta">
                <span class="pub-type">{paper["type"]}</span>
                <span class="pub-year">{paper["year"]}</span>
            </div>
            <div class="pub-title">{paper["title"]}</div>
            <div class="pub-desc">{paper["desc"]}</div>
            <div class="tag-row">{tags_html}</div>
            {link_html}
        </div>
        """, unsafe_allow_html=True)

with tab_patents:
    patents = [
        {
            "title": "Autonomous Underwater Surveillance Drone (AUSD)",
            "type": "Published Indian Patent • 202631069434 A",
            "year": "Jun 2026",
            "desc": "Self-sustaining autonomous underwater vehicle combining active/passive sonar, SLAM navigation for GPS-denied environments, an AI threat detection engine, encrypted telemetry, and an autonomous recharging dock.",
            "tags": ["Autonomous Robotics", "SLAM Navigation", "Maritime AI", "Sonar Sensing"],
        },
        {
            "title": "Advanced Dust-Attracting Broom Attachment for Household and Commercial Cleaning",
            "type": "Published Indian Patent • 202631069516 A",
            "year": "Jun 2026",
            "desc": "Detachable, washable broom head attachment utilizing electrostatic microfiber, triboelectric polymer mesh, and optional magnetic elements to trap fine dust and airborne particles during sweeping.",
            "tags": ["Product Design", "Electrostatic Materials", "Consumer Hardware", "Sustainability"],
        },
        {
            "title": "Eco-Friendly Edible Food Packaging Film Derived from Banana Stem Fibers",
            "type": "Published Indian Patent • 202631069293 A",
            "year": "Jun 2026",
            "desc": "Biodegradable, edible food packaging film formulated from agricultural-waste banana stem cellulose fibers, edible biopolymers, and natural antimicrobial/antioxidant agents to extend shelf life.",
            "tags": ["Sustainable Materials", "Biopolymers", "Food Tech", "Green R&D"],
        },
        {
            "title": "Adaptive Neural-Biofeedback Orthosis for Tremor Suppression",
            "type": "Published Indian Patent • 202631069265 A",
            "year": "Jun 2026",
            "desc": "Wearable closed-loop EMG-driven orthosis using a Predictive-Suppression Algorithm (PSA) and Variable Stiffness Actuators to anticipate and attenuate pathological tremors while preserving voluntary motion.",
            "tags": ["Biomedical AI", "EMG Signal Processing", "Wearable Robotics", "Closed-Loop Control"],
        },
        {
            "title": "Self-Healing Random-Access DNA Data Storage Architecture Using CRISPR-Indexed Memory Blocks and MEMS Microfluidic Control",
            "type": "Published Indian Patent • 202631068138 A",
            "year": "Jun 2026",
            "desc": "Ultra-dense molecular data storage system combining synthetic DNA memory blocks, programmable CRISPR-Cas random-access retrieval, MEMS microfluidic automation, and autonomous self-healing repair.",
            "tags": ["DNA Storage", "CRISPR-Cas", "MEMS Microfluidics", "Bio-Computing"],
        },
        {
            "title": "Smart Anti-Cheating System Using Wi-Fi Signal Distortion Detection",
            "type": "Published Indian Patent • 202631063134 A",
            "year": "May 2026",
            "desc": "Privacy-preserving anti-cheating framework using a Wi-Fi mesh network, Channel State Information (CSI), and ML anomaly detection to triangulate hidden electronic devices on a real-time heatmap dashboard.",
            "tags": ["Machine Learning", "Wi-Fi CSI", "RF Sensing", "Security Systems"],
        },
        {
            "title": "Smart Holographic Security System with Voice and Gesture-Controlled Authentication",
            "type": "Published Indian Patent • 202631053133 A",
            "year": "May 2026",
            "desc": "Contactless multimodal authentication system fusing dynamic 3D holographic projections with AI-driven voice and gesture biometric verification against encrypted templates.",
            "tags": ["Multimodal Biometrics", "Holography", "AI Security", "Access Control"],
        },
        {
            "title": "Neural Dust-Powered Brain-Computer Interface (BCI)",
            "type": "Published Indian Patent • 202631047364 A",
            "year": "Apr 2026",
            "desc": "Minimally invasive BCI utilizing ultraminiature (10–100 µm) wireless, battery-free piezoelectric neural dust nodes, ultrasonic backscatter power/data transfer, and real-time AI neural decoding.",
            "tags": ["Brain-Computer Interface", "Neural Dust", "Ultrasonic Telemetry", "AI Decoding"],
        },
        {
            "title": "Multisensory Puzzle Block Device for Dyslexia-Friendly Literacy and Numeracy Learning",
            "type": "Published Indian Patent • 202631016767 A",
            "year": "Apr 2026",
            "desc": "Modular interlocking learning blocks using asymmetrical geometry, tactile encoding, and an optional microcontroller sensor base to prevent letter reversals and deliver haptic/auditory feedback.",
            "tags": ["Assistive Tech", "Hardware Design", "Embedded Sensors", "EdTech"],
        },
        {
            "title": "Smart Self-Adjusting Ergonomic Chair with AI-Powered Posture Correction and Inbuilt Massager",
            "type": "Published Indian Patent • 202531057454 A",
            "year": "Jun 2025",
            "desc": "Fully offline AI-driven ergonomic chair combining embedded pressure/IMU sensors, silent actuators, and an inbuilt multi-mode massager for autonomous real-time posture correction.",
            "tags": ["Offline AI", "Embedded Systems", "Biomechanics", "Smart Furniture"],
        },
        {
            "title": "3D AI Painter for Enhanced Crime Investigation and Security Applications",
            "type": "Published Indian Patent • 202531017608 A",
            "year": "Mar 2025",
            "desc": "AI-powered 3D modeling system using NLP, machine learning, and computer vision to generate 3D facial reconstructions, crime scenes, and age-progressed images from descriptions with AR/VR support.",
            "tags": ["AI & NLP", "Computer Vision", "3D Modeling", "AR/VR"],
        },
        {
            "title": "AI-Backed Anti-Harassment System for Women with Wearable Safety Pendant",
            "type": "Published Indian Patent • 202531017617 A",
            "year": "Mar 2025",
            "desc": "Discreet wearable pendant integrating a 1080P camera, motion/audio/pressure sensors, onboard AI threat detection, stealth alerts, and wireless/solar charging.",
            "tags": ["Wearable IoT", "Edge AI", "Sensor Fusion", "Personal Safety"],
        },
    ]

    for pat in patents:
        tags_html = "".join([f'<span class="mini-tag">{t}</span>' for t in pat["tags"]])
        st.markdown(f"""
        <div class="pub-card">
            <div class="pub-meta">
                <span class="pub-type patent">{pat["type"]}</span>
                <span class="pub-year">{pat["year"]}</span>
            </div>
            <div class="pub-title">{pat["title"]}</div>
            <div class="pub-desc">{pat["desc"]}</div>
            <div class="tag-row">{tags_html}</div>
        </div>
        """, unsafe_allow_html=True)

# --- EXPERIENCE & MILESTONES ---
st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow">05 / Journey</div>', unsafe_allow_html=True)
st.markdown('<div class="section-heading">Experience & Highlights</div>', unsafe_allow_html=True)

st.markdown("""
<div class="timeline-item">
    <div class="timeline-date">August 2025 — Present</div>
    <div class="timeline-role">AICTE IDEA Lab Ambassador</div>
    <div class="timeline-org">JIS College of Engineering, Kalyani</div>
    <div class="timeline-desc">
        Spearheaded hands-on technical workshops, coordinated institutional outreach visits
        for visiting schools and colleges, and managed student internship programs alongside
        industrial exposure visits.
    </div>
</div>
<div class="timeline-item">
    <div class="timeline-date">January 2025 — Present</div>
    <div class="timeline-role">IIC Innovation Ambassador</div>
    <div class="timeline-org">Institution's Innovation Council (IIC), JIS College of Engineering</div>
    <div class="timeline-desc">
        Managed institutional documentation, compiled structured event and innovation activity
        reports, maintained participant records, and supported compliance reporting for IIC initiatives.
    </div>
</div>
<div class="timeline-item">
    <div class="timeline-date">December 2024 — June 2025</div>
    <div class="timeline-role">AICTE IDEA Lab Student Coordinator</div>
    <div class="timeline-org">JIS College of Engineering, Kalyani</div>
    <div class="timeline-desc">
        Coordinated hands-on internship programs on Advanced Prototyping and Fabrication Technologies, leading technical training sessions on 3D printing, CO2 laser cutting, CNC milling, and Arduino/IoT for visiting polytechnic students, alongside organizing industrial exposure visits.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- EDUCATION SECTION ---
st.markdown('<div id="education"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow">06 / Academic Background</div>', unsafe_allow_html=True)
st.markdown('<div class="section-heading">Education</div>', unsafe_allow_html=True)

education = [
    {
        "degree": "B.Tech in Computer Science & Engineering (AI & ML)",
        "institution": "JIS College of Engineering, Kalyani, West Bengal",
        "year": "2024 — 2028 (Pursuing)",
        "details": "Coursework in Python Programming, Database Management Systems (DBMS), Operating Systems, Machine Learning, and Statistical Modeling. Active AICTE IDEA Lab Ambassador & IIC Innovation Ambassador.",
    },
    {
        "degree": "Higher Secondary (Class XII)",
        "institution": "Midnapore Mission Girls' High School, Board: WBCHSE",
        "year": "2023",
        "details": "Science Stream (Physics, Chemistry, Mathematics, Computer Application). Score: 80%",
    },
    {
        "degree": "Secondary (Class X)",
        "institution": "Midnapore Mission Girls' High School, Board: WBBSE",
        "year": "2021",
        "details": "Score: 78.71%",
    },
]

for edu in education:
    st.markdown(f"""
<div class="pub-card">
<div class="pub-meta">
<span class="pub-type">{edu["institution"]}</span>
<span class="pub-year">{edu["year"]}</span>
</div>
<div class="pub-title">{edu["degree"]}</div>
<div class="pub-desc">{edu["details"]}</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- CONTACT SECTION ---
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow">07 / Connect</div>', unsafe_allow_html=True)
st.markdown('<div class="section-heading">Let\'s Work Together</div>', unsafe_allow_html=True)

c_left, c_right = st.columns([1, 1.2], gap="large")

with c_left:
    st.markdown("""
    <p style="color:#a1a1aa; font-size:1rem; line-height:1.7;">
        Have an internship opportunity, data analytics project, or collaboration in mind?
        Send a message using the form or reach out directly.
    </p>
    <p style="margin-top:1.5rem; color:#d4d4d8; line-height:1.9;">
        <strong>Email:</strong> sanjukta2005123@gmail.com<br>
        <strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/sanjukta245" target="_blank" style="color:#c084fc; text-decoration:none;">linkedin.com/in/sanjukta245</a><br>
        <strong>GitHub:</strong> <a href="https://github.com/msanjukta" target="_blank" style="color:#c084fc; text-decoration:none;">github.com/msanjukta</a><br>
        <strong>Location:</strong> West Bengal, India
    </p>
    """, unsafe_allow_html=True)

with c_right:
    # Real email delivery powered by FormSubmit (free, no backend needed)
    st.markdown("""
    <form class="contact-form" action="https://formsubmit.co/sanjukta2005123@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" rows="4" placeholder="Tell me about your project or opportunity..." required></textarea>
        <button type="submit">Send Message</button>
    </form>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div style="text-align:center; color:#52525b; font-size:0.85rem; margin-top:4rem; padding-top:1.5rem; border-top:1px solid #18181b;">
    Built with Python & Streamlit  •  © 2026 Sanjukta Mandal
</div>
""", unsafe_allow_html=True)