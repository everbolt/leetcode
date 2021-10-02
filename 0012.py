def intToRoman(num):
    char_list = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    num_list = [(1000, 900), (500, 400), (100, 90), (50, 40), (10, 9), (5, 4), (1, 1)]
    num_dict = {char_list[i]: num_list[i] for i in range(7)}
    data = {i: [0, False] for i in char_list}
    s = ""
    
    for char in char_list:
        current_num = num_dict[char][0]
        current_small = num_dict[char][1]
        data[char][0], num = num // current_num, num % current_num
        if num >= current_small: data[char][1], num = True, num - current_small

    for i in data.keys():
        while data[i][0] > 0:
            s, data[i][0] = s + i, data[i][0] - 1
        if data[i][1]:
            s += char_list[char_list.index(i) // 2 * 2 + 2] + i
    return s

input = 1994
print(intToRoman(input))