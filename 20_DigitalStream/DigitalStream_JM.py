import random,time,shutil

MAX_STREAM = 14
MIN_STREAM = 6

STREAM_CHARS = ['0', '1']
DENSITY = 0.02

WIDTH = shutil.get_terminal_size()[0]
WIDTH -= 1

columns = [0] * WIDTH
while True:

    for i in range(WIDTH):
        if columns[i] == 0:
            if random.random() < DENSITY:
                columns[i] = random.randint(MIN_STREAM,MAX_STREAM)

        if columns[i] > 0:
            print(random.choice(STREAM_CHARS), end='')
            columns[i] -= 1
        else:
            print(' ', end='')
    print()
    time.sleep(0.1)

