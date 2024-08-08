# ContentCrafter: Your AI Writing Companion

ContentCrafter is an AI-driven application designed to help you generate high-quality, SEO-friendly blog posts, headline ideas, and LinkedIn posts with ease. With Google's Gemini, ContentCrafter can assist writers, marketers, and content creators in crafting engaging and well-structured content.

## Features

- **Generate Blog Posts**: Create comprehensive, detailed, and non-AI generated looking blog posts based on the provided title and keywords.
- **Headline Ideas**: Get 5 SEO-friendly headline variations for your blog article.
- **LinkedIn Posts**: Generate 2 LinkedIn posts with 3 hashtags each to share your blog after publishing.

## Installation

To get started with ContentCrafter, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/shivamchhuneja/contentcrafter.git
    cd contentcrafter
    ```

2. **Create and Activate a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:
    Create a `.env` file in the root directory of the project and add your API keys:
    ```plaintext
    GOOGLE_GEMINI_API_KEY=your_google_gemini_api_key
    ```
    Alternatively if you're running this locally, you can add your keys manually to apikey.py file.(avoid pushing to GitHub with the keys still in place)

## Usage

1. **Run the Streamlit Application**:
    ```bash
    streamlit run app.py
    ```

2. **Input Content Details**:
    - **Content Title**: Enter the title of your blog post.
    - **Keywords**: Provide keywords, separated by commas.
    - **Number of Words**: Select the desired length of the blog post using the slider.

3. **Generate Content**:
    Click the "Generate Content" button to create a blog post, headline ideas, and LinkedIn posts.

## Example

After running the application and inputting your content details, you will receive the following outputs:

1. **Blog Post**:
    A comprehensive, detailed, and non-AI generated looking blog post based on the provided title and keywords.

2. **Headline Ideas**:
    5 SEO-friendly headline variations for the blog article.

3. **LinkedIn Posts**:
    2 LinkedIn posts with 3 hashtags each to share the blog after publishing.