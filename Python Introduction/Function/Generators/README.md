## Generators

- **Generators** are a type of iterable, like lists or tuples.

- Unlike lists, they don't allow indexing with arbitrary indices, but they can still be iterated through with **for** loops.

- They can be created using functions and the **yield** statement.

- The **yield** statement is used to define a generator, replacing the return of a function to provide a result to its caller without destroying local variables.

- Due to the fact that they **yield** one item at a time, generators don't have the memory restrictions of lists. 

- In fact, they can be **infinite**!