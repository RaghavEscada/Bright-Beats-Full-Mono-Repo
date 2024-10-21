import streamlit as st
from pathlib import Path
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine
from langchain_groq import ChatGroq

# Set up Streamlit page configuration
st.set_page_config(page_title="Bright Beats <Playground>", page_icon="🎓", layout="wide")

# Custom CSS for improved aesthetics
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #9B2D6B 0%, #5E2B8D 100%);
        color: #FFFFFF;
        font-family: 'Georgia', serif;
    }
    .stChatMessage {
        background-color: rgba(50, 50, 50, 0.9);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
        border: 2px solid rgba(255, 255, 255, 0.2);
    }
    .stButton > button {
        background-color: #B06AB6;
        color: white;
        border-radius: 25px;
        padding: 10px 20px;
        font-weight: bold;
        transition: all 0.3s ease;
        border: 2px solid #EDE3E8;
    }
    .stButton > button:hover {
        background-color: #A75DAF;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
    }
    .stChatInput input {
        border-radius: 25px;
        padding: 15px;
        background-color: rgba(255, 255, 255, 0.2);
        color: #EDE3E8;
        border: none;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
    }
    .stChatInput input:focus {
        background-color: rgba(255, 255, 255, 0.3);
        outline: none;
        box-shadow: 0 0 10px rgba(255, 255, 255, 0.6);
    }
    .stChatInput {
        background-color: transparent;
    }
    .stTitle {
        color: #F9E6F0;
        font-size: 6rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
        text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.5);
    }
    .input-prompt {
        font-size: 18px;
        color: #333;
        font-weight: bold;
        text-align: center;
        background-color: #f0f0f0;
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        border: 2px solid #ddd;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and description
st.title("Bright Beats 🦋")
st.markdown("Powered by Groq & MySQL Workbench  | © Z-Bond ❤️")

# MySQL connection details
mysql_host = "localhost"
mysql_port = "3306"
mysql_user = "root"
mysql_password = "Swa%402008"  # URL-encoded password
mysql_db = "bright_beats"  # Your database name

# Hardcoded Groq API Key (for local use)
api_key = "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"

# Ensure API key is provided
if not api_key:
    st.info("Please add the Groq API key.")

# Initialize LLM model
llm = ChatGroq(groq_api_key=api_key, model_name="gemma2-9b-it", streaming=True)

@st.cache_resource(ttl="2h")
def configure_db(mysql_host, mysql_user, mysql_password, mysql_db):
    try:
        connection_string = f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_db}"
        return SQLDatabase(create_engine(connection_string))
    except Exception as e:
        st.error(f"Error connecting to the database: {str(e)}")
        st.stop()

# Connect to the MySQL database
db = configure_db(mysql_host, mysql_user, mysql_password, mysql_db)

# Initialize toolkit
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# Create SQL agent
agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

# Initialize chat message history
if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
    st.session_state["messages"] = [{"role": "assistant", "content": "Ayo! Drop a message below to find people and watch your SQL query skeleton 🩻 "}]
    

# Display previous messages
for msg in st.session_state.messages:
    message_type = msg["role"] if msg["role"] in ["user", "assistant"] else "assistant"
    st.chat_message(message_type).write(msg["content"])

# User input for database query
user_query = st.chat_input(placeholder="e.g., show me people who know Flutter along with some app ideas")

# Hide sample prompts if user has entered a query
if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        with st.spinner("Generating response..."):
            streamlit_callback = StreamlitCallbackHandler(st.container())
            response = agent.run(user_query, callbacks=[streamlit_callback])
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.write(response)

else:
    # Display sample prompts
    st.markdown("Try these Sample Prompts in the Chat Box :-")
  

    col1, col2, col3, col4 = st.columns(4)

    def set_sample_query(query):
        st.session_state["messages"].append({"role": "user", "content": query})
        st.experimental_rerun()

    with col1:
        st.button('Who all are data science folks?', on_click=set_sample_query, args=('Who all are data science folks?',), disabled=True)

    with col2:
        st.button('How to reach Raghav?', on_click=set_sample_query, args=('How to reach Raghav?',), disabled=True)

    with col3:
        st.button('People from IIIT K?', on_click=set_sample_query, args=('People from IIIT K?',), disabled=True)

    with col4:
        st.button('Show me some Flutter guys', on_click=set_sample_query, args=('Show me some Flutter guys',), disabled=True)

# Footer




st.markdown("""
<style>
.input-prompt {
    background: linear-gradient(to right, #9b59b6, #8e44ad); /* Purple gradient */
    color: white; /* Change text color to white for better contrast */
    padding: 10px; /* Add some padding */
    border-radius: 100px; /* Optional: rounded corners */
    text-align: center; /* Center align the text */
}
</style>

<div class="input-prompt">
   Please enter your prompt below 💬, then check out the SQL query contaim!
</div>
""", unsafe_allow_html=True)
