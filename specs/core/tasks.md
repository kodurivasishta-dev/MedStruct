# Tasks: MedStruct AI Core Engine

**Input**: Design documents from `specs/core/`

**Prerequisites**: plan.md (required), spec.md (required for user stories)

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Cache Models & Setup Ollama: Download Q4 GGUF models and configure local Ollama instance with custom Modelfile. (Nikhil)
- [ ] T002 Compile whisper.cpp: Clone and build whisper.cpp locally with CPU optimization flags (AVX2). (Nikhil)
- [ ] T003 Scaffold App & DB Init: Create Streamlit app shell and SQLite schema creation scripts (`scripts/init_db.py`). (Vasishta)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

- [ ] T004 [P] Pydantic Schema Layer: Define core data models (PatientRecord, LabMetric) using Pydantic v2 in `core/schemas.py`. (Vasishta)
- [ ] T005 [P] SQLite Mapping: Write functions to map validated Pydantic objects to SQLite table inserts in `db/database.py`. (Vasishta)
- [ ] T006 LLM Structural Constraint: Implement retry logic/constrained generation so LLM outputs match Pydantic schemas in `core/inference.py`. (Nikhil)

---

## Phase 3: User Story 1 - Doctor Uploads Voice Note (P1)

- [ ] T007 Audio Ingestion Pipeline: Write Python wrapper to pass uploaded audio to whisper.cpp and retrieve text in `core/audio/`. (Nikhil)
- [ ] T008 UI Audio Uploader: Implement Streamlit components for drag-and-drop of audio in `app/main.py`. (Vasishta)
- [ ] T009 Link audio text to SQLite visits schema.

---

## Phase 4: User Story 2 - Lab Report Ingestion (P1)

- [ ] T010 VLM Image Extraction: Engineer prompts and pipeline to pass prescription images/PDFs to local VLM for parsing. (Nikhil)
- [ ] T011 UI File Uploaders: Implement Streamlit components for drag-and-drop of PDFs and images in `app/main.py`. (Vasishta)
- [ ] T012 Link parsed LabMetrics to SQLite lab_metrics schema.

---

## Phase 5: User Story 3 - Derived Risk Computation (P2)

- [ ] T013 Derived Risk Logic: Build algorithmic evaluator for lab metrics to compute Low/Medium/High risk summaries in `core/logic.py`. (Nikhil)
- [ ] T014 Analytical Health Charts: Add local chart visualizations for tracking lab metrics and risk over time in `app/components/`. (Vasishta)

---

## Phase 6: User Story 4 - Semantic Search (P3)

- [ ] T015 Semantic Search Integration: Build a local SQLite search capability to query patient history and meds in `db/queries.py`. (Vasishta)
- [ ] T016 Patient Timeline Dashboard: Develop Streamlit UI for visual timeline of patient visits and metrics integrating the search. (Vasishta)

---

## Phase 7: Polish & Cross-Cutting Concerns

- [ ] T017 Network OFF Verification: Physically disconnect internet and test end-to-end ingestion and chat. (Nikhil)
- [ ] T018 Inference Optimization: Tune local threads/context size to ensure UI remains responsive during generation. (Nikhil)

---

## Parallel Team Strategy & Work Plan

To ensure maximum efficiency during the hackathon, Nikhil and Vasishta will execute tasks in parallel utilizing their core competencies. 

### Day 1 Strategy
1. **Morning Kick-off**: 
   - **Nikhil** completes T001 and T002 (Engine Setup).
   - **Vasishta** completes T003 (App Shell and DB init).
2. **Afternoon Foundation**: 
   - **Vasishta** tackles T004 and T005, establishing the DB schemas.
   - **Nikhil** focuses on T006, ensuring the LLM outputs valid JSON that Vasishta's Pydantic schemas can accept.
   - *End of Day Checkpoint*: Nikhil's Python output successfully writes to Vasishta's database without errors.

### Day 2 Strategy
1. **Morning (User Story 1)**:
   - **Nikhil** works on T007 (Whisper wrapper).
   - **Vasishta** builds T008 (UI File Uploader).
   - *Integration (T009)*: UI passes file to wrapper, wrapper passes text to DB.
2. **Afternoon (User Story 2 & 3)**:
   - **Nikhil** knocks out T010 (VLM logic) and T013 (Derived risk logic).
   - **Vasishta** handles T011 (PDF/Image uploaders) and T014 (Health Charts).
   - *End of Day Checkpoint*: The core value proposition works. Uploading an image updates the charts.

### Day 3 Strategy
1. **Morning (User Story 4)**:
   - **Vasishta** completes T015 and T016 (Semantic Search & Timeline).
2. **Afternoon (Polish)**:
   - **Nikhil** executes T017 (Network OFF test) and T018 (Inference Speed-ups).
   - *Final Presentation Prep*: Run through the demo completely offline.
