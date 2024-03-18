import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
st.set_page_config(page_title="AIML - A",page_icon=":🤖:",layout="wide")

with st.container():
    st.title("B.TECH AI&ML 2022-2026")
    st.subheader("Welcome to AIML - A's web portal :wave:")

lottie_coding = "https://lottie.host/d9031a8b-0fce-47db-9b79-5567c89037e9/H4Z3BRmkCm.json"
img_contact_form=Image.open("Images/pancake.png")
img_lottie_animation=Image.open("Images/peach.png")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


with st.container():
    st.write("---")
    left_column, right_column=st.columns(2)
    with left_column:
        st.header("Class Notes")
        st.write("##")
        st.subheader("Current semester's subjects")
        subjects="""<p>1. Computer Networks<br>2. Computer Organisation and Architecture<br>3. Mathematics - 4<br>4. Environmental science<br>5. Personality development - 2<br>6. Database management system<br>7. Programming for AIML</p>"""
        st.markdown(subjects, unsafe_allow_html=True)
        st.write("[Upload class notes >](https://www.discord.com)")
        st.write("[View class notes >](https://www.discord.com)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


with st.container():
    st.write("---")
    st.header("Contact")
    st.write("##")
    contact_form="""<form action="https://formsubmit.co/jabez123jaze@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="Message" placeholder="Your message" required></textarea>
     <button type="submit">Send</button></form>"""
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
