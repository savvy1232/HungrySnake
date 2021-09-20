import random
test_seed =int(input("Create a seed number"))
random.seed(test_seed)
import random
test_seed = int(input("Create a seed number:"))
random.seed(test_seed)
random_seed = random.randint(0,1)
if random_seed == 1:
    print("Heads")
else:
    print("Tails")