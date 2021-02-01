import socket

'''Create a new socket connection & assign to a variable:

- Format: socket.socket(address_family, socket_type)

'''
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

'''
socket.AF_INET = IPv4
socket.SOCK_STREAM = TCP
'''