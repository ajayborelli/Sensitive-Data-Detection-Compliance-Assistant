import streamlit as st
import pandas as pd
from PyPDF2 import PdfReader
from detector import detect_sensitive_data, classify_risk
from summarizer import generate_summary
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title="Sensitive Data Detection Assistant")

st.title("🔒 Sensitive Data Detection & Compliance Assistant")

uploaded_file = st.file_uploader(
    "Upload a document",
    type=["pdf", "txt", "csv"]
)

if uploaded_file:

    st.success(f"Uploaded: {uploaded_file.name}")

    # TXT FILES
    
    if uploaded_file.name.endswith(".txt"):

        text = uploaded_file.read().decode("utf-8")

        st.subheader("Document Content")
        st.text_area("", text, height=300)

        results = detect_sensitive_data(text)
        risk = classify_risk(results)

        st.subheader("Risk Classification")
        st.warning(risk)

        st.subheader("Detected Sensitive Data")
        st.write(results)

        st.subheader("AI Compliance Summary")

        if st.button("Generate AI Summary"):
            summary = generate_summary(text, api_key)
            st.write(summary)

        st.subheader("Ask Questions About the Document")

        question = st.text_input(
            "Ask a question",
            placeholder="What sensitive data exists in the document?"
        )

        if st.button("Get Answer"):

            question = question.lower()

            if "sensitive" in question:
                st.write(results)

            elif "email" in question:
                st.write(f"Email addresses found: {len(results['Email'])}")

            elif "phone" in question:
                st.write(f"Phone numbers found: {len(results['Phone'])}")

            elif "pan" in question:
                st.write(f"PAN numbers found: {len(results['PAN'])}")

            elif "aadhaar" in question:
                st.write(f"Aadhaar numbers found: {len(results['Aadhaar'])}")

            elif "employee" in question:
                st.write(f"Employee IDs found: {len(results['Employee ID'])}")

            elif "bank" in question:
                st.write(f"Bank Accounts found: {len(results['Bank Account'])}")

            elif "api" in question:
                st.write(f"API Keys found: {len(results['API Key'])}")

            elif "password" in question:
                st.write(f"Passwords found: {len(results['Password'])}")

            elif "risk" in question:
                st.write(f"Risk Classification: {risk}")

            elif "summary" in question:
                summary = generate_summary(text, api_key)
                st.write(summary)

            else:
                st.write("Sorry, I could not understand the question.")

    # PDF FILES
    elif uploaded_file.name.endswith(".pdf"):

        pdf_reader = PdfReader(uploaded_file)

        text = ""

        for page in pdf_reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

        st.subheader("Document Content")
        st.text_area("", text, height=300)

        results = detect_sensitive_data(text)
        risk = classify_risk(results)

        st.subheader("Risk Classification")
        st.warning(risk)

        st.subheader("Detected Sensitive Data")
        st.write(results)

        st.subheader("AI Compliance Summary")

        if st.button("Generate AI Summary PDF"):
            summary = generate_summary(text, api_key)
            st.write(summary)

        st.subheader("Ask Questions About the PDF")

        question = st.text_input(
            "Ask a question about the PDF",
            placeholder="What sensitive data exists in the document?"
        )

        if st.button("Get Answer PDF"):

            question = question.lower()

            if "sensitive" in question:
                st.write(results)

            elif "email" in question:
                st.write(f"Email addresses found: {len(results['Email'])}")

            elif "phone" in question:
                st.write(f"Phone numbers found: {len(results['Phone'])}")

            elif "pan" in question:
                st.write(f"PAN numbers found: {len(results['PAN'])}")

            elif "aadhaar" in question:
                st.write(f"Aadhaar numbers found: {len(results['Aadhaar'])}")

            elif "employee" in question:
                st.write(f"Employee IDs found: {len(results['Employee ID'])}")

            elif "bank" in question:
                st.write(f"Bank Accounts found: {len(results['Bank Account'])}")

            elif "api" in question:
                st.write(f"API Keys found: {len(results['API Key'])}")

            elif "password" in question:
                st.write(f"Passwords found: {len(results['Password'])}")

            elif "risk" in question:
                st.write(f"Risk Classification: {risk}")

            elif "summary" in question:
                summary = generate_summary(text, api_key)
                st.write(summary)

            else:
                st.write("Sorry, I could not understand the question.")

    # CSV FILES
    elif uploaded_file.name.endswith(".csv"):

        df = pd.read_csv(uploaded_file)

        st.subheader("CSV Preview")
        st.dataframe(df)

        text = df.to_string()

        results = detect_sensitive_data(text)
        risk = classify_risk(results)

        st.subheader("Risk Classification")
        st.warning(risk)

        st.subheader("Detected Sensitive Data")
        st.write(results)

        st.subheader("AI Compliance Summary")

        if st.button("Generate AI Summary CSV"):
            summary = generate_summary(text, api_key)
            st.write(summary)

        st.subheader("Ask Questions About the CSV")

        question = st.text_input(
            "Ask a question about the CSV",
            placeholder="How many employee IDs are present?"
        )

        if st.button("Get Answer CSV"):

            question = question.lower()

            if "employee" in question:
                st.write(f"Employee IDs found: {len(results['Employee ID'])}")

            elif "email" in question:
                st.write(f"Email addresses found: {len(results['Email'])}")

            elif "risk" in question:
                st.write(f"Risk Classification: {risk}")

            elif "summary" in question:
                summary = generate_summary(text, api_key)
                st.write(summary)

            else:
                st.write(results)