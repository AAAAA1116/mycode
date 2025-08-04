def reserve_str(s):
    if len(s) <= 1:
        return s
    return reserve_str(s[1:]) + s[0]

print(reserve_str("hello"))