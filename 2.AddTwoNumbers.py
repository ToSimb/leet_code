# class ListNode
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# functions
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode(0)
    x = head
    transfer = 0
    while l1 is not None or l2 is not None or transfer !=0 :
        d1 = l1.val if l1 is not None else 0
        d2 = l2.val if l2 is not None else 0
        sum = d1 + d2 + transfer
        if sum > 9:
            transfer = 1
            sum -= 10
        else:
            transfer = 0
        a = ListNode(sum)
        head.next = a
        head = head.next
        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None
    return x.next

# формирование mas1
mas1 = ListNode(5)
mass1 = mas1
mass1.next = ListNode(8)
mass1 = mass1.next
mass1.next = ListNode(2)
mass1 = mass1.next
mass1.next = ListNode(2)
mass1 = mass1.next
mass1.next = ListNode(2)

# формирование mas2
mas2 = ListNode(2)
mass2 = mas2
mass2.next = ListNode(5)

mas3 = addTwoNumbers(mas1,mas2)
# вывод
while mas3 is not None:
    print (mas3.val)
    mas3 = mas3.next

