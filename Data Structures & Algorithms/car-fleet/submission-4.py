class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        time = []

        cars = list(zip(position,speed))
        s_cars = sorted(cars, key=lambda car_pair: car_pair[0], reverse = True)

        for position, speed in s_cars:
            time.append((target - position) / speed)

        fleets = []

        for i in time:
            if len(fleets) == 0:
                fleets.append(i)
            elif i <= fleets[-1]:
                fleets.append(i)
        
        return len(fleets)

                
        

        

