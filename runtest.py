
result = []
result.append(chr(int("1010011", 2)))
result.append(chr(int("101", 8)))
result.append(chr(int("57", 16)))
result.append(chr((10**2) - 35))
result.append(chr(sum([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) - 51))
result.append(chr(__import__('functools').reduce(lambda ab, _: (ab[1], ab[0] + ab[1]), range(9), (1, 1))[1]))
result.append(chr((ord('A') + ord('i')) - ord('i')))
result.append(chr(sum(int(d) for d in "99999") + 1))
result.append(chr((ord('z') - ord('h')) + 69))

email = "".join(result)
print("Email:", email)
