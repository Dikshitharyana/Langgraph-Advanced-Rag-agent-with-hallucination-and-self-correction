# config.py
import os
from dotenv import load_dotenv

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if TOGETHER_API_KEY is None:
    raise ValueError("Missing TOGETHER_API_KEY in .env")
if TAVILY_API_KEY is None:
    raise ValueError("Missing TAVILY_API_KEY in .env")
