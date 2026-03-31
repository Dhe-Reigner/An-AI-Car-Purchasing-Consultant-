import yaml
import os
from langchain_groq import ChatGroq

def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

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
    agent = load_yaml("config/agents.yaml")["car_expert"]
    task = load_yaml("config/tasks.yaml")["recommend_car"]

    # llm = ChatGroq(
    #     api_key="YOUR_GROQ_API_KEY",
    #     model="llama3-8b-8192"
    # )
    api_key = os.getenv('GROQ_API_KEY')

    llm = ChatGroq(model='llama-3.1-8b-instant', temperature=0.6,api_key=api_key)

    prompt = build_prompt(agent, task, user_input)
    response = llm.invoke(prompt)

    return response.content