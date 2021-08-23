# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        addition_val = 0
        cont = True
        l1_node = l1
        l2_node = l2
        iterator = 0
        
        while cont is True:
            if l1_node.next != None and l2_node.next != None:

                addition_val += l1_node.val*10**iterator + l2_node.val*10**iterator
                l1_node = l1_node.next
                l2_node = l2_node.next
                
            elif l1_node.next == None and l2_node.next != None:

                
                addition_val += l1_node.val*10**iterator + l2_node.val*10**iterator
                
                new_node = ListNode()
                new_node.val = 0
                new_node.next = None
                l1_node = new_node
                l2_node = l2_node.next
                
            elif l1_node.next != None and l2_node.next == None:

                addition_val += l1_node.val*10**iterator + l2_node.val*10**iterator
                
                new_node = ListNode()
                new_node.val = 0
                new_node.next = None
                l2_node = new_node
                l1_node = l1_node.next

            else:       
                
                addition_val += l1_node.val*10**iterator + l2_node.val*10**iterator
                cont = False
            
            iterator += 1
                              
        #make new linked_list
        list_of_nodes = []
        string = str(addition_val)
        #print(string)
        
        for char in string:
            next_node = ListNode()
            next_node.val = int(char)
            next_node.next = None
            list_of_nodes.append(next_node)    
            
        first_node = list_of_nodes[len(list_of_nodes)-1]   
        
        if len(list_of_nodes) == 2:
            first_node.next = list_of_nodes[0]
            return first_node
            
        for node in range(len(list_of_nodes)-2, 0, -1):
            list_of_nodes[node].next = list_of_nodes[node-1]
            if node == len(list_of_nodes)-2:
                first_node.next = list_of_nodes[node]
                
        return first_node        