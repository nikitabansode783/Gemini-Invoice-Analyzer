from dotenv import load_dotenv
import os
import streamlit as st
from PIL import Image
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Loading Google API Key from .env file
api_key = os.getenv("GOOGLE_API_KEY")

def get_gemini_response(input_text, image, prompt):
    try:
        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content([input_text, image[0], prompt])
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {"mime_type": uploaded_file.type, "data": bytes_data}
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Set page configuration
favicon_path = 'star.ico'  # Replace with your actual path or URL
st.set_page_config(page_title="Gemini Invoice Insight", page_icon=favicon_path, layout="wide")

# Define colors
PRIMARY_COLOR = "#007BFF"
SECONDARY_COLOR = "#6C757D"
BACKGROUND_COLOR = "#F8F9FA"
TEXT_COLOR = "#212529"

# Apply custom CSS
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {BACKGROUND_COLOR};
        color: {TEXT_COLOR};
    }}
    .stButton>button {{
        background-color: {PRIMARY_COLOR};
        color: white;
    }}
    .stTextInput>div>div>input {{
        background-color: white;
        color: black;
    }}
    .stFileUploader>div>div>button {{
        background-color: {PRIMARY_COLOR};
        color: white;
    }}
    .stSpinner>div>div>div {{
        color: {PRIMARY_COLOR};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar for additional information
st.sidebar.title("Instructions")
st.sidebar.info(
    """
    1. Upload your invoice image (jpg, jpeg, png).
    2. Enter a prompt for analysis.
    3. Click the 'Analyze Image' button.
    """
)

# App title and description
st.title("Gemini Invoice Insight")
st.markdown("### Upload your invoices and get detailed analysis")

# Main interface with tabs
tab1, tab2 = st.tabs(["Upload & Analyze", "Analysis Result"])

with tab1:
    st.subheader("Step 1: Upload Your Invoice")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)
    
    st.subheader("Step 2: Enter Analysis Prompt")
    input_text = st.text_input("Input Prompt:", key="input", placeholder="Enter your prompt here")

    submit = st.button("Analyze Image")

with tab2:
    st.subheader("Step 3: View Analysis Result")
    if submit:
        if uploaded_file is not None:
            try:
                image_data = input_image_setup(uploaded_file)
                input_prompt = "You are an expert in understanding invoices. You will receive input images as invoices & you will have to answer questions based on the input image."
                with st.spinner("Analyzing the invoice..."):
                    response = get_gemini_response(input_text, image_data, input_prompt)
                    st.write(response)
            except FileNotFoundError as e:
                st.error(f"Error: {str(e)}")
            except Exception as e:
                st.error(f"Unexpected error: {str(e)}")
        else:
            st.error("Please upload an image to analyze.")

# Footer with contact information
st.markdown(
    """
    <div style='text-align: center; color: #888;'>
    <p>Developed by Nikita Bansode | <a href='nikitabansode783@gmail.com'>Contact Us</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
