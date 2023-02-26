## List Slices


make some difficult multiple choice questions to test one's knowledge of Python list slices 

1. Given the list lst = [1, 2, 3, 4, 5], what is the output of lst[1:3] + lst[0:2]?

a) [2, 3, 1, 2]

b) [2, 3, 1, 2, 3]

c) [2, 3, 4, 1, 2]

d) [2, 3, 4, 5, 1, 2]

2. What is the output of list(range(10))[::2][1:3]?

a) [0, 2]

b) [1, 3]

c) [2, 4]

d) [3, 5]

3. Given the list lst = [1, 2, 3, 4, 5], what is the output of lst[-3:-1] + lst[1:3]?

a) [2, 3, 4, 2, 3]

b) [2, 3, 4, 3, 4]

c) [3, 4, 2, 3]

d) [3, 4, 3, 4]

4. What is the output of list(range(1, 10))[2:7:2]?

a) [3, 5, 7]

b) [3, 6, 9]

c) [2, 4, 6, 8]

d) [2, 5, 8]

5. Given the list lst = [1, 2, 3, 4, 5], what is the output of lst[1:4][::2]?

a) [1, 3]

b) [2, 4]

c) [2]

d) [3]

6. What is the output of list(range(5))[::-1]?

a) [5, 4, 3, 2, 1]

b) [4, 3, 2, 1, 0]

c) [0, 1, 2, 3, 4]

d) [1, 0]

7. Given the list lst = [1, 2, 3, 4, 5], what is the output of lst[2:] + lst[:2]?

a) [1, 2, 3, 4, 5]

b) [3, 4, 5, 1, 2]

c) [1, 2, 3, 4]

d) [3, 4, 5, 2, 1]

8. What is the output of list(range(5))[2::-1]?

a) [2, 1, 0]

b) [3, 2, 1, 0]

c) [2, 1]

d) [0, 1, 2]

9. Given the list lst = [1, 2, 3, 4, 5], what is the output of lst[-3::-1]?

a) [3, 2, 1]

b) [3, 2, 1, 5, 4]

c) [3, 2, 1, 4]

d) [2, 1]

10. What is the output of `list(range(3, 11))[::3][-1]

a) 6

b) 7

c) 8

d) 9

11. Given the list lst = [1, 2, 3, 4, 5], what is the output of lst[::-1][::2]?

a) [5, 3, 1]

b) [5, 4, 3]

c) [4, 2]

d) [4, 2, 1]

12. What is the output of list(range(5))[::2][::-1]?

a) [4, 2, 0]

b) [2, 4]

c) [3, 1]

d) [1, 3, 4]

13. Given the list lst = [1, 2, 3, 4, 5], what is the output of lst[3:1:-1]?

a) [4, 3]

b) [4, 2]

c) [3, 2]

d) [2, 3]

14. What is the output of list(range(10))[::-1][::3]?

a) [9, 6, 3, 0]

b) [9, 7, 5, 3, 1]

c) [8, 5, 2]

d) [8, 5, 2, 0]

15. Given the list lst = [1, 2, 3, 4, 5], what is the output of lst[2:4][::-1]?

a) [3, 2]

b) [4, 3]

c) [4, 2]

d) [3, 4]

16. What is the output of list(range(10))[2:6][::2][::-1]?

a) [5, 3]

b) [5, 7]

c) [7, 5]

d) [3, 5]

17. Given the list lst = [1, 2, 3, 4, 5], what is the output of lst[-2:][::-1] + lst[:-2]?

a) [4, 5, 1, 2, 3]

b) [5, 4, 3, 1, 2]

c) [4, 5, 3, 2, 1]

d) [5, 4, 3, 2, 1]

18. What is the output of list(range(4))[::-1][::2]?

a) [3, 1]

b) [2, 0]

c) [2]

d) [1, 3]

19. Given the list lst = [1, 2, 3, 4, 5], what is the output of lst[2:][::-1][::2]?

a) [5, 3]

b) [4, 2]

c) [5, 2]

d) [3, 1]

20. What is the output of list(range(5))[::2][::-1][::2]?

a) [4]

b) [2, 0]

c) [3, 1]

d) [4, 2]

Here are the answers to the multiple choice questions:

1. b, 2. c, 3. c, 4. a, 5. b, 6. b 

### the :: notation and start:stop:step

In Python, the :: notation is used in list slices to indicate the step or stride size of the slice. The notation is used as follows:

start:stop:step

Where start is the index at which the slice starts. If not specified, it defaults to 0.
stop is the index at which the slice stops. If not specified, it defaults to the length of the list.
step is the number of indices to skip between each item in the slice. If not specified, it defaults to 1.

So, the :: notation is used to specify the step or stride size of the slice. For example, my_list[::2] would create a new list containing every second element of my_list, starting from the first element.

In general, the syntax for slicing a list in Python is:

```python
new_list = my_list[start:stop:step]
```
Note that all three components start, stop, and step can be omitted, in which case the default values are used.

### Up to but not including 

Potential tricky point: Remember the last number means, "up to but not including." 

So, the expression [1:3] refers to a slice of a list that includes all elements starting at index 1 and up to (but not including) index 3. In other words, it creates a new list that contains the elements at index 1 and index 2 of the original list. The original list is not modified.






