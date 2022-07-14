from dotenv import load_dotenv
from os.path import dirname, join

def load_env():
    dotenv_path = join(dirname(__file__), '../../.env')
    load_dotenv(dotenv_path) 