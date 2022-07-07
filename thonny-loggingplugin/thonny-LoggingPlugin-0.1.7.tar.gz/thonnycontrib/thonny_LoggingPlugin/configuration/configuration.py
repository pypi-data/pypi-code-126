from thonnycontrib.thonny_LoggingPlugin.configuration.globals import OPTIONS,WB

from thonny.config_ui import ConfigurationPage

def init_options():
    for el in OPTIONS :
        if not WB.get_option(el) :
            WB.set_default("loggingPlugin."+el,OPTIONS[el])
    
def get_option(name: str):
        return WB.get_option("loggingPlugin."+name)

class plugin_configuration_page(ConfigurationPage):
    def __init__(self, master):
        ConfigurationPage.__init__(self, master)
        self.add_checkbox("loggingPlugin.log_in_console","print logs in console ?")
        self.add_checkbox("loggingPlugin.store_logs","store logs in files ?")
        self.add_checkbox("loggingPlugin.send_logs", "Send logs to a server ?")
        self.add_entry("loggingPlugin.server_address", row=None, column=0, pady=10, padx=0, columnspan=1,width=100)
        self.add_entry("loggingPlugin.local_path", row=None, column=0, pady=10, padx=0, columnspan=1,width=100)