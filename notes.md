# Arrays with Brady Fukumoto

## An array is a **sequence** of elements of the **same type** stored in a **contiguous block of memory**

### I. How do you declare an array?
1. Determine how big the array needs to be
2. Request a block of memory that will fit the array
3. Receive the memory address of the reserved block
4. Write your values into that array

#### Example:

*Before we start*:
- A byte consists of 8 bits, and a bit is either a 1 or a 0.
- 4 bytes is going to be 32 bits.

        Declare the array: [2, 3, 4, 5]

1. **Step 1: How big?**: 
   1. An integer is 4 bytes, so the array needs to be 16-bytes because there's 4 integers.
2. **Step 2: Request memory space**: 
   1. So we request 16 bytes from the computer.
3. **Step 3: Get the Address**: 
   1. Once the operating system reserves that memory, it returns to us the address to the start of that reserved block.
4. **Step 4: Write Values**: 
   1. And then we can put our values into that array. We can set our reserved memory to be `[2, 3, 4, 5]`

#### How it looks like in memory:

- The address of the memory block in on the top of the row (e.g. 25600).
- You can see that there's 8 `1`'s or `0`'s. This is because there's 8 bits in one byte, as mentioned above; Therefore in memory we should see 16 blocks, which represents 16 bytes of memory alloted for our array.
- So 25600 would be the 25600th block of memory, as you can imagine memory as a huge series of contiguous blocks.

| 25600    | 25601    | 25602    | 25603    |
| -------- | -------- | -------- | -------- |
| 00000000 | 00000000 | 00000000 | 00000010 |

| 256004   | 25605    | 25606    | 25607    |
| -------- | -------- | -------- | -------- |
| 00000000 | 00000000 | 00000000 | 00000011 |

| 25608    | 25609    | 25610    | 25611    |
| -------- | -------- | -------- | -------- |
| 00000000 | 00000000 | 00000000 | 00000100 |

| 25612    | 25613    | 25614    | 25615    |
| -------- | -------- | -------- | -------- |
| 00000000 | 00000000 | 00000000 | 00000101 |

**Notes on size**:

- A `kilobyte` is a thousand bytes of memory.
- A `megabyte` is a million bytes of memory.
- A `gigabyte` is a billon bytes of memory.

**Notes on Binary**:
- The 1s and 0s are representative of numbers since computers represent integers on a base 2 system of 0 and 1

#### To access an index in the array:

To access an index of an array, you multiply the index with the size of the type and add the start address.

    index * sizeof(type) + start_address

For example, if you want to access the third index of the array, you have to do:

    2 * 4 + 25600 = 25608

Where:
- index : `2`
- size of type which is 4 bytes (an integer is 4 bytes): `4`
- add to start address which is `25600`
- So that gives us the address of the third element of the array

>Accessing a specific address in memory happens in constant time (O(1)) which is the fastest it can be
>Overall, arrays are the most time and space efficent data structure that we have


#### How do you add an element to the end of an array?

1. Take the size of your current array and increase it by one element
2. Request a block of memory of the new size
3. Copy each element from the old space to the new space one at a time
4. Free the memory from the old array
   1. This is an O(n) operation because you're copying element one by one

## Python Lists:

### Python lists are arrays with a lot of built-in functionality.
- Python will allocate a few empty spaces each time the array grows
- Each time it grows, it allocates a bite more extra space than the previous
- Adding an element to the end of a list is usually O(1) but sometimes O(n)
  - On average, can be considered O(1)
  
### How does Python add an element to the end of a list?

```python
    import sys
    x = []
    sizes = [sys.getsizeof(x)]

    for i in range(0, 100):
        x.append(1)
        sizes.append(sys.getsizeof(x))

    print(sizes)

```
The code above would output:


    [56, 
    88, 88, 88, 88, 
    120, 120, 120, 120, 
    184, 184, 184, 184, 184, 184, 184, 184, 
    256, 256, 256, 256, 256, 256, 256, 256, 256, 
    336, 336, 336, 336, 336, 336, 336, 336, 336, 336, 
    424, 424, 424, 424, 424, 424, 424, 424, 424, 424, 424, 
    520, 520, 520, 520, 520, 520, 520, 520, 520, 520, 520, 520, 
    632, 632, 632, 632, 632, 632, 632, 632, 632, 
    632, 632, 632, 632, 632, 
    760, 760, 760, 760, 760, 760, 760, 760, 760, 760, 760, 760, 760, 760, 760, 760, 
    904, 904, 904, 904, 904, 904, 904, 904, 904, 904, 904, 904]       

>The `sys` module has this neat function called `getsizeof()` which tells you how much memory each of these is occupying.

>In the above function, you append an integer into the `x` array, and for each added element, you append the size of the array inside the `sizes` array.

#### Steps:

1. Overhead metadata(like size of array) in an empty list would be 56 bits. 
2. Apparently each object in my computer would be 56 bits.
   1. This will be the same as saying 8 bytes
3. Allocating space initially in a list will grow by 4 bytes, so then we would have `88` 4 times, because `56 + 32 = 88`
4. As the list grows larger, it then adds 8 bytes instead of 4, so you get `184` eight times as `120 + 64 = 184`
   
#### Time complexity:

- Each time the size stays the same, it's a O(1) operation
- Each time the size grows, it's a O(n) operation since we need to copy everything from the old array to the new array
- Efficient mathematically, but you cannot guarantee when you're going to have an O(n) operation

### How does Python add an element to the BEGINNING of a list?

1. Check if there's any empty space at the end of the array
2. If not:
   1. Allocate a new array, place the first element and copy over the rest
   2. Free memory from the old array
3. If so:
   1. Starting from the back, move EACH element to the right one space
   
#### Time complexity of this operation will always be O(n) no matter what because you have to shift every element to the right to insert that element to the beginning of the list

```python

# 0(n)
def add_to_back(n):
    x = []
    for i in range(0, n):
        x.append(i + 1)
    return x

# 0(n^2)
def add_to_front(n):
    x = []
    for i in range(0, n):
        x.insert(0, n - i)
    return x

```

To test out the runtimes:

```python

import time

# adding to the back is O(n)
start_time = time.time()
add_to_back(500000) 
end_time = time.time()
print (f'runtime: {end_time - start_time} seconds')

# runtime: 0.08344292640686035 seconds

# adding to the front is O(n^2)
start_time = time.time()
add_to_front(500000) 
end_time = time.time()
print (f'runtime: {end_time - start_time} seconds')

# runtime: 50.613221168518066 seconds

```
From the output, you can tell that `add_to_back()` is over 600x faster than `add_to_front`!!

This is because you have hidden nested for loops when you add to the front because you're shifting all the numbers to allocate for the inserted number in the front

## In conclusion

1. Arrays are extremely time and space efficient 
   - In theory, arrays are extremely space efficient because it takes the minimal amount of space and space isn't so wasted
   - But not always in the event of over-allocations in python lists
2. Python lists take care of simple operations for you
   - But it's not magic.
   - Inserting an element in front of an array is still an O(n^2) operation
3. Understanding arrays can make your code much more efficient!

# Hash Tables

>"Hash tables are arguably the single most important data structure known to mankind. You absolutely **have** to know how they work." -"Get That Job at Google" by Steve Yegge

>Hash tables have the coveted property of constant time complexity for search, insertion, and deletion which no other data structure can match.

