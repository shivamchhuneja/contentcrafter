import streamlit as st

#set the layout
st.set_page_config(layout="wide")

#App title
st.title('ContentCrafter: Your AI Writing Companion')

#subheader
st.subheader("Now you can create perfect pieces of content with the help of AI")

#left sidebar for user input

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



