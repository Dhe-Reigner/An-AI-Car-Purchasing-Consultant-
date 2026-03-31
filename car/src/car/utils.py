import yaml
import os
from langchain_groq import ChatGroq

def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

# Absolute path to agents.yaml
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # points to car/src/car/
agents_path = os.path.join(BASE_DIR, "config", "agents.yaml")

def build_prompt(agent, task, user_input):
    return f"""
You are a {agent['role']}.

Goal:
{agent['goal']}

Task:
{task['description']}

User Input:
{user_input}

Respond with:
- Recommended car
- Budget category
- Key features
- Reasoning
"""

def run_ai(user_input):
    agent = load_yaml(agents_path)["final_recommendation_agent"]
    task = {
        "description": "Analyze user input and recommend the best car options."
    }

    # llm = ChatGroq(
    #     api_key="YOUR_GROQ_API_KEY",
    #     model="llama3-8b-8192"
    # )
    api_key = os.getenv('GROQ_API_KEY')

    llm = ChatGroq(model='llama-3.1-8b-instant', temperature=0.6,api_key=api_key)

    prompt = build_prompt(agent, task, user_input)
    response = llm.invoke(prompt)

    return response.content