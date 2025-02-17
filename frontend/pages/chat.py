import streamlit as st
import requests

backend_url = "http://127.0.0.1:8000"

st.title("💬 AI Chatbot for Grievance Assistance")

user_query = st.text_area("Describe your issue and get AI assistance:")

if st.button("Submit Query"):
    response = requests.post(f"{backend_url}/chat/", json={"user_query": user_query})
    if response.status_code == 200:
        st.write("🧠 AI Response:", response.json()["reply"])
    else:
        st.error("❌ Error fetching AI response. Try again!")
