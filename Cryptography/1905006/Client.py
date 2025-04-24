import socket
import json


from AES import aes_decryption
from Elyptic_Curve import generate_ec , generate_a_b_p , generate_key , send_a_b_p_G , initialize

def make_key(conn):
    a , b , p , gx , gy = initialize()
    private_k , public_k = generate_ec(a , b , p , gx , gy)
    tuple_s = (a , b , p , gx , gy , public_k)
    message_json = json.dumps(tuple_s)
    conn.sendall(message_json.encode('utf-8'))

    data = conn.recv(1024)
    if not data:
        raise Exception("No data available")
    
    received_data = json.loads(data.decode('utf-8'))
    
    key = generate_key(private_k, received_data , a , b , p)
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

HOST = "127.0.0.1"
PORT = 65433 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    key = make_key(s)
    key = key | 1 << 127

    data = s.recv(1024)
    key_str = make_key_str(key)

    _ , plain_text , _ = aes_decryption(data.decode('utf-8'), key_str)
    print(plain_text)


    
    # aes
    # round_keys = generateKeys(key)
    
    # data = s.recv(1024)
    # cipher = pickle.loads(data)
    
    # plain = aes_decrypt(cipher, round_keys)
    # print("".join([chr(x) for x in plain]))


    # key = "BUET CSE19 Batch"
    # _ , plain_text , _ = aes_decryption(data.decode('utf-8'), key)
    # received_tuple = json.loads(data.decode('utf-8'))
    # print('Received Tuple:', received_tuple)
    # print(received_tuple)