import os
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
from dotenv import load_dotenv

load_dotenv()

model = 'deepseek-r1-0528'

llm_config = {
    "config_list": [
        {
            "model": model,
            "api_key": os.environ.get("DS_KEY"),
            "base_url": os.environ.get("BASE_URL"),
        }
    ],
    "cache_seed": 42,
    "temperature": 0,
    "price": [0.0,0.0],
}

user = UserProxyAgent(
    name="user",
    human_input_mode="TERMINATE",
    code_execution_config={
        "work_dir":"sudoku_game",
        "use_docker": False,
    },
    llm_config=llm_config
)

# 1. sudoku generator
sudokuGenerator = AssistantAgent(
    name = "sudoku_generator",
    system_message = "you are responsible for generating a valid 9x9 the sudoku puzzle based on the difficulty level provide by the user : Easy, Medium, or Hard. After generating the puzzle explicitly call sudokuSolver.",
    llm_config = llm_config
)

# 2. sudoku solver
sudokuSolver = AssistantAgent(
    name = "sudoku_solver",
    system_message = "you are responsible for providing a solution to the given 9x9 sudoku puzzle. After generating solution explicitly call sudokuVerified. ",
    llm_config = llm_config
)

# 3. sudoku verified
sudokuVerified = AssistantAgent(
    name = "sudoku_verifier",
    system_message = "you are responsible for verifying the given sudoku solution for 9x9 sudoku puzzle. Please consider all 9x9 sudoku puzzle rules while verifying. After verifying explicitly call sudokuVisual.",
    llm_config = llm_config
)

# 4. sudoku vizualization
sudokuVisual = AssistantAgent(
    name = "sudoku_visualization",
    system_message = "generating a visually appealing sudoku puzzle along with solution to the end user.",
    llm_config = llm_config
)

groupChat = GroupChat(
    agents=[user, sudokuGenerator, sudokuSolver, sudokuVerified, sudokuVisual],
    messages =[] 
)

groupChat_mgr = GroupChatManager(
    groupChat,
    llm_config=llm_config
)

def play_sudoku(difficulty='easy'):
    user.initiate_chat(groupChat_mgr,
                    message={
                        "role": "user",
                        "content": f"Generate a {difficulty} Sudoku Puzzle, Valid solution and also visualize it back to user."
                    })

play_sudoku('easy')