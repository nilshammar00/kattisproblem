import sys
import math
from io import StringIO

# Simulated input data as a multi-line string
input_data = """4"""
sys.stdin = StringIO(input_data)
#print(int(input()))
print(math.ceil(1+math.log2(int(input()))))
