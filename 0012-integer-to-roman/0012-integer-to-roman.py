class Solution:
    def intToRoman(self, num: int) -> str:
        
        # include the normal and the exception cases (subtraction cases basically)
        value_roman_pairs = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

        # after creating the above table, it's a simple coin change question
        result = []

        for value, symbol in value_roman_pairs:
            while(num >= value):
                result.append(symbol)
                num -= value
        
        return "".join(result)

