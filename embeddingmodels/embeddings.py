from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv

load_dotenv()##needed for other models but hugging face we don't need api keys

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)

texts = [
    "hello this is sarthak",
    "this is vscode",
    "we are dumb"
]

vector = embeddings.embed_documents(texts)

print(vector)