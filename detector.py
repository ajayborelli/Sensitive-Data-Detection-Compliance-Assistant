import re

def detect_sensitive_data(text):

    patterns = {
        "Email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "Phone": r"\b[6-9]\d{9}\b",
        "PAN": r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",
        "Aadhaar": r"\b\d{4}\s\d{4}\s\d{4}\b",
        "Credit Card": r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b",
        "Employee ID": r"\bEMP\d{4,}\b",
        "Bank Account": r"\b\d{9,18}\b",
        "IFSC Code": r"\b[A-Z]{4}0[A-Z0-9]{6}\b",
        "Password": r"(?i)password\s*[:=]\s*\S+",
        "API Key": r"(?i)api\s*key\s*[:=]\s*\S+"
    }

    results = {}

    for key, pattern in patterns.items():
        results[key] = re.findall(pattern, text)

    confidential_keywords = [
        "confidential",
        "internal use only",
        "acquisition",
        "financial projections",
        "trade secret"
    ]

    results["Confidential Business Information"] = []

    for keyword in confidential_keywords:
        if keyword.lower() in text.lower():
            results["Confidential Business Information"].append(keyword)

    return results

def classify_risk(results):

    total_sensitive_items = sum(
        len(items) for items in results.values()
    )

    if total_sensitive_items <= 3:
        return "Low Risk"

    elif total_sensitive_items <= 8:
        return "Medium Risk"

    else:
        return "High Risk"