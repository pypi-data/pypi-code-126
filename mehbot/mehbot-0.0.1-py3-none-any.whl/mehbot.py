from utils.mehbot_error import MehbotException
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from utils.funct_responce import debut, error, responce

class Mehbot:
    
    def __init__(self, api_key: str = None) -> None:
        
        def check_dot_env() -> str:
            import configparser
            default_path_to_conf_file = "/etc/mehbot/mehbot.conf"
            try:
                config = configparser.ConfigParser()
                config.read(default_path_to_conf_file)
                api_key = config["mehbot"]["API_KEY"]
            except Exception:
                raise MehbotException(f"The configuration file is not good")
            return api_key
        
        api_key = check_dot_env()
        
        self.__updater = Updater(api_key, use_context=True)
        
        self.__updater.dispatcher.add_handler(CommandHandler('start', debut))
        self.__updater.dispatcher.add_handler(MessageHandler(Filters.text, responce))
        self.__updater.dispatcher.add_error_handler(error)
        
        
    def start_bot(self) -> None:
        self.__updater.start_polling()
        self.__updater.idle()
        
if __name__ == "__main__":
    bot = Mehbot()
    bot.start_bot()