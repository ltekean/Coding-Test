import sys

def cal(target):
    stack = []
    for s in target:
        if not len(stack) and s in [")", "]"]:
            return "no"
        elif s in ["(", "["]:
            stack.append(s)
        elif s == ")":
            if stack[-1] != "(":
                return "no"
            stack.pop()
        elif s == "]":
            if stack[-1] != "[":
                return "no"
            stack.pop()
    if not len(stack):
        return "yes"
    return "no"

while True:
    target = sys.stdin.readline().rstrip()
    if target == ".":
        break
    print(cal(target))