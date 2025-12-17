from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_openai import ChatOpenAI


# LLM
llm = ChatOpenAI(
    temperature=0,
    model="gpt-4"
)

# Database connection
db = SQLDatabase.from_uri(
    "postgresql+psycopg2://postgres:1234@localhost:5432/company_db",
    schema="public",
    include_tables=["employees", "departments"]
)

# SQL Agent
sql_agent = create_sql_agent(
    llm=llm,
    db=db,
    verbose=True,
    agent_executor_kwargs={
        "handle_parsing_errors": True  
    }
)

def run_sql_query(user_query: str):
    response = sql_agent.invoke({"input": user_query})
    return response["output"]
