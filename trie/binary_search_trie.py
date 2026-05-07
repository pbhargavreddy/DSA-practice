from collections import deque

class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.left: Node | None = None
        self.right: Node | None = None
        
class BinarySearchTrie():
    def __init__(self):
        self.root = None
        pass
    
    def insertNode(self,val):
        new_node = Node(val) # type: ignore 
        if not self.root:
            self.root = new_node
            return
        curr = self.root

        while(True):
            if curr.val < val :
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = new_node
                    return
            else:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = new_node
                    return
    
    # In below function, in for loop, at first we do it for in range(len(q)). 
    # Inside loop even though we appedn to q the loop would itterate for the first len(q) only.
    def printLevelOrder(self):
        if not self.root:
            return
        
        q = deque([self.root])
        res = [[]]
        curr_index = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if curr_index >= len(res):
                    res.append([])
                res[curr_index].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            curr_index +=1
        # print(res)
        return res
    


if __name__ == '__main__':
    bst = BinarySearchTrie()
    nums = [4, 2, 6, 1, 3, 5, 7]
    for num in nums:
        bst.insertNode(num)
    res = bst.printLevelOrder()
    if res:
        for level in res:
            print(*level)
        