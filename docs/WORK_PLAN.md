# MedStruct AI - Phased Roadmap & Team Work-Division

## Overview
This document outlines the 4 distinct execution phases leading up to the live hackathon presentation. Task assignments are divided between Nikhil (Core AI / Inference) and Vasishta (Data / Frontend).

### Phase 1: Environment & Engine Setup
**Goal:** Establish a fully offline foundation with local binaries and optimized model weights.
- **Nikhil:**
  - Download and cache GGUF quantized models (Qwen/Gemma).
  - Setup Ollama and write `Modelfile` for system prompts.
  - Compile `whisper.cpp` locally for CPU-accelerated transcription.
- **Vasishta:**
  - Initialize the Python virtual environment and resolve dependencies.
  - Scaffold the basic Streamlit application structure.
  - Create the SQLite database initialization script.

### Phase 2: Ingestion & Extraction Core
**Goal:** Build the pipelines that convert raw audio, images, and text into string payloads.
- **Nikhil:**
  - Build the audio ingestion wrapper around `whisper.cpp`.
  - Implement Vision-Language Model (VLM) prompts to extract text from prescription images and PDF lab reports.
  - Optimize the prompt engineering for deterministic JSON output from the local models.
- **Vasishta:**
  - Build upload handlers in Streamlit for audio files, images, and PDFs.
  - Setup temporary local staging directories for file processing.

### Phase 3: Data Integrity & Storage
**Goal:** Enforce strict data structures and persist them to the database.
- **Vasishta:**
  - Write Pydantic v2 schemas (`PatientRecord`, `ClinicalInsight`, etc.).
  - Implement the SQLite pipeline (ORM or raw SQL queries) to map Pydantic models to database tables.
  - Develop the local semantic search architecture for querying patient history.
- **Nikhil:**
  - Integrate the Pydantic validation layer directly with the LLM output generation (using constrained decoding or retry loops).
  - Write the logic for the "Derived Value Feature" (computing Low/Medium/High risk levels based on extracted lab metrics).

### Phase 4: Interface & Polishing
**Goal:** Finalize the UI, ensure offline compliance, and prepare for presentation.
- **Vasishta:**
  - Build the interactive timeline tracker in Streamlit.
  - Implement analytical health charts using local plotting libraries.
  - Ensure the UI seamlessly integrates the local search/chat functionality.
- **Nikhil:**
  - Perform the "Network OFF" verification test (disconnect Wi-Fi and run full pipeline).
  - Optimize inference latency (adjust threads, CPU scaling).
  - Finalize the README setup instructions for judges.
