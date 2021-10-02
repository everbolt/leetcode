def print_sums(n):
    print(n)
    def next_sum(k):
        return print_sums(n + k)
    return next_sum


        #     for i in range(k - 1, -1, -1):
        #     c_len = len(temp) // k
        #     for j in range(len(temp) - 1, len(temp) - c_len - 1, -1):
        #         box_tails[i].next = temp[j]
        #         box_tails[i] = box_tails[i].next
        #     temp = temp[:len(temp) - c_len]
        # return box_heads