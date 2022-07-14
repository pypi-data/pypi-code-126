from pathlib import Path
from dotenv import dotenv_values

settings = dotenv_values(Path(__file__).parent / ".env")
