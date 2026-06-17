from scapy.all import *

class TokenHeader(Packet):
    name = "TokenHeader"
    fields_desc = [
        XBitField("token", 0, 128)
    ]

MAC_VETH0 = "00:00:00:00:00:01"
MAC_VETH8 = "00:00:00:00:00:02"

TOKEN1 = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
TOKEN2 = 0x99999999999999999999999999999999
TOKEN3 = 0x11111111111111111111111111111111

pacote = Ether(src=MAC_VETH0, dst=MAC_VETH8, type=0xFFFF) / TokenHeader(token=TOKEN1)
print("Atualizado token secreto")
sendp(pacote, iface="veth0")

pacote = Ether(src=MAC_VETH0, dst=MAC_VETH8, type=0x1111) / TokenHeader(token=TOKEN1)
print("Enviado pacote com token correto")
sendp(pacote, iface="veth0")

pacote = Ether(src=MAC_VETH0, dst=MAC_VETH8, type=0x1111) / TokenHeader(token=TOKEN2)
print("Enviado pacote com token errado")
sendp(pacote, iface="veth0")

pacote = Ether(src=MAC_VETH0, dst=MAC_VETH8, type=0xFFFF) / TokenHeader(token=TOKEN3)
print("Atualizado token secreto")
sendp(pacote, iface="veth0")

pacote = Ether(src=MAC_VETH0, dst=MAC_VETH8, type=0x1111) / TokenHeader(token=TOKEN1)
print("Enviado pacote com token antigo")
sendp(pacote, iface="veth0")

pacote = Ether(src=MAC_VETH0, dst=MAC_VETH8, type=0x1111) / TokenHeader(token=TOKEN3)
print("Enviado pacote com token novo")
sendp(pacote, iface="veth0")
