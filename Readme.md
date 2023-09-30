# Random Data Generation and Insertion Sort

This Python script generates random data for rows of numbers, calculates the sum of each row, and performs insertion sort based on the sum. The original and sorted data are then written to files along with the time taken for the sorting operation.

## Code Overview

### Functions

1. **`generate_random_data()`**
   - Generates a list of random integers between 1 and 99 for a row.

2. **`calculate_row_sum(row)`**
   - Calculates the sum of a given row.

3. **`insertionSort(data)`**
   - Performs insertion sort on the data based on the sum of each row (4th column).

### Data Generation and Sorting

The script generates data for different row counts (20, 100, 2000, and 6000) and performs the following steps for each dataset:

1. Generates random data.
2. Calculates the sum for each row.
3. Appends the sum to the row.
4. Writes the original data to a file (`arr{count}.txt`).
5. Measures the time taken for insertion sort using the `timeit` module.
6. Sorts the data using insertion sort.
7. Writes the sorted data along with the sorting time to a new file (`arrIS_O_{count}.txt`).

## Usage

1. Ensure you have Python installed on your system.
2. Run the script using the following command:

    ```bash
    python script_name.py
    ```

3. Check the generated files for the original and sorted data.

## Files

1. **`script_name.py`**
   - The main Python script.

2. **`arr{count}.txt`**
   - Files containing the original unsorted data for each dataset.

3. **`arrIS_O_{count}.txt`**
   - Files containing the sorted data along with the time taken for sorting.

## Dependencies

- `random` module (for random number generation).
- `timeit` module (for measuring execution time).

## Notes

- The sorting time is measured using the `timeit` module, and the results may vary based on the system's performance.

Feel free to explore and modify the script for your specific use case or dataset.
