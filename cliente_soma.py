"""Aqui vamos testar o cliente passando o tamanho do vetor a ser somado"""

import time
import rpyc
import sys

if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]
conn = rpyc.connect(server, 18861)

n = int(input("Digite o tamanho do vetor a ser somado: "))
arr = list(range(n))

start = time.time()
resultado, tempo_servidor = conn.root.sum_array(arr)
end = time.time()

print("Tempo de execução no cliente: {}".format(end - start))
print("Tempo de execução no servidor: {}".format(tempo_servidor))
print("A soma do vetor é: {}".format(resultado))
