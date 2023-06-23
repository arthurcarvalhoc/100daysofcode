from scapy.all import *
import time

# Define o endereço IP de destino
dest_ip = "localhost"

# Cria um pacote SYN
start = time.time_ns()

# definir um limite de tempo
segundos = 10 * (10 ** 9)
print(segundos)
i = 0
while True:
    tempo = (time.time_ns() - start )
    syn_packet = IP(dst=dest_ip)/TCP(dport=80, flags="S")

    # Envia o pacote SYN
    send(syn_packet, verbose=0)
    print(i)
    i = i + 1
    if(tempo > (segundos)):
        print("limite de tempo atingido.")
        break

print("Fim do experimento")
