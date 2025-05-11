class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, h = 0, len(nums)-1

        if h==0:
            return nums[0]

        while l <= h:

            m = (l+h)//2
            back_repeat = m>0 and nums[m] == nums[m-1]
            forw_repeat = m<len(nums)-1 and nums[m] == nums[m+1]



            alternate = False
            if (h-l)%4!=0:
                alternate = True
                # back_repeat, forw_repeat = forw_repeat, back_repeat
            print(f"l:{l} h:{h} m:{m} nums[m]:{nums[m]} back:{back_repeat} forw:{forw_repeat} alternate:{alternate}")
            if alternate:
                if back_repeat:
                    l = m + 1
                else:
                    if forw_repeat:
                        h = m - 1
                    else:
                        return nums[m]
            else:
                if forw_repeat:
                    l = m
                else:
                    if back_repeat:
                        h = m
                    else:
                        return nums[m]
        # [3,3,7,7,10,11,11]

        return nums[m]