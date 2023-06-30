from pathlib import Path

import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir/"styles"/"main.css"
resume_file = current_dir/"assets"/"cv.pdf"
profile_pic = current_dir/"assets"/"profile-pic.png"

# --- General Setting --- #

PAGE_TITLE = "Digital CV | Tathagata Basu"
PAGE_ICON = ":wave:"
NAME = "Tathagata Basu"
DESCRIPTION = """QA ENGINEER || DATA ANALYST"""
EMAIL = "tgbasu89@gmail.com"
SOCIAL_MEDIA = dict(LinkedIn="https://www.linkedin.com/in/basutathagata/",
                    GitHub="https://github.com/tgbasu/MachineLearningModels",
                    Twitter="https://twitter.com/logxdx")
PROJECTS = {

}

st.set_page_config(page_title=PAGE_TITLE,page_icon="PAGE_ICON")
st.title("Welcome Aboard")


# --- Load CSS,PDF & PROFIL PIC ---#
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html = True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---##
col1, col2 = st.columns(2, gap = "small")
with col1:
    st.image(profile_pic,width = 230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = " Download Resume",
        data = PDFbyte,
        file_name=resume_file.name,
        mime = "application/octet-stream",
    )
    st.write(" ", EMAIL)


# --- SOCIAL LINKS --- #

    st.write("#")
    cols = st.columns(len(SOCIAL_MEDIA))
    index: int
    for index, (platform,link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")

    # --- Experience & Qualifications---

    st.write("#")
    st.subheader("Experience & Qualifications")
    st.write(
        """
        - collaborate with cross-functional teams to identify opportunities 
        - collect and analyze data, and build predictive models \n
        - to drive data-driven decision-making \n
        
        """
    )

    #---sKILLS---
    st.write("#")
    st.subheader("Skills")
    st.write(
        """
        - Strong Statistical and Analytical Skills
        - Programming Skills 
        - Machine Learning and Data Modeling
        - Data Visualization
        - Domain Knowledge. 
        """
    )
    # --- work history
    # ---sKILLS---
    st.write("#")
    st.subheader("Work History")
    st.write(
        """
        - Oracle 
        - Accenture 
        - ABiNbEV
        - vmWARE
        - Ascendum
        """
    )
















