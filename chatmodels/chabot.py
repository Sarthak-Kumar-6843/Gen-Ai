from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

model = init_chat_model("groq:openai/gpt-oss-120b",temperature=0.9)

print("Choose your AI mode")
print("1 for Angry Mode")
print("2 for funny Mode")
print("3 for very sad Mode")

choice = int(input("tell your response :- "))

if choice == 1:
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif choice == 2:
    mode = "You are a very funny AI agent. You respond with humor and jokes."
elif choice == 3:
    mode = "You are an AI agent. You respond aggressively and impatiently."
    
messages = [
    SystemMessage(content=mode)
]

print("--------------------welcom type 0 to exit the application-----------------------------")
while True:
    
    prompt = input("You : ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))

    print("Bot : ",response.content)
    
print(messages)    