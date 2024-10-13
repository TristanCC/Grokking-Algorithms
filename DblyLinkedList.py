#   Array:
#   Reading: O(1) Insertion: O(n) Deletion: O(n)
#   
#   Linked List 
#   Reading: O(n) Insertion: O(1) Deletion: O(1) (ONLY IF AT BEGINNING OR END) otherwise O(n)
# 

class Node:
    def __init__(self, val, next = None, prev = None) -> None:
        self.val = val
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self, head: Node, tail = None) -> None:
        self.head = head
        self.tail = head

def buildLinkedList(arr) -> LinkedList:

    list = LinkedList(Node(arr[0]))
    curr = list.head
    for i in range(1,len(arr)):
        temp = curr
        curr.next = Node(arr[i])
        curr = curr.next
        curr.prev = temp
    list.tail = curr
    return list


def printLinkedList(list: LinkedList):

    curr = list.head
    ret = ''
    while curr:
        ret += f'{curr.val}' + '<--->'
        curr = curr.next
    print(ret)
    return ret

def searchForward(list: LinkedList, target):
    curr = list.head
    pos = 1        # 1 indexed
    while curr and curr.val != target:
        curr = curr.next
        pos += 1
    if curr.val == target:
        
        print(f'found {target} at {pos} (1-indexed)')

def searchBackward(list: LinkedList, target):
    curr = list.tail
    pos = -1        # 1 indexed
    while curr and curr.val != target:
        curr = curr.prev
        pos -= 1
    if curr.val == target:

        print(f'found {target} at {pos} (-1-indexed)')


arr = [1,2,3,4,5,6,7,8,9,10]

linkedList = buildLinkedList(arr)

printLinkedList(linkedList)

searchForward(linkedList,5)
searchBackward(linkedList, 5)