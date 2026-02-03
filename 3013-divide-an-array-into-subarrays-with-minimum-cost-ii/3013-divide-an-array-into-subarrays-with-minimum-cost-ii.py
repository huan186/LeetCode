class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        import heapq

        n = len(nums)
        used = [False for i in range(n)]
        k_heap = [] #Max heap, (-nums[i], i)
        unused_dist_heap = [] #Min heap, (nums[i], i)

        ans = 0
        for i in range(1, k):
            ans += nums[i]
            used[i] = True
            heapq.heappush(k_heap, (-nums[i], i) )

        cur = ans
        for i in range(k, n):
            while k_heap and k_heap[0][1] < i - dist: 
                heapq.heappop( k_heap )
            
            while unused_dist_heap and unused_dist_heap[0][1] < i - dist: 
                heapq.heappop( unused_dist_heap )

            if i - dist - 1 >= 1 and used[i - dist - 1]:
                cur -= nums[i - dist - 1]
                used[i - dist - 1] = False

                if not unused_dist_heap or unused_dist_heap[0][0] > nums[i]:     
                    used[i] = True
                    cur += nums[i]
                    heapq.heappush( k_heap, (-nums[i], i) )
                
                else:
                    _, idx = heapq.heappop( unused_dist_heap )
                    used[idx] = True
                    cur += nums[idx]
                    heapq.heappush( k_heap, ( -nums[idx], idx) )
                    heapq.heappush( unused_dist_heap, (nums[i], i) )
                
            else: 
                if k_heap[0][0] * -1 > nums[i]: 
                    _, idx = heapq.heappop( k_heap )
                    
                    cur -= nums[idx]
                    cur += nums[i]
                    used[idx] = False
                    used[i] = True

                    heapq.heappush(k_heap, (-nums[i], i) )
                    heapq.heappush( unused_dist_heap, (nums[idx], idx) )
                
                else:
                    heapq.heappush( unused_dist_heap, (nums[i], i) ) 

            ans = min(ans, cur)
        
        return ans + nums[0]