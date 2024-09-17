import math
import random
import sys

print(sys.path)
print('-'*80)
for path in sys.path:
    print(path)

print('-'*80)
print(f"random: {random.__file__}\n{random.__doc__}")
print(f"math: {math.__doc__}")
