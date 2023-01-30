# Find K Closest Elements

Problem can be found in [here](https://leetcode.com/problems/find-k-closest-elements/)!

### [Solution](/Binary%20Search/658-FindKClosestElements/solution.py): Binary Search

```python
def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    if len(arr) == k:
        return arr

    left, right = 0, len(arr)-k
    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid+k] - x:
            left = mid + 1
        else:
            right = mid

    return arr[left:left+k]
```

Time Complexity: ![O(log(n-k)+k)](<https://latex.codecogs.com/svg.image?\inline&space;O(log(n-k)+k)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>), where n is the length of array arr and k is the value of input k.
