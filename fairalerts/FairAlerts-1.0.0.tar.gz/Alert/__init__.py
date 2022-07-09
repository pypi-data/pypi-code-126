from Alert import DiscordAlert

def send_alert(message):
    DiscordAlert.send_channel_alert(message)