import socket
import re
import sys
import socket
from base import TcpModule
from lib.bitcoin import Connection, ProtocolError

class BitcoinModule(TcpModule):

name =  'bitcoin '
description =  'Grabs a banner for proprietary FOX protocol by Tridium '
port = 8333
timeout = 3

def process(self, ip, port):
to_addr = (ip, port)
handshake_msgs = []
addr_msg = {}

connection = Connection(to_addr)
try:
connection.open()
handshake_msgs = connection.handshake()
addr_msg = connection.getaddr()
except (ProtocolError, socket.error) as err:
return None
finally:
connection.close()

if len(handshake_msgs) > 0:
data =  ' '
for msg in handshake_msgs:
if  'checksum ' in msg:
msg[ 'checksum '] = msg[ 'checksum '].encode( 'string-escape ')
if  'magic_number ' in msg:
msg[ 'magic_number '] = msg[ 'magic_number '].encode( 'string-escape ')
if  'user_agent ' in msg:
data +=  'User-Agent: %s\
' % msg[ 'user_agent ']
if  'version ' in msg:
data +=  'Version: %s\
' % msg[ 'version ']
if  'lastblock ' in msg:
data +=  'Lastblock: %s\
' % msg[ 'lastblock ']

addresses = []
if  'addr_list ' in addr_msg:
for addr in addr_msg[ 'addr_list ']:
if addr[ 'ipv6 '] !=  ' ':
ip = addr[ 'ipv6 ']
else:
ip = addr[ 'ipv4 ']
addresses.append({
'ip ': ip,
'port ': addr[ 'port '],
})

banner = {
'data ': data,
'opts ': {
'bitcoin ': {
'handshake ': handshake_msgs,
'addresses ': addresses,
}
},
}
return banner

return None

if __name__ ==  '__main__ ':
import sys

mod = BitcoinModule()
print mod.process(sys.argv[1], 8333)