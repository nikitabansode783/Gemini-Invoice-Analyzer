# Gemini-Invoice-Analyzer
Gemini Invoice Analyzer is a Streamlit app using Google Gemini API to analyze invoice images. Users upload invoices, which are processed to extract key information, streamlining financial management.
### API Key Setup

1. **Generate API Key:**
   - Visit your API provider's site.
   - Create and copy a new API key.

2. **Create `.env` File:**
   - In your project's root directory, create a file named `.env`.

3. **Store API Key:**
   - Open `.env` and add:
     ```
     API_KEY=YOUR_API_KEY
     ```

4. **Load Environment Variables:**
   - Install `python-dotenv`:
     ```sh
     pip install python-dotenv
     ```
   - Add to your script:
     ```python
     from dotenv import load_dotenv
     import os

     load_dotenv()
     api_key = os.getenv('API_KEY')
     ```
