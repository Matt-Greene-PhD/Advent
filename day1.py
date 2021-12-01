import advent

ad = advent.Advent()

intlist = [int(x) for x in ad.get_input(1).rstrip().split('\n')]

diffs = [intlist[i+1] - intlist[i] for i in range(len(intlist) - 1)]
ad.submit_answer(1, 1, len([x for x in diffs if x > 0]))

diffs = [intlist[i+3] - intlist[i] for i in range(len(intlist) - 3)]
ad.submit_answer(1, 2, len([x for x in diffs if x > 0]))
