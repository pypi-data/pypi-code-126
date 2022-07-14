from dotenv import load_dotenv
from os.path import join

def load_env(place):
    print(place)
    dotenv_path = join(dirname(__file__), '../.env')
    load_dotenv(dotenv_path) 