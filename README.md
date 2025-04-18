# 🧠 MCP Agent CLI with Langchain & Groq

This project is a command-line tool powered by the **Model Context Protocol (MCP)** that connects to various MCP servers and uses **Langchain**, **Groq LLM (LLaMA3)**, and multiple web integrations like DuckDuckGo, Playwright, and Airbnb.

---

## 🚀 Features

- Integrates with [Langchain](https://python.langchain.com/)
- Uses [Groq](https://groq.com/) to run `llama3-8b-8192`
- Supports multiple MCP servers via a config file:
  - `DuckDuckGo Search`
  - `Playwright Automation`
  - `Airbnb Data Agent`
- Built-in memory (can be cleared)
- Simple command-line interface
- Interactive query agent

---

## 📁 Project Structure

```bash
.
├── app.py                    # Main entrypoint for the MCP agent
├── servers_config.json        # Configuration for external MCP servers
├── .env                       # Environment variables (GROQ API key)
└── README.md                  # You're here!
```

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/chandima2000/MCP-CLI-Agent.git
cd MCP-CLI-Agent
```

### 2. Create and activate a virtual environment

```bash
uv venv .venv
source .venv/bin/activate 
```

### 3. Create .env File and add your Groq API key
```bash
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Install dependencies using uv
```bash
uv add mcp-use langchain-groq
```

---

## 🧠 How to Use

Run the CLI tool:
```bash
uv run app.py
```

---

## 🌐 MCP Server Configuration

- The file ```servers_config.json``` contains configuration for each MCP server.

- Make sure you have ``Node.js`` installed and ``npx`` available to run these MCP servers.

---

## 📌 Notes
- The MCPAgent integrates multiple tools into a single conversational AI interface.

- You can customize the config file to add more MCP tools or replace existing ones.