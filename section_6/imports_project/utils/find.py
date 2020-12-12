def find_in(iterable, finder, expected):
    for i in iterable:
        if finder(i) == expected:
            return i
    raise NotFoundError(f'{expected} not found in iterable')


class NotFoundError(Exception):
    pass


if __name__ == '__main__':
    x = find_in(['Rolf', 'Jose', 'Jan'], lambda x: x, 'Rolf')
    print(x)
