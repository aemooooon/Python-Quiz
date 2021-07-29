# custom Stack
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

class Calculator:
    # Transfer the user input from infix to postfix
    def infix2Postfix(self, infix):
        prec = {}
        prec["*"] = 5
        prec["/"] = 5
        prec["+"] = 3
        prec["-"] = 3
        prec["("] = 1
        prec[")"] = 1
        self.stack = Stack()
        self.PostFix = []
        self.TempArr = []
        self.comb = []
        self.infix = infix
        inlen = len(infix)

        for arr in range(inlen):
            self.TempArr.append(infix[arr])

        for value in self.TempArr:
            if value.isnumeric():
                self.PostFix.append(int(value))
            elif value == "(":
                self.stack.push(value)
            elif value == ")":
                topValue = self.stack.pop()
                while topValue != "(":
                    self.PostFix.append(topValue)
                    topValue = self.stack.pop()
            else:
                while (not self.stack.isEmpty()) and (
                    prec[self.stack.peek()] >= prec[value]
                ):
                    self.PostFix.append(self.stack.pop())
                self.stack.push(value)
        while not self.stack.isEmpty():
            self.PostFix.append(self.stack.pop())
        return self.PostFix

    # Calculate postfix expression
    def postfixCalculator(self, list):
        self.stack = Stack()
        for item in list:
            if str(item).isnumeric():
                self.stack.push(item)
            else:
                b = self.stack.pop()
                a = self.stack.pop()
                if item == "+":
                    self.stack.push(a + b)
                if item == "-":
                    self.stack.push(a - b)
                if item == "*":
                    self.stack.push(a * b)
                if item == "/":
                    self.stack.push(a / b)
        return self.stack.pop()

if __name__ == "__main__":
    c = Calculator()
    print(
        "This postfix calculator only supports single-digit addition, subtraction, multiplication and division(Priority provided)."
    )
    print('To quit this Calculator, please type "exit" then press Enter')
    inf = input(
        "To start a calculation just type infix expression then press Enter: "
    ).strip()
    while inf != "exit":
        pfix = c.infix2Postfix(inf)
        print("The expression your typed is: ", inf)
        print("Result: ", c.postfixCalculator(pfix))
        inf = input(
            "To start a calculation just type infix expression then press Enter: "
        ).strip()
    print("Thanks, Bye Bye...")