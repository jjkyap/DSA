# 📚 DSA of the Day  

A personal challenge to practice **one Data Structures & Algorithms problem per day** as part of my FAANG prep cycle.  
Problems are organized by **topic** and **language** (Python, Java, C++).  

---

## 📌 Goals
- Build **consistency** (daily coding practice).  
- Cover **core patterns** (arrays, strings, trees, DP, graphs, recursion, etc).  
- Gain **multi-language fluency** (Python first, then Java & C++).  
- Create a **public record** of progress.  

---

## 📂 Repository Structure  

```
dsa-of-the-day/
  README.md
  arrays/
    python/
      two_sum.py
      max_subarray.py
    java/
      TwoSum.java
    cpp/
      two_sum.cpp
  strings/
    python/
      valid_anagram.py
    java/
      ValidAnagram.java
    cpp/
      valid_anagram.cpp
  trees/
    python/
      max_depth.py
    java/
      MaxDepth.java
```

- **Category folders** (arrays, strings, trees, etc).  
- Inside each → **subfolders by language**.  
- Each file includes problem link, explanation, and time/space complexity.  

---

## 🚀 Progress Tracker
<div style="max-height: 400px; overflow-y: auto; border: 1px solid #ddd; padding: 5px;">

### 📚 Week 1 (Concept-Driven Scaling Cycle)

| Day | Category                | Problem                                                                                                                         | Python | Java | C++ |
| --- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------ | ---- | --- |
| 1   | Arrays & Hash Map       | [Two Sum](https://leetcode.com/problems/two-sum/)                                                                               | ✅      |      |     |
| 2   | Two Pointers (Same Dir) | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)                       | ✅     |      |     |
| 3   | Hash Maps               | [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/)                         | ✅      |      |     |
| 4   | Stacks                  | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)                                                           | ✅        |      |     |
| 5   | Two Pointers (Opp Dir)  | [Two Sum II – Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)                           |        |      |     |
| 6   | Sliding Window          | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) |        |      |     |
| 7   | Prefix Sums             | [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)                                         |        |      |     |
     |        |      |     |

✅ = solved in that language  
🔁 = currently working on  

</div>
---

## 📝 Example Solution Format  

**Python (`arrays/python/two_sum.py`):**
```python
"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Language: Python
Approach: Hashmap O(n) time, O(n) space
"""

def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
```

**Java (`arrays/java/TwoSum.java`):**
```java
// Problem: Two Sum
// Link: https://leetcode.com/problems/two-sum/
// Language: Java
// Approach: HashMap O(n) time, O(n) space

import java.util.*;

class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (seen.containsKey(diff)) {
                return new int[] { seen.get(diff), i };
            }
            seen.put(nums[i], i);
        }
        return new int[] {};
    }
}
```

---

## 🏆 Long-Term Vision
- Solve **200+ problems** across categories.  
- Revisit solved problems in **Java & C++** for depth.  
- Use repo as **interview prep portfolio** alongside Myndex project. 
