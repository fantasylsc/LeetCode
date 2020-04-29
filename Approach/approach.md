# Data Strucutre & Algorithms Classification

## 1. Data Structures

### Linear Data Structure

- Queue: BFS

- Stack:  [Min Stack](../Algorithm/Python/175/0155_Min_Stack.py) | [Max Stack](../Algorithm/Python/725/0716_Max_Stack.py) |[Implement Queue using Stacks](../Algorithm/Python/250/0232_Implement_Queue_using_Stacks.py) | [Implement Stack using Queues](../Algorithm/Python/225/0225_Implement_Stack_using_Queues.py) | [Largest Rectangle in Histogram](../Algorithm/Python/100/0084_Largest_Rectangle_in_Histogram.py) | [Maximum Binary Tree](../Algorithm/Python/675/0654_Maximum_Binary_Tree.py) | [Monotone Stack Summary](https://www.cnblogs.com/grandyang/p/8887985.html) |

- Hash: [LRU Cache](../Algorithm/Python/150/0146_LRU_Cache.py) | [Longest Consecutive Sequence](../Algorithm/Python/150/0128_Longest_Consecutive_Sequence.py) | 

### Tree Data Structure

- Heap: [Find Median from Data Stream](../Algorithm/Python/300/0295_Find_Median_from_Data_Stream.py) | [The Skyline Problem](..//Algorithm/Python/225/0218_The_Skyline_Problem.py) ([Ref](https://zxi.mytechroad.com/blog/tree/leetcode-218-the-skyline-problem/)) | 

- Trie: [Implement Trie (Prefix Tree)]() | [Word Search II]() |




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

|[Binary Search](./Classification/Binary_Search.py) | [Binary Search (NineChapter)](./Classification/Binary_Search_NineChapter.py) | Search Lower Bound | Search Upper Bound |

Binary Search: | search for a target, search for the first target, search for the last target, search for a range | [Search Insert Position](../Algorithm/Python/50/0035_Search_Insert_Position.py) | [Search in rotated sorted array](../Algorithm/Python/50/0033_Search_in_Rotated_Sorted_Array.py) | [Search in rotaed sorted array II](../Algorithm/Python/100/0081_Search_in_Rotated_Sorted_Array_II.py) | [Search a 2D matrix](../Algorithm/Python/75/0074_Search_a_2D_Matrix.py) | [Median of two sorted arrays](../Algorithm/Python/25/0004_Median_of_Two_Sorted_Arrays.py) | [Rotate Array](../Algorithm/Python/175/0189_Rotate_Array.py) |

## 4. Binary Tree, DFS, BFS, and Divide & Conquer

Binary Tree Traversal: traverse order 1-2-3-4-5. 

[Preorder](../Algorithm/Python/150/0144_Binary_Tree_Preorder_Traversal.py) (root, left, right) 

[Postorder](../Algorithm/Python/150/0145_Binary_Tree_Postorder_Traversal.py) (left, right, root) 

[Inorder](../Algorithm/Python/100/0094_Binary_Tree_Inorder_Traversal.py) (left, root, right)

[Level order](../Algorithm/Python/125/0102_Binary_Tree_Level_Order_Traversal.py) (BFS)

<p align="center">
<img width="500"  src=./Materials/DFSBFS.png >
</p>

Binary Tree: [DFS](https://www.geeksforgeeks.org/dfs-traversal-of-a-tree-using-recursion/)(Iterative: using stack), [BFS (Level Order Tree Traversal)](https://www.geeksforgeeks.org/level-order-tree-traversal/)(Iterative: using queue), [DFS vs BFS](https://www.geeksforgeeks.org/bfs-vs-dfs-binary-tree/)

### Divide & Conquer

Merge Sort, Quick Sort, Most of the Binary Tree Problems.

[Maximum Depth of Binary Tree](../Algorithm/Python/125/0104_Maximum_Depth_of_Binary_Tree.py) | [Minimum Depth of Binary Tree](../Algorithm/Python/125/0111_Minimum_Depth_of_Binary_Tree.py) | [Balanced Binary Tree](../Algorithm/Python/125/0110_Balanced_Binary_Tree.py) | [Binary Tree Maximum Path Sum](../Algorithm/Python/125/0124_Binary_Tree_Maximum_Path_Sum.py) | [Lowest Comman Ancestor](../Algorithm/Python/250/0236_Lowest_Common_Ancestor_of_a_Binary_Tree.py) | [Lowest Common Ancestor of a Binary Tree](../Algorithm/Python/250/0235_Lowest_Common_Ancestor_of_a_Binary_Search_Tree.py) | [Binary Tree Order Level Traversal](../Algorithm/Python/125/0102_Binary_Tree_Level_Order_Traversal.py) | [Valid Binary Search Tree](../Algorithm/Python/100/0098_Validate_Binary_Search_Tree.py) | [Insert into a Binary Search Tree](../Algorithm/Python/725/0701_Insert_into_a_Binary_Search_Tree.py) | [Search Range in a Binary Search Tree](./Classification/searchRange_BST.py) | [Binary Search Tree Iterator ](../Algorithm/Python/175/0173_Binary_Search_Tree_Iterator.py) | [Delete Node in a BST](..//Algorithm/Python/450/0450_Delete_Node_in_a_BST.py) | [Largest Rectangle in Histogram](../Algorithm/Python/100/0084_Largest_Rectangle_in_Histogram.py)

[Binary Tree Template (good)](./Classification/Binary%20Tree%20DFS%20Template.py)

## 5. Linked List
| Delete node | Have a cycle | Reverse a linked list | Kth to last node | Go in a cycle, find length of cycle, find first node in a cylce |
[Remove Duplicates from Sorted List](../Algorithm/Python/100/0083_Remove_Duplicates_from_Sorted_List.py) | [Remove Duplicates from Sorted LIst II](../Algorithm/Python/100/0082_Remove_Duplicates_from_Sorted_List_II.py) | [Reverse Linked List](../Algorithm/Python/225/0206_Reverse_Linked_List.py) | [Reverse Linked List II](../Algorithm/Python/100/0092_Reverse_Linked_List_II.py) | [Partition List](../Algorithm/Python/100/0086_Partition_List.py) | [Sort List](../Algorithm/Python/150/0148_Sort_List.py) | [Reorder List](../Algorithm/Python/150/0143_Reorder_List.py) | [Linked List Cycle](../Algorithm/Python/150/0141_Linked_List_Cycle.py) | [Linked List Cycle II](../Algorithm/Python/150/0142_Linked_List_Cycle%20II.py) | [Merge K Sorted Lists](../Algorithm/Python/25/0023_Merge_k_Sorted_Lists.py) | [Copy List with Random Pointer](../Algorithm/Python/150/0138_Copy_List_with_Random_Pointer.py) | [Convert Sorted List to Binary Search Tree](../Algorithm/Python/125/0109_Convert_Sorted_List_to_Binary_Search_Tree.py) | 

Basic Skills:

1. Insert a Node in Sorted List

2. Remove a Node from Linked List

3. Reverse a Linked List

4. Merge Two Linked Lists

5. Find the Middle of a Linked List

## 6. Recursion and Dynamic Programming

### Recursion

Example: [Calculate Fibonacci Number](https://leetcode.com/problems/fibonacci-number/): [Approach Compare](https://github.com/fantasylsc/LeetCode/blob/master/Algorithm/Python/525/0509_Fib_Number.py) (1. Recusion without memoization, 2. Recursion with memoization, 3. Bottom up Dynamic Programming)

Backtracking: [Combinatinos](../Algorithm/Python/100/0077_Combinations.py) | [Letter Combinations of a Phone Number](../Algorithm/Python/25/0017_Letter_Combinations_of_a_Phone_Number.py) | [Generate Parentheses](../Algorithm/Python/25/0022_Generate_Parentheses.py) | [Combination Sum](../Algorithm/Python/50/0039_Combination_Sum.py) | [Permutations](../Algorithm/Python/50/0046_Permutations.py) | [Permutations II](../Algorithm/Python/50/0047_Permutations_II.py) | [Word Search](../Algorithm/Python/100/0079_Word_Search.py) | [Subsets II](../Algorithm/Python/100/0090_Subsets_II.py) | [Path Sum II](../Algorithm/Python/125/0113_Path_Sum_II.py) |

### Dynamic Programming

Dynamic Programming properties: [Overlapping Subproblems Property](https://www.geeksforgeeks.org/overlapping-subproblems-property-in-dynamic-programming-dp-1/) and [Optimal Substructure Property](https://www.geeksforgeeks.org/optimal-substructure-property-in-dynamic-programming-dp-2/).

When to use DP:

1) One of the following three:

      a) Maximum/Minimum

      b) Yes/No

      c) Count all possible solutions

2) Can not sort/Swap (longest consecutive sequence)

Four elements of DP:

1) State, 2) Function, 3) Initialization, 4) Answer.

