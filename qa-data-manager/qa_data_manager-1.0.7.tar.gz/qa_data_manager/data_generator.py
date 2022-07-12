from config import Config as cfg
from qa_data_manager.data_base_model import database


class DataGenerator:

    @staticmethod
    def db_connection(db_host, db_name, db_port, user_name, user_password, base_url):
        database.init(db_name, host=db_host, port=db_port, user=user_name, password=user_password)
        cfg.url = base_url
