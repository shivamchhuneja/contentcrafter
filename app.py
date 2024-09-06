import streamlit as st
import google.generativeai as genai
from apikey import google_gemini_api_key


# Configure the API keys
genai.configure(api_key=google_gemini_api_key)


# Define generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Set up the Gemini model
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)

# Set the layout
st.set_page_config(layout="wide")

# App title
st.title('ContentCrafter: Your AI Writing Companion')

# Subheader
st.write("Now you can create perfect pieces of content with the help of AI. Just add the information about the blog piece in the right sidebar and ContentCrafter will generate a blog post, Headline Ideas & a LinkedIn post to share the blog after publishing.")

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

    # Submit button
    submit_button = st.button("Generate Content")

if submit_button:
    # Define the prompt
    prompt = f"You are a world-class content writer with expertise in crafting well-structured, engaging, and data-driven content. Your writing is varied, captivating, and includes verified data and citations where relevant. Please generate the following: 1.	A comprehensive, well-structured, detailed, and natural-sounding blog post based on the provided Title: “{blog_title}” and Keywords: “{keywords}”. The post should be approximately {num_words} words, optimized for online reading and SEO best practices. Ensure the content is original, maintains a consistent tone, and incorporates pop culture references where appropriate. The goal is to provide value, keep the reader engaged, and offer a memorable reading experience. 2.	5 SEO-optimized headline variations for the blog article, each designed to capture attention and improve click-through rates. 3. 2 LinkedIn posts to promote the blog when published, with compelling copy and 3 relevant hashtags for each post."

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
