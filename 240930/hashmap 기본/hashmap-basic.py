n = int(input())
d = dict()
for _ in range(n):
    inputs = input().split()

    command = inputs[0]
    params = inputs[1::]

    if command == "add":
        d[params[0]] = params[1]
    elif command == "find":
        if params[0] in d:
            print(d[params[0]])
        else:
            print(None)
    elif command == "remove":
        d.pop(params[0])