Four categories of DP:

1) Matrix DP (10%): [Triangle](../Algorithm/Python/125/0120_Triangle.py) | [Unique Path](../Algorithm/Python/75/0062_Unique_Paths.py) | [Unique Path II](../Algorithm/Python/75/0063_Unique_PathsII.py) | [Unique Path III](../Algorithm/Python/1000/0980_Unique_Paths_III.py) | [Minimum Path Sum](../Algorithm/Python/75/0064_Minimum_Path_Sum.py) |  

2) Sequence (40%): [Climbing Stairs](../Algorithm/Python/75/0070_Climbing_Stairs.py) | [Jump Game](../Algorithm/Python/75/0055_Jump_Game.py) | [Jump Game II](../Algorithm/Python/50/0045_Jump_Game_II.py) | [Palindrome Partitioning II](../Algorithm/Python/150/0132_Palindrome_Partitioning_II.py) | [Word Break](../Algorithm/Python/150/0139_Word_Break.py) | [Longest Increasing Subsequence](../Algorithm/Python/300/0300_Longest_Increasing_Subsequence.py) | [Combination Sum IV](../Algorithm/Python/400/0377_Combination_Sum_IV.py) |

3) Two Sequences (40%): [Longest Common Subsequence](../Algorithm/Python/1150/1143_Longest_Common_Subsequence.py) | [Longest Common Substring](./Classification/Longest_Common_Substring.py) | [Edit Distance](../Algorithm/Python/75/0072_Edit_Distance.py) | [Distinct Subsequences](../Algorithm/Python/125/0115_Distinct_Subsequences.py) | [Interleaving String](../Algorithm/Python/100/0097_Interleaving_String.py) |

