# Search Suggestions System

Problem can be found in [here](https://leetcode.com/problems/search-suggestions-system/)!

### [Solution](/String/1268-SearchSuggestionsSystem/solution.py): Sort + Binary Search

```python
def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:
    products.sort()
    result, prefix, i = [], '', 0

    for char in searchWord:
        prefix += char
        i = bisect_left(products, prefix, i)
        result.append([w for w in products[i:i + 3] if w.startswith(prefix)])

    return result
```

Time Complexity: ![O(nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogn)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)
