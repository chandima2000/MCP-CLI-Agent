import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient

async def main():
    # Load environment variables
    load_dotenv()
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    # Config file path
    config_file_path = os.path.join(os.path.dirname(__file__), "servers_config.json")

    # Create MCPClient from config file
    client = MCPClient.from_config_file( config_file_path )

    # Create LLM
    llm = ChatGroq(model="llama3-8b-8192")

    # Create agent with the client
    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=20,
        use_server_manager=True,  # Enable the Server Manager
        memory_enabled=True,
    )

    print("Initializing agent...")
    print("Enter 'exit' to quit the program.")
    print("Enter 'clear' to clear the memory.")
    print("Enter 'help' to get help.")
    print("----------------------")

    # Run the query
    try:
       while True:
            # Get user input
           query = input("Enter a query: ")
           
           if query.lower() == "exit":
               print("Exiting Conversation...")
               break
           elif query.lower() == "clear":
               agent.memory.clear()
               print("Memory cleared.")
               continue
           elif query.lower() == "help":
               print("Available commands:")
               print("exit - Exit the conversation")
               print("clear - Clear the memory")
               print("help - Display this help message")
           else:
               result = await agent.run(query)
               print(result)
    
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Clean up all sessions
        await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(main())