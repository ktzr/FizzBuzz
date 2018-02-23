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
            output += str(i)
        print(output)


def lets_add_parameters(length, fizz_number, buzz_number):
    """ Hey Kevin, what if we need to print fizz when a number is divisible by 7, not 3‽ (It's an interrobang ! + ? = ‽)
    Easy fix, we take our best implementation (so far), and parametrise it!

    Calling lets_add_parameters(100, 3, 5) would have the same effect as above examples.

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
            output += str(i)
        print(output)


def what_if_we_want_more_triggers(length, numbers, words):
    """ Hey Kevin, turns out fizz needs to print on 3, it's Bazz that needs to print on 7.
    Now we can add Bazz very easily, take in a extra parameter `bazz_number` and add this after the Buzz check
    ```
    if i % bazz_number == 0:
        output += "Bazz"
    ```
    But this isn't going to work if we keep needing to add new numbers,

    Calling what_if_we_want_more_triggers(100, [3, 5], ['Fizz', 'Buzz']) would have the same effect as above.

    """
    for i in range(1, length + 1):
        output = ""
        for number, word in zip(numbers, words):
            if i % number == 0:
                output += word
        if output == "":
            output += str(i)
        print(output)


def numbers_and_words_are_relation_1(length, triggers):
    """ In the last example we need to pass both a numbers and words argument.
    They are related to each other but that relation cant be seen in our code.
    Let's increase the cohesion of our code, and keep the number and words together.

    Now we can create a Class with two fields, but this is python! Lets use a dictionary.
    You may jump to a list of dicts e.g. [{'number':3,'word':'Fizz'},{'number':5,'word':'Buzz'}]
      this is effectively the same as using a class
    But each number must have a unique word so we can index our dict on the numbers e.g. {3:'Fizz',5:'Buzz'}
        Kevin why don't we just use a list of tuples? We can, and will, I just like dict's so I put them first.
            As of python 3.6 they take up about as much space as list and are ordered,
            More info in this Raymond Hettinger talk here https://www.youtube.com/watch?v=npw4s1QTmPg


    Calling numbers_and_words_are_relation_1(100, {3:'Fizz',5:'Buzz'}) would have the same effect as above.

    """
    for i in range(1, length + 1):
        output = ""
        for number, word in triggers.items():
            if i % number == 0:
                output += word
        if output == "":
            output += str(i)
        print(output)


def numbers_and_words_are_relation_2(length, triggers):
    """ This is basally the same as the last example but we use a list of tuples, instead of dicts.
        Calling numbers_and_words_are_relation_2(100, [(3,'Fizz'),(5,'Buzz')]) would have the same effect as above.
    """
    for i in range(1, length + 1):
        output = ""
        for trigger in triggers:
            if i % trigger.number == 0:
                output += trigger.word
        if output == "":
            output += str(i)
        print(output)


from fizzbuzz_triggers import Trigger


def numbers_and_words_are_relation_3(length, triggers):
    """ Kevin we want to use classes!
        Ok.
        Calling numbers_and_words_are_relation_3(100, [Trigger(3,'Fizz'),Trigger(5,'Buzz')])
          would have the same effect as above.
    """
    for i in range(1, length + 1):
        output = ""
        for number, word in triggers:
            if i % number == 0:
                output += word
        if output == "":
            output += str(i)
        print(output)


def lets_change_the_operation(length, triggers, operation):
    """ Im going to continue from numbers_and_words_are_relation_1 as I like that implantation the most.
    Kevin we are board of doing simple division, we want to say the word,
      when the square root is divisible by the number!

    We can take in the operation as a variable this means we aren't constrained to always doing mod, simple change.

    But how do we use it we take in a function, operation with to args,
      the number we are on and the trigger number, that returns a bool.
    the operation for the above scenario would be `lambda number, trigger: int(math.sqrt(number)) % trigger == 0`


    Calling lets_change_the_operation(100, {3:'Fizz',5:'Buzz'},lambda number, trigger: number % trigger == 0)
      would have the same effect as above.

    """
    for i in range(1, length + 1):
        output = ""
        for number, word in triggers.items():
            if operation(i, number):
                output += word
        if output == "":
            output += str(i)
        print(output)


def we_cant_test_this(length, triggers, operation):
    """ Kevin how we meant to test this?
    Our functions doesnt alter state or return anything, we can't test this.
      (technically printing to stout is altering state and testable but lets not go down that road)

    Easy fix, we return a list of strings, the person calling the function can handle the io.
    This also solve the problem of "what if I don't want to print the results"

    See `fizzbuzz_triggers.py` for example tests.

    Calling we_cant_test_this(100, {3:'Fizz',5:'Buzz'},lambda number, trigger: number % trigger == 0)
      would have the same effect as above.

    """
    output = []
    for i in range(1, length + 1):
        candidate = ""
        for number, word in triggers.items():
            if operation(i, number):
                candidate += word
        if candidate == "":
            candidate += str(i)
        output.append(candidate)
    return output


def one_liner():
    """ I quite like this implementation.
    It's not real an improvement on the above, but it does solve our original requirements,
      and i have nowhere else to put it

    For a sequence of numbers X, for x in X.
    x%n will cycle from 0 to n-1.
    as range starts at 0, the n-1's apreat every n'th index.
    Interger division by n-1 will replace all number less then n-1 with 0 and those equal with 1.
    multiply you word by ether 1 or 0, gives the word or the empty string.
    if none if you have the empty sting pring x+1 (remember FizzBuzz starts at 1)
    Yes the irony if a 11 line comment on a 1 line piece of code is not lost on me.
    """
    for x in range(100): print(x % 3 // 2 * 'Fizz' + x % 5 // 4 * 'Buzz' or x + 1)

