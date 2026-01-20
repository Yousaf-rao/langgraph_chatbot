# LangGraph Chatbot with Streamlit & SQLite

A persistent chatbot application built using **LangGraph**, **LangChain**, and **Streamlit**, featuring streaming responses and conversation history stored in a **SQLite** database.

## Features

- **Persistant Memory**: Conversations are stored in a local SQLite database (`chatbot.db`).
- **Multiple Threads**: Create and switch between different conversation threads.
- **Streaming Responses**: Real-time streaming of AI responses.
- **Modern UI**: Built with Streamlit for a clean and responsive interface.

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: LangGraph, LangChain
- **Database**: SQLite (via `langgraph.checkpoint.sqlite`)
- **LLM**: OpenAI GPT (via `langchain_openai`)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Yousaf-rao/langgraph_chatbot.git
   cd langgraph_chatbot
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv myenv
   # Windows
   .\myenv\Scripts\activate
   # Linux/Mac
   source myenv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install streamlit langgraph langchain-openai langchain-core
   ```

4. **Set up Environment Variables**:
   Create a `.env` file in the root directory and add your OpenAI API Key:
   ```env
   OPENAI_API_KEY="sk-..."
   ```

## Usage

1. **Run the Streamlit App**:
   ```bash
   streamlit run streaming_fronthend_database.py
   ```

2. **Interact**: Open your browser to the local URL provided (usually `http://localhost:8501`).

## Project Structure

- `streaming_fronthend_database.py`: Key frontend file handling the UI and Streamlit logic.
- `langgraph_database_backend.py`: Backend logic defining the LangGraph workflow and database connection.
