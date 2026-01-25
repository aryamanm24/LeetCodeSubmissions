class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # list comprehension
        pairs = [[p, s] for p, s in zip(position, speed)]

        # now we'll have a list of list like:
        # [[10, 2], [8, 4], [0, 1], [5, 1], [3, 3]]
        
        # Now, we sort pairs in terms of its positions (index 0 for each list)

        stack = []
        for p, s in sorted(pairs)[::-1]: # going in reverse order

            stack.append((target-p)/s)

            # check if the car that comes now is faster compared to the any of the car fleets in the stack
            # collision happens
            if(len(stack) >= 2 and stack[-1] <= stack[-2]):
                stack.pop()

        return len(stack)