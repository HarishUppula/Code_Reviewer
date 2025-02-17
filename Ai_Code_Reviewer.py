import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Set your Gemini API key securely

genai.configure(api_key=os.getenv("API_KEY"))



def review_code(code):
    """Sends code to Gemini AI for review and suggestions."""
    prompt = f"""You are an AI code reviewer. Review the following code for:
    - Best practices
    - Security vulnerabilities
    - Performance optimizations
    - Readability improvements

    Code:
    ```
    {code}
    ```

    Provide a detailed and structured review with clear explanations and suggested improvements.
    """
    
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text  # Extract response text
    except Exception as e:
        return f"Error: {str(e)}"

st.set_page_config(page_title="AI Code Reviewer", page_icon="🤖", layout="wide")
st.title("🤖 AI Code Reviewer using Gemini AI")
st.write("Paste your code below and get AI-powered insights & suggestions.")

code_input = st.text_area("📝 Paste your code here:", height=250)

if st.button("🔍 Review Code"):
    if code_input.strip():
        with st.spinner("Reviewing code... ⏳"):
            review_result = review_code(code_input)
        st.subheader("✅ AI Code Review & Suggestions:")
        st.write(review_result)
    else:
        st.warning("⚠️ Please enter some code before submitting.")


