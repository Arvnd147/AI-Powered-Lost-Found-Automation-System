import streamlit as st
import requests

backend_url = "http://127.0.0.1:8000"

st.title("🔍 Lost & Found Automation System")

st.subheader("1️⃣ Upload Image & Detect Lost Item")

image_url = st.text_input("Enter Image URL:")

if st.button("Detect Item"):
    response = requests.post(f"{backend_url}/detect_lost_item/", json={"image_url": image_url})
    if response.status_code == 200:
        st.write("📌 Detected Objects:", response.json()["detected_objects"])
    else:
        st.error("Error detecting object.")

st.subheader("2️⃣ Report a Lost Item")

name = st.text_input("Your Name")
roll_number = st.text_input("Roll Number")
description = st.text_area("Describe the lost item")

if st.button("Submit Lost Item"):
    response = requests.post(f"{backend_url}/submit_lost_item/", json={
        "uploaded_by": name, "roll_number": roll_number, "description": description, "image_url": image_url
    })
    if response.status_code == 200:
        st.success("✅ Lost item reported successfully!")
    else:
        st.error("Failed to report lost item.")