4) Knapsack (10%): [0-1 Knapsack](./Classification/Backpack.py) | [K Sum](./Classification/kSum.py) | [Minimum Adjustment Cost](./Classification/Minimum_Adjustment_Cost.py) | [Coin Change](../Algorithm/Python/325/0322_Coin_Change.py) |


[Dynamic Progrmming Problem Archives](https://www.geeksforgeeks.org/category/dynamic-programming/)

[Coin Change 2](../Algorithm/Python/525/0518_Coin_Change_2.py)

Typical Dynamic Programming Problems: [Traveling Salesman Problem](https://www.geeksforgeeks.org/travelling-salesman-problem-set-1/) ([Video](https://www.youtube.com/watch?v=Q4zHb-Swzro), [Image](./Materials/TSP.md))

## 7. Graph & Search

Graph: [DFS](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/) and [BFS](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)

Graph: [Clone Graph](../Algorithm/Python/150/0133_Clone_Graph.py) | [Topological Sorting](./Classification/Topological_Sorting.py) 
   
Search (DFS and BFS): [Permutations](../Algorithm/Python/50/0046_Permutations.py) | [Subsets](../Algorithm/Python/100/0078_Subsets.py) | [N Queens](../Algorithm/Python/75/0051_N-Queens.py) | [Subsets II](../Algorithm/Python/100/0090_Subsets_II.py) | [Palindrome Partitioning](../Algorithm/Python/150/0131_Palindrome_Partitioning.py) | [Combination Sum](../Algorithm/Python/50/0039_Combination_Sum.py) | [Combination Sum II](../Algorithm/Python/50/0040_Combination_Sum_II.py) | [Word Ladder](../Algorithm/Python/150/0127_Word_Ladder.py) | [Word Ladder II]() |     

DFS  (O(2^n), O(n!)) (idea: construct search tree + judge feasibility)
   1. Find all possible solutions
   2. Permutations / Subsets

BFS  (O(m), O(n))
   1. Graph traversal (Visit each node once)
   2. Find shortest path in a simple graph 



   

## Class Design

### LRU Cache

### LFU Cache

### Max Stack













