class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []

        def apply(x,y,op):
            if op == "+":
                return x+y
            if op == "-":
                return x-y
            if op == "*":
                return x*y
            else:

                return int(x/y)
        
        for token in tokens:
            if token in ['*','+',"/","-"]:
                b,a = operands.pop(), operands.pop()
                res = apply(a, b, token)
                print(a,token,b,"=", res)
                operands.append(res)
            else:
                operands.append(int(token))
        
        return operands[0]