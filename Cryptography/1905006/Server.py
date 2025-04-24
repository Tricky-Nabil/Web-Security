import socket
import json


from AES import aes_encryption
from Elyptic_Curve import generate_ec , generate_a_b_p , generate_key , send_a_b_p_G

def make_key(conn):
    data = conn.recv(1024)
    if not data:
        return None 
    received_data = json.loads(data.decode('utf-8'))

    private_k , public_k = generate_ec(received_data[0] , received_data[1] , received_data[2] , received_data[3] , received_data[4])
    # print("private key")
    # print(type(private_k))
    # print("public key")
    # print(type(public_k))

    message_json = json.dumps(public_k)
    conn.sendall(message_json.encode('utf-8'))

    key = generate_key(private_k , received_data[5] , received_data[0] , received_data[1] , received_data[2])
    return key

def make_key_str(key):
    hex_string = hex(key)[2:]
    temp_key_str = [[] , [] , [] , []]
    k = 0
    for j in range(0 , 32 , 2):
        temp_key_str[k].append(chr(int(hex_string[j:j+2] , 16)))
        k = (k+1) % 4
    
    key_str = ""
    for i in range(4):
        for j in range(4):
            key_str+= temp_key_str[j][i]
    return key_str

# # Send the JSON string through the socket

#     data = conn.recv(1024)
#     if not data:
#         return None

# def establishKey(nbits, conn):
#     data = conn.recv(1024)
#     if not data:
#         return None
    

HOST = "127.0.0.1" 
PORT = 65433

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")

        key = make_key(conn)
        key = key | 1 << 127

        key_str = make_key_str(key)

        # key = "BUET CSE19 Batch"
        msg = "Never Gonna Give you up" 
        cipher , _ , _ = aes_encryption(msg, key_str)
        # tuple_s = (10 , "ami" , (1 , 2))
        # message_json = json.dumps(tuple_s)
        # conn.sendall(message_json.encode('utf-8'))
        conn.send(cipher.encode('utf-8'))
        