def crange(*config):
    if len(config) == 3:
        start, end, step = config
    elif len(config) == 2:
        (start, end), step = config, 1
    elif len(config) == 1:
        start, end, step = 0, *config, 1
    else:
        raise TypeError('Expected at least 1 argument, got 0')

    val = start
    while val < end:
        yield val
        val += step

for i in crange(0,11):
    print(i)
        