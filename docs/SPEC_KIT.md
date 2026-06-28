# MedStruct AI - System Spec & Architecture

## Tech Stack Matrix
| Component | Specific Tech Choice | CPU Optimization Strategy |
| :--- | :--- | :--- |
| **Frontend UI** | Streamlit | Lightweight, thin client, zero JS overhead. |
| **Execution Core** | Python 3.11 | Minimal dependency footprint. |
| **LLM Inference** | Ollama / llama.cpp (Qwen-2.5-3B-Instruct GGUF) | 4-bit quantization (Q4_K_M), AVX2/ARM Neon enabled. |
| **Audio Processing** | whisper.cpp | Natively compiled C++ engine for CPU-bound audio transcription. |
| **Data Validation** | Pydantic v2 | High-performance core (Rust-based) for struct enforcement. |
| **Database** | SQLite3 | Local, file-based persistence, no network daemon overhead. |

## System Architecture Diagram
```ascii
+-----------------------+       +-------------------------+
| Unstructured Inputs   |       | Local Inference Engines |
| (Images, PDFs, Audio) +------>+ (llama.cpp, whisper.cpp)|
+-----------------------+       +-----------+-------------+
                                            |
                                            v
+-----------------------+       +-------------------------+
| SQLite Database       |       | Parsing Filter          |
| (Patients, Metrics)   +<------+ (Pydantic Validation)   |
+-----------+-----------+       +-------------------------+
            |
            v
+-----------------------+
| Streamlit Interface   |
| (Dashboard, Timeline) |
+-----------------------+
```

## Database Schema (SQL DDL)
```sql
CREATE TABLE patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE visits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    visit_date DATE NOT NULL,
    notes TEXT,
    FOREIGN KEY(patient_id) REFERENCES patients(id)
);

CREATE TABLE diagnoses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    visit_id INTEGER,
    icd_10_code TEXT,
    description TEXT,
    risk_level TEXT CHECK(risk_level IN ('Low', 'Medium', 'High')),
    FOREIGN KEY(visit_id) REFERENCES visits(id)
);

CREATE TABLE medications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    visit_id INTEGER,
    medication_name TEXT NOT NULL,
    dosage TEXT NOT NULL,
    frequency TEXT,
    FOREIGN KEY(visit_id) REFERENCES visits(id)
);

CREATE TABLE lab_metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    visit_id INTEGER,
    metric_name TEXT NOT NULL,
    metric_value REAL NOT NULL,
    unit TEXT NOT NULL,
    is_abnormal BOOLEAN,
    FOREIGN KEY(visit_id) REFERENCES visits(id)
);
```

## Pydantic Data Models
```python
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date

class LabMetric(BaseModel):
    metric_name: str
    metric_value: float
    unit: str
    is_abnormal: bool = Field(description="Computed by comparing against standard baselines")

class Medication(BaseModel):
    medication_name: str
    dosage: str
    frequency: str

class Diagnosis(BaseModel):
    icd_10_code: Optional[str]
    description: str
    risk_level: str = Field(pattern="^(Low|Medium|High)$")

class ClinicalInsight(BaseModel):
    visit_date: date
    notes_summary: str
    diagnoses: List[Diagnosis]
    medications: List[Medication]
    lab_metrics: List[LabMetric]
    overall_patient_risk: str = Field(
        pattern="^(Low|Medium|High)$", 
        description="Derived from evaluating abnormal blood metrics and diagnoses"
    )

class PatientRecord(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date
    insights: List[ClinicalInsight]
```
