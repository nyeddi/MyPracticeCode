from collections import deque
def palchecker(aString):
    chardeque = deque()

    for ch in aString:
        chardeque.appendleft(ch)

    stillEqual = True

    while len(chardeque) > 1 and stillEqual:
        first = chardeque.popleft()
        last = chardeque.pop()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
