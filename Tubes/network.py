import socket
import pickle


class Network:
    def __init__(self):
        """
        inisialisasi network
        """
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.8"
        self.port = 5555
        self.addr = (self.server, self.port)
        # self.client.connect(self.addr)
        # self.p = self.client.recv(10240).decode()
        self.p = self.connect()

    def getP(self):
        """
        Fungsi untuk koneksiin satu player
        """
        return self.p

    def connect(self):
        """
        Fungsi untuk koneksiin player
        """
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        """
        Fungsi untuk ngirim data dari client ke server
        """
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048*2))
        except socket.error as e:
            print(e)