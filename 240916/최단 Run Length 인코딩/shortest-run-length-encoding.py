A = input()
ans = []

def encoding(arr):
    count = 1
    new_str = ''
    for i in range(1,len(arr)):
        if arr[i] == arr[i-1]:
            count += 1
        else:
            if count > 0:
                new_str += str(count) + arr[i-1]

            count = 1

    if count > 0:
        new_str += str(count) + arr[-1]

    return new_str


variant_A = A

variant_A__list = list(variant_A)

variant_A__list.insert(0,variant_A__list.pop())

ans.append(len(encoding(variant_A__list)))

while ''.join(variant_A__list) != A:
    variant_A__list.insert(0, variant_A__list.pop())
    ans.append(len(encoding(variant_A__list)))

print(min(ans))