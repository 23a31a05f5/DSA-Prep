def generate_pascals_triangle(rows):
    triangle = []
    
    for i in range(rows):
        # Start each row with a 1
        row = [1]
        
        if triangle:
            last_row = triangle[-1]
            # Calculate the middle values based on the previous row
            for j in range(len(last_row) - 1):
                row.append(last_row[j] + last_row[j+1])
            # End each row with a 1
            row.append(1)
            
        triangle.append(row)
        
    return triangle

def print_triangle(triangle):
    n = len(triangle)
    for i, row in enumerate(triangle):
        # Format the row as a string of numbers
        row_str = " ".join(map(str, row))
        # Center the string to create the visual triangle shape
        print(row_str.center(n * 3))

# Generate and display the first 6 rows (Rows 0 to 5)
num_rows = 6
pascals_triangle = generate_pascals_triangle(num_rows)
print_triangle(pascals_triangle)

# o/p:
#         1         
#        1 1        
#       1 2 1       
#      1 3 3 1      
#     1 4 6 4 1     
#   1 5 10 10 5 1  