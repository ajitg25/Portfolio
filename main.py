import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image
from pathlib import Path
from streamlit_lottie import st_lottie

PAGE_TITLE = "Portfolio | Ajit Gupta"
PAGE_ICON = ":wave:"

st.set_page_config(layout="wide",page_title=PAGE_TITLE, page_icon=PAGE_ICON)

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "AjitGupta.pdf"
css_file = current_dir / "styles" / "main.css"
EMAIL = "ajitg131@email.com"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/ajit-gupta25/",
    "GitHub": "https://github.com/ajitg25",
    "LeetCode": "https://leetcode.com/ajitg131/",
    "CodeForces": "https://codeforces.com/profile/ajit_25",
    "CodeChef" : "https://www.codechef.com/users/ajit_25_2"
}

def loadUrl(url):
    response=requests.get(url)
    if response.status_code!=200:
        return None
    return response.json()

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()


coder= loadUrl("https://lottie.host/120d4a92-ef4c-4b54-8d52-f965069e45ba/L8meiSr4kh.json")
contact_us= loadUrl("https://lottie.host/50af316e-8f92-46c2-94d3-ca354369d1a4/5oPpKCzznQ.json")
profile_pic = loadUrl("https://lottie.host/29721b90-34fe-4554-bf91-0391f38ed6c9/kRoX3IZIw2.json")



col1,col2=st.columns((2,1))
with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Hello World!!! :wave:")
            st.header("""I am Ajit Gupta, """)
            st.subheader("Welcome To My Data-Driven Wonderland :)")
            st.write("##")
            st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
             )
            st.write("📫", EMAIL)
            st.write('\n')
            cols = st.columns(len(SOCIAL_MEDIA))
            for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
                cols[index].write(f"[{platform}]({link})")
            with col2:
             st_lottie(profile_pic,height=300)
st.write("##")


st.write("---")

with st.container():
    selected=option_menu(
        menu_title=None,
        options=['About','Projects','Contact'],
        icons=['person','code-slash','chat-left-text-fill'],
        orientation='horizontal'
        )
if selected =='About':
    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st_lottie(coder)
        with col4:
            st.write('##')
            st.write("""## Unveiling My Arsenal 

Here's a glimpse of what I bring to the tech table:

🐍 Python Power

🔮 Machine Learning Magician

📊 Data Sorcery

🌐 Web Wizardry

⛓️ Hackathon Winner

💻 Code Conjurer

🔧 Problem-Solving C++ Sorcerer

🎨 Art of Visualization

🚀 Lifelong Learner

So, let's embark on a magical journey together and witness the wonders we can create with technology!
""")
            
   
    st.write("---")  
    with st.container():
        st.header('Work Experiences :')
        st.write("##")
        st.subheader("""
►SDE Intern @ Hinge Health
    -Time Period : Aug 2023 - PRESENT 
    -Bengaluru, Karnataka, India · Remote
    -Working as a ML engineer intern.
                     """)  
        st.write("##")
        st.write("##")
        st.subheader("""
►R&D Intern @  SAMSUNG PRISM
    -Time Period : Dec 2022 - Jun 2023
    -Bengaluru, Karnataka, India · Hybrid
    - Developed a machine learning model to predict the best WiFi access point and exposed it as an API using Flask.
    - Developed an Android app which selects the best wifi-access point.
""")
        st.write("##")
        st.write("##")
        st.subheader("""
►ML Intern @ G-KnowMe 
    -Time Period : Nov 2022-Dec 2022
    -Bengaluru, Karnataka, India · Hybrid
    -Developed an OCR module using OpenCV and Pytesseract to accurately extract medical report details, with a
        specific focus on extracting tabular data directly to a CSV.
    - Created a Flask API that accepts images as input and returns the extracted data in JSON format.
                     """)
        st.write("##")
        st.write("##")
        st.subheader("""
►R&D Intern @ Dassault Systemes La Foundation
    -Time Period : Mar 2022-Aug 2022
    -Bengaluru, Karnataka, India · Hybrid
    - Explored and compared different YOLO models and experimented with a CNN-based approach in a project aimed
        at optimizing object detection performance.
    -Developed and deployed models on Raspberry Pi for shrimp identification and disease prediction, enabling real-time decision-making in aquaculture.
                     """)
    st.write("---")  
    st.write("---") 
    with st.container():
        st.header('Education :') 
        st.subheader("""
►BMS COLLEGE OF ENGINEERING
    -B.TECH @ EEE,
    -Time Period : 2020-2024
    -Bengaluru, Karnataka, India 
    - CGPA - 9.2/10
    """) 
    

if selected == 'Projects':
    with st.container():
        st.header('MY Projects')
        st.write('##')
        st.subheader(f"[🏆 Thera-Buddy](https://github.com/ajitg25/Thera-Buddy)")
        st.write(f"[Developed an neural network model which predicts the suicidal/depressing nature and deployed the model on Flask API.Developed a chrome extension which tracks user keyboard input in the browser and analyzes the text using the Flask API.A chat-bot powered by dialogflow appears for depressed people.](https://github.com/ajitg25/Thera-Buddy)")
        
        st.write('##')
        
        st.subheader(f"[🏆 PharmaBot (e-yantra,IITB)](https://github.com/ayushsh314/eyrc22_PB_1976)")
        st.write(f"[Implemented OpenCV to recognize roads, start and end points, and dynamically directed the delivery of unique packages to their respective destinations in a project. Utilized CoppeliaSim as the simulation environment for testing and evaluating the project.](https://github.com/ayushsh314/eyrc22_PB_1976)")
        
        st.write('##')

if selected=='Contact':
    st.header("Get In Touch")
    st.write('##')
    st.write('##')
    
    contact_form="""
  <form target="_blank" action="https://formsubmit.co/ajitg131@gmail.com" method="POST">
     <input type="text" name="name" class="form-control" placeholder="Enter Your Full Name"  required>
     
     <input type="email" name="email" class="form-control" placeholder="Enter Your Email Address"  required>   
     
    <textarea type="message" placeholder="Enter Your Message" class="text_area" name="input_message"  rows="10" required></textarea>
     
    <button type="submit" class="btn" >Send</button>
       
  </form>
    """
    left_col, right_col= st.columns((2,1))
    with left_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_col:
        st_lottie(contact_us, height=300)
        
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
