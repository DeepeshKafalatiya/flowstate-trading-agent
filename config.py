import os
from dotenv import load_dotenv

load_dotenv()

# Variables for potential expansion or API integration later
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
DB_NAME = "trading_flowstate.db"