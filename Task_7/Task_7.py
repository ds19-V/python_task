# user defined module
import module

print(module.d)
module.d = [i - 4 for i in module.d]
print(module.d)

# pandas package
import pandas as p

k = ['d', 'e', 'e', 'p' , 'a' , 's' , 'r', 'e' , 'e' ]
l = p.Series(k)
print(l)

# random module
import random as r

rm = list(range(1, 101))
print(r.choice(rm))

# sys package and python path
import sys

for o in sys.path:
   print(o)
