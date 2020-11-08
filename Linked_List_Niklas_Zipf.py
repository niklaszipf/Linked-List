class Node: 
    def __init__(self, data = None, next_item = None):
        self.data = data
        self.next_item = next_item
        self.head = None


    # We define the Class Node. This Node is a Data Structure, which is needed to create linked lists.
    # The init function creates the first Node of the linked list. A Node contains the data and the information, which element is the next element of the list.
    # The initial Node which is created contains no data and no link, because there exists no other Node. It is the head Node of the linked List.


    def insert_at_beginning_ll(self, data): 
        node = Node(data, self.head)
        self.head = node


    # The insert_at_beginning_ll function creates a new Node, which stores the current head Node as the next item.
    # So the new Node will be created in front of the previously first element of the linked list.
    # As it is now the head node, the head of the linked list has to be updated.


    def len_ll(self):
        counter = 0
        cur = self.head
        while cur:
            counter += 1
            cur = cur.next_item
            
        return counter
    

    # The len_ll function iterates thru the entire linked list and thereby counts the elements to find out the length of the list.


    def goto_index_ll(self, position):
        if position > self.len_ll()-1:
            return 'Position index out of range'
        
        index = 0
        current_node = self.head
        while index < position:
            current_node = current_node.next_item
            index +=1
            
        return current_node


    # The goto_index_ll function returns the Node at the position equal to the index which was given to the function.
    # It iterates thru the linked list until it is at the right position and then returns the Node
    # Before it does that, it checks whether the given index is larger than the length of the list and if true, returns an error message.
    # This function is used with the 


    def insert_ll(self, current_node, data):
            
        node = Node(data, current_node.next_item)
        current_node.next_item = node


    # The insert_ll function takes in the Node after which the new Node should be inserted and the data of the new Node.
    # It creates the new Node with the next item beeing the next item of the Node, after which it should be inserted.
    # So that our new node doesn´t get skipped in the list, the pointer of the Node in front of our new Node gets updated to point to our new Node.
    # You have to use the goto_index_ll function, to get the current node, after which the new Node should be inserted.
    # You could do it in these two ways:
    #
    #   1.    linked_list.insert(linked_list.goto_index_ll(i), data)
    # or
    #   2.    x = linked_list.goto_index_ll(i)
    #         linked_list.insert(x, data)
    #
    # You could combine these two functions into one, but for proving that insertion at any place and for any size of list is constant,
    # it is easier to have two separate functions.
    #
    # The combined function could look like this:
    # 
    # def insertll(self, position, data):
    #   if position > self.lenll()-1:
    #       return 'Position index out of range'
    #   
    #   index = 0
    #   current_node = self.head
    #   while index < position:
    #       current_node = current_node.next_item
    #       index +=1
    #       
    #   node = Node(data, current_node.next_item)
    #   current_node.next_item = node


    def print_ll(self):
        
        list_ = []
        cur = self.head
        
        while cur:
            list_.append(cur.data)
            cur = cur.next_item
        
        return list_


    # This function creates an empty list (not a linked list) and iterates thru the linked list, on which the function was called.
    # It appends the data of every item to the list and in the end returns the list.
    # This function was used to check whether the insertion operations worked as they were supposed to do.



# ~~~ Time Complexity ~~~


# In the following linked lists of different sizes are created (100K, 200K, 400K, 800K, 1.6M, 3.2M).
# For a list of every size, an element gets inserted after the element with index 0, index 10.000 and index 50.000.
# The Time for every insertion is measured and printed, together with the information on list size and position of insertion.
# In the End all the results are printed together for each position of insertion.
# I will explain the calculation of the time for insertion after index 0. The calculation for the other positions is the same, just with a different index.
# When running the code it will be shown that no matter where the item is inserted or how large the list is,
# the time it takes to insert the element is always constant (On my Computer always Zero, but it may differ depending on hardware.)


import time # We import time, so that we can measure the runtime of our function.

# ~~~ Insertion after position 0 ~~~

results_insert_at_0_lists = [] # In this list the results of the runtime will be stored

n = 100000 # Our first list will be of this size

while n <= 3200000: # At the end of the loop we will double the list size, to get larger lists. This determines our maximum list size.
    
    insert_at_0_list = Node() # An empty linked list is created.
    
    for z in range(0, n): # We fill in n elements into the linked list. 
        insert_at_0_list.insert_at_beginning_ll(z) # We insert at the beginning, because it is the quickest method.
    
    i = insert_at_0_list.goto_index_ll(0) # We find the Node of the given index and store it as i.
                                          # We do it before the time measurement, because it is not part of calculating the time complexity.
        
    start = time.time() # We start the time measurement
    
    insert_at_0_list.insert_ll(i, 1) # The new item gets inserted after the previously found Node i. 
    
    end = time.time() # We end the time measurement
    
    total_time = end - start # The runtime is calculated
    
    print('Insertion after position 0 of a linked_list with n = ' + str(n) + " :") # Here we print the information for the afterwards printed result.

    print(total_time) # The result is printed.
    
    results_insert_at_0_lists.append(total_time) # The time gets stored in our list of results
    
    n = n * 2  # The variable determining the list size gets doubled. 
    

# ~~~ Insertion after position 10000 ~~~

    
results_insert_at_10000_lists = []

n = 100000

while n <= 3200000:
    
    insert_at_10000_list = Node()
    
    for z in range(0, n):
        insert_at_10000_list.insert_at_beginning_ll(z)
    
    i = insert_at_10000_list.goto_index_ll(10000)
    
    start = time.time()
    
    insert_at_10000_list.insert_ll(i, 1)
    
    end = time.time()
    
    total_time = end - start
    
    print('Insertion after position 10.000 of a linked_list with n = ' + str(n) + " :")

    print(total_time)
    
    results_insert_at_10000_lists.append(total_time)
    
    n = n * 2


# ~~~ Insertion after position 50000 ~~~


results_insert_at_50000_lists = []

n = 100000

while n <= 3200000:
    
    insert_at_50000_list = Node()
    
    for z in range(0, n):
        insert_at_50000_list.insert_at_beginning_ll(z)
    
    i = insert_at_50000_list.goto_index_ll(50000)
    
    start = time.time()
    
    insert_at_50000_list.insert_ll(i, 1)
    
    end = time.time()
    
    total_time = end - start
    
    print('Insertion after position 50.000 of a linked_list with n = ' + str(n) + " :")

    print(total_time)
    
    results_insert_at_50000_lists.append(total_time)
    
    n = n * 2
    


print('Times for insertion after position 0 in different sized Linked_Lists: ' + str(results_insert_at_0_lists))
print('Times for insertion after position 10.000 in different sized Linked_Lists: ' + str(results_insert_at_10000_lists))
print('Times for insertion after position 50.000 in different sized Linked_Lists: ' + str(results_insert_at_50000_lists))