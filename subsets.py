def subsets(nums):
    result = []

    def backtrack(index, current):
        result.append(current[:])

        for i in range(index, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result


nums = [1, 2, 3]
print(subsets(nums))
