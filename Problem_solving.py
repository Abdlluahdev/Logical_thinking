# The correct soultion
def is_prime(num):
    #
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def prime_nums():
    for i in range(1, 101):
        if is_prime(i):
            print(i)
prime_nums()