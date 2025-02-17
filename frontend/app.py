import streamlit as st
import requests

# Backend URL
backend_url = "http://127.0.0.1:8000"

# Page Configuration
st.set_page_config(page_title="Grievance Portal", page_icon="🏛")

st.title("🎓 AI-Powered Grievance & Lost & Found Portal")

st.sidebar.title("Navigation")
st.sidebar.page_link("pages/chat.py", label="💬 Chat with AI")
st.sidebar.page_link("pages/track.py", label="📌 Track Grievance")
st.sidebar.page_link("pages/lost_found.py", label="🔍 Lost & Found")

# ----------- Grievance Submission Form -----------
st.header("📝 Submit a Grievance")

name = st.text_input("Your Name")
roll_number = st.text_input("Roll Number")
category = st.selectbox("Category", ["Academics", "Hostel", "Administration", "Technical", "Other"])
description = st.text_area("Describe your issue")

if st.button("Submit Grievance"):
    response = requests.post(f"{backend_url}/submit_grievance/", json={
        "name": name,
        "roll_number": roll_number,
        "category": category,
        "description": description
    })
    
    if response.status_code == 200:
        ticket_id = response.json().get("ticket_id")
        st.success(f"✅ Grievance submitted successfully! Your Ticket ID: {ticket_id}")
    else:
        st.error("❌ Failed to submit grievance. Try again!")
