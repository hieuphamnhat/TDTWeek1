import collections
linked_lst = collections.deque()
linked_lst.append('1')
linked_lst.append('2')
linked_lst.append('3')
  
print("elements in the linked_list:")
print(linked_lst)
  
#adding element at an arbitary position
linked_lst.insert(1,'4')
  
print("elements in the linked_list:")
print(linked_lst)
  
#deleting the last element 
linked_lst.pop()
  
print("elements in the linked_list:")
print(linked_lst)
  
#removing a specific element
linked_lst.remove('4')
  
print("elements in the linked_list:")
print(linked_lst)
