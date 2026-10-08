import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

pdf_path = "resume.pdf"
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    rightMargin=36,
    leftMargin=36,
    topMargin=36,
    bottomMargin=36
)

styles = getSampleStyleSheet()

# Colors
navy = colors.HexColor("#0f172a")
primary_blue = colors.HexColor("#2563eb")
dark_gray = colors.HexColor("#334155")
light_gray = colors.HexColor("#64748b")
accent = colors.HexColor("#4f46e5")
rule_color = colors.HexColor("#cbd5e1")

# Custom Styles
title_style = ParagraphStyle(
    'DocTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=20,
    leading=24,
    textColor=navy,
    alignment=0
)

subtitle_style = ParagraphStyle(
    'DocSubtitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=14,
    textColor=accent,
    alignment=0
)

contact_style = ParagraphStyle(
    'ContactText',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=12,
    textColor=dark_gray,
    alignment=0
)

section_heading = ParagraphStyle(
    'SectionHeading',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10.5,
    leading=14,
    textColor=navy,
    spaceBefore=4,
    spaceAfter=2
)

body_style = ParagraphStyle(
    'Body',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=11.5,
    textColor=dark_gray
)

bold_label = ParagraphStyle(
    'BoldLabel',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=8.5,
    leading=11.5,
    textColor=navy
)

bullet_style = ParagraphStyle(
    'Bullet',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.2,
    leading=11,
    textColor=dark_gray,
    leftIndent=10
)

elements = []

# Header
elements.append(Paragraph("YASHICA M", title_style))
elements.append(Paragraph("Artificial Intelligence & Data Science Engineer (Honors)", subtitle_style))
elements.append(Spacer(1, 4))

contact_text = (
    "<b>Email:</b> yashica586@gmail.com &nbsp;|&nbsp; "
    "<b>LinkedIn:</b> linkedin.com/in/yashica-m-586-leadingstar &nbsp;|&nbsp; "
    "<b>GitHub:</b> github.com/yashica-tech-flare &nbsp;|&nbsp; "
    "Madurai, TN, India"
)
elements.append(Paragraph(contact_text, contact_style))
elements.append(Spacer(1, 6))
elements.append(HRFlowable(width="100%", thickness=1.5, color=accent, spaceBefore=2, spaceAfter=6))

# Profile Summary
elements.append(Paragraph("PROFESSIONAL SUMMARY", section_heading))
summary_text = (
    "Final-year B.Tech AI & Data Science (Honors) student (CGPA: 8.41/10) with 2 peer-reviewed publications "
    "and a research internship at IIT Jammu. Skilled in applied machine learning, convolutional neural networks (CNNs), "
    "Gemini LLM API integration, and full-stack web applications. Seeking entry-level AI/ML, Software Development, "
    "or Data Engineering roles."
)
elements.append(Paragraph(summary_text, body_style))
elements.append(Spacer(1, 6))

# Education
elements.append(Paragraph("EDUCATION", section_heading))
edu_data = [
    [
        Paragraph("<b>B.Tech in Artificial Intelligence & Data Science (Honors)</b><br/>K.L.N. College of Engineering (Affiliated to Anna University)", body_style),
        Paragraph("<b>2023 – 2027</b><br/><b>CGPA: 8.41 / 10</b> (through 6th sem)", ParagraphStyle('R', parent=body_style, alignment=2))
    ],
    [
        Paragraph("<b>Higher Secondary Certificate (Class XII)</b><br/>Annamalaiyaar Matriculation Higher Secondary School, Madurai", body_style),
        Paragraph("<b>2023</b><br/><b>Percentage: 82.83%</b>", ParagraphStyle('R2', parent=body_style, alignment=2))
    ]
]
edu_table = Table(edu_data, colWidths=[4.2*inch, 3.1*inch])
edu_table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ('TOPPADDING', (0,0), (-1,-1), 1),
    ('LEFTPADDING', (0,0), (-1,-1), 0),
    ('RIGHTPADDING', (0,0), (-1,-1), 0),
]))
elements.append(edu_table)
elements.append(Spacer(1, 6))

# Experience & Research
elements.append(Paragraph("EXPERIENCE & RESEARCH INTERNSHIPS", section_heading))

exp1_title = [
    [
        Paragraph("<b>Research Intern</b> — <i>RISE UP 2026, IIT Jammu</i>", bold_label),
        Paragraph("<b>Jun 2026 – Jul 2026</b>", ParagraphStyle('ExpDate', parent=body_style, alignment=2))
    ]
]
t1 = Table(exp1_title, colWidths=[5.3*inch, 2.0*inch])
t1.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('PADDING', (0,0), (-1,-1), 0)]))
elements.append(t1)
elements.append(Paragraph("• Investigated heat transport in additively manufactured TPMS (Triply Periodic Minimal Surfaces) lattice structures for prosthetic socket thermal management.", bullet_style))
elements.append(Paragraph("• Implemented infrared thermography, heat-flux sensing calibration, and ML analysis using Supervised, Unsupervised, and Physics-Informed Neural Networks (PINN).", bullet_style))
elements.append(Paragraph("• Delivered peer-evaluated poster presentation at IIT Jammu RISE UP research symposium.", bullet_style))
elements.append(Spacer(1, 4))

