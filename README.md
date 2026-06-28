# MedStruct AI

### Offline-First Medical Intelligence System for Structured Healthcare Data Extraction

---

## Overview

MedStruct AI is an offline-first, CPU-optimized medical intelligence system designed to convert unstructured healthcare data into structured, machine-readable records.

Healthcare information is often available in the form of scanned prescriptions, laboratory reports, handwritten notes, medical documents, and physician voice recordings. These formats are difficult to organize, search, and integrate into digital healthcare systems.

MedStruct AI addresses this challenge by performing all processing locally on the user's device. Using lightweight AI models optimized for CPU inference, the application extracts clinically relevant information and transforms it into a standardized JSON schema while maintaining complete offline functionality.

The generated structured data is stored locally using SQLite, enabling efficient retrieval, search, and future analysis without relying on cloud infrastructure.

---

## Problem Statement

Healthcare professionals routinely manage large volumes of unstructured medical data, including:

* Laboratory reports
* Medical prescriptions
* Discharge summaries
* Clinical notes
* Diagnostic reports
* Physician voice recordings

Manual extraction and digitization of these records is time-consuming, error-prone, and often requires internet-based services that may compromise privacy and availability.

There is a need for an intelligent, privacy-preserving solution capable of transforming heterogeneous medical data into structured digital records while operating entirely offline.

---

## Proposed Solution

MedStruct AI provides a local AI pipeline that extracts meaningful medical information from multiple input formats and converts it into standardized structured records.

The application performs all inference on-device using CPU-optimized models, ensuring privacy, reliability, and offline accessibility.

---

## Key Features

* Offline-first medical document processing
* CPU-only AI inference without GPU dependency
* OCR-based extraction from scanned documents and prescription images
* Speech-to-text transcription of physician voice notes
* Local Small Language Model (SLM) for structured information extraction
* Automatic JSON schema generation
* Local SQLite database for persistent storage
* Offline semantic search across stored records
* Interactive question-answering over structured patient information
* No dependency on external cloud APIs

---

## Supported Input Formats

### Documents

* Laboratory Reports
* Blood Test Reports
* Medical PDFs
* Discharge Summaries

### Images

* Prescription Images
* Scanned Medical Reports
* Handwritten Clinical Notes

### Audio

* Physician Voice Notes
* Consultation Recordings

---

## Structured Output

The extracted information is transformed into a standardized schema.

Example:

```json
{
  "patient_name": "Rahul Sharma",
  "age": 35,
  "gender": "Male",
  "doctor": "Dr. Kumar",
  "hospital": "ABC Hospital",
  "diagnosis": [
    "Type 2 Diabetes"
  ],
  "symptoms": [
    "Fatigue",
    "Frequent Urination"
  ],
  "medications": [
    {
      "name": "Metformin",
      "dosage": "500 mg",
      "frequency": "Twice Daily"
    }
  ],
  "recommended_tests": [
    "HbA1c",
    "Blood Sugar"
  ],
  "follow_up": "30 Days"
}
```

---

## System Architecture

```
Medical Documents / Images / Audio
                │
                ▼
     OCR / Speech Recognition
                │
                ▼
      Text Preprocessing
                │
                ▼
     Local Small Language Model
                │
                ▼
      Structured JSON Output
                │
                ▼
         SQLite Database
                │
                ▼
 Offline Search & Intelligent Querying
```

---

## Technology Stack

| Component              | Technology                         |
| ---------------------- | ---------------------------------- |
| Frontend               | Streamlit                          |
| Backend                | Python                             |
| OCR Engine             | PaddleOCR / Tesseract OCR          |
| Speech Recognition     | Whisper.cpp                        |
| Local Language Model   | Ollama (Gemma 3, Phi-3, Qwen GGUF) |
| Data Storage           | SQLite                             |
| Optional Vector Search | FAISS                              |
| Runtime Environment    | CPU-Only                           |

---

## Workflow

1. Upload a medical document, prescription image, or physician voice recording.
2. Extract textual information using OCR or speech recognition.
3. Normalize the extracted content.
4. Process the text using a locally hosted Small Language Model.
5. Convert the information into a predefined JSON schema.
6. Store the structured records in SQLite.
7. Retrieve information through offline search or natural language queries.

---

## Alignment with Hackathon Objectives

| Requirement                | Implementation                                                     |
| -------------------------- | ------------------------------------------------------------------ |
| Offline-First              | Complete local execution without internet connectivity             |
| CPU-Optimized              | Lightweight AI models designed for CPU inference                   |
| Unstructured to Structured | Converts medical documents into standardized JSON                  |
| Local Storage              | SQLite-based structured database                                   |
| Privacy-Preserving         | No external API or cloud dependency                                |
| AI Inference               | Fully local OCR, speech recognition, and language model processing |

---

## Future Enhancements

* Multi-language medical document support
* Medical timeline visualization
* Automatic abnormal laboratory value detection
* Drug interaction analysis
* Patient history comparison
* Clinical analytics dashboard
* FHIR-compatible data export for interoperability

---

## License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.
