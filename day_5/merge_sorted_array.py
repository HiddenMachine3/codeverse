class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr = [0]*(m+n)
        i,j,k = 0,0,0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                arr[k] = nums1[i]
                i += 1
            else:
                arr[k] = nums2[j]
                j += 1
            k+=1
        while i < m:
            arr[k] = nums1[i]
            i+=1
            k+=1
        # print(arr, i, j, k)
        
        while j < n:
            arr[k] = nums2[j]
            # print(j, nums2[j], n)
            j += 1
            k += 1
            
        for i in range(len(nums1)):
            nums1[i] = arr[i]
        