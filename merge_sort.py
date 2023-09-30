import timeit

# Function to perform merge sort on data based on the 4th column (Sum)
def mergeSort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i][3] < right_half[j][3]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

# Loop to sort data in each of the four files and generate output files
rowNumber = [20, 100, 2000, 6000]

for count in rowNumber:
    inputFile = f'arr{count}.txt'
    outputFile = f'arrMR_O_{count}.txt'

    # Read data from input file
    data = []
    with open(inputFile, 'r') as file:
        lines = file.readlines()
        for line in lines:
            randomValues = line.strip().split(' ')
            data.append([int(value) for value in randomValues])

    # Measure the time taken to perform merge sort using timeit
    elapsedTime = timeit.timeit(lambda: mergeSort(data), number=1)

    # Write the sorted data and sorting time to the output file
    with open(outputFile, 'w') as file:
        # Write sorted data rows
        for row in data:
            file.write(' '.join(map(str, row)) + '\n')
        file.write(f"Sorting time: {elapsedTime:.6f} seconds")

    print(f"File '{outputFile}' generated successfully.")
    #print(f"Time taken for sorting {count} rows: {elapsedTime:.6f} seconds\n")