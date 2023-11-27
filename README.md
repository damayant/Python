# Python
Below is a chart of popular and common data structures in Python, along with brief descriptions and examples of their implementations:

| Data Structure     | Description                                                                 | Example Implementation                                                    |
|--------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Lists              | Ordered, mutable collections of elements                                    | ```my_list = [1, 2, 3, 'hello', True]```                                  |
| Tuples             | Immutable ordered collections of elements                                   | ```my_tuple = (1, 2, 3, 'hello', True)```                                |
| Sets               | Unordered collections of unique elements                                    | ```my_set = {1, 2, 3, 3, 4}```                                           |
| Dictionaries       | Key-value mappings                                                          | ```my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}```           |
| Strings            | Sequence of characters                                                      | ```my_string = 'Hello, World!'```                                        |
| Stack              | Last In, First Out (LIFO) data structure                                    | Using a list with `append()` and `pop()` methods                         |
| Queue              | First In, First Out (FIFO) data structure                                    | Using `collections.deque` with `append()` and `popleft()` methods        |
| Linked List        | Collection of elements, each connected by a link                            | Implementing a simple Linked List class with nodes and pointers          |
| Trees              | Hierarchical data structure with nodes connected by edges                   | Implementing Binary Search Tree, AVL Tree, etc.                          |
| Heaps              | Special type of binary tree satisfying the heap property                    | Using `heapq` module in Python                                            |
| Hash Tables        | Key-value data structure using a hash function to index data                | Using Python's built-in dictionary (dictionary comprehension)            |
| Graphs             | Collection of nodes and edges connecting those nodes                        | Implementing an adjacency list or adjacency matrix representation       |



#### Strings : https://www.thelearningpoint.net/computer-science/learning-python-programming-and-data-structures/learning-python-programming-and-data-structures--tutorial-12--string-manipulation

#### LIST vs TUPLE vs SET vs DICTIONARY 
https://www.geeksforgeeks.org/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/
Lists and tuples are both data structures in Python used to store collections of elements, but they have some key differences in terms of mutability, syntax, and use cases. Here's a comparison between lists and tuples:

Lists:
1. Mutability: Lists are mutable, which means you can add, remove, or modify elements after creating the list.
2. Syntax: Lists are defined using square brackets `[]`.
3. Use cases: Lists are suitable for collections where elements may need to be modified or reordered, such as a list of tasks, items in a shopping cart, etc.
4. Performance: Due to their mutability, lists might consume more memory and have slightly slower performance compared to tuples.

Example:
```python
my_list = [1, 2, 3, 'hello', True]
my_list.append(4)      # Modify - Adding an element
my_list[1] = 'world'   # Modify - Modifying an element
```

Tuples:
1. Immutability: Tuples are immutable, which means once created, you cannot modify their elements.
2. Syntax: Tuples are defined using parentheses `()`.
3. Use cases: Tuples are suitable for situations where the collection of elements should remain unchanged throughout the program, such as coordinates, date and time values, etc.
4. Performance: Tuples are generally more memory-efficient and have slightly better performance compared to lists because of their immutability.

Example:
```python
my_tuple = (1, 2, 3, 'hello', True)
# my_tuple[1] = 'world'  # Error - Tuples are immutable, so you can't modify elements
```

In summary, use lists when you need a mutable collection that can be modified, and use tuples when you need an immutable collection to ensure data integrity and for more memory-efficient storage of constant data.

### Slicing : https://www.geeksforgeeks.org/string-slicing-in-python/?ref=lbp

