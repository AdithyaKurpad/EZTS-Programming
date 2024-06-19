class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None

def leaf(root):
    if root==None:
        return 0
    LH=leaf(root.left)
    RH=leaf(root.right)
    if LH==0 and RH==0:
        print(root.value,end=" ")


if __name__=="__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(3)
    root.left.left=node(4)
    root.left.right=node(5)
    root.right.left=node(6)
    root.right.right=node(7)
    root.left.right.left=node(9)
    root.left.right.right=node(10)
    root.right.right.right=node(11)
    root.left.right.left.left=node(12)
    root.left.right.left.right=node(13)
    leaf(root)