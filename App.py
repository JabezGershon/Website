import streamlit as st
from PIL import Image
import requests
import pickle
from pathlib import Path
from streamlit_lottie import st_lottie
import streamlit_authenticator as stauth
st.set_page_config(page_title="AIML - A",page_icon=":🤖:",layout="wide")
names = ["Gershon","Jabez"]
usernames = ["G_.bez","Jayz"]

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
"App", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    with st.container():
            st.title("B.TECH AI&ML 2022-2026")
            st.subheader("Welcome to AIML - A's web portal :wave:")
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
            lottie_coding = "https://lottie.host/d9031a8b-0fce-47db-9b79-5567c89037e9/H4Z3BRmkCm.json"
            img_contact_form=Image.open("Images/pancake.png")
            img_lottie_animation=Image.open("Images/peach.png")
            st.header("Class Notes")
            st.write("[Upload class notes >](https://www.discord.com)")
            st.write("[View class notes >](https://www.discord.com)")
            st.write("##")
            st.header("Current semester's subjects")
            subjects="""<p>1. Computer Networks<br>2. Computer Organisation and Architecture<br>3. Mathematics - 4<br>4. Environmental science<br>5. Personality development - 2<br>6. Database management system<br>7. Programming for AIML</p>"""
            st.markdown(subjects, unsafe_allow_html=True)
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

    
