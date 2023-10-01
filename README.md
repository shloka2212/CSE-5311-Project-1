# Random Data Generation and Sorting

This Python script generates random data for rows of numbers, calculates the sum of each row, and performs insertion, merge, and quick sorts based on the sum. The original and sorted data, along with the time taken for the sorting operation, are then written to files.

## Code Overview

### Functions

1. **`generate_random_data()`**
   - Generates a list of random integers between 1 and 99 for a row.

2. **`calculate_row_sum(row)`**
   - Calculates the sum of a given row.

3. **`insertionSort(data)`**
   - Performs insertion sort on the data based on the sum of each row (4th column).

4. **`mergeSort(data)`**
   - Performs merge sort on the data based on the sum of each row (4th column).

5. **`quickSort(data)`**
   - Performs quick sort on the data based on the sum of each row (4th column).

### Data Generation and Sorting

The script generates data for different row counts (20, 100, 2000, and 6000) and performs the following steps for each dataset:

1. Generates random data.
2. Calculates the sum for each row.
3. Appends the sum to the row.
4. Writes the original data to a file (`arr{count}.txt`).
5. Reads the original data from the file (`arr{count}.txt`) than Sorts the data using insertion sort and writes the sorted data to a new file (`arrIS_O_{count}.txt`).
6. Measures the time taken for insertion sort using the `timeit` module.
7. Reads the original data from the file (`arr{count}.txt`) than Sorts the data using merge sort and writes the sorted data to a new file (`arrMR_O_{count}.txt`).
8. Measures the time taken for merge sort using the `timeit` module.
9. Reads the original data from the file (`arr{count}.txt`) than Sorts the data using quick sort and writes the sorted data to a new file (`arrQK_O_{count}.txt`).
10. Measures the time taken for quick sort using the `timeit` module.

## Usage

1. Ensure you have [Python](https://www.python.org/downloads/) installed on your system.
2. Run the script using the following command:

    ```bash
    python insertion_sort.py
    ```
    
3. Check the generated files for the original and sorted data.
4. Similarly, run the second script using the following command:

   ```bash
   python merge_sort.py
   ```
   
5. Check the generated files with sorted data.
6. Similarly, run the third script using the following command:

   ```bash
   python quick_sort.py
   ```
   
7. Check the generated files with sorted data.   

## Files

1. **[insertion_sort.py](insertion_sort.py)**
   - Uses Insertion Sort Algorithm to sort the elements.

2. **[merge_sort.py](merge_sort.py)**
   - Uses Merge Sort Algorithm to sort the elements.
     
3. **[quick_sort.py](quick_sort.py)**
   - Uses Quick Sort Algorithm to sort the elements.
   
5. **`arr{count}.txt`**
   - Files containing the original unsorted data for each dataset.

6. **`arrIS_O_{count}.txt`**
   - Files containing the sorted data using insertion sort along with the time taken for sorting.

7. **`arrMR_O_{count}.txt`**
   - Files containing the sorted data using merge sort along with the time taken for sorting.

8. **`arrQK_O_{count}.txt`**
   - Files containing the sorted data using quick sort along with the time taken for sorting.

## Dependencies

- [`random`](https://docs.python.org/3/library/random.html) module (for random number generation).
- [`timeit`](https://docs.python.org/3/library/timeit.html#timeit-examples) module (for measuring execution time).

## Notes

- The sorting time is measured using the `timeit` module, and the results may vary based on the system's performance.

Feel free to explore and modify the script for your specific use case or dataset.