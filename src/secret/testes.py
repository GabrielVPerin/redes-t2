from scapy.all import *

class TokenHeader(Packet):
    name = "TokenHeader"
    fields_desc = [
        ShortField("token", 0) # ShortField = 16bits
    ]

MAC_VETH0 = "00:00:00:00:00:01"
MAC_VETH8 = "00:00:00:00:00:02"

pkt_update = Ether(src=MAC_VETH0, dst=MAC_VETH8, type=0xFFFF) / TokenHeader(token=0xABCD)

print("Atualizado token secreto")
sendp(pkt_update, iface="veth0")

pkt_normal_certo = Ether(src=MAC_VETH0, dst=MAC_VETH8, type=0x1111) / TokenHeader(token=0xABCD)

print("Enviado pacote com token correto")
sendp(pkt_normal_certo, iface="veth0")

pkt_normal_errado = Ether(src=MAC_VETH0, dst=MAC_VETH8, type=0x1111) / TokenHeader(token=0x9999)

print("Enviado pacote com token errado")
sendp(pkt_normal_errado, iface="veth0")
