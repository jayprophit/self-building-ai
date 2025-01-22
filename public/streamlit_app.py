import streamlit as st
import openai
from dotenv import load_dotenv
import os
import streamlit.components.v1 as components

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set the title of the app
st.title("Self-Building AI Interface")

# Sidebar for navigation
st.sidebar.header("Navigation")
options = ["Home", "Code Fixer", "Preview"]
choice = st.sidebar.selectbox("Choose a feature", options)

# Home Page
if choice == "Home":
    st.write("Welcome to the Self-Building AI Interface!")
    st.write("Use the sidebar to navigate and interact with the system.")

# Code Fixer
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

# Preview Area (for visualizing designs, code, etc.)
elif choice == "Preview":
    st.header("Preview Area")
    st.write("Here, you can visualize your project.")

    # User input area for HTML, CSS, or other code to preview
    code_input = st.text_area("Enter your HTML/CSS code to preview:")

    if st.button("Render Preview"):
        if code_input:
            components.html(code_input, height=400)
        else:
            st.warning("Please enter HTML/CSS code to preview.")

    st.subheader("Additional Preview Options")
    st.write("Here, you can also explore different project types.")
    project_type = st.selectbox("Select a project type to preview", ["Website", "App", "Game", "3D Model"])

    if project_type == "Website":
        st.write("This will preview the website code.")
    elif project_type == "App":
        st.write("This will preview the app design.")
    elif project_type == "Game":
        st.write("This will preview the game design.")
    elif project_type == "3D Model":
        st.write("This will preview the 3D model.")
