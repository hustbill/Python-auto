document = {"forgiveness", "is","better", "than", "permission", "this", "is", "better", "choice"}

word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

print("*** 1  ***")
print(word_counts)

#word_counts= {}
for word in document:
    previous_cout = word_counts.get(word, 0)
    word_counts[word] = previous_cout + 1
print("*** 2  ***")
print(word_counts)


from collections import defaultdict

word_counts = defaultdict(int)   # int() produces 0
for word in document:
    word_counts[word] += 1
print("*** 3  ***")
print(word_counts)

# They also be useful with list or dict or even your own functions:
dd_list = defaultdict(list)     # list() produces an empty list
dd_list[2].append(1)            # now dd_list contains {2: [1]}
print("dd_list : ")
print(dd_list)

dd_dict = defaultdict(dict)         # dict() products an empty dictionary
dd_dict["Joel"]["City"] = "Settle"  # {"Joel" : {"City" : Seattle"}}
print("dd_dict")
print(dd_dict)

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1                       # now dd_pair contains {2, [0,1]}
print("dd_pair")
print(dd_pair)
