

def merge_intervals(intervals: list) -> list:
    intervals.sort(key=lambda x: x[0])
    result = []
    current_start, current_end = intervals[0]

    for start, end in intervals[1:]:
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            result.append((current_start, current_end))
            current_start = start
            current_end = end

    result.append((current_start, current_end))

    return result


print(merge_intervals(intervals=[(1, 3), (2, 6), (8, 10)]))
