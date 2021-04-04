# 14 Patterns for Coding Questions

Summarize 14 patterns for coding questions.
Reference: https://mp.weixin.qq.com/s/gUU0m-MrKV3tJl-MiawhpA

## 1. Sliding Window

When to use:
* linear data structure, eg. linked list, array or string
* search for value that made by longest/shortest substring or subarray

Commmon questions:
* 53.[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) (Easy)
* 395.Longest Substring with At Least K Repeating Characters (Medium)
* 567.Permutation in String (Difficult)

Related questions: 3, 30, 76

## 2. Two pointers

When to use:
* Search for a set of elements that satisfy constrains in a sorted array or linked list
* The element sets in array are paired, triad, or subarray

Common questions:
* 977.Squares of a Sorted Array
* 15.3Sum
* 844.Backspace String Compare

## 3. Slow fast pointers

When to use:
* The cyclic problem in linked list or array
* Need to know position of specific element or length or linked list

Common questions:
* 141.Linked List Cycle
* 234.Palindrome Linked List (Easy)
* 457.Circular Array Loop


## 4. Merge Interval

When to use:
* Mutually exclusive intervals
* Overlapping intervals

Common questions:
* 56.Merge Intervals
* 621.Task Scheduler

## 5. Cyclic Sort

When to use:
* Questions related with sorted array in a value range
* Find missing, duplicated, minimum value in sorted/rotated array

Common questions:
* 268.Missing Value
* 41.First Missing Positive
* 287.Find the Duplicate Number
* 442.Find All Duplicates in an Array
* 448.Find All Numbers Disappeared in an Array 
* 645.Set Mismatch 


## 6. Reverse Linked List in Place

When to use:
Reverse linked list without extra memory

Common questions:
* 206.Reverse Linked List
* 25.Reverse Nodes in k-Group


## 7. Tree BFS

When to use:
Traverse a tree by level

Common questions:
* 102.Binary Tree Level Order Traversal  
* 103.Binary Tree Zigzag Level Order Traversal


## 8. Tree DFS

When to use:
* In-order, pre-order, or post-order tree traversal
* Search node close to leaf node

Common questions:
* 62.Unique Paths
* 112.Path Sum  

## 9. Two Heaps

Divide elements into two parts. Use a Min Heap and a Max Heap.


When to use:
* Priority queue, schedule
* Find min/max/middle element in a set
* Some times can be used for binary tree questions


Common questions:
* 295.Find Median from Data Stream



## 10. Subset

When to use:
Combination or permutation questions

Common questions:
* 78.Subsets
* 90.Subsets II
* 784.Letter Case Permutation


## 11. Binary Search

When to use:
Search for a specific element in a sorted array, linked list, or matrix.


Common questions:
* Binary search not related with order
* Search in sorted infinite array

## 12. First K Elements

Use heap to track K elements.

When to use:
* Find first k max, min, most frequently occurred elements


Common questions:
* 215.Kth Largest Element in an Array  

## 13. K-Way Merge

1. Put first element in k sorted arrays into Min-Heap
2. Pop top element in Min-Heap and add it into merged list

When to use:
* Sorted array, list or matrix questions
* Merge sorted lists and find the minimum element in the sorted list


Common questions:
* 23.Merge k Sorted Lists

## 14. Topological Sort

Find the linear order of dependent elements.

When to use:
* undirected cyclic graph
* Update with sorted order
* Elements that follow specific order

Common questions:
* Task scheduling
* 310.Minimum Height Trees


