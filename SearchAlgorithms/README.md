## ExponentialSearch

- **Pros:**
  - Optimal for unbounded lists.
  - Reduces the number of comparisons compared to linear search.
  - Requires a sorted list, leveraging the sorted nature to quickly narrow down the search range.

- **Cons:**
  - Less efficient than Binary Search for smaller lists due to overhead in finding the appropriate range.
  - Requires random access to elements, which might not be available in all data structures.

- **Class**: Search algorithm
- **Data structure**: Array
- **Worst-case performance**: O(log n)
- **Best-case performance**: O(1)
- **Average performance**: O(log n)
- **Worst-case space complexity**: O(1)
- **Optimal**: Yes

## BinarySearch

- **Pros:**
  - Highly efficient with a time complexity of O(log n).
  - Works with sorted lists, allowing for fast searching.
  - Relatively simple to implement and understand.

- **Cons:**
  - Requires the list to be sorted initially.
  - Not suitable for unsorted lists.
  - No guaranteed improvements over linear search for very small lists.

- **Class**: Search algorithm
- **Data structure**: Array
- **Worst-case performance**: O(log n)
- **Best-case performance**: O(1)
- **Average performance**: O(log n)
- **Worst-case space complexity**: O(1)
- **Optimal**: Yes

## Binary Search Demo

![Binary Search Demo](https://upload.wikimedia.org/wikipedia/commons/8/83/Binary-search-work.gif)
