class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        if(len(position)==1):
            return 1
        
        # sort, so that the ones closer to target are first
        # zip(list1, list2) makes you consider both lists at once
        # so x = a tuple (position, speed); so x[0] is a position value
        cars = sorted(zip(position, speed), key=lambda x:x[0], reverse=True)

        # [(10, 2), (8, 4), (5, 1), (3, 3), (0, 1)]


        num_fleets = 0
        max_time = 0

        for pos, spd in cars:

            time_taken = (target - pos)/ spd

            if(time_taken > max_time):
                num_fleets += 1
                max_time = time_taken
        
        return num_fleets