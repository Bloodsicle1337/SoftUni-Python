from collections.abc import Generator


def get_primes(numbers: list[int]) -> Generator[int, None, None]:
    for number in numbers:
        if number < 2:
            continue

        is_prime = True

        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break

        if is_prime:
            yield number