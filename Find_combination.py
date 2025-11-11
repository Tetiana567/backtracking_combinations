def find_combinations(candidates, target):
    result = []
    def backtrack(path, total, start):
        if total ==target:
            result.append(path[:])
            return
        if total> target:
            return
        for i in range (start,
                        len(candidates)):
            path.append(candidates[i])
            backtrack(path,
                      total + candidates[i], i + 1)
            path.pop()
    backtrack([],0, 0)
    return result
print(find_combinations([2,3,4,5,6], 7))

