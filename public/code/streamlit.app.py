import streamlit as st

st.title("Self-Building AI Interface")
st.sidebar.header("Navigation")

options = ["Home", "Subscriptions", "Logs"]
choice = st.sidebar.selectbox("Go to", options)

if choice == "Home":
    st.write("Welcome to the Self-Building AI App!")
    st.write("Use this interface to manage the AI system.")
elif choice == "Subscriptions":
    st.write("Manage user subscriptions here.")
elif choice == "Logs":
    st.write("View system logs here.")