def double(number):
    if isinstance(number, int):
        return number * 2
    elif isinstance(number, float):
        return number * 2


if __name__ == "__main__":
    print(double(5))
