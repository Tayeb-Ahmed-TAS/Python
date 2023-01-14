## List Comprehension

- List comprehensions are a useful way of quickly creating lists whose contents obey a rule.

- Example:

        cubes = [i**3 for i in range(5)]

        print(cubes)

  - Output: [0, 1, 8, 27, 64]

- List comprehensions are inspired by set-builder notation in mathematics.

- A list comprehension can also contain an if statement to enforce a condition on values in the list.

- Example:

        evens=[i**2 for i in range(10) if i**2 % 2 == 0]

        print(evens)

  - Output: [0, 4, 16, 36, 64]

### Symtax =>

    [ expression for item in list ]
