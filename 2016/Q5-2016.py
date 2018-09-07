import timeit

start = timeit.default_timer()


def getvalues(filename):
    try:
        file = open(filename, 'r')
    except IOError:
        print('Problem with file ', filename)
    qtype = file.readline()
    size = int(file.readline())
    dmojistan = list(map(int, file.readline().split()))
    pegland = list(map(int, file.readline().split()))
    if qtype.strip() == "1":
        minspeedfinder( size, dmojistan, pegland)
    else:
        maxspeedfinder(size, dmojistan, pegland)


def minspeedfinder(size, dmojistan, pegland):
    dmojistan.sort()
    pegland.sort()
    min = 0
    for x in range(size):
        if dmojistan[x] >= pegland[x]:
            min += dmojistan[x]
        else:
            min += pegland[x]
    print(min)


def maxspeedfinder(size, dmojistan, pegland):
    dmojistan.sort(reverse=True)
    pegland.sort(reverse=True)
    max = 0
    dcounter = 0
    pcounter = 0
    for x in range(size):
        if dmojistan[dcounter] > pegland[pcounter]:
            max += dmojistan[dcounter]
            dcounter += 1
        else:
            max += pegland[pcounter]
            pcounter += 1
    print(max)


getvalues("C:\\Users\\rbhandar\\PycharmProjects\\CCC\\2016\\input.txt")
stop = timeit.default_timer()
print('Time: ', stop - start)
