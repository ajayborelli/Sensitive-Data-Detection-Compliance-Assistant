from google import genai

def generate_summary(text, api_key):

    try:

        client = genai.Client(api_key=api_key)

        prompt = f"""
        Analyze the following document and provide:

        1. Compliance Observations
        2. Security Risks
        3. Suggested Remediation Steps

        Document:
        {text}
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error generating summary: {str(e)}"