![data structure time complexity](https://i.imgur.com/Xg4VK5f.png "Time Complexity of Data Structures")

## What are hash tables?

### They're the data structure behind:
1. Associative Arrays and Dictionaries
2. Objects (Python, Javascript, Ruby)
   1. Hash tables are used to implement functionality underneath the hood behind the objects
3. Caches
   1. Memcached, which does HTTP caching
4. Dynamic Programming, Memoization

## How do Hash Tables work?

![data structure time complexity](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Hash_table_3_1_1_0_1_0_0_SP.svg/1200px-Hash_table_3_1_1_0_1_0_0_SP.svg.png "Hash Table")

>Hash Tables are basically an implementation of key and value data storage and retrieval.

Aforementioned, an array is a sequence of elements of the same type stored in a contiguous block of memory, which allows for constant time access.
    - What that means is that each element of an array is right next to each other in memory.
    - Which means that, if you want to get to the fifth element, all you have to do is multiply 5 times the size of your data, and then you can skip right there.

**Steps:**
1. A Hash table will take a key in any form, usually a string, 
2. runs it through a hash function, which will change that key into an integer
3. The integer is then run through a modulo function to make sure it's within a certain range, in the above case, `0 - 15`.
4. John Smith is a string:
   1. he gets run through a hash function 
   2. he turns into a 2
   3. and then the value associated with the john smith key gets put into this #2 bucket in the hash array
5. Lisa smith the strong gets run through the hash function
   1. it becomes 1
   2. then 1 is where our value is stored

**Pseudo-code:**

    hash_table[Key] = Value;

    // int index = hash_function(Key) % array.length;
    // array[index] = Value;

## What is a Hash Function?

1. One-way mapping from arbitrary data to fixed data size and type
2. There's many different hash functions with different attributes:
   1. **Deterministic:** with the same input and the same function you'll always get the same output (cryptographic hashing)
   2. **Uniform Distribution:** an input that's very close to another input will be on average, very very far away from the original input
   3. **Non-invertible:** you cannot take the result of the hash function and reverse construct the input
   4. **Continuous vs. non-continuous** 

The following hash function sums the ascii values of the characters in a string, add them together, and returns the total modulo of 32, which will be an integer between 0 and 31.

>The ASCII table has 128 characters, with values from 0 through 127. Thus, 7 bits are sufficient to represent a character in ASCII; however, most computers typically reserve 1 byte, (8 bits), for an ASCII character.
```c++
    // String --> integer (0, 31)

int basic_string_hash (char str[]) {
    {
        int hash = 0;
        for (int i = 0 ; str[i] != '\0' ; i++) {
            hash += str[i];
        } 
        return hash % 32
    }
}
```

So if we were to hash the string `hello`

```c++

basic_string_hash("Hello");
// ['H', 'e', 'l', 'l', 'o'] -> [72, 101, 108, 108, 111] -> 500
// 500 % 32 = 20

basic_string_hash("World");
// ['W', 'o', 'r', 'l', 'd'] -> [87, 111, 114, 108, 100] -> 520
// 520 % 32 = 8
```

The purpose of the hash function when it comes to hash tables is to turn an input key into an array index, and since our array is size 32, we want an index to be between 0 to 31.

### How it works:

1. **Declare an empty array**
   1. Usually in powers of 2 (32) so that it fits nicely in memory
   2. Allocate that much memory using the malloc function in C (where Keys are of type string and Values of type integer)
      1. `arr = malloc (DEFAULT_SIZE * sizeof(VALUE_TYPE));`
      2. so `32 * sizeof(integer)`
2. To find out where we're going to store it, we **hash the Key**:
   1. `basic_string_hash("Hello")` -> 20
3. Then we store our value, or **Assign Value to hash index**
   1. arr[20] = Value;
   2. so it's stored in slot 20 of our array `arr[20] = 1224` 

# Collisions and Resizing

## What are collisions?

Hash table collisions are when two keys hash to the same index.

### What are the chances of a collision?

To look at the chances of a collision, we look at the *Birthday Problem.*

>"In probability theory, the birthday problem or birthday paradox concerns the probability that, in a set of n randomly chosen people, some pair of them will have the same birthday. By the pigeonhole principle, the probability reaches 100% when the number of people reaches 367 (since there are only 366 possible birthdays, including February 29). However, 99.9% probability is reached with just 70 people, and 50% probability with 23 people. These conclusions are based on the assumption that each day of the year (excluding February 29) is equally probable for a birthday." -Wikipedia

The collision formula is:

    collision_probablity = 1 - k! / ((k - n)! * k^n)

The takeaway is that collisions are unavoidable. There isn't a way to avoid collisions mathematically so we develop ways to address them.

### Handling collisions
1. Open Addressing
2. Linked List Chaining

### Linked List Chaining
1. Elements in the hash table are stored as linked lists
   1. In each of these elements you store the key and the value and the pointer to the next value in the chain
   2. If it's the only element, the pointer will be a null pointer which tells you that you've reached the end of a list
   3. The general hash table methods still apply:
      1. you take a key 
      2. you run it through a hash function
      3. based on that you get an index of an array
      4. you use that index, in an insert case, to insert it into the appropriate bucket
2. When retrieving a value, traverse down the linked list until you find the matching key
   1. What changes here is that you don't have just one element in an array you might have a linked list, so in this (insert) case:
      1. you need to traverse down the linked list to see if the key is already there
      2. so if you have 3 elements in a linked list chain you need to traverse it to see if the key matches
      3. if it doesn't, move onto the second,
      4. then move onto third to `null` pointer, and then put it at the end of the linked list
3. When you do see a matching key, with linked list you want to overwrite the value
   1. So if found, overwrite
   2. If not, add to end of linked list

### Linked List Chaining Performance

1. Time complexity is linear time since we need to go through each element of the linked list, and you have no information-- if it's the first, second or third element
   1. Insert, delete, and search for linked lists are `O(n)`
   2. In a worst case scenario, let's say you insert five keys and it all hashes to the same value
      1. Then these insert, delete, and search elements would degrade from constant time complexity or O(1) to linear time complexity, or O(n)
         1. Since you'll need to hit n elements in order to get down to the nth element of the linked list chain
2. Linked lists also have some effect on space complexity
   1. Instead of storing the value as you would in a normal array, you must store the key so you can check (when you're doing your linked list check) the value (which is the value that's stored), and also a pointer to the next entry
      1. This is all extra overhead and it could take up to triple or even more space over a regular linked list without any chaining
   2. Must store key, value, and pointer for each hash table entry
   3. You may have a lot of empty slots
      1. Worst case scenario--all five elements hashing to the same element
      2. you may have a hash table with 128 slots but all the values are placed in one slot so your hash tables have 127 empty slots
   4. To store n elements in a hash table it is still a O(n) no matter if your elements are all hashed to the same slot

### Hash Table Resizing

>The load factor is a measure of how full the hash table is allowed to get before its capacity is automatically increased. ... The expected number of entries in the map and its load factor should be taken into account when setting its initial capacity, so as to minimize the number of rehash operations.

#### Resources

1. [hashing and hash tables](https://www.ibrahimgabr.com/blog/2017/12/17/python-hashing-and-hash-tables)
2. [load factor and rehashing](https://www.geeksforgeeks.org/load-factor-and-rehashing/)

>The more elements you have to traverse down a linked list chain, the closer to that big-O of n you're going to hit--that's measured as the load factor.

1. Load factor = (number of entries) / (hash table capacity)
2. When load factor passes a certain threshold, resizing can occur
   1. create a new hash table with double capacity
   2. copy elements from the old hash table to the new one at a time
   3. resizing is O(n) BUT occurs at O(log n) frequency


1. In our basic hash table with no collision handling, we have a max load capacity of `1`. That means every single slot of the hash table is occupied-- so the total number of entries is equal to the total capacity.

2. However, with linked list it's possible to have `load factor > 1`, since you can have every slot in the hash table full, but also have each slot contain multiple elements in a linked list chain.

3. However, the longer our linked list get, the worse the performance the hash table gets. So in most high level languages, you would have a test or a check every time you do an insert, and when the load factor passes a certain threshold, like 0.7 like Java, it will resize the entire hash table.

4. It will create an empty hash table double the size of the original hash table, and then copy over the elements one at a time. Each of the keys is re-hashed, and when everything is copied over, it will free all the memory from the original hash table.

#### Time complexity

1. Resizing is a O(n) since we have to copy over each element from the list, but since it occurs at a log(n) declining frequency, it still averages out to a constant time insert O(1).