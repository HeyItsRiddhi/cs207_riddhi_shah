class Node():
    def __init__(self,value):
        self.value = value
        self.left_child = None
        self.right_child = None
class BinaryTree():
    def __init__(self):
        self.tree = None
    def insert(self,val):
        if(self.tree == None):
            self.tree = Node(val)
        else:
            self.add(val,self.tree)
    def add(self,value,node):
        if(value < node.value):
            if(node.left_child == None):
                node.left_child = Node(value)
            else:
                self.add(value,node.left_child)
        else:
            if(node.right_child == None):
                node.right_child = Node(value)
            else:
                self.add(value,node.right_child)
    def getValues(self,depth,node=None,vals=[]):
        if(node == None):
            if(self.tree == None):
                return []
            node = self.tree 
            vals = []
        if (depth==0):
            vals.append(node.value)
        else:
            if(node.left_child != None):
                self.getValues(depth-1,node.left_child,vals)
            else:
                for i in range(int(2**(depth-1))):
                    vals.append(None)
            if(node.right_child != None):
                self.getValues(depth-1,node.right_child,vals)
            else:
                for i in range(int(2**(depth-1))):
                    vals.append(None)
        return vals

    def search(self,value, node,parent=None):
        if(node != None):
            if(value < node.value):
                return self.search(value, node.left_child,node)
            elif(value > node.value):
                return self.search(value,node.right_child,node)
            elif(node.value == value):
                return parent,node
        else:
            raise Exception()
                    
    def remove(self, val):
        parent, node = self.search(val,self.tree)
        if(parent == None):
            self.tree = None
            return
        if((node.left_child == None) and (node.right_child == None)):
            if (parent.value > val):
                parent.left_child = None
            if (parent.value < val):
                parent.right_child = None
        if((node.left_child == None) or (node.right_child == None)):
            if (node.left_child != None):
                replacing_node = node.left_child
            if (node.right_child != None):
                replacing_node = node.right_child
            if (parent.value > val):
                parent.left_child = replacing_node
            if (parent.value < val):
                parent.right_child = replacing_node
        if((node.left_child != None) and (node.right_child != None)):
            replacing_node = node.left_child
            if (parent.value > val):
                parent.left_child = replacing_node
            if (parent.value < val):
                parent.right_child = replacing_node
                
from enum import Enum

class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3
    
class DFSTraversal():
    def __init__(self,tree,traversalType):
        self.tree = tree
        if(traversalType != DFSTraversalTypes.PREORDER and traversalType != DFSTraversalTypes.INORDER 
           and traversalType != DFSTraversalTypes.POSTORDER):
            raise ValueError("Must input a traversal type of the form DFSTraversalTypes.INORDER")
        else:
            self.type = traversalType
        #self.i = self.__iter__()
    
    def preorder(self, tree):
        if tree != None:
            yield tree.value
            yield from self.preorder(tree.left_child)
            yield from self.preorder(tree.right_child)
            
    def postorder(self, tree):
        if tree != None:
            yield from self.postorder(tree.left_child)
            yield from self.postorder(tree.right_child)
            yield tree.value
            
    def inorder(self,tree):
        if tree != None:
            yield from self.inorder(tree.left_child)
            yield tree.value
            yield from self.inorder(tree.right_child)
    
    def __iter__(self):
        if(self.type == DFSTraversalTypes.PREORDER):
            yield from self.preorder(self.tree)
        elif(self.type == DFSTraversalTypes.POSTORDER):
            yield from self.postorder(self.tree)
        else:
            yield from self.inorder(self.tree)
            
    '''def __next__(self):
        while True:
            try:
                return next(self.i)
            except StopIteration:
                break'''
    
    def changeTraversalType(self, traversalType):
        self.type = traversalType