def merge(intervals):
    enc = ()

    for interval in intervals:
        for c in enc:
            if 







    result = [[start, end] for start, end in enc]
    return result


intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))

intervals = [[1,4],[4,5]]
print(merge(intervals))