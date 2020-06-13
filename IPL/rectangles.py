# Table dimensions: n x m
s = input().split()
n = int(s[0])
m = int(s[1])

def calculate_sets(numElems):
    return (2**numElems) - 1

def calculate_axis_sums(table):
    row_sums = [0 for i in range(n)]
    col_sums = [0 for i in range(m)]

    # Calculate row sums
    for r in range(n):
        row_sums[r] = sum(table[r])

    # Calculate column sums
    for c in range(m):
        col_sum = 0
        for r in range(n):
            col_sum += table[r][c]
        col_sums[c] = col_sum

    return row_sums, col_sums

# Initializing table with input values
table = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    r = input().split()
    for j in range(m):
        table[i][j] = int(r[j])

# Calculating number of sets
num_sets = -(n * m)
row_sum, col_sum = calculate_axis_sums(table)

for i in range(n):
    num_first_color = row_sum[i]
    num_second_color = m - num_first_color

    num_sets += calculate_sets(num_first_color)
    num_sets += calculate_sets(num_second_color)

for i in range(m):
    num_first_color = col_sum[i]
    num_second_color = n - num_first_color

    num_sets += calculate_sets(num_first_color)
    num_sets += calculate_sets(num_second_color)


print(num_sets)
