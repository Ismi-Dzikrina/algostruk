class Node(object):
    """sebuah simpul di linked list"""
    def __init__(self,data,next= None):
        self.data = data
        self.next = next
def kunjungi(head):
    curNode=head
    while curNode is not None:
        print(curNode.data)
        curNode = curNode.next

m = 4 
n = 5 
x = [0]*m 
for i in range(m): 
    x[i] = [1]*n 
print (x)

