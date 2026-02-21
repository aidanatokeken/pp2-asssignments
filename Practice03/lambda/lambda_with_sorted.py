#1
nums = [5, 2, 9, 1]
sorted_nums = sorted(nums, key=lambda x: x)
print(sorted_nums)

#2
words = ["apple", "banana", "kiwi", "cherry"]
sorted_words = sorted(words, key=lambda w: len(w))
print(sorted_words)

#3
pairs = [(1, 3), (4, 1), (2, 5)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)

#4
nums = [7, 3, 10, 1]
sorted_desc = sorted(nums, key=lambda x: x, reverse=True)
print(sorted_desc)

#5
words = ["apple", "banana", "kiwi", "cherry"]
sorted_by_last = sorted(words, key=lambda w: w[-1])
print(sorted_by_last)
