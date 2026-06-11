class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        count = len(temperatures)
        result = [0] * count

        stack = []  # indices

        for index in range(count):
            while stack and temperatures[index] > temperatures[stack[-1]]:
                prev = stack.pop()
                result[prev] = index - prev

            stack.append(index)

        return result