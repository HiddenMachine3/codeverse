from collections import deque


class Solution:

    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)

        if n==k:
            return "0"
        if k==0:
            return str(int(num))

        stack = deque()
        idx = 0

        def top():
            nonlocal stack
            try:
                ele = stack[-1]
                return ele
            except Exception:
                return None

        while idx < n:
            curr = int(num[idx])

            # print(f"idx:{idx} top_ele:{top()} curr:{curr} stack:{stack}")
            while (
                k > 0
                and (len(stack) > 0 and top() > curr)
            ):
                popped = stack.pop()
                # print(f"\tpopped:{popped} stack:{stack}")
                k -= 1
            stack.append(curr)
            # print(f"pushing {curr} to stack, stack:{stack}")
            idx += 1

        while k>0:
            stack.pop()
            k -= 1
        res_list = list(stack)

        idx = 0
        while idx < len(stack) and res_list[idx] == 0:
            idx += 1
        return "".join(map(str, res_list[idx:])) if idx < len(stack) else "0"