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
### (Week 1: Scaling Cycle)

| Day | Category   | Problem | Python | Java | C++ |
|-----|------------|---------|--------|------|-----|
| 1   | Arrays     | [Two Sum](https://leetcode.com/problems/two-sum/) | ✅ |  |  |
| 2   | Strings    | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) |  |  |  |
| 3   | Strings    | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) |  |  |  |
| 4   | Strings    | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | |  |  |
| 5   | Arrays     | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) |  |  |  |
| 6   | Arrays     | [Binary Search](https://leetcode.com/problems/binary-search/) |  |  |  |
| 7   | Trees      | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) |  |  |  |

✅ = solved in that language  
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
