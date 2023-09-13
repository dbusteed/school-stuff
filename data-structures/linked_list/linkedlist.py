#!/usr/bin/env python3


class LinkedList(object):
    '''
    A linked list implementation that holds arbitrary objects.
    '''

    def __init__(self):
        '''Creates a linked list.'''
        self.head = None
        self.size = 0


    def debug_print(self):
        '''Prints a representation of the entire list.'''
        print('{} >>> {}'.format(self.size, ', '.join([ str(item) for item in self ])))


    def __iter__(self):
        '''Iterates through the linked list, implemented as a generator.'''
        for node in self._iter_nodes():
            yield node.value


    def _iter_nodes(self):
        '''Iterates through the nodes of the list, implemented as a generator.'''
        current = self.head
        while current != None:
            yield current
            current = current.next


    def _check_index(self, index):
        return True if index >= 0 and index < self.size else False


    def _get_node(self, index):
        '''Retrieves the Node object at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        if self._check_index(index):
            for i,n in enumerate(self._iter_nodes()):
                if i == index:
                    return n
        else:
            return None


    def add(self, item):
        '''Adds an item to the end of the linked list.'''
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

        self.size += 1


    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right.'''
        if self._check_index(index):
            new_node = Node(item)
            if index == 0:
                old_head = self.head
                self.head = new_node
                new_node.next = old_head
            else:
                prev = self._get_node(index - 1)
                curr = self._get_node(index)
                prev.next = new_node
                new_node.next = curr

            self.size += 1
        else:
            print(f'Error: {index} not within bounds of list')


    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        if self._check_index(index):
            new_node = Node(item)            # need to make a new node? or just change value of old one? 
            old_node = self._get_node(index) # should i delete the old node?
            if index == 0:        
                second = self.head.next
                self.head = new_node
                new_node.next = second
            else:
                new_node.next = self._get_node(index+1)
                self._get_node(index-1).next = new_node

            del old_node
        else:
            print(f'Error: {index} not within bounds of list')


    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        if self._check_index(index):
            return self._get_node(index).value
        else:
            print(f'Error: {index} not within bounds of list')


    def delete(self, index):
        '''Deletes the item at the given index. Throws an exception if the index is not within the bounds of the linked list.'''
        if self._check_index(index):
            del_node = self._get_node(index)
            if index == 0:  
                self.head = self._get_node(1)
            else:
                self._get_node(index-1).next = self._get_node(index+1)

            del del_node
            self.size -= 1
        else:
            print(f'Error: {index} not within bounds of list')


    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''
        if self._check_index(index1) and self._check_index(index2):
            
            # works but is a little messy?

            if index1 == index2:
                return
            
            # sort index-es so that we only need
            # to handle the 'index1 == 0' case
            if index1 > index2:
                index1, index2 = index2, index1

            node1 = self._get_node(index1)
            node2 = self._get_node(index2)

            if (index2 - index1) == 1 and index1 == 0:
                next2 = self._get_node(index2+1)
                self.head = node2
                node2.next = node1
                node1.next = next2

            elif (index2 - index1) == 1:
                prev1 = self._get_node(index1-1)
                next2 = self._get_node(index2+1)
                prev1.next = node2
                node2.next = node1
                node1.next = next2

            elif index1 == 0:
                next1 = self._get_node(1)
                prev2 = self._get_node(index2-1)
                next2 = self._get_node(index2+1)

                self.head = node2
                node2.next = next1

                prev2.next = node1
                node1.next = next2

            else:
                prev1 = self._get_node(index1-1)
                next1 = self._get_node(index1+1)
                prev2 = self._get_node(index2-1)
                next2 = self._get_node(index2+1)
                
                prev1.next = node2
                node2.next = next1

                prev2.next = node1
                node1.next = next2

        else:
            print(f'Error: {index1} and/or {index2} not within bounds of list')


######################################################
###   A node in the linked list

class Node(object):
    '''A node on the linked list'''

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return '<Node: {}>'.format(self.value)
