#!/usr/bin/env python3
from collections import deque

class BinaryTree(object):
    '''
    A binary tree.
    '''
    def __init__(self):
        self.root = None


    def __repr__(self):
        return repr(self.root)


    # multiple? ???
    def set(self, key, value):
        '''
        Adds the given key=value pair to the tree.
        '''
        
        new_node = Node(None, key, value)

        # handle first node
        if not self.root:            
            self.root = new_node
            return
        
        # raise error if key already exists
        if self._find(key, self.root):
            raise Exception('Key already exists')
        
        def _insert(top_node, new_node):            
            
            # on the left?
            if new_node.key < top_node.key:                
                if not top_node.left:
                    top_node.left = new_node
                    new_node.parent = top_node
                else:
                    _insert(top_node.left, new_node)

            # or on the right?
            else:
                if not top_node.right:
                    top_node.right = new_node
                    new_node.parent = top_node
                else:
                    _insert(top_node.right, new_node)

        _insert(self.root, new_node)


    def get(self, key):
        '''
        Retrieves the value under the given key.
        Returns None if the key does not exist.
        '''
        
        # if tree NOT empty
        if self.root:
            node = self._find(key, self.root)

            if node:
                return node.value
            else:
                return None
        
        # if tree is empty
        else:
            print('empty!')
            return None


    def remove(self, key):
        '''
        Removes the given key from the tree.
        Returns silently if the key does not exist.
        '''

        # if tree NOT empty
        if self.root:

            del_node = self._find(key, self.root)

            # if node not found
            if not del_node:
                return ''

            # check if single-node tree
            if not self.root.left and not self.root.right:
                self.root = None
                return ''

            hasLeft = bool(del_node.left)
            hasRight = bool(del_node.right)

            # check if leaf-node
            if not hasLeft and not hasRight:
                
                # figure out if its the 'left' child
                # or the 'right' child
                if del_node.parent.left == del_node:
                    del_node.parent.left = None
                else:
                    del_node.parent.right = None

                del del_node

            # if node has one child (XOR)
            elif hasLeft != hasRight:
                
                if del_node.parent.left == del_node:
                    if hasLeft:
                        del_node.parent.left = del_node.left
                    else:
                        del_node.parent.left = del_node.right
                else:
                    if hasLeft:
                        del_node.parent.right = del_node.left
                    else:
                        del_node.parent.right = del_node.right

                del del_node

            # if node has two children
            else:

                replacement = del_node.right

                while replacement.left:
                    replacement = replacement.left

                replacement.parent.left = None            

                replacement.right = del_node.right
                replacement.right.parent = replacement

                replacement.left = del_node.left
                replacement.left.parent = replacement

                if del_node.parent.left == del_node:
                    del_node.parent.left = replacement                    
                else:
                    del_node.parent.right = replacement                    


        return ''


    def walk_dfs_inorder(self):
        '''
        An iterator that walks the tree in DFS fashion.
        Yields (key, value) for each node in the tree.
        '''

        def walk(node):
            if node.left:
                yield from walk(node.left)
            
            yield (node.key, node.value)
            
            if node.right:
                yield from walk(node.right)

        # if tree NOT empty
        if self.root:
            yield from walk(self.root)

        return []


    def walk_dfs_preorder(self, node=None, level=0):
        '''
        An iterator that walks the tree in preorder DFS fashion.
        Yields (key, value) for each node in the tree.
        '''

        def walk(node):
            yield (node.key, node.value)

            if node.left:
                yield from walk(node.left)
            
            if node.right:
                yield from walk(node.right)

        # if tree NOT empty
        if self.root:
            yield from walk(self.root)

        return []


    def walk_dfs_postorder(self, node=None, level=0):
        '''
        An iterator that walks the tree in inorder DFS fashion.
        Yields (key, value) for each node in the tree.
        '''

        def walk(node):
            if node.left:
                yield from walk(node.left)
            
            if node.right:
                yield from walk(node.right)

            yield (node.key, node.value)

        # if tree NOT empty
        if self.root:
            yield from walk(self.root)

        return []


    def walk_bfs(self):
        '''
        An iterator that walks the tree in BFS fashion.
        Yields (key, value) for each node in the tree.
        '''

        # if tree NOT empty
        if self.root:
            queue = deque()
            queue.append(self.root)

            while len(queue) > 0:
                node = queue[0]
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                # dequeue and return
                queue.popleft()
                yield (node.key, node.value)

        return []


    ##################################################
    ###   Helper methods


    def _replace_node(self, oldnode, newnode):
        '''
        Internal method to remove a node from its parent
        '''
        #TODO: feel free to use or remove this method
        pass

    def _find(self, key, current_node):
        '''
        Internal method to find a node by key.
        Returns (parent, node).
        '''

        if key == current_node.key:            
            return current_node

        else:
            if key < current_node.key and current_node.left:
                return self._find(key, current_node.left)
            
            elif key > current_node.key and current_node.right:
                return self._find(key, current_node.right)
            
            # if key not found
            else:
                return None




class Node(object):
    '''
    A node in a binary tree.
    '''
    def __init__(self, parent, key, value):
        '''Creates a linked list.'''
        self.parent = parent
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        result = []
        def recurse(node, prefix1, side, prefix2):
            if node is None:
                return
            result.append(prefix1 + node.key + side)
            if node.right is not None:
                recurse(node.left, prefix2 + '\u251c\u2500\u2500 ', ' \u2c96', prefix2 + '\u2502   ')
            else:
                recurse(node.left, prefix2 + '\u2514\u2500\u2500 ', ' \u2c96', prefix2 + '    ')
            recurse(node.right, prefix2 + '\u2514\u2500\u2500 ', ' \u1fe5', prefix2 + '    ')
        recurse(self, '', '', '')
        return '\n'.join(result)
