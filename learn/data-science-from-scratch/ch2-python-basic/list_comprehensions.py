even_numbers = [x for x in range(5) if x % 2 == 0]    #[0, 2, ,4]
squares      = [x * x for x in range(5)]              #[0, 1, 4, 5, 16]
even_squares = [x * x for x in even_numbers]

print even_numbers
print squares
print even_squares

square_dict = { x : x * x for x in range(5)}    # { 0:0, 1:1, 2:4, 3:9, 4:6}
square_set = {x * x for x in [1, -1]}           # {1 }
print square_dict
print square_set

zeros = [ 0 for _ in even_numbers]      # has same length as even_numbers
print zeros


pairs = [(x, y)
          for x in range(10)
          for y in range(10)]         # 100 pairs (0,0) (0,1) ... (9,8), (9,9)
print pairs

increasing_pairs = [(x, y)              # only pairs with x < y
          for x in range(10)            # range(lo, hi) equals
          for y in range(x + 1, 10)]    # [lo, lo + 1, ..., hi - 1]
print increasing_pairs
