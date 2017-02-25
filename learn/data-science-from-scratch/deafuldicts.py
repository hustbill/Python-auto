document = ["forgiveness", "is", "better", "than", "permission", "than", "is", "better", "choice", "better"]
print("document:")
print(document)

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

from collections import Counter
c = Counter([0, 1, 2, 0])           # c is (basically) {0 : 2, 1 : 1, 2 : 1}
print(c)
word_counts = Counter(document)
print("word_counts :")
print(word_counts)

# print the 10 most common words and their counts
for word, count in word_counts.most_common(10):
    print word, count


# Set
s = set()
s.add(1)
s.add(2)
s.add(2)

x = len(s)
print x

y = 2 in s
z = 3 in s
print y, z

# Control Flow
x = 0

for x in range(10):
    if x == 3:
      continue     # go immediately to the next iteration
    if x == 5:
      break         # quit the loop entirely
    print x

# Sorting
x = [4, 1, 2, 3]
y = sorted(x)  # is [1, 2, 3, 4], x is unchanged
print y
print "x before:" , x
x.sort()       # now x is [1, 2, 3, 4]
print "x end: ", x


# sort the list by absolute value from largest to smallest
x = sorted([-4, 1, -2, 3], key=abs, reverse=True)  # is [-4, 3, -2, 1]
print "x: ", x

# sort the words and counts from highest count to lowest
wc = sorted(word_counts.items(),
            key=lambda (word, count): count,
            reverse=True)
print "wc: ", wc
