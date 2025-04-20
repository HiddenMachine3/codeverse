from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        orig_heights = height.copy()
        rep = [i for i in range(len(height))]

        def display():
            nonlocal orig_heights, height, rep
            new_height_sum = 0
            diff_sum = 0
            i = 0

            while i < len(height):

                # print(("#"*(height[rep[i]])+"\n")*(rep[i] - i + 1),end="")
                new_height = height[rep[i]]
                for j in range(i, rep[i] + 1):
                    curr_height = orig_heights[j]
                    diff = new_height - curr_height
                    print(
                        "#" * orig_heights[j]
                        + (
                            "\033[38;2;0;0;255m" + "#" * diff + "\033[0m"
                            if diff
                            else ""
                        )
                        + f"\t\t{j}\t{rep[i]}"
                    )
                    diff_sum += diff

                new_height_sum += height[rep[i]] * (rep[i] - i + 1)
                i = rep[i] + 1

            return diff_sum

        def water_sum():
            nonlocal orig_heights, height, rep
            new_height_sum = 0
            diff_sum = 0
            i = 0

            while i < len(height):
                new_height = height[rep[i]]
                for j in range(i, rep[i] + 1):
                    curr_height = orig_heights[j]
                    diff = new_height - curr_height
                    diff_sum += diff

                new_height_sum += height[rep[i]] * (rep[i] - i + 1)
                i = rep[i] + 1

            return diff_sum

        # print("initially")
        # display()

        tot_water = 0
        tallest_index = 0
        smallest_index = 0

        for i in range(len(height)):
            # if i >= len(height) - 2:
            #     print(
            #         "\n"
            #         + str(i)
            #         + f"\ttallest idx : {tallest_index} ({height[rep[tallest_index]]})"
            #     )
            #     display()

            if height[i] > height[rep[smallest_index]]:
                l_height = min(height[rep[tallest_index]], height[i])
                # print(f"l_height : {l_height}")
                j = tallest_index
                while j < i:
                    if height[rep[j]] < l_height:
                        # if height[rep[j]] < l_height:
                        # tot_water += (l_height - height[rep[j]]) * (rep[j] - j + 1)
                        height[rep[j]] = l_height
                        height[j] = l_height

                        # print(f"i:{i} j:{j} l_height:{l_height}")
                        # display()

                        orig_j = j
                        j = rep[j] + 1
                        # speed up
                        if height[rep[tallest_index]] >= height[i]:
                            rep[orig_j] = i
                            j = rep[orig_j] + 1
                    else:
                        j = rep[j] + 1

            if height[i] > height[rep[tallest_index]]:
                tallest_index = i
                smallest_index = i
            elif height[i] < height[smallest_index]:
                smallest_index = i

            # if i >= len(height) - 2:
            #     print(
            #         "\n"
            #         + str(i)
            #         + f"\ttallest idx : {tallest_index} ({height[rep[tallest_index]]})"
            #     )
            #     display()

        print("\nfinal")
        tot_water = water_sum()

        # print(display())

        return tot_water


# print(Solution().trap(height=[4, 2, 0, 3, 2, 5]))  # 9 # [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
# print(Solution().trap(height=[0, 4, 7, 0, 0, 4, 5, 6, 7, 4, 7]))  # 23
# print(Solution().trap(height=[5,4,2,5,7,8,6,2,9,1,6,9,1,0,3,7,7,7,3,4,7])) # 47
