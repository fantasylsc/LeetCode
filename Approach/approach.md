# Approach Classification

## 1. Data Structures

### List

### Sets


### Linked List

| Delete node | Have a cycle | Reverse a linked list | Kth to last node | Go in a cycle, find length of cycle, find first node in a cylce |

### Hash Tables


### Tree



## 2. Sorting Algorithms

| Sorting Algorithm  | Average | Best | Worst | Complexity | Note |
|-------------------| ------- | ---- | ----- |----------- |----- |
|[Bubble Sort](./Classification/Bubble_Sort.py)| Θ(n^2) | Ω(n) | O(n^2) | O(1) |[Optimized Version](./Classification/Bubble_Sort_optimized.py)|
|[Selection Sort](./Classification/Selection_Sort.py)| Θ(n^2) | Ω(n^2) | O(n^2) | O(1) | |
|[Insertion Sort](./Classification/Insertion_sort.py)| Θ(n^2) | Ω(n) | O(n^2) | O(1) | |
|[Merge Sort](./Classification/Merge_Sort.py)| Θ(nlogn) | Ω(nlogn) | O(nlogn) | O(n) | |
|[Heap Sort](./Classification/Heap_Sort.py)| Θ(nlogn) | Ω(nlogn) | O(nlogn) | O(1) |[Build Max Heap](https://www.geeksforgeeks.org/building-heap-from-array/)|
|[Quick Sort](./Classification/Quick_Sort.py)| Θ(nlogn) | Ω(nlogn) | O(n^2) | O(nlogn)| |
|[Radix Sort](./Classification/Radix_Sort.py)| Θ(nk) | Ω(nk) | O(nk) | O(n+k) |k is the maximum number of digits [Visualization](https://www.cs.usfca.edu/~galles/visualization/RadixSort.html)|
|[Counting Sort](./Classification/Counting_Sort.py)| Θ(n+k) | Ω(n+k) | O(n+k) | O(k) |k is the range of input|
|[Bucket Sort](./Classification/Bucket_Sort.py)| Θ(n+k) | Ω(n+k) | O(n^2) | O(n) |k is the number of buckets|
   

## 3. Binary Search and Sorted Array

|[Binary Search](./Classification/Binary_Search.py) | [Binary Search (NineChapter)](./Classification/Binary_Search_NineChapter.py) |

Binary Search: | search for a target, search for the first target, search for the last target, search for a range, search for [Insert position](Approach/Classification/Binary_Search_Insert_Position.py) | [Search in rotated sorted array](./Algorithm/Python/50/0033_Search_in_Rotated_Sorted_Array.py) | [Search in rotaed sorted array II](./Algorithm/Python/100/0081_Search_in_Rotated_Sorted_Array_II.py) | [Search a 2D matrix](./Algorithm/Python/75/0074_Search_a_2D_Matrix.py) | [Median of two sorted arrays](./Algorithm/Python/25/0004_Median_of_Two_Sorted_Arrays.py) | [Rotated sorted array](https://leetcode.com/problems/rotate-array/) (Three steps rotations)

## 4. Binary Tree, Divide Conquer, DFS, and BFS

Binary Tree: [DFS](https://www.geeksforgeeks.org/dfs-traversal-of-a-tree-using-recursion/), [BFS (Level Order Tree Traversal)](https://www.geeksforgeeks.org/level-order-tree-traversal/), [DFS vs BFS](https://www.geeksforgeeks.org/bfs-vs-dfs-binary-tree/)

## 5. Recursion and Dynamic Programming

### Recursion

Example: [Calculate Fibonacci Number](https://leetcode.com/problems/fibonacci-number/): [Approach Compare](https://github.com/fantasylsc/LeetCode/blob/master/Algorithm/Python/525/0509_Fib_Number.py) (1. Recusion without memoization, 2. Recursion with memoization, 3. Bottom up Dynamic Programming)

[322. Coin Change](https://leetcode.com/problems/coin-change/)

[17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | [39. Combination Sum]() | [46. Permutations]() | [47. Permutations II]() | [77. Combinatinos]() | [90. Subsets II]() | [113. Path Sum II]() |

### Dynamic Programming

Dynamic Programming properties: [Overlapping Subproblems Property](https://www.geeksforgeeks.org/overlapping-subproblems-property-in-dynamic-programming-dp-1/) and [Optimal Substructure Property](https://www.geeksforgeeks.org/optimal-substructure-property-in-dynamic-programming-dp-2/).

[Dynamic Progrmming Problem Archives](https://www.geeksforgeeks.org/category/dynamic-programming/)

Coin Change, Coin Change 2 (Review)

Typical Dynamic Programming Problems: [Traveling Salesman Problem](https://www.geeksforgeeks.org/travelling-salesman-problem-set-1/) ([Video](https://www.youtube.com/watch?v=Q4zHb-Swzro), [Image](./Materials/TSP.md))

## Class Design

### LRU Cache

### LFU Cache

### Max Stack













