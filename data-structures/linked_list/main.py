#!/usr/bin/env python3
from linkedlist import LinkedList
import csv

DATA_FILE = 'data.csv'

link = None

with open(DATA_FILE, 'r') as csv_file:
    
    reader = csv.reader(csv_file)
    
    for i,cmd in enumerate(reader):

        try:
            print(f'{i}:{cmd[0]},{cmd[1]},{cmd[2]}')
        except:
            print('Error: Invalid CSV syntax')

        if cmd[0] == 'CREATE':
            link = LinkedList()
        
        elif cmd[0] == 'DEBUG':
            link.debug_print()
        
        elif cmd[0] == 'ADD':
            link.add( cmd[1] )
        
        elif cmd[0] == 'SET':
            link.set( int(cmd[1]) , cmd[2] )
        
        elif cmd[0] == 'GET':
            print( link.get(int(cmd[1])) ) if link.get( int(cmd[1]) )  else 0
        
        elif cmd[0] == 'DELETE':
            link.delete( int(cmd[1]) )
        
        elif cmd[0] == 'INSERT':
            link.insert( int(cmd[1]) , cmd[2] )
        
        elif cmd[0] == 'SWAP':
            link.swap( int(cmd[1]) , int(cmd[2]) )
        
        else:
            print(f'Error: "{cmd[0]}" not a recognized command')