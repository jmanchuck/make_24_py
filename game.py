class Game:

    @staticmethod
    def get_pair_and_remaining(numbers):
        n = len(numbers)
        for i in range(n-1):
            for j in range(i + 1, n):
                copy = list(numbers)
                x = numbers[i]
                y = numbers[j]
                copy.remove(x)
                copy.remove(y)
                yield x, y, copy

    @staticmethod
    def all_operations(x, y):
        if x > y:
            yield x - y
        elif x < y:
            yield y - x
        if y % x == 0:
            yield y // x
        if x % y == 0:
            yield x // y
        yield x * y
        yield x + y
