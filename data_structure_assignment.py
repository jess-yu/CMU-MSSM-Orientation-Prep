def lifeguards(infile_name):
    # Each event is a 2-element tuple
    # (time, lifeguard id)
    events = []

    # read file
    with open(infile_name) as f:
        lines = [line.rstrip() for line in f]

    n = int(lines[0])
    for i, line in enumerate(lines[1:]):
        start, end = line.split(" ")
        start = int(start)
        end = int(end)
        # create start and end events
        events.append((start, i))
        events.append((end, i))
    # sort events by time
    events.sort(key=lambda x: x[0])

    # keep track of current lifeguards
    cur_set = set()

    # record each lifeguard's alone time
    alone_time = [0] * n
    total_time = 0
    prev_time = 0
    for e in events:
        if len(cur_set) > 0:
            # update additional covered time
            total_time += (e[0] - prev_time)
        if len(cur_set) == 1:
            # this interval is alone
            only_lifeguard_id = next(iter(cur_set)) 
            alone_time[only_lifeguard_id] += (e[0] - prev_time)
        # update current lifeguard set
        if e[1] in cur_set:
            cur_set.remove(e[1])
        else:
            cur_set.add(e[1])
        # update prev time
        prev_time = e[0]

    # find minimum alone time
    min_alone_time = min(alone_time)
    return total_time - min_alone_time


if __name__ == '__main__':
    for i in range(1, 11):
        answer = lifeguards(f"{i}.in")
        print(answer)

        with open(f"{i}.out", mode="w") as outf:
            outf.write(str(answer))
