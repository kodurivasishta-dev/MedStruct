# MedStruct AI - GitLab Issues

| Issue ID | Title | Description | Assignee | Est. Time (Hours) | Due Date (Hackathon Day Timeline) | Milestone |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #1 | Cache Models & Setup Ollama | Download Q4 GGUF models and configure local Ollama instance with custom Modelfile. | Nikhil | 2 | Day 1 - 10:00 AM | Phase 1 |
| #2 | Compile whisper.cpp | Clone and build whisper.cpp locally with CPU optimization flags (AVX2). | Nikhil | 1 | Day 1 - 11:00 AM | Phase 1 |
| #3 | Scaffold App & DB Init | Create Streamlit app shell and SQLite schema creation scripts (init_db.py). | Vasishta | 2 | Day 1 - 12:00 PM | Phase 1 |
| #4 | Audio Ingestion Pipeline | Write Python wrapper to pass uploaded audio to whisper.cpp and retrieve text. | Nikhil | 3 | Day 1 - 04:00 PM | Phase 2 |
| #5 | VLM Image Extraction | Engineer prompts and pipeline to pass prescription images to local VLM for parsing. | Nikhil | 3 | Day 1 - 07:00 PM | Phase 2 |
| #6 | UI File Uploaders | Implement Streamlit components for drag-and-drop of PDFs, images, and audio. | Vasishta | 2 | Day 1 - 05:00 PM | Phase 2 |
| #7 | Pydantic Schema Layer | Define core data models (PatientRecord, LabMetric) using Pydantic v2. | Vasishta | 2 | Day 2 - 09:00 AM | Phase 3 |
| #8 | SQLite ORM Mapping | Write functions to map validated Pydantic objects to SQLite table inserts. | Vasishta | 3 | Day 2 - 12:00 PM | Phase 3 |
| #9 | LLM Structural Constraint | Implement retry logic/constrained generation so LLM outputs match Pydantic schemas. | Nikhil | 4 | Day 2 - 02:00 PM | Phase 3 |
| #10 | Derived Risk Logic | Build algorithmic evaluator for lab metrics to compute Low/Medium/High risk summaries. | Nikhil | 2 | Day 2 - 04:00 PM | Phase 3 |
| #11 | Semantic Search Integration | Build a local SQLite search capability to query patient history and meds. | Vasishta | 3 | Day 2 - 05:00 PM | Phase 3 |
| #12 | Patient Timeline Dashboard | Develop Streamlit UI for visual timeline of patient visits and metrics. | Vasishta | 4 | Day 3 - 09:00 AM | Phase 4 |
| #13 | Analytical Health Charts | Add local chart visualizations for tracking lab metrics over time. | Vasishta | 2 | Day 3 - 11:00 AM | Phase 4 |
| #14 | Network OFF Verification | Physically disconnect internet and test end-to-end ingestion and chat. | Nikhil | 1 | Day 3 - 12:00 PM | Phase 4 |
| #15 | Inference Optimization | Tune local threads/context size to ensure UI remains responsive during generation. | Nikhil | 2 | Day 3 - 02:00 PM | Phase 4 |
