# Top K Frequent Elements

Problem can be found in [here](https://leetcode.com/problems/top-k-frequent-elements/)!

### [Solution1](/Hash%20Table/347-TopKFrequentElements/solution1.py): Sorting + Hash Table

```python
def topKFrequent(nums: List[int], k: int) -> List[int]:
    memo = {}
    for num in nums:
        try:
            memo[num] += 1
        except KeyError:
            memo[num] = 1

    top_k_number = sorted(memo.items(), key=lambda x: x[1], reverse=True)[:k]
    return [i[0] for i in top_k_number]
```

Explanation: After counting the number of occurence for each number using a hash table, we can sort it based on its frequency.

Time Complexity: ![O(nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogn)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

### [Solution2](/Hash%20Table/347-TopKFrequentElements/solution2.py): Bucket Sort + Hash Table

```python
def topKFrequent(nums: List[int], k: int) -> List[int]:
    buckets = defaultdict(list)
    for num, count in Counter(nums).items():
        buckets[count].append(num)

    output_list = []
    for i in range(len(nums), -1, -1):
        output_list.extend(buckets[i])
        if len(output_list) == k:
            break

    return output_list
```

Explanation: The small modification is that instead of sorting directly, we can use the property of a hash table (constant look-up time). Since we know there are only $nums.length$ unique elements, we can add elements incrementally until the length of the array equals to $k$.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)
