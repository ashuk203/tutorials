import string
import random

# len_s = int(input())
# s = input()

def is_deletable_max(s_arr, i):
    if i == 0:
        if len(s_arr) > 1:
            return (ord(s_arr[i]) - ord(s_arr[i + 1]) == 1)
        return False

    if i == len(s_arr) - 1:
        return (ord(s_arr[i]) - ord(s_arr[i - 1]) == 1)

    left_diff = ord(s_arr[i]) - ord(s_arr[i - 1])
    right_diff = ord(s_arr[i]) - ord(s_arr[i + 1])
    left_is_previous = left_diff == 1
    right_is_previous = right_diff == 1

    return (left_is_previous or right_is_previous) and (left_diff >= 0) and (right_diff >= 0)

def strip_iter(s):
    len_s = len(s)
    s_arr = [s[i] for i in range(len_s)]

    # Greedy remove elements
    curr_idx = 0
    while curr_idx < len(s_arr):
        if is_deletable_max(s_arr, curr_idx):
            del s_arr[curr_idx]
            curr_idx = 0
        else:
            curr_idx += 1

    return "".join(s_arr)

def get_max_deletes(s_orig):
    last_s = s_orig
    curr_s = strip_iter(last_s)

    return len(s_orig) - len(curr_s)


def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def test_random_str():
    while True:
        str_len = 2
        rand_str = randomString(str_len)
        rand_str_rvrs = ''.join(reversed(rand_str))

        rand_str_diff = get_max_deletes(rand_str)
        rand_str_rvrs_diff =  get_max_deletes(rand_str_rvrs)
        if rand_str_diff != rand_str_rvrs_diff:
            print(rand_str)
            print(rand_str_diff)
            print("vs.")
            print(rand_str_rvrs)
            print(rand_str_rvrs_diff)
            break

# test_random_str()

s = "ab"
print(get_max_deletes(s))
