import streamlit as st

from medstruct_ai.db.database import init_db

st.set_page_config(page_title="MedStruct AI", layout="wide")

init_db()

st.title("MedStruct AI")
st.markdown("Offline-first clinical intelligence system")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Patient Records", "Upload"])

if page == "Dashboard":
    st.header("Dashboard")
    st.info("Health charts and risk overview will appear here.")

elif page == "Patient Records":
    st.header("Patient Records")
    st.info("Patient list and timeline view will appear here.")

elif page == "Upload":
    st.header("Upload Medical Data")
    st.info("Audio, PDF, and image uploaders will appear here.")
