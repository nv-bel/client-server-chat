import Pyro5.api
import threading

@Pyro5.api.expose
class Client:
    def __init__(self):
        self.server = Pyro5.api.Proxy('PYRONAME:chat-server')
        
    def receive(self, message):
        print(message)
        
    def sendMessage(self, message):
        self.server.broadcast(f'{self.nickname}: {message}')
        
def main():
    nickname = input('\n> Enter your nickname: ')
    client = Client()
    client.nickname = nickname
    
    client.server.registerClient(client)
    
    while True:
        pass