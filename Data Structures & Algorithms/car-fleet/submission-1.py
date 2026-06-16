class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        time = []

        cars = list(zip(position,speed))
        s_cars = sorted(cars, key=lambda car_pair: car_pair[0], reverse = True)

        for position, speed in s_cars:
            time.append((target - position) / speed)

        i = 0
        j = 1

        while j <= len(time) - 1 :
            if time[j] < time[i]:
                time[i] = time[j]
            
            i += 1
            j += 1
        
        return len(set(time))


                
        

        

