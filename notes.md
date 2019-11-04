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

1. **Step 1: How big?**: An integer is 4 bytes, so the array needs to be 16-bytes because there's 4 integers.
2. **Step 2: Request memory space**: So we request 16 bytes from the computer.
3. **Step 3: Get the Address**: Once the operating system reserves that memory, it returns to us the address to the start of that reserved block.
4. **Step 4: Write Values**: And then we can put our values into that array. We can set our reserved memory to be `[2, 3, 4, 5]`

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
   - This is an O(n) operation because you're copying element one by one

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


    [56, 88, 88, 88, 88, 120, 120, 120, 120, 184, 184, 184, 184, 184, 184, 184, 184, 256, 256, 256, 256, 256, 256, 256, 256, 256, 336, 336, 336, 336, 336, 336, 336, 336, 336, 336, 424, 424, 424, 424, 424, 424, 424, 424, 424, 424, 424, 520, 520, 520, 520, 520, 520, 520, 520, 520, 520, 520, 520, 632, 632, 632, 632, 632, 632, 632, 632, 632, 
    632, 632, 632, 632, 632, 760, 760, 760, 760, 760, 760, 760, 760, 760, 760, 760, 760, 760, 760, 760, 760, 904, 904, 904, 904, 904, 904, 904, 904, 904, 904, 904, 904]       

>The `sys` module has this neat function called `getsizeof()` which tells you how much memory each of these is occupying.

>In the above function, you append an integer into the `x` array, and for each added element, you append the size of the array inside the `sizes` array.

#### Steps:

1. Overhead metadata(like size of array) in an empty list would be 56 bits. 
2. Apparently each object in my computer would be 56 bits.
  - This will be the same as saying 8 bytes
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

>Hash tables are arguably the single most important data structure known to mankind. You absolutely **have** to know how they work. -"Get That Job at Google" by Steve Yegge

>Hash tables have the coveted property of constant time complexity for search, insertion, and deletion which no other data structure can match.

![data structure time complexity](https://i.imgur.com/Xg4VK5f.png "Time Complexity of Data Structures")
