import tempfile
from datetime import date, datetime
from pathlib import Path

import streamlit as st

from core.audio.transcriber import transcribe_audio
from medstruct_ai.core.schemas import ClinicalInsight, PatientRecord
from medstruct_ai.db.database import get_patient_record, init_db, insert_patient_record

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

    upload_type = st.radio("Select input type", ["Audio Note (.wav)"])

    if upload_type == "Audio Note (.wav)":
        uploaded_file = st.file_uploader(
            "Choose a WAV audio file", type=["wav"]
        )

        if uploaded_file is not None:
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
                tmp.write(uploaded_file.read())
                tmp_path = tmp.name

            with st.spinner("Transcribing audio..."):
                try:
                    transcription = transcribe_audio(tmp_path)
                    st.success("Transcription complete")
                    st.text_area("Transcribed Text", transcription, height=200)

                    st.divider()
                    st.subheader("Save to Patient Record")

                    col1, col2 = st.columns(2)
                    with col1:
                        first_name = st.text_input("First Name")
                        last_name = st.text_input("Last Name")
                    with col2:
                        dob = st.date_input("Date of Birth", value=date(1980, 1, 1))
                        visit_date = st.date_input("Visit Date", value=date.today())

                    if st.button("Save Transcription"):
                        if not first_name or not last_name:
                            st.error("First name and last name are required.")
                        else:
                            record = PatientRecord(
                                first_name=first_name.strip(),
                                last_name=last_name.strip(),
                                dob=dob,
                                insights=[
                                    ClinicalInsight(
                                        visit_date=visit_date,
                                        notes=transcription,
                                    )
                                ],
                            )
                            pid = insert_patient_record(record)
                            st.success(
                                f"Saved transcription for {first_name} {last_name} "
                                f"(Patient ID: {pid})"
                            )
                except Exception as e:
                    st.error(f"Transcription failed: {e}")
                finally:
                    Path(tmp_path).unlink(missing_ok=True)
