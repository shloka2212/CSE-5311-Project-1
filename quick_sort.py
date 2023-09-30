import timeit

# Function to perform quick sort on data based on the 4th column (Sum)
def quickSort(data):
    def partition(arr, p, r):
        pivot = arr[r][3]
        i = p - 1
        for j in range(p, r):
            if arr[j][3] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[r] = arr[r], arr[i + 1]
        return i + 1

    def sort(arr, p, r):
        if p < r:
            q = partition(arr, p, r)
            sort(arr, p, q - 1)
            sort(arr, q + 1, r)

    sort(data, 0, len(data) - 1)

# Loop to sort data in each of the four files and generate output files
rowNumber = [20, 100, 2000, 6000]

for count in rowNumber:
    inputFile = f'arr{count}.txt'
    outputFile = f'arrQK_O_{count}.txt'

    # Read data from input file
    data = []
    with open(inputFile, 'r') as file:
        lines = file.readlines()
        for line in lines:
            randomValues = line.strip().split(' ')
            data.append([int(value) for value in randomValues])

    # Measure the time taken to perform quick sort using timeit
    elapsedTime = timeit.timeit(lambda: quickSort(data), number=1)

    # Write the sorted data and sorting time to the output file
    with open(outputFile, 'w') as file:
        # Write sorted data rows
        for row in data:
            file.write(' '.join(map(str, row)) + '\n')
        file.write(f"Sorting time: {elapsedTime:.6f} seconds")

    print(f"File '{outputFile}' generated successfully.")
    #print(f"Time taken for sorting {count} rows: {elapsedTime:.6f} seconds\n")
