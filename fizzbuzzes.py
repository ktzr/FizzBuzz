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
    and can convince ourselves saying "we are only checking each modulo once".
    The double companions is hiding here `output == "" `
    The beauty of FizzBuzz is its always hiding somewhere.
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


def lets_add_parameters(fizz_number, buzz_number, length):
    """ Hey kevin, what if we need to print fizz when a number is divisible by 7, not 3‽ (It's an interrobang ! + ? = ‽)
    Easy fix, we take our best implementation (so far), and parametrise it!

    Calling lets_add_parameters(3,5,100) would have the same effect as the above examples.

    Note - if you pass a negative length there will be no output,
           you can make range count backwards, by setting step=-1 (the 3rd argument)
    """
    for i in range(1, length + 1):
        output = ""
        if i % fizz_number == 0:
            output += "Fizz"
        if i % buzz_number == 0:
            output += "Buzz"
        if output == "":
            output += i
        print(output)

