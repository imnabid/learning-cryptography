def crange(*config):
    if len(config) == 3:
        start, end, step = config
    elif len(config) == 2:
        (start, end), step = config, 1
    else:
        start, end, step = 0, *config, 1
        
    val = start
    while val < end:
        yield val
        val += step

for i in crange(0,11):
    print(i)
        