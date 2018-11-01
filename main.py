from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class ArrayTree:
    def __init__(self, arr):
        self.arr = arr
        self.head = None

    def getHead(self):
        self.head = TreeNode(self.arr[0])
        head, arr = self.head, self.arr
        dq = deque([head])
        
        for i in range(1, len(arr), 2):
            temp = dq.popleft()
            while (not temp or not temp.val) and dq:
                temp = dq.popleft()
            
            if temp and temp.val:
                temp.left = TreeNode(arr[i])
                dq.append(temp.left)
                if i + 1 < len(arr):
                    temp.right = TreeNode(arr[i+1])
                    dq.append(temp.right)

        return head

class Utils:
    def arrFind(self, arr, val):
        try:
            return arr.index(val)
        except ValueError:
            return -1
