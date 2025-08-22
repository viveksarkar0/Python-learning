# 🐍 Python Coding Challenges - Interview Practice

## 📋 Table of Contents
1. [String Manipulation](#string-manipulation)
2. [Array/List Problems](#arraylist-problems)
3. [Number Problems](#number-problems)
4. [Data Structure Problems](#data-structure-problems)
5. [Algorithm Problems](#algorithm-problems)

---

## 📝 String Manipulation

### Challenge 1: Reverse Words in a String
**Problem:** Reverse the order of words in a string while keeping the words themselves unchanged.

```python
def reverse_words(s):
    """Reverse words in a string"""
    # Split the string into words
    words = s.split()
    # Reverse the list of words
    words.reverse()
    # Join them back with spaces
    return ' '.join(words)

# Test cases
print(reverse_words("Hello World"))  # "World Hello"
print(reverse_words("Python is awesome"))  # "awesome is Python"
```

### Challenge 2: Check if String is Palindrome
**Problem:** Determine if a string reads the same forwards and backwards.

```python
def is_palindrome(s):
    """Check if string is palindrome"""
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

# Test cases
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))  # False
print(is_palindrome("Was it a car or a cat I saw?"))  # True
```

### Challenge 3: Find First Non-Repeating Character
**Problem:** Find the first character that appears only once in a string.

```python
from collections import Counter

def first_unique_char(s):
    """Find first non-repeating character"""
    # Count frequency of each character
    count = Counter(s)
    
    # Find first character with count 1
    for i, char in enumerate(s):
        if count[char] == 1:
            return char
    
    return -1  # No unique character found

# Test cases
print(first_unique_char("leetcode"))  # 'l'
print(first_unique_char("loveleetcode"))  # 'v'
print(first_unique_char("aabb"))  # -1
```

---

## 📊 Array/List Problems

### Challenge 4: Two Sum
**Problem:** Find two numbers in an array that add up to a target value.

```python
def two_sum(nums, target):
    """Find two numbers that add up to target"""
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
    
    return []  # No solution found

# Test cases
print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
print(two_sum([3, 2, 4], 6))  # [1, 2]
print(two_sum([3, 3], 6))  # [0, 1]
```

### Challenge 5: Remove Duplicates from Sorted Array
**Problem:** Remove duplicates from a sorted array in-place.

```python
def remove_duplicates(nums):
    """Remove duplicates from sorted array in-place"""
    if not nums:
        return 0
    
    # Two-pointer approach
    write_index = 1
    
    for read_index in range(1, len(nums)):
        if nums[read_index] != nums[read_index - 1]:
            nums[write_index] = nums[read_index]
            write_index += 1
    
    return write_index

# Test cases
nums1 = [1, 1, 2]
print(remove_duplicates(nums1))  # 2
print(nums1[:2])  # [1, 2]

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(remove_duplicates(nums2))  # 5
print(nums2[:5])  # [0, 1, 2, 3, 4]
```

### Challenge 6: Maximum Subarray Sum (Kadane's Algorithm)
**Problem:** Find the maximum sum of a contiguous subarray.

```python
def max_subarray_sum(nums):
    """Find maximum subarray sum using Kadane's algorithm"""
    if not nums:
        return 0
    
    max_current = max_global = nums[0]
    
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)
    
    return max_global

# Test cases
print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(max_subarray_sum([1]))  # 1
print(max_subarray_sum([5, 4, -1, 7, 8]))  # 23
```

---

## 🔢 Number Problems

### Challenge 7: Fibonacci Number
**Problem:** Calculate the nth Fibonacci number efficiently.

```python
def fibonacci(n):
    """Calculate nth Fibonacci number"""
    if n <= 1:
        return n
    
    # Dynamic programming approach
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

# Test cases
print(fibonacci(4))  # 3
print(fibonacci(10))  # 55
print(fibonacci(20))  # 6765
```

### Challenge 8: Count Primes
**Problem:** Count the number of prime numbers less than n.

```python
def count_primes(n):
    """Count primes less than n using Sieve of Eratosthenes"""
    if n < 2:
        return 0
    
    # Initialize sieve
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    
    # Sieve of Eratosthenes
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Mark multiples as not prime
            for j in range(i*i, n, i):
                is_prime[j] = False
    
    return sum(is_prime)

# Test cases
print(count_primes(10))  # 4 (2, 3, 5, 7)
print(count_primes(20))  # 8 (2, 3, 5, 7, 11, 13, 17, 19)
```

### Challenge 9: Power of Two
**Problem:** Determine if a number is a power of two.

```python
def is_power_of_two(n):
    """Check if n is a power of two"""
    if n <= 0:
        return False
    
    # A power of 2 has exactly one bit set
    return (n & (n - 1)) == 0

# Test cases
print(is_power_of_two(1))  # True (2^0)
print(is_power_of_two(16))  # True (2^4)
print(is_power_of_two(3))  # False
print(is_power_of_two(0))  # False
```

---

## 🏗️ Data Structure Problems

### Challenge 10: Valid Parentheses
**Problem:** Check if a string of parentheses is valid.

```python
def is_valid_parentheses(s):
    """Check if parentheses string is valid"""
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != brackets[char]:
                return False
    
    return len(stack) == 0

# Test cases
print(is_valid_parentheses("()"))  # True
print(is_valid_parentheses("()[]{}"))  # True
print(is_valid_parentheses("(]"))  # False
print(is_valid_parentheses("([)]"))  # False
```

### Challenge 11: Implement Stack using Lists
**Problem:** Implement a stack data structure using Python lists.

```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to top of stack"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return top item"""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")
    
    def peek(self):
        """Return top item without removing"""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")
    
    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return size of stack"""
        return len(self.items)

# Test the stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # 3
print(stack.peek())  # 2
print(stack.size())  # 2
```

---

## 🧮 Algorithm Problems

### Challenge 12: Binary Search
**Problem:** Implement binary search to find a target in a sorted array.

```python
def binary_search(nums, target):
    """Binary search in sorted array"""
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Target not found

# Test cases
nums = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(nums, 7))  # 3
print(binary_search(nums, 10))  # -1
print(binary_search(nums, 1))  # 0
```

### Challenge 13: Merge Two Sorted Arrays
**Problem:** Merge two sorted arrays into one sorted array.

```python
def merge_sorted_arrays(nums1, nums2):
    """Merge two sorted arrays"""
    result = []
    i = j = 0
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1
    
    # Add remaining elements
    result.extend(nums1[i:])
    result.extend(nums2[j:])
    
    return result

# Test cases
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
print(merge_sorted_arrays(arr1, arr2))  # [1, 2, 3, 4, 5, 6, 7, 8]
```

---

## 🎯 Interview Tips

### Before Starting:
1. **Clarify the problem** - Ask questions about edge cases
2. **Think out loud** - Explain your approach
3. **Start with brute force** - Then optimize
4. **Consider time/space complexity**

### During Implementation:
1. **Write clean, readable code**
2. **Handle edge cases**
3. **Test with examples**
4. **Explain your solution**

### Common Mistakes to Avoid:
1. **Not handling edge cases**
2. **Not considering time complexity**
3. **Not testing with examples**
4. **Not explaining your approach**

---

## 📚 Practice Resources

- **LeetCode**: leetcode.com
- **HackerRank**: hackerrank.com
- **CodeSignal**: codesignal.com
- **InterviewBit**: interviewbit.com

---

**💡 Remember: Practice makes perfect! Start with easy problems and gradually move to harder ones.**
