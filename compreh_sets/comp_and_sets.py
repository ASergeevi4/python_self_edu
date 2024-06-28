# first list option

squares = [i ** 2 for i in range(1,10)]
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]

# print(even_squares)

#second list option
numbers = [1, 2, 3, 4, 5, 6, 6, 7, 7, 8]
labeled_numbers = ['even' if x % 2 == 0 else 'odd' for x in numbers]

# print(labeled_numbers)

# dict comprehention option
my_dict = {x: x ** 3 for x in range(1,11)}
# print(my_dict)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# matrix transpose 

transpose_matrix = []

for i in range(len(matrix)):
    transpose_row = []
    for row in matrix:
        transpose_row.append(row[i])
    transpose_matrix.append(transpose_row)
# print(transpose_matrix)

# matrix transpose comprehention

transpose_matrix_compr = [[row[i] for row in matrix] for i in range(len(matrix))]
print(transpose_matrix_compr)