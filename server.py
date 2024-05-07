import Pyro5.api

@Pyro5.api.expose
class Server:
    def __init__(self):
        self.clients=[]
        
    def broadcast(self, message):
        for client in self.clients:
            client.receive(message)
    
    def registerClient(self, client):
        self.clients.append(client)
        
    def removeClient(self, client):
        self.clients.remove(client)
        
def main():
    daemon = Pyro5.api.Daemon()
    ns = Pyro5.api.locate_ns()
    
    server = Server()
    
    uri = daemon.register(server)
    ns.register("chat-server", uri)
    
    print('Chat server ready!')
    daemon.requestLoop()
    
if __name__ == '__main__':
    main()