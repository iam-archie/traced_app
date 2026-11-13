import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Initialize OpenAI model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# Three different prompts
prompts = [
    "Explain Generative AI in simple terms.",
    "What is the difference between LangChain and LangGraph?",
    "Explain how an AI agent works with a practical example."
]

# Execute prompts
for i, prompt in enumerate(prompts, start=1):
    print(f"\n{'=' * 50}")
    print(f"RUN {i}")
    print(f"PROMPT: {prompt}")

    response = llm.invoke(prompt)

    print(f"ANSWER: {response.content}")
