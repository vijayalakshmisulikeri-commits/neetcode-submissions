class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        
        
        most_common = freq_map.most_common(k)
        
        
        return [num for num, count in most_common]
        