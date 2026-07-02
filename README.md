# Sensitive Data Detection & Compliance Assistant

## Overview
Sensitive Data Detection & Compliance Assistant is an AI-powered application that helps identify sensitive information in uploaded documents, assess risk levels, generate compliance summaries, and answer questions about document content.

The application supports multiple file formats and provides automated compliance insights using Google Gemini AI.

### Document Upload
Supported file formats:
- PDF
- TXT
- CSV

### Sensitive Data Detection
The system detects:
- Aadhaar Numbers
- PAN Numbers
- Email Addresses
- Phone Numbers
- Credit Card Numbers
- Employee IDs
- Bank Account Numbers
- IFSC Codes
- Passwords
- API Keys

### Risk Classification
Documents are classified into:
- Low Risk
- Medium Risk
- High Risk
Based on the quantity of sensitive information detected.

### AI Compliance Summary
Using Google Gemini AI, the application generates:
- Compliance Observations
- Security Risks

### Question Answering
Users can ask questions such as:
- What sensitive data exists in the document?
- How many email addresses are present?
- How many employee IDs are present?
- How many API keys are present?
- What is the risk classification?
- Summarize this document.

## Architecture Overview

User Uploads Document
          │
Streamlit Interface
          │
Document Processing
          │
Sensitive Data Detection
          │
Risk Classification
          │
Gemini AI Compliance Summary
          │
Question Answering

## AI/ML Approach Used

### Rule-Based Detection
Sensitive information is identified using Python Regular Expressions (Regex).

Examples include:
- Email Detection
- PAN Detection
- Aadhaar Detection
- Phone Number Detection
- Credit Card Detection
- Employee ID Detection
- Bank Account Detection
- IFSC Code Detection
- Password Detection
- API Key Detection

### Generative AI

Google Gemini AI is used to generate:
- Compliance Analysis
- Security Risk Assessment
- Remediation Recommendations
- Document Summaries

## Technologies Used

- Python
- Streamlit
- Pandas
- PyPDF2
- Google Gemini AI
- Regex
- Python Dotenv

## Setup Instructions

### Clone Repository

```bash
git clone <repository-url>
cd Sensitive-Data-Detection-Compliance-Assistant
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### Run Application

```bash
python -m streamlit run app.py
```

---

## Challenges Faced
- Handling multiple document formats.
- Designing accurate Regex patterns for sensitive data.
- Integrating Google Gemini AI.
- Managing API availability and response handling.
- Building a unified workflow across TXT, PDF, and CSV files.

## Future Improvements
- Data Masking and Redaction
- ChromaDB / Vector Database Integration
- Multi-document Analysis
- Audit Logging
- User Authentication
- Dashboard Analytics
- Cloud Deployment Enhancements

## Project Structure

Sensitive-Data-Detection-Compliance-Assistant
│
├── app.py
├── detector.py
├── summarizer.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env

# Author

Ajay Kumar