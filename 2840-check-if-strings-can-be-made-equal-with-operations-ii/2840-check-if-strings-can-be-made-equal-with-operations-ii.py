class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        
        # characters at even positions always stay at even positions --(1)
        # characters at odd positions always stay at odd positions --(2)

        # (1): even lane
        # (2): odd lane

        length = len(s1)

        even_lane_1 = sorted(s1[i] for i in range(0, length, 2))
        even_lane_2 = sorted(s2[i] for i in range(0 ,length, 2))

        odd_lane_1 = sorted(s1[i] for i in range(1, length, 2))
        odd_lane_2 = sorted(s2[i] for i in range(1, length, 2))

        return even_lane_1==even_lane_2 and odd_lane_1==odd_lane_2