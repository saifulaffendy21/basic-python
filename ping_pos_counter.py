#ping POS counter

import os
import socket

branch = input('\nBranch code: ')
pos_type = input('\nPOS counter type [POS, BAR, CUS]: ')
pos_number = input('\nNumber of POS counter: ')

for i in range(int(pos_number)):
    current_pos = branch+pos_type+str(i+1).zfill(3)
    try:
        ip = socket.gethostbyname(current_pos)
        print("\nThe IP address of",current_pos,"is",ip)
    except socket.gaierror:
        print("The IP address of",current_pos,"cant be resolve by DNS in this network "  )
    
    
    
    
    
    
    
    
#test cpdinf





