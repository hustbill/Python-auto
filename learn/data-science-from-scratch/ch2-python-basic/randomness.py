import random

four_uniform_randoms = [random.random() for _ in range(4)]
# random.random() produces numbers uniformly between 0 and 1
# it's the random function we'll use most ofen
print four_uniform_randoms

# we can set wtih random.seed if we want to get reproducible results

random.seed(10)                        # set the seed to 10
print random.random()                  # 0.57140259469
random.seed(10)                        # reset the seed to 10
print random.random()                  # 0.57140259469



# random.randrange
ran1 = random.randrange(20)            # choose randomly from range(10) =[0, 1, ..., 9]
ran2 = random.randrange(3,6)           # choose randomly from range(3, 6) = [3, 4, 5]
print ran1
print ran2


up_to_ten = range(10)
random.shuffle(up_to_ten)
print up_to_ten

my_best_friend = random.choice(["Alice", "Bob", "Charlie"])
print my_best_friend

# random.sample
# randomly choose a sample of elements without replacement (i.e. with no duplicates)
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)  # [16, 36, 10, 6, 25, 9]
print winning_numbers

# to choose a sample of elments with replacement (i.e., allowing duplicates), you can just
# make multiple calls to random.choice
four_with_replacement = [random.choice(range(10))
                        for _ in range(4)]
print four_with_replacement
