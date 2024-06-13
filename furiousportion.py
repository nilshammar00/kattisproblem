import sys
from io import StringIO
input_data = """3 2 
4 
3
2"""

# Use StringIO to simulate standard input
sys.stdin = StringIO(input_data)

'''def furious_cocktail(n, t, durations):
    durations.sort()
    required_time = (n - 1) * t
    if durations[0] + required_time <= durations[-1]:
        return "YES"
    else:
        return "NO"
'''
# Read input
res = list(map(int, input(11).strip().split()))
durations = [int(input(11).strip())]# for _ in range(n)]
print(res)
print(durations)
# Output the result
#print(furious_cocktail(n, t, durations))