exp2_title = [
    [
        Paragraph("<b>In-House Internship cum Project Work</b> — <i>K.L.N. IRP</i>", bold_label),
        Paragraph("<b>Jan 2025 – Dec 2025</b>", ParagraphStyle('ExpDate2', parent=body_style, alignment=2))
    ]
]
t2 = Table(exp2_title, colWidths=[5.3*inch, 2.0*inch])
t2.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('PADDING', (0,0), (-1,-1), 0)]))
elements.append(t2)
elements.append(Paragraph("• Engineered structured beginner-to-expert learning stages, aptitude evaluation modules, and technical interview simulations for an AI career guidance platform.", bullet_style))
elements.append(Paragraph("• Architected company-specific technical round dashboards, candidate scoring pipelines, and analytics reporting.", bullet_style))
elements.append(Spacer(1, 4))

exp3_title = [
    [
        Paragraph("<b>AI (Python) Intern</b> — <i>SkillForge</i>", bold_label),
        Paragraph("<b>Dec 2024 – Jan 2025</b>", ParagraphStyle('ExpDate3', parent=body_style, alignment=2))
    ]
]
t3 = Table(exp3_title, colWidths=[5.3*inch, 2.0*inch])
t3.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('PADDING', (0,0), (-1,-1), 0)]))
elements.append(t3)
elements.append(Paragraph("• Built, tuned, and evaluated supervised ML classification and regression models in Python.", bullet_style))
elements.append(Paragraph("• Automated dataset preprocessing, EDA visualizations, and cross-validation pipelines with Scikit-learn and Pandas.", bullet_style))
elements.append(Spacer(1, 6))

# Publications
elements.append(Paragraph("PUBLICATIONS", section_heading))
elements.append(Paragraph("• <b>AI NEWUS: An AI-Powered Career Guidance and Placement Preparation Platform</b><br/><i>International Journal of Computer &amp; Organization Trends (IJCOT)</i> — May 2026", bullet_style))
elements.append(Spacer(1, 2))
elements.append(Paragraph("• <b>Federated Learning-Based Recommender System with Data Anonymization and Encryption</b><br/><i>International Journal of Emerging Engineering Trends &amp; Research (IJEETR)</i> — March 2026", bullet_style))
elements.append(Spacer(1, 6))

# Projects
elements.append(Paragraph("KEY PROJECTS", section_heading))
elements.append(Paragraph("• <b>AI Newus — Career Guidance &amp; Placement Readiness Web Platform</b> | <i>React, Node.js, MongoDB, Python</i><br/>Full-stack platform delivering tiered career learning stages, interactive aptitude benchmarks, mock interview simulation, and company-specific assessment dashboards.", bullet_style))
elements.append(Spacer(1, 2))
elements.append(Paragraph("• <b>CVInsightAI — AI Resume Analyzer &amp; ATS Optimizer</b> | <i>Python, Streamlit, Gemini API, PyPDF, gTTS</i><br/>Interactive ATS analyzer parsing resumes against job descriptions, identifying critical keyword gaps, and generating text-to-speech audio feedback for job seekers.", bullet_style))
elements.append(Spacer(1, 2))
elements.append(Paragraph("• <b>Fashion-MNIST Classifier — Deep Convolutional Neural Network</b> | <i>TensorFlow, Keras, NumPy, Matplotlib</i><br/>Trained custom CNN architecture classifying 10 apparel categories with &gt;93% validation accuracy, confusion matrix analysis, and epoch loss visualizations.", bullet_style))
elements.append(Spacer(1, 6))

# Skills
elements.append(Paragraph("TECHNICAL SKILLS", section_heading))
skills_data = [
    [Paragraph("<b>Programming Languages:</b>", bold_label), Paragraph("Python, Java, C, JavaScript, SQL", body_style)],
    [Paragraph("<b>AI / Machine Learning:</b>", bold_label), Paragraph("Machine Learning, CNNs, PINN, TensorFlow, Keras, Scikit-learn, LLM API (Gemini)", body_style)],
    [Paragraph("<b>Data Science:</b>", bold_label), Paragraph("Pandas, NumPy, Matplotlib, Seaborn, Data Cleaning, EDA, Data Visualization", body_style)],
    [Paragraph("<b>Web &amp; Automation:</b>", bold_label), Paragraph("React.js, Node.js, Streamlit, n8n, HTML5, CSS3, REST APIs", body_style)],
    [Paragraph("<b>Databases &amp; Tools:</b>", bold_label), Paragraph("MySQL, MongoDB, PostgreSQL, Git, GitHub, Jupyter, Google Colab, Anaconda", body_style)]
]
skills_table = Table(skills_data, colWidths=[1.8*inch, 5.5*inch])
skills_table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ('TOPPADDING', (0,0), (-1,-1), 1),
    ('LEFTPADDING', (0,0), (-1,-1), 0),
    ('RIGHTPADDING', (0,0), (-1,-1), 0),
]))
elements.append(skills_table)
elements.append(Spacer(1, 6))

# Honors & Achievements
elements.append(Paragraph("HONORS &amp; ACHIEVEMENTS", section_heading))
elements.append(Paragraph("• <b>Rank 1</b> — Foundation for Data Science (KLNCE, 1st Year Academic Excellence 2023–2024)", bullet_style))
elements.append(Paragraph("• <b>Elite + Silver Certificate</b> — NPTEL Human-Computer Interaction (IIT Delhi)", bullet_style))
elements.append(Paragraph("• <b>Skillrack Coding Excellence</b> — 500+ problems solved, 700+ points scored", bullet_style))

doc.build(elements)
print("resume.pdf generated successfully.")
