def find_combinations_iter(candidates, target):
    result = []
    stack = [([], 0, 0)]  # (aktuelle Kombination, Summe, Startindex)

    while stack:
        path, total, start = stack.pop()
        if total == target:
            result.append(path)
            continue
        if total > target:
            continue

        for i in range(start, len(candidates)):
            new_path = path + [candidates[i]]
            new_total = total + candidates[i]
            stack.append((new_path, new_total, i + 1))
    return result


print(find_combinations_iter([2, 3, 4, 5, 6], 7))

