#!/usr/bin/env python3
from array_api import Array
import csv

DATA_FILE = 'data.csv'

arr = None  

with open(DATA_FILE, 'r') as csv_file:
    
    reader = csv.reader(csv_file)
    
    for i,cmd in enumerate(reader):

        try:
            print(f'{i}:{cmd[0]},{cmd[1]},{cmd[2]}')
        except:
            print('Error: Invalid CSV syntax')

        if cmd[0] == 'CREATE':
            arr = Array()
        
        elif cmd[0] == 'DEBUG':
            arr.debug_print()
        
        elif cmd[0] == 'ADD':
            arr.add( cmd[1] )
        
        elif cmd[0] == 'SET':
            arr.set( int(cmd[1]) , cmd[2] )
        
        elif cmd[0] == 'GET':
            print( arr.get(int(cmd[1])) ) if arr.get( int(cmd[1]) )  else 0
        
        elif cmd[0] == 'DELETE':
            arr.delete( int(cmd[1]) )
        
        elif cmd[0] == 'INSERT':
            arr.insert( int(cmd[1]) , cmd[2] )
        
        elif cmd[0] == 'SWAP':
            arr.swap( int(cmd[1]) , int(cmd[2]) )
        
        else:
            print(f'Error: "{cmd[0]}" not a recognized command')
