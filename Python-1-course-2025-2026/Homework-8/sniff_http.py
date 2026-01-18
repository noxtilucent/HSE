from scapy.all import *

def sniff_http(pkt):
    if pkt.haslayer(Raw):
        payload = pkt[Raw].load
        if b"HTTP" in payload:
            try:
                print(payload.decode(errors="ignore"))
            except:
                print(payload)

sniff(filter="tcp port 8008", prn=sniff_http, store=0)
