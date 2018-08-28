# Emulating switch using dictionary of callable

# Way 1

def go_east():
    print('Going east')


def go_west():
    print('Going west')


def go_north():
    print('Going North')


def go_south():
    print('Going South')


def invalid():
    print('Not A valid direction')


mapping = dict(E=go_east,
               S=go_south,
               W=go_west,
               N=go_north)


def myfunc(key):
    try:
        func = mapping[key]
    except:
        print('Not A valid direction')
    else:
        func()  # calling function


# switch case with default condition
import collections

mapping2 = collections.defaultdict(lambda: invalid,  # it will be excute if key not found
                                  E=go_east,
                                  S=go_south,
                                  W=go_west,
                                  N=go_north
                                 )
if __name__ == '__main__':
    print(' basic Exception based switch case Emmulation ')
    myfunc('E')
    myfunc('W')
    myfunc('D')
    print('Using Dict with default case also')
    mapping2['E']()
    mapping2['D']()