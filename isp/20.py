import re


pattern = r"[+-/*\d\[\](){}]*"

ex = "(1+3)*[14/2]()[{{}}]"

print(re.fullmatch(pattern,ex))
stack = []
# data.json = {"[":0,"(":0,"{":0}
pat_open = "([{"
pat_close = ")]}"
flag = True
for symbol in ex:
    #     открывающая сразу добавляю
    if symbol in pat_open:
        stack.append(symbol)
        # data.json[symbol]+=1
    elif symbol in pat_close:
        #  закрывающая
        if len(stack)==0:
            flag=False
            break
        else :
            prev = stack[-1]
            if pat_open.index(prev) == pat_close.index(symbol):
                stack.pop()
            else:
                flag=False
                break

if len(stack) != 0:
    flag = False


if flag:
    print("ok")
else:
    print("unbalanced")
