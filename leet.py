def romanToInt(s):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    d2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    x = 0
    sum = 0
    while x < len(s):
        if x < len(s) - 1:
            if s[x] + s[x + 1] in d2:
                sum += d2[s[x] + s[x + 1]]
                x += 2
            else:
                sum += d[s[x]]
                x += 1
        else:
            sum += d[s[x]]
            x += 1
    return sum