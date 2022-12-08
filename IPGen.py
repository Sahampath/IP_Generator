
import random

def ip_generator():
    number = random.randint(0,256)
    return number

print(f'IP is: {ip_generator()}.{ip_generator()}.{ip_generator()}.{ip_generator()}')
