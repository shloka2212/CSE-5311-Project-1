import random
import timeit

# Function to generate random data
def generate_random_data():
    return [random.randint(1, 99) for _ in range(3)]

# Function to calculate the sum of a row
def calculate_row_sum(row):
    return sum(row)

# Function to perform insertion sort on data based on the 4th column (Sum)
def insertionSort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key[3] < data[j][3]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

# Loop to generate data for 20, 100, 2000, and 6000 rows
row_counts = [20, 100, 2000, 6000]

for count in row_counts:
    data = []
    for _ in range(count):
        row = generate_random_data()
        row_sum = calculate_row_sum(row)
        row.append(row_sum)
        data.append(row)

    # Generate a unique file name for each dataset
    file_name = f'arr{count}.txt'

    # Write the data to a file
    with open(file_name, 'w') as file:
        # Write data rows
        for row in data:
            file.write(' '.join(map(str, row)) + '\n')

    print(f"File '{file_name}' generated successfully.")

    # Measure the time taken to perform insertion sort using timeit
    elapsedTime = timeit.timeit(lambda: insertionSort(data), number=1)

    outputFile = f'arrIS_O_{count}.txt'

    # Write the sorted data to the output file
    with open(outputFile, 'w') as file:
        # Write sorted data rows
        for row in data:
            file.write(' '.join(map(str, row)) + '\n')
        file.write(f"Sorting time: {elapsedTime:.6f} seconds")

    print(f"File '{outputFile}' generated successfully.")
