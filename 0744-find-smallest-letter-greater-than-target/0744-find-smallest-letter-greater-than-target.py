class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = letters[0]
        low, high = 0, len(letters) - 1
        while low <= high:
            mid = (low + high) // 2
            if letters[mid] > target:
                ans = letters[mid]
                high = mid - 1
            else:
                low = mid + 1
        return ans