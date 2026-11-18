from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model("groq:openai/gpt-oss-120b",temperature=0.9)

response = model.invoke("write poem for AI")

print(response.content)