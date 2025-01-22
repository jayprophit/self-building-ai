import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit app
st.title("Self-Building AI Interface")

st.sidebar.header("Navigation")
options = ["Home", "Code Fixer", "Preview"]
choice = st.sidebar.selectbox("Choose a feature", options)

if choice == "Home":
    st.write("Welcome to the Self-Building AI Interface!")
    st.write("Use the sidebar to navigate.")
elif choice == "Code Fixer":
    st.header("Code Fixer")
    user_input = st.text_area("Enter the error message here:")
    if st.button("Fix Error"):
        if user_input:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Fix the following error: {user_input}",
                max_tokens=100
            )
            fix = response.choices[0].text.strip()
            st.write("Suggested Fix:")
            st.code(fix)
        else:
            st.warning("Please enter an error message.")
elif choice == "Preview":
    st.header("Preview Area")
    st.write("Here, you can visualize your project.")
