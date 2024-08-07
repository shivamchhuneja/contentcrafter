import streamlit as st
import google.generativeai as genai
from apikey import google_gemini_api_key

# Configure the API key
genai.configure(api_key=google_gemini_api_key)

# Define generation configuration
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

# Set up the model
model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

# Set the layout
st.set_page_config(layout="wide")

# App title
st.title('ContentCrafter: Your AI Writing Companion')

# Subheader
st.write("Now you can create perfect pieces of content with the help of AI. Just add the information about the blog piece in the right sidebar and ContentCrafter will generate a blog post as well as a LinkedIn post to share the blog after publishing.")

# Left sidebar for user input
with st.sidebar:
    st.title("Input your Content Details")
    st.subheader("Share the details of the content piece you want to generate in as much detail as possible.")

    # Content Title
    blog_title = st.text_input("Content Title")

    # Keywords Input
    keywords = st.text_area("Keywords (comma-separated)")

    # Number of words
    num_words = st.slider("Number of Words", min_value=100, max_value=1500, step=100)

    # Number of images
    num_images = st.number_input("Number of Images", min_value=1, max_value=5, step=1)

    # Submit button
    submit_button = st.button("Generate Content")

if submit_button:
    prompt = f"Generate 2 items for me. 1 A comprehensive, well structured, detailed and non AI generated looking blog post based on the given Title: \"{blog_title}\", Keywords: \"{keywords}\". The blog should be approximately {num_words} words in length, suitable for online reading & SEO friendly. Ensure that the content maintains a consistent tone, is original, interesting, uses pop culture references time to time, and aims at providing value while holding reader interest throughout the piece. And 2. A LinkedIn post to share this blog when published on LinkedIn."

    # Start chat session and generate content
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    prompt,
                ],
            },
        ]
    )

    response = chat_session.send_message(prompt)

    # Display the generated content
    st.write(response.parts[0].text)
