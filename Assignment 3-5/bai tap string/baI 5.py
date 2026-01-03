def negav_number(str):
    result = []
    i = 0
    while i < len(str):
        if str[i] == '-' and i + 1 < len(str) and str[i + 1].isdigit():
            num = '-'
            i += 1
            while i < len(str) and str[i].isdigit():
                num += str[i]
                i += 1
            result.append(int(num))
        else:
            i += 1

    for num in result:
        print(num)
negav_number("abc-5xyz-12k9l--34p")
