# def move_zeros(lst: list) -> list:
#     counter_of_zeros = 0
#     temporary_list = list()
#     for i in range(len(lst)):
#         if lst[i] == 0:
#             counter_of_zeros += 1
#         else:
#             temporary_list.append(lst[i])
#     temporary_list += [0] * counter_of_zeros
#     return temporary_list

# print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))  # [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
# print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))  # [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# print(move_zeros([0, 0]))  # [0, 0]
# print(move_zeros([]))  # []
# ================================================
#  1.0.0
# def two_squares(n: int) -> int:
#     max_sum = 0
#     root_n = int(n ** 0.5)
#     for i in range(root_n + 1):
#         a_squared = i ** 2
#         for j in range(root_n + 1):
#             b_squared = j ** 2
#             if a_squared + b_squared == n:
#                 summ = i + j
#                 max_sum = i + j if summ > max_sum else max_sum
#     if not max_sum:
#         return 0
#     else:
#         return max_sum
# 1.0.1
# def two_squares(n: int) -> int:
#     max_sum = 0
#     root_n = int(n ** 0.5)
#     list_squares = [i ** 2 for i in range(root_n + 1)]
#     set_squares = set(list_squares)
#     for i in list_squares:
#         if n - i in set_squares:
#             root_square_a = int(i ** 0.5)
#             root_square_b = int((n - i) ** 0.5)
#             summ = root_square_a + root_square_b
#             max_sum = summ if summ > max_sum else max_sum
#     if not max_sum:
#         return 0
#     else:
#         return max_sum

# 1.0.2

# def can_be_expressed_as_sum_of_two_squares(n):
#     if n < 0:
#         return False
#     while n % 4 == 0:
#         n //= 4
#     if n % 8 == 7:
#         return False
#     p = 3
#     while p * p <= n:
#         count = 0
#         while n % p == 0:
#             n //= p
#             count += 1
#         if p % 4 == 3 and count % 2 != 0:
#             return False
#         p += 2
#     return n % 4 != 3
#
#
# def two_squares(n: int) -> int:
#     if not can_be_expressed_as_sum_of_two_squares(n):
#         return 0
#
#     root_n = int(n ** 0.5)
#     list_squares = [(i, i ** 2) for i in range(root_n + 1)]
#     set_squares = {i ** 2 for i in range(root_n + 1)}
#
#     max_sum = 0
#
#     for a, a_squared in list_squares:
#         b_squared = n - a_squared
#         if b_squared in set_squares:
#             b = int(b_squared ** 0.5)
#             if a + b > max_sum:
#                 max_sum = a + b
#
#     return max_sum
# 1.0.3
# def can_be_expressed_as_sum_of_two_squares(n):
#     if n < 0:
#         return False
#     while n % 4 == 0:
#         n //= 4
#     if n % 8 == 7:
#         return False
#     p = 3
#     while p * p <= n:
#         count = 0
#         while n % p == 0:
#             n //= p
#             count += 1
#         if p % 4 == 3 and count % 2 != 0:
#             return False
#         p += 2
#     return n % 4 != 3
#
#
# def two_squares(n: int) -> int:
#     if not can_be_expressed_as_sum_of_two_squares(n):
#         return 0
#
#     root_n = int(n ** 0.5)
#     list_squares = [(i, i ** 2) for i in range(root_n + 1)]
#     set_squares = {i ** 2 for i in range(root_n + 1)}
#
#     max_sum = 0
#
#     i, j = 0, len(list_squares) - 1
#     while i <= j:
#         a, a_squared = list_squares[i]
#         b, b_squared = list_squares[j]
#         current_sum = a_squared + b_squared
#
#         if current_sum == n:
#             max_sum = max(max_sum, a + b)
#             i += 1
#             j -= 1
#         elif current_sum < n:
#             i += 1
#         else:
#             j -= 1
#
#     return max_sum
# print(two_squares(440)) # 0
# print(two_squares(369)) # 27
# print(two_squares(481)) # 31
# print(two_squares(773)) # 39
# print(two_squares(546)) # 0
# print(two_squares(256)) # 16
# print(two_squares(78400)) # 392
# print(two_squares(428216372)) # 29262
# print(two_squares(767307925)) # 0
# =======================================
# def all_squared_pairs(n: int) -> list:
#     root_n = int(n ** 0.5)
#     final_list = list()
#     list_squares = [i ** 2 for i in range(root_n + 1)]
#     set_squares = set(list_squares)
#     for i in list_squares:
#         if n - i in set_squares:
#             root_square_a = int(i ** 0.5)
#             root_square_b = int((n - i) ** 0.5)
#             if ([root_square_a, root_square_b] not in final_list) and ([root_square_b, root_square_a]\
#                 not in final_list):
#                 final_list.append([root_square_a, root_square_b])
#     return final_list
#

