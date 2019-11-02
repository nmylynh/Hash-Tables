# Arrays with Brady Fukumoto

## An array is a sequence of elements of the **same type** stored in a contiguous block of memory

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

- **Step 1, How big?**: An integer is 4 bytes, so the array needs to be 16-bytes because there's 4 integers.
- **Step 2, Request memory space**: So we request 16 bytes from the computer.
- **Step 3, Get the Address**: Once the operating system reserves that memory, it returns to us the address to the start of that reserved block.
- **Step 4, Write Values**: And then we can put our values into that array. We can set our reserved memory to be `[2, 3, 4, 5]`

#### How it looks like in memory:

- The address of the memory block in on the top of the row (e.g. 25600).
- You can see that there's 8 `1`'s or `0`'s. This is because there's 8 bits in one byte, as mentioned above. Therefore in memory we should see 16 blocks, which represents 16 bytes of memory alloted for our array.

| 25600       | 25601       | 25602      | 25603      |
|-------------|-------------|------------|------------|
| 00000000    | 00000000    | 00000000   | 00000000   |
| ----------  | ----------- | -----------| ---------- |
| 25604       | 25605       | 25606      | 25607      |
| ----------- | ----------  | ---------- | ---------- |
| 00000000    | 00000000    | 00000000   | 00000000   |
| ----------  | ----------- | -----------| ---------- |
| 25608       | 25609       | 25610      | 25611      |
| ----------- | ----------  | ---------- | ---------- |
| 00000000    | 00000000    | 00000000   | 00000000   |
| ----------  | ----------- | -----------| ---------- |
| 25612       | 25613       | 25614      | 25615      |
| ----------- | ----------  | ---------- | ---------- |
| 00000000    | 00000000    | 00000000   | 00000000   |

