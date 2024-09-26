from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field


app = Flask(__name__)

app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Kratos1000Kratos@localhost:2000/querydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --------------------------------------------------------------------------------------------------------------
groq_api_key = os.getenv("groq_api_key")
langchain_api_key = os.getenv("langchain_api_key")
langchain_endpoint = os.getenv("langchain_endpoint")

model = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0,
    max_tokens=2048,
    timeout=None,
    max_retries=2,
    groq_api_key=groq_api_key
)
print("Model retrieved")

# --------------------------------------------------------------------------------------------------------------
class QueryClassification(BaseModel):
    product_type: str = Field(
        description="Classify the type of product. Possible types include 'GPU', 'CPU' and 'Monitor'. Return only the product type."
    )
    severity: int = Field(
        description="Classify the severity of the complain on a scale from 0 to 3. 0 being normal and 3 being needs urgent care."
    )
    product_desc : str = Field(
        description="Description of the product complain in short."
    )

# Create structured LLM grader
structured_llm_grader = model.with_structured_output(QueryClassification)

# Define system prompt for disaster classification
system_prompt = """You are an expert in customer query management. Given the description of a product complain, classify it into one of the following types: 'GPU', 'CPU' and 'Monitor'. 
    Additionally, assess the severity of the complain on a scale from 0 to 3, where 0 indicates normal and 3 indicates needs urgent care. 
    Also provide a short description of the product complain.
    Provide accurate and detailed classifications based on the given description."""

# Create the prompt template
product_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "Product description: {query}")
    ]
)

# Combine prompt template with structured output
query_classifier = product_prompt | structured_llm_grader
# --------------------------------------------------------------------------------------------------------------

from custom import routes