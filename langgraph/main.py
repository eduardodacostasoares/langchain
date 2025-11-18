from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

# creating the agent
llm = ChatOpenAI(model="gpt-5")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from react-agent!")
    result = agent.invoke({"messages":HumanMessage(content="Search in linkeding 3 internships in Ontario that requires knowledge about LLM and langchain")})
    print(result)
if __name__ == "__main__":
    main()
