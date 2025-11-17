sudokuMultiAgen

A simple project that builds, solves, verifies, and visualizes a Sudoku puzzle using a multi-agent system powered by Python and AutoGen.

This project demonstrates how a team of specialized AI agents can collaborate to complete a complex, multi-step task. The agents work together by writing and executing Python code, managed by a central "Project Manager" agent.

How It Works (The Workflow)

The entire process is managed by a GroupChatManager agent who directs a team of specialists. The workflow is as follows:

User Request: The user (you) initiates the chat with a request, such as "Generate an easy Sudoku puzzle."

Generation: The GroupChatManager passes the task to the sudoku_generator. This agent writes Python code to create a 9x9 puzzle.

Execution: The user agent (acting as the code executor) receives the Python code, runs it, and prints the generated puzzle.

Solving: The manager then passes the puzzle to the sudoku_solver, which writes Python code to find the solution.

Execution: The user agent runs the solver's code and gets the solution.

Verification: The manager passes the solution to the sudoku_verifier, which writes Python code to check if the solution is 100% valid (all rows, columns, and 3x3 boxes are correct).

Execution: The user agent runs the verification code.

Visualization: Finally, the manager asks the sudoku_visualization agent to write Python code to print a "pretty" ASCII version of the puzzle and its solution side-by-side.

Execution: The user agent runs the visualization code, presenting the final result.

Termination: The sudoku_visualization agent says "TERMINATE", ending the chat.

The Agent Team (Elements of the Agents)

This system consists of one "worker" agent and a team of four "specialist" agents.

UserProxyAgent (user)

Role: The Code Executor (The "Hands").

Job: This agent represents the user and is the only agent with code_execution_config. It does not write code, but it executes all Python code provided by the other agents and reports the results (the stdout or any errors) back to the group.

AssistantAgent (sudoku_generator)

Role: The Puzzle Creator.

Job: Its system_message instructs it to be a puzzle generator. Its sole purpose is to write and provide Python code that creates a 9x9 Sudoku grid.

AssistantAgent (sudoku_solver)

Role: The Problem Solver.

Job: This agent's system_message commands it to be a Sudoku solver. It receives a puzzle and writes a Python function to find the complete and correct solution.

AssistantAgent (sudoku_verifier)

Role: The Quality Assurance.

Job: Its system_message defines it as a verifier. It writes Python code to check a solved 9x9 grid against all Sudoku rules (rows, columns, 3x3 boxes) and report if it's valid.

AssistantAgent (sudoku_visualization)

Role: The Presenter.

Job: This agent's system_message instructs it to be a data visualizer. It writes Python code to print a formatted, human-readable ASCII grid for the user to see.

GroupChatManager (groupChat_mgr)

Role: The Project Manager.

Job: This agent is an LLM itself. It reads the entire chat history and the user's initial request. Its system_message commands it to follow the strict workflow (Generate -> Solve -> Verify -> Visualize) and call the correct agent at each step.

Configuration (The Model)

This project is configured to be model-agnostic, meaning you can use any LLM that is compatible with the OpenAI API format (like DeepSeek, Groq, Llama, etc.).

1. The .env File

The agent configuration is loaded from environment variables using python-dotenv. You must create a file named .env in the same directory as your Python script.

To use DeepSeek (as shown in the code), your .env file should look like this:

# The API key you generated from DeepSeek

DS_KEY="your-deepseek-api-key-goes-here"

# The official base URL for the DeepSeek API

BASE_URL="[https://api.deepseek.com](https://api.deepseek.com)"

If you wanted to use OpenAI, you would change the variables to:

OPENAI_KEY="your-openai-api-key-goes-here"

...and then adjust the llm_config in the Python script accordingly.

2. The llm_config Object

This Python dictionary in the script is what tells AutoGen how to connect to your model:

llm_config = {
"config_list": [
{ # "model" tells the API which model to use
"model": "deepseek-r1-0528",

            # "api_key" is loaded from the .env file
            "api_key": os.environ.get("DS_KEY"),

            # "base_url" is also loaded from the .env file
            "base_url": os.environ.get("BASE_URL"),
        }
    ],
    "cache_seed": 42,      # Enables caching for consistent responses
    "temperature": 0,      # Removes randomness for predictable results
    "price": [0.0,0.0],    # Disables cost tracking

}

This llm_config is passed to all agents, giving them their "brain."

How to Run

Clone the Repository:

git clone [https://github.com/your-username/sudokuMultiAgen.git](https://github.com/your-username/sudokuMultiAgen.git)
cd sudokuMultiAgen

Create a Python Virtual Environment:
On Windows:

python -m venv envm
.\envm\Scripts\activate

On macOS/Linux:

python3 -m venv envm
source envm/bin/activate

Install Dependencies:

pip install -r requirements.txt

Create Your .env File:

Create a file named .env.

Add your API key and base URL (see "Configuration" section above).

Create the Working Directory:
The UserProxyAgent needs a "sandbox" to save and run code.

mkdir sudoku_game

Run the Project!

python your_main_script_name.py
