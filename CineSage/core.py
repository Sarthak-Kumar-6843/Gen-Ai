from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser
load_dotenv()
model = ChatGroq(
    model="openai/gpt-oss-120b",
)

class Movie(BaseModel):# like creating a google form
    title: str
    release_year : Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str
    
parser = PydanticOutputParser(pydantic_object=Movie)#for checking Movie


prompt = ChatPromptTemplate.from_messages([
    ("system", 
    """
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

    ("human", """Extract information from this paragraph : {paragraph}""")
])

para = input("Give your paragraph : ")

final_prompt = prompt.invoke(
    {"paragraph" : para}
) 


response = model.invoke(final_prompt)

print(response.content)






#check core2