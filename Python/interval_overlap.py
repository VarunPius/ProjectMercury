
def process_intervals(intervals):
    up_interval = []
    down_interval = []

    for interval in intervals:
        if interval[2] == "up":
            up_interval.append(interval)
        else:
            down_interval = interval
    
    print("Up Interval: ", up_interval)
    print("Down Interval: ", down_interval)

    results = []
    for up_i in up_interval:
        print("**", up_i)
        if up_i[0] >= down_interval[0] and up_i[1] <= down_interval[1]:
            continue
        elif up_i[0] < down_interval[0] and up_i[1] <= down_interval[1]:
            interval = [up_i[0], down_interval[0], "up"]
            results.append(interval)
        elif up_i[0] >= down_interval[0] and up_i[1] > down_interval[1]:
            interval = [down_interval[1], up_i[1], "up"]
            results.append(interval)
        elif up_i[0] < down_interval[0] and up_i[1] > down_interval[1]:
            print("inside", up_i)
            start, end = up_i[0], up_i[1]
            #up_interval.remove(up_i)
            up_low = [start, down_interval[0], "up"]
            up_high = [down_interval[1], end, "up"]

            results.append(up_low)
            results.append(up_high)


    print("Post:")
    print("Up Interval: ", results)
    print("Down Interval: ", down_interval)

    return

def main():
    overlap_interval = [3, 6, "down"]
    intervals = []
    intervals.append([0, 4, "up"])
    intervals.append([5, 9, "up"])
    intervals.append([4, 5, "up"])
    intervals.append([2, 7, "up"])
    intervals.append(overlap_interval)

    print("Initial intervals: ", intervals)

    process_intervals(intervals)

main()

"""
Initial intervals: [[0, 4, 'up'], [5, 9, 'up'], [4, 5, 'up'], [2, 7, 'up'], [3, 6, 'down']]

Up Interval:  [[0, 4, 'up'], [5, 9, 'up'], [4, 5, 'up'], [2, 7, 'up']]
Down Interval:  [3, 6, 'down']
** [0, 4, 'up']
** [5, 9, 'up']
** [4, 5, 'up']
** [2, 7, 'up']
inside [2, 7, 'up']
Post:
Up Interval:  [[0, 3, 'up'], [6, 9, 'up'], [2, 3, 'up'], [6, 7, 'up']]
Down Interval:  [3, 6, 'down']
"""