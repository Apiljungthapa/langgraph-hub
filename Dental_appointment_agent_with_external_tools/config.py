"""
Configuration settings for the dental appointment scheduling bot.
"""
import os
import dotenv
from datetime import datetime

# Load environment variables
dotenv.load_dotenv()

# API Keys
COMPOSIO_API_KEY = os.getenv("COMPOSIO_API_KEY", "u1ypnmbeydnhtgxwxrdb1b")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "AIzaSyBWaaZb3o19abScB3R6Y1t7EDQNZwfcdik")

# LLM Configuration
LLM_MODEL = "gemini-2.0-flash-exp"

# Workflow Configuration
TIMEZONE = "UTC"