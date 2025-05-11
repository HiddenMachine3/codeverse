class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:

        def partition(arr, s, e):
            i, j = s, e
            pivot = s

            while i < j:
                # print(i, j)
                i += 1
                while arr[i] <= arr[pivot]:
                    i += 1

                j -= 1
                while arr[j] > arr[pivot]:
                    j -= 1

                if i < j:
                    arr[i], arr[j] = arr[j], arr[i]

            arr[pivot], arr[j] = arr[j], arr[pivot]

            return j

        def quick_sort(arr, s, e):
            if s >= e:
                return

            pivot = partition(arr, s, e)
            # print(pivot, arr)
            quick_sort(arr, s, pivot)
            quick_sort(arr, pivot + 1, e)
            # print(pivot, arr)

        nums = nums + [float('inf')]
        quick_sort(nums, 0, len(nums)-1)

        return nums[:-1]