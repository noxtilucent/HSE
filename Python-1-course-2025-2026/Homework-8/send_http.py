from scapy.all import *

ip = IP(dst="127.0.0.1")
tcp_syn = TCP(dport=8008, sport=RandShort(), flags="S")
synack = sr1(ip/tcp_syn)

tcp_ack = TCP(
    dport=8008,
    sport=tcp_syn.sport,
    seq=synack.ack,
    ack=synack.seq + 1,
    flags="A"
)
send(ip/tcp_ack)

http_get = b"GET / HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n"
tcp_push = TCP(
    dport=8008,
    sport=tcp_syn.sport,
    seq=synack.ack,
    ack=synack.seq + 1,
    flags="PA"
)

send(ip/tcp_push/http_get)
