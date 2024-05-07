import Pyro5.api
import threading

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
        
    def start(self) :
        daemon = Pyro5.api.Daemon()
        ns = Pyro5.api.locate_ns()
        
        server = Server()
        
        uri = daemon.register(server)
        ns.register("chat-server", uri)
        
        print('Chat server ready!')
        daemon.requestLoop()  
        
def main():
    server=Server()
    serverThread=threading.Thread(target=server.start)
    serverThread.start()
    serverThread.join() #Espera a thread do server terminar
    
    
if __name__ == '__main__':
    main()