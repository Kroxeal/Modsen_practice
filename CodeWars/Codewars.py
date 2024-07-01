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
#
# MORSE_CODE_DICT = {
#     '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
#     '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
#     '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
#     '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
#     '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
#     '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
#     '---..': '8', '----.': '9', '...---...': 'SOS',
#     '.-.-.-': '.', '--..--': ',', '..--..': '?', '-.-.--': '!', '-....-': '-',
#     '-.--.': '(', '-.--.-': ')', '...-..-': '$', '.-...': '&'
# }
#
#
# def decode_morse(morse_code):
#     morse_code = morse_code.strip()
#
#     words = morse_code.split('   ')
#
#     decoded_message = []
#
#     for word in words:
#         characters = word.split(' ')
#         decoded_word = ''.join(MORSE_CODE_DICT[char] for char in characters)
#         decoded_message.append(decoded_word)
#
#     return ' '.join(decoded_message)
#
# print()
# print(decode_morse('--...'))
# # print(decode_morse('...-..- ...-..- ...-..-'))
# print(decode_morse('.   .'))
# print(decode_morse('. .'))
# print(decode_morse('...-..- ...-..- ...-..-'))
# =============================================
# Linked list(data structures)
#
# class Node:
#     def __init__(self, data, next=None) -> None:
#         self.data = data
#         self.next = next
#
#
# class LinkedList:
#     def __init__(self, head) -> None:
#         self.head = head
#
#     def append(self, data):
#         tmp = self.head
#         while tmp.next:
#             tmp = tmp.next
#         tmp.next = Node(data)
#
#     def output(self):
#         tmp = self.head
#         while tmp.next:
#             print(tmp.data, tmp.next, end='\n')
#             tmp = tmp.next
#         print(tmp.data, tmp.next, end='\n')
#
#     def pop(self):
#         tmp = self.head
#         while tmp.next.next:
#             tmp = tmp.next
#         tmp.next = None
#
# head = Node(1)
# ll = LinkedList(head)
# ll.append(10)
# ll.append(18)
# ll.append(22)
# ll.append(1)
# ll.output()
# ll.pop()
# ll.output()
# =========================================
# Highest Scoring Word
# Letters = [
#     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
#     'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#     'u', 'v', 'w', 'x', 'y', 'z'
# ]
#
# def high(x: str) -> str:
#     splitted_string = x.split(" ")
#     biggest_word = ''
#     biggest_score = 0
#     for i in range(len(splitted_string)):
#         tmp_biggest_score = 0
#         for j in range(len(splitted_string[i])):
#             tmp_biggest_score += Letters.index(splitted_string[i][j]) + 1
#         if tmp_biggest_score > biggest_score:
#             biggest_score = tmp_biggest_score
#             biggest_word = splitted_string[i]
#     return biggest_word
#
#
# print(high('sdfs sdf jcvb pd p'))
# print(high('aa b')) # aa
# print(high('b aa')) # b
# print(high("aaa b")) # aaa
# ===================================
# Counting Duplicates
# def duplicate_count(text: str) -> int:
#     final_dictionary = dict()
#     count_of_letters = 0
#     text_lower = text.lower()
#     for i in range(len(text_lower)):
#         if text_lower[i] not in final_dictionary:
#             final_dictionary[text_lower[i]] = 1
#         else:
#             final_dictionary[text_lower[i]] += 1
#             if final_dictionary[text_lower[i]] == 2:
#                 count_of_letters += 1
#
#
#     return count_of_letters
#
#
# print(duplicate_count("hello world"))
# print(duplicate_count("Indivisibilities"))
# print(duplicate_count("abcdeaB"))
# print(duplicate_count("abcdeaa"))
# print(duplicate_count("abcde"))
# ==================================
# Basics 08: Find next higher number with same Bits (1's)
# def next_higher(n: int) -> str:
#     binary = bin(n).replace("0b", "")
#     reversed_binary = binary[::-1]
#     new_binary = ''
#     # prev = -1
#     # print(binary, 'dsf')
#     # print(reversed_binary, 'hell')
#     # # print(binary[-2])
#     # index = reversed_binary.find('0')
#     # new_binary = reversed_binary[:index] + '1' + '0' + reversed_binary[index + 2:]
#     # print(index)
#     # print(new_binary[::-1])
#     # return new_binary
#     is_previous_one = False
#     for i in range(len(reversed_binary)):
#         if reversed_binary[i] == '1':
#             if not is_previous_one and i == 0:
#                 new_binary += reversed_binary[i]
#             elif is_previous_one and
#
#
#
# print(next_higher(10))
# print(next_higher(129))
# print(next_higher(127))
# print(next_higher(1))
# print(next_higher(323423))
# ======================
# Next smaller number with the same digits
# def next_smaller(n):
#     digits = list(str(n))
#
#     i = len(digits) - 2
#     while i >= 0 and digits[i] <= digits[i + 1]:
#         i -= 1
#
#     if i == -1:
#         return -1
#
#     j = len(digits) - 1
#     while digits[j] >= digits[i]:
#         j -= 1
#
#     # Step 3: Swap X and Y
#     digits[i], digits[j] = digits[j], digits[i]
#
#     result = digits[:i + 1] + sorted(digits[i + 1:], reverse=True)
#
#     if result[0] == '0':
#         return -1
#
#     result = int(''.join(result))
#
#     return result
#
# print(next_smaller(907))
# print(next_smaller(1234567908)) # 1234567890
# print(next_smaller(531))
# print(next_smaller(2071))
# print(next_smaller(2017))
# print(next_smaller(9))
# print(next_smaller(135))
# print(next_smaller(1027))
# ==================================
# Next bigger number with the same digits
# def next_bigger(n):
#     digits = list(str(n))
#
#     i = len(digits) - 2
#     while i >= 0 and digits[i] >= digits[i + 1]:
#         i -= 1
#
#     if i == -1:
#         return -1
#
#     j = len(digits) - 1
#     while digits[j] <= digits[i]:
#         j -= 1
#
#     digits[i], digits[j] = digits[j], digits[i]
#
#     result = digits[:i + 1] + sorted(digits[i + 1:])
#
#     result = int(''.join(result))
#
#     return result
#
#
# print(next_bigger(513))
# print(next_bigger(21))
# print(next_bigger(12))
# print(next_bigger(9))
# print(next_bigger(111))
#
# ==============================
# IP Validation
# import re
#
#
# def is_valid_IP(strng):
#     ip_pattern = r'(([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}\Z'
#
#     return re.match(ip_pattern, strng) is not None
#
#
# print(is_valid_IP('12.255.56.1'))
# print(is_valid_IP('123.255.789.0'))
# print(is_valid_IP('1.2.3'))
# print(is_valid_IP(''))
# print(is_valid_IP('257.2.3.5'))
# ==============================
# sort the odd

# def quick_sort(array: list) -> list:
#     for i in range(len(array)):
#         pass


def sort_array(source_array: list) -> list:
    odd_digits_list = [] # nechetnie

    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            odd_digits_list.append(source_array[i])

    odd_digits_list = sorted(odd_digits_list)

    iter_of_odd_digits = iter(odd_digits_list)

    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = next(iter_of_odd_digits)

    return source_array


print(sort_array([5, 3, 2, 8, 1, 4, 6, 7, 4, 3, 3]))
print(sort_array([5, 3, 1, 8, 0])) # [1, 3, 5, 8, 0]
print(sort_array([7, 1])) # [1, 7]
print(sort_array([5, 8, 6, 3, 4])) # [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
print(sort_array([5, 3, 2, 8, 1, 4])) # [5, 8, 6, 3, 4]  =>  [1, 3, 2, 8, 5, 4]


