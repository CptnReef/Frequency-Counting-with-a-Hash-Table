from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)


  # 1️⃣ TODO: Complete the create_arr method.

  # Each element of the hash table (arr) is a linked list.
  # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.

  def create_arr(self, size):
    # creates array for linked list
    arr = []
    # I need every linked list to append to the array
    for i in range(size):
      #creating new linked list
      new_link = LinkedList()
      #adding it to the array
      arr.append(new_link)
    return arr



  # 2️⃣ TODO: Create your own hash function.

  # Hash functions are a function that turns each of these keys into an index value that we can use to decide where in our list each key:value pair should be stored. 

  def hash_func(self, key):
    # 1. Get the first letter of the key and lower case it 
    first_letter = key[0].lower() #"[a]pple"
    # 2. Calculate the distance from letter a
    distance_from_a = ord(first_letter) - ord('a')
    # 3. Mod it to make sure it is in range
    index = distance_from_a % self.size
    # returns index 
    return index



  # 3️⃣ TODO: Complete the insert method.

  # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

  def insert(self, key, value):
    # Check link_list is empty or not.  
    index = self.hash_func(key)
    self.linked_ls = self.arr[index]
    current = self.linked_ls.head

    # Going through the Hash Table for an empty node to assign key/value
    while current != None:
      # add if current node and key is True
      if current.data[0] == key:
        current.data[1] += value
        return
      # goes to the next node
      current = current.next

    # After Checking through Hash Table and linked list is empty
    self.linked_ls.append([key, value])
    


  # 4️⃣ TODO: Complete the print_key_values method.

  # Traverse through the every Linked List in the table and print the key value pairs.

  # For example: 
  # a: 1
  # again: 1
  # and: 1
  # blooms: 1
  # erase: 2

  def print_key_values(self):
    
    #Check all linked lists in the hashtable
    for self.linked_ls in self.arr:
      current = self.linked_ls.head
      
      while current != None:
        if current.data:
          print(f'({current.data[0]}: {current.data[1]}')
        current = current.next
              
          

    