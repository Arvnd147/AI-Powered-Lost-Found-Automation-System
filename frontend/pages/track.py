import streamlit as st
import requests

backend_url = "http://127.0.0.1:8000"

st.title("📌 Track Your Grievance")

ticket_id = st.text_input("Enter Ticket ID:")

if st.button("Track Status"):
    response = requests.get(f"{backend_url}/track/{ticket_id}")
    data = response.json()

    if "error" in data:
        st.error("❌ Ticket not found!")
    else:
        st.write("📝 Description:", data["description"])
        st.write("📍 Status:", data["status"])
