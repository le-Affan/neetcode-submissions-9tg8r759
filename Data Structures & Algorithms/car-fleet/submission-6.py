class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dist = [0] * len(position)
        timeNpos = [0] * len(position)

        for i in range(len(dist)):
            dist[i] = target - position[i]
        
        for i in range(len(timeNpos)):
            timeNpos[i] = [dist[i] / speed[i],position[i]]
        
        timeNpos.sort(key = lambda x:x[1], reverse = True)

        stack = []

        for time,pos in timeNpos:
            if not stack or time > stack[-1]:
                stack.append(time)
            # if time is smaller than stack top => car joins the fleet
            # else that greater time car gets added to the stack
        return len(stack)


        

