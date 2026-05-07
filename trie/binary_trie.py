from collections import deque
class Node():
    def __init__ (self,data : int):
        self.val :int= data
        self.left : Node | None = None
        self.right :Node | None = None

class BinaryTrie():
    def __init__(self):
        self.root = None

        pass

    def insertNode(self,val):
        new_node = Node(val)
        if not self.root :
            self.root = new_node
            return
        
        #travers and append
        q = deque([self.root])
        while q:
                node = q.popleft()
                if node.left == None:
                    node.left = new_node
                    return
                else :
                    q.append(node.left)
                if node.right == None:
                    node.right = new_node
                    return
                else:
                    q.append(node.right)
                    
    def printLevelOrder(self,node):
            if node == None:
                 return
            q = deque([self.root])
            res = [[]]
            curr_level = 0
            while q:
                for _ in range(len(q)):
                    n = q.popleft()
                    if curr_level >= len(res):
                         res.append([])

                    res[curr_level].append(n.val) # type: ignore
                    if n.left: # type: ignore
                         q.append(n.left) # type: ignore
                    if n.right: # type: ignore
                         q.append(n.right) # type: ignore
                curr_level +=1
            return res
    
if __name__ == '__main__':
    trie = BinaryTrie()
    nums = [1,2,3,4,5,6,7]

    for num in nums:
        trie.insertNode(num)

    res = trie.printLevelOrder(trie.root)
    print(res)