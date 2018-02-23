def naive_approach_1():
    """ It's short , it works but it's not pretty, and it's defiantly not DRY"""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def naive_approach_2():
    """ Still not DRY, but a bit better than `naive_approach_1`"""
    for i in range(1, 101):
        if i % 3 == 0:
            print("Fizz", end="")
        if i % 5 == 0:
            print("Buzz", end="")
        if i % 3 != 0 or i % 5 != 0:
            print(i, end="")
        print()  # dont forget to add the newline


def naive_approach_3():
    """ Here we make it DRY, and hide the double comparison,
    and can convince ourselves saying "we are only checking each modulo once"
    the double companions is hiding here `output == "" `
    """
    for i in range(1, 101):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if output == "":
            output += i
        print(output)
