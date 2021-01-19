
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


def has_solution(numbers):
    if len(numbers) == 1:
        return numbers[0] == 24

    for x, y, remaining in get_pair_and_remaining(numbers):
        for z in all_operations(x, y):
            remaining.append(z)
            if has_solution(remaining):
                return True
            remaining.pop()

    return False


if __name__ == "__main__":
    numbers = [6, 6, 6, 6]

    print(has_solution(numbers))
