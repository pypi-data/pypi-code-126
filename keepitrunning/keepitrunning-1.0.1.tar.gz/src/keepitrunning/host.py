from flask import Flask
from threading import Thread

class Host:
  app = Flask('')

  @app.route('/')
  def main():
    return 'The project is running. Please copy the link and host it on uptimerobot.com'
    
  def run(self, port):
    app.run(host="0.0.0.0", port=port)
  def keep_running(self, port = 8080):
    server = Thread(target=self.run(port=port))
    server.start()