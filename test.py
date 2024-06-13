import sys
from io import StringIO

# Simulated input data as a multi-line string
input_data = """3 
4
3
2"""

# Use StringIO to simulate standard input
sys.stdin = StringIO(input_data)
print(4/4 + 4 + 4)
