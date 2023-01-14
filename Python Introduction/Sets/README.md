## Sets

- Sets are similar to lists or dictionaries.

- They are created using **curly braces { }**, and are unordered, which means that they can't be indexed.

- Due to the way they're stored, it's faster to check whether an item is part of a set using the in operator, rather than part of a list.

- Sets cannot contain duplicate elements.

### add() function

- You can use the add() function to add new items to the set

- Example:

        nums = {1, 2, 1, 3, 1, 4, 5, 6}

        nums.add(-7)

### remove() function

- You can use the remove() to delete a specific element to the set

- Duplicate elements will automatically get removed from the set.

- Example:

        nums = {1, 2, 1, 3, 1, 4, 5, 6}

        nums.remove(3)

### len() function

- The len() function can be used to return the number of elements of a set.

- Example:

        nums = {1, 2, 1, 3, 1, 4, 5, 6}

        print(len(nums))


