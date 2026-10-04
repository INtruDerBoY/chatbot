# My AI Chatbot

A simple conversational AI chatbot built with [Streamlit](https://streamlit.io/), [LangGraph](https://langchain-ai.github.io/langgraph/), and [Groq](https://groq.com/). The app provides a browser-based chat interface and uses LangGraph to manage message state for a conversation.

## Features

- Interactive chat UI powered by Streamlit
- Groq-hosted language model responses
- LangGraph state graph for message handling
- In-memory conversation checkpointing
- Conversation history displayed during the current app session

## Tech stack

- Python 3.10+
- Streamlit
- LangGraph
- LangChain Core
- `langchain-groq`
- `python-dotenv`

## Prerequisites

- Python 3.10 or newer
- A [Groq API key](https://console.groq.com/keys)

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repository>.git
cd <your-repository>
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv myenv
.\myenv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 3. Install dependencies

```bash
pip install streamlit langgraph langchain-core langchain-groq python-dotenv
```

### 4. Configure the Groq API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Do not commit `.env` or share your API key publicly.

### 5. Run the application

```bash
streamlit run frontend.py
```

Streamlit will print a local URL, usually `http://localhost:8501`, where you can open the chatbot in your browser.

## How it works

1. `frontend.py` renders the Streamlit interface and stores the displayed message history in `st.session_state`.
2. User messages are converted into LangChain `HumanMessage` objects.
3. `backend.py` sends the messages through a LangGraph state graph.
4. The graph invokes the Groq model `openai/gpt-oss-120b`.
5. The assistant response is returned to the UI and displayed in the chat.

The current implementation uses `InMemorySaver`, so conversation checkpoints are kept only in memory and are lost when the app process restarts.

## Project structure

```text
.
├── backend.py       # LangGraph workflow and Groq model configuration
├── frontend.py      # Streamlit chat interface
├── .env             # Local API key configuration (do not commit)
└── README.md        # Project documentation
```

## Configuration

The language model is configured in `backend.py`:

```python
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
)
```

You can change the model or temperature there if your Groq account supports the selected model.

## Limitations

- Chat history is not persisted to a database.
- The current configuration uses a single thread ID, `thread-1`.
- A valid Groq API key is required to generate responses.
- There are no automated tests or production deployment configuration yet.

## Contributing

1. Create a feature branch.
2. Make and test your changes locally.
3. Open a pull request with a clear description of the change.

## License

No license has been specified yet. Add a license file before distributing this project publicly.
