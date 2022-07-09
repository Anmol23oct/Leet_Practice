class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort(reverse=True)
        ans = last = 0
        for bus in buses:
            left, stack = capacity, [last]
            while left and passengers and passengers[-1] <= bus:
                left -= 1
                stack.append(passengers.pop())
                last = stack[-1]
                if stack[-1] > stack[-2] + 1:
                    ans = stack[-1] - 1
            if left and stack[-1] < bus:
                ans = bus
        return ans