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


prompt = ChatPromptTemplate.from_messages(
    [(
        'system',"""
        Extract movie information from paragraph
            {format_instruction}
        """
    ),
    ("human","{paragraph}")]
)




para = input("Give your paragraph : ")

final_prompt = prompt.invoke(
    {"paragraph" : para,
     'format_instruction': parser.get_format_instructions()}
) 


response = model.invoke(final_prompt)

print(response.content)