class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int_digit_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        
        curr = 0
        prev_digit=0
        for i in range(len(s) - 1, -1, -1):
            curr_digit = roman_int_digit_map[s[i]]
            
            if curr_digit>=curr or curr_digit==prev_digit:
                curr += curr_digit
            else:
                curr = curr - curr_digit
            
            prev_digit = curr_digit
        return curr