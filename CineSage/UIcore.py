from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import streamlit as st

load_dotenv()

st.set_page_config(page_title="Movie Information Extractor", page_icon="🎬")

model = ChatGroq(
    model="openai/gpt-oss-120b"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", """
    You are a movie information extraction assistant.

    Analyze the following paragraph and extract:

    1. Movie Name
    2. Release Year
    3. Director
    4. Genre
    5. Cast
    6. Main Plot
    7. Location / Setting
    8. Main Themes
    9. Music Composer
    10. IMDb Rating
    11. Critical Reception

    Also provide a short summary of the movie in 2-3 sentences.

    Only extract information supported by the paragraph.
    If information is unavailable, write "Not mentioned".
    """),

    ("human", "Extract information from this paragraph: {paragraph}")
])

chain = prompt | model

# UI
st.title("🎬 Movie Information Extractor")

st.write("Enter a movie paragraph to extract its information and summary.")

paragraph = st.text_area(
    "Enter Movie Paragraph",
    height=200,
    placeholder="Paste your movie paragraph here..."
)

if st.button("Extract Information"):

    if paragraph.strip():

        with st.spinner("Extracting movie information..."):

            try:
                response = chain.invoke({
                    "paragraph": paragraph
                })

                st.subheader("Extracted Movie Information")
                st.write(response.content)

            except Exception as error:
                st.error(f"Something went wrong: {error}")

    else:
        st.warning("Please enter a movie paragraph.")