# print(all_squared_pairs(325)) # [[1, 18], [6, 17], [10, 15]]
# =========================================
# def strip_comments(string: str, markers: list):
#     new_string = string.split(' ' + markers[1])[0] # string without part after markers[1]
#     start_substring = new_string.find(' ' + markers[0])
#     end_of_substring = new_string.find('\n')
#
#     return new_string[:start_substring] + new_string[end_of_substring:]
#
# # print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))
# print(strip_comments('a #b\nc\nd $e f g', ['#', '$']))
# =========================================
# def find_uniq(arr: list):
#     set_arr = set(arr)
#     str_arr = str(arr)
#     item = set_arr.pop()
#     if str_arr.count(str(item)) == 1:
#         return item
#     else:
#         return set_arr.pop()
#
# print(find_uniq([1, 1, 3, 1, 1]))
# =========================================
# class Vector:
#
#     def __init__(self, lst: list):
#         self.lst = lst
#
#     def __str__(self):
#         return str(tuple(self.lst)).replace(' ', '')
#
#     def __iter__(self):
#         return iter(self.lst)
#
#     def __len__(self):
#         return len(self.lst)
#
#     def equals(self, other):
#         return self.lst == other.lst
#
#     def add(self, other):
#         if len(self.lst) != len(other):
#             raise Exception
#         new_lst = list()
#         for i, j in zip(self.lst, other):
#             new_lst.append(i + j)
#         return Vector(new_lst)
#
#     def subtract(self, other):
#         new_lst = list()
#         for i, j in zip(self.lst, other):
#             new_lst.append(i - j)
#         return Vector(new_lst)
#
#     def dot(self, other):
#         new_lst = list()
#         for i, j in zip(self.lst, other):
#             new_lst.append(i * j)
#         return sum(new_lst)
#
#     def norm(self):
#         new_lst = list()
#         for i in self.lst:
#             new_lst.append(i ** 2)
#         return sum(new_lst) ** 0.5
#
#
# a = Vector([1, 2, 3])
# b = Vector([4, 5, 6])
# c = Vector([4, 5, 6, 7])
# d = Vector([1, 2, 3])
#
# print(a.add(b))
# # print(a.add(c))
# print(a.subtract(b))
# print(a.dot(b))
# print(a.norm())
# print(a.equals(d))
# print(a)
# ===========================================
# def make_readable(seconds: int) -> str:
#     minutes = 0
#     hours = 0
#     while seconds >= 60 or minutes >= 60:
#         if seconds >= 60:
#             seconds -= 60
#             minutes += 1
#         if minutes >= 60:
#             minutes -= 60
#             hours += 1
#
#     if not hours:
#         hours_str = "00"
#     else:
#         hours_str = '0' + str(hours) if not hours // 10 else str(hours)
#
#     if not minutes:
#         minutes_str = '00'
#     else:
#         minutes_str = '0' + str(minutes) if not minutes // 10 else str(minutes)
#
#     if not seconds:
#         seconds_str = "00"
#     else:
#         seconds_str = '0' + str(seconds) if not seconds // 10 else str(seconds)
#
#     return str(f"{hours_str}:{minutes_str}:{seconds_str}")
#
#
# print(make_readable(60))
# print(make_readable(180))
# print(make_readable(59))
# print(make_readable(3599))
# print(make_readable(3600))
# print(1 // 10)

# ==================================================

MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9', '...---...': 'SOS',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '-.-.--': '!', '-....-': '-',
    '-.--.': '(', '-.--.-': ')', '...-..-': '$', '.-...': '&'
}


def decode_morse(morse_code):
    morse_code = morse_code.strip()

    words = morse_code.split('   ')

    decoded_message = []

    for word in words:
        characters = word.split(' ')
        decoded_word = ''.join(MORSE_CODE_DICT[char] for char in characters)
        decoded_message.append(decoded_word)

    return ' '.join(decoded_message)

print()
print(decode_morse('--...'))
# print(decode_morse('...-..- ...-..- ...-..-'))
print(decode_morse('.   .'))
print(decode_morse('. .'))
print(decode_morse('...-..- ...-..- ...-..-'))
