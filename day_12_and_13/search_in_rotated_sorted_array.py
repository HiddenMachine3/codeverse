class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)-1

        if l == h == 0:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        k = 0
        while l <= h :

            m = (l+h)//2
            
            print(f"l:{l} h:{h} m:{m}")
            if m < len(nums)-1 and nums[m+1]<nums[m]:
                print("1")
                k = m + 1
                break
            elif m == len(nums)-1 and nums[0] < nums[m]:
                print("2")
                k = 0
                break
            elif nums[l]>nums[m]:
                print("3")
                h = m -1
            else:
                print("4")
                l = m + 1
        
        print(f"k:{k}")

        l = 0
        h = len(nums)-1

        while l <= h:
            m = (l+h)//2
            m_r = (m+k)%len(nums)

            if nums[m_r] < target:
                l = m + 1
            elif nums[m_r] > target:
                h = m - 1
            else:
                return m_r
        
        return -1