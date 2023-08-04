import sys


def process_stack(command, stack):
    if command[0] == "push":
        stack.append(int(command[1]))
    elif command[0] in ["pop", "top"]:
        if stack:
            return stack.pop() if command[0] == "pop" else stack[-1]
        else:
            return -1
    elif command[0] == "size":
        return len(stack)
    elif command[0] == "empty":
        return 0 if stack else 1


input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    command = input().rstrip().split()
    result = process_stack(command, stack)
    if result is not None:
        print(result)