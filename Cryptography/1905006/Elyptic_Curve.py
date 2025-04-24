from typing import Any
from Crypto.Util import number
from Crypto.Random import random
import math



def gety2(a , b , p , x):
    y2 = (x**3 + a * x + b) % p
    if pow(y2 , (p-1)//2 , p ) == 1:
        return pow(y2 , (p-1)//4 , p)
    else:
        return None
    

def generate_a_b_p():
    p = number.getPrime(bits)
    a = number.getRandomRange(2 , p)
    b = number.getRandomRange(2 , p)
    while(4 * a * a * a + 27 * b * b ) % p == 0:
        a = number.getRandomRange(2 , p)
        b = number.getRandomRange(2 , p)
   
    return a,b,p

def generate_G(a , b , p):
    #print(a , b , p , sep=',')
    #print(p)
    gx = number.getRandomRange(1 , p)
    gy = gety2(a , b , p , gx)
    while not gy:
        #print(gx , gy , sep=',')
        gx = number.getRandomRange(1 , p)
        gy = gety2(a , b , p , gx)
    
    return gx , gy
    
def generate_private_key(p):
    private_key = random.getrandbits(bits)
    while private_key > p:
        private_key = random.getrandbits(bits)
    return private_key
    
def addition(x1 , y1 , x2 , y2 , a , b , p):
    # print("XXXXXXXXX:")
    # print(x2 - x1)
    # print("YYYYYYYY:")
    # print(y2 - y1)
    t1 = number.inverse(x2 - x1 , p)
    s = (y2 - y1) * t1 % p
    x3 = (s * s - x1 - x2) % p
    y3 = (s * (x1 - x3) - y1) % p

    return x3 , y3

def multiplication(x1 , y1 , a , b , p):
    #print(x1 , y1 , p , sep = ',')
    t1 = number.inverse(2 * y1 , p)
    s = (3 * x1 * x1 + a) * t1 % p
    x3 = (s * s - 2 * x1) % p
    y3 = (s*(x1-x3) - y1) % p

    return x3 , y3

def power_ec(x1 , y1 , private_key , a , b , p):
    resx , resy = x1 , y1

    for i in reversed(range(0,127)):
        resx , resy = multiplication(resx , resy , a , b , p)
        if (private_key & 1 << i):
            resx , resy = addition(resx , resy , x1 , y1 , a , b , p)
    return resx , resy

def generate_ec(a , b , p , gx , gy):
    #gx , gy = generate_G()

    private_key = generate_private_key(p)
    public_key = power_ec(gx , gy , private_key ,  a , b , p)

    #print(private_key , public_key[0] , public_key[1] , sep=',')
    return private_key , public_key

def generate_key(private_key , public_key , a , b , p):
    key , _ = power_ec(public_key[0] , public_key[1] , private_key , a , b , p)
    return key

def send_a_b_p_G():
    return a , b , p , gx , gy

def initialize():
    a , b , p = generate_a_b_p()
    gx , gy = generate_G(a , b , p)
    return a , b , p , gx , gy

def print_key():
    print(generate_key(private_1 , public_2 , a , b , p))
    print(generate_key(private_2 , public_1, a , b , p))
bits = 128
a , b , p , gx , gy = initialize()
# a, b , p = generate_a_b_p()  
# gx , gy = generate_G(p)
# m , n = addition(3 , 4 , 7 , 8)
# print(a , b , p , sep=',')
# gx, gy= generate_G()
# print(gx, gy)
private_1 , public_1 = generate_ec(a , b , p , gx , gy)
private_2 , public_2 = generate_ec(a , b , p , gx , gy)

#generate_key(private_1 , public_2)

#print_key()


