class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        count = 1
        n = len(position)
        if n == 0:
            return 0
        cars = [(position[i], speed[i]) for i in range(n)]
        cars.sort()
        times = []
        for i in range(n):
            time_to_target = (target - cars[i][0]) / cars[i][1]
            times.append(time_to_target)
        cur_t = times[-1]
        for i in range(n):
            if times[n - i - 1] <= cur_t:
                continue
            else:
                cur_t = times[n - i - 1]
                count += 1
        return count