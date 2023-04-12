def infinite_sequence():
    i = 0

    while True:
        yield i

        i += 1


for i in infinite_sequence():
    print(i)
