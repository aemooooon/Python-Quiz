import time
import traceback


def log(func):
    def inner(*args, **kwargs):
        myfunc = func(*args, **kwargs)
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        f = str(func).split(" ")[1]
        p = [arg for arg in args]
        r = func(*args, **kwargs)
        e = traceback.format_exc()
        print("Time: ", t)
        print("Function Name: ", f)
        print("Arguments: ", p)
        print("Return Value: ", r)
        print("Exceptions: ", e)
        return myfunc

    return inner


@log
def sayHello(name):
    return "Hello {}".format(name)


@log
def divided(a, b):
    a = int(a)
    b = int(b)
    if b == 0:
        raise ArithmeticError("Divisor cannot be zero")
    return a / b


if __name__ == "__main__":
    print(sayHello("Tom"))
    divided(3, 1)
