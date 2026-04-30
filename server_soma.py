"""Aqui vamos testar o servidor fazendo a soma de vetores passados pelo cliente"""

import time
import rpyc

class MyService(rpyc.Service):

    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_sum_array(self, arr):
        start = time.time()
        result = sum(arr)
        end = time.time()
        tempo = end - start
        print("Tempo de execução: {}".format(tempo))
        return result, tempo

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    t.start()