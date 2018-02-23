def naive_aproach_0():
    """ Please if you ever get asked to write FizzBuzz, DON'T do this!
    Yes it works, no you wont the the job. """
    print("1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz\nFizz\n22\n"
          "23\nFizz\nBuzz\n26\nFizz\n28\n29\nFizzBuzz\n31\n32\nFizz\n34\nBuzz\nFizz\n37\n38\nFizz\nBuzz\n41\nFizz\n43\n"
          "44\nFizzBuzz\n46\n47\nFizz\n49\nBuzz\nFizz\n52\n53\nFizz\nBuzz\n56\nFizz\n58\n59\nFizzBuzz\n61\n62\nFizz\n"
          "64\nBuzz\nFizz\n67\n68\nFizz\nBuzz\n71\nFizz\n73\n74\nFizzBuzz\n76\n77\nFizz\n79\nBuzz\nFizz\n82\n83\nFizz\n"
          "Buzz\n86\nFizz\n88\n89\nFizzBuzz\n91\n92\nFizz\n94\nBuzz\nFizz\n97\n98\nFizz\nBuzz")


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


def lets_add_parameters(length, fizz_number, buzz_number):
    """ Hey Kevin, what if we need to print fizz when a number is divisible by 7, not 3‽ (It's an interrobang ! + ? = ‽)
    Easy fix, we take our best implementation (so far), and parametrise it!

    Calling lets_add_parameters(100, 3, 5) would have the same effect as the above examples.

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


def what_if_we_want_more_triggers(length, numbers, words):
    """ Hey Kevin, turns out fizz needs to print on 3, it's Bazz that needs to print on 7.
    Now we can add Bazz very easily, take in a extra parameter `bazz_number` and add this after the Buzz check
    ```
    if i % bazz_number == 0:
        output += "Bazz"
    ```
    But this isn't going to work if we keep needing to add new numbers,

    Calling what_if_we_want_more_triggers(100, [3, 5], ['Fizz', 'Buzz']) would have the same effect as the above.

    """
    for i in range(1, length + 1):
        output = ""
        for number, word in zip(numbers, words):
            if i % number == 0:
                output += word
        if output == "":
            output += i
        print(output)
