from scapy.all import *

# 1. Definindo o seu cabeçalho customizado (espelho do P4)
class TokenHeader(Packet):
    name = "TokenHeader"
    fields_desc = [
        ShortField("token", 0) # Campo de 16 bits
    ]

# MACs baseados na imagem fornecida
MAC_VETH0 = "00:00:00:00:00:01"
MAC_VETH8 = "00:00:00:00:00:02"

# 3. Criando o pacote para ATUALIZAR a senha na SRAM
# Vamos definir a senha como 0xABCD
pkt_update = Ether(src=MAC_VETH0, dst=MAC_VETH8, type=0xFFFF) / TokenHeader(token=0xABCD)

print("Enviando pacote de ATUALIZACAO de token...")
send(pkt_update, iface="veth0")

# 4. Criando o pacote NORMAL com a senha CORRETA
pkt_normal_certo = Ether(src=MAC_VETH0, dst=MAC_VETH8, type=0x1111) / TokenHeader(token=0xABCD)

print("Enviando pacote normal com token CORRETO...")
sendp(pkt_normal_certo, iface="veth0")

# 5. Criando o pacote NORMAL com a senha ERRADA
pkt_normal_errado = Ether(src=MAC_VETH0, dst=MAC_VETH8, type=0x1111) / TokenHeader(token=0x9999)

print("Enviando pacote normal com token ERRADO...")
sendp(pkt_normal_errado, iface="veth0")