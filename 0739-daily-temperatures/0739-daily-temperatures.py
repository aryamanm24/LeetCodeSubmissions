class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        answer = [0] * len(temperatures)

        stack = [] # monotonic stack -> store indices

        for index, temp in enumerate(temperatures):

            while(stack and temp>temperatures[stack[-1]]):
                answer[stack[-1]] = index - stack[-1]
                stack.pop()

            stack.append(index)
        
        return answer