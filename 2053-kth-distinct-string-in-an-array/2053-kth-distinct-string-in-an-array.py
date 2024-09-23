class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        distinct_str = []
        for c in arr:
            if count[c] == 1:
                distinct_str.append(c)
        return distinct_str[k-1] if k <= len(distinct_str) else ""
