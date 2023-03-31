# Python studies
This project was made in order to understand the main python concepts using selection and searching algorithms.

## Concepts
- List comprehension:
    * Extract a list from another;
    * Elegant syntax;
    * Example:
    ```py
    ordered_list = [1, 2, 3, 4, 5]
    square = [x ** 2 for x in ordered_list] # [1, 4, 9, 16, 25]
    ```
- Lambda:
    * Allow write one liners functions;
    * Compact functions;
    * Example:
    ```py
    ordered_list = [1, 2, 3, 4, 5]
    reversed_list = list(reversed(ordered_list))
    square = lambda n: [x ** 2 for x in n]
    squared_ordered_list = square(ordered_list) # [1, 4, 9, 16, 25]
    squared_reversed_list = square(reversed_list) # [25, 16, 9, 4, 1]
    ```