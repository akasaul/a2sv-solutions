def interpret(command: str) -> str:
    res = []

    for i in command:
        if i == ')':
            if res[-1] == '(':
                res.pop()
                res.append('o')
            else:
                temp = []
                for i in reversed(res):
                    if i != '(':
                        temp.append(res.pop())
                    else:
                        break
                res.pop()
                res = res + list(reversed(temp))
        else:
            res.append(i)
    return "".join(res)


print(interpret("G()(al)"))
