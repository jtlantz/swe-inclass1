import sys
import pandas as pd


def verify_input(fn):
    import re
    # Regular expression pattern to match numbers
    pattern = r'^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$'
    with open(fn, 'r') as file:
        for line in file:
            # Use the search() function to check if the line matches the pattern
            match = re.search(pattern, line)
            if not match:
                return False
    return True

#main function
def compute(file):
    #read each line in file
    arr = []
    with open(file, 'r') as f:
        arr = [float(line) for line in f]
    #convert to dataframe
    df = pd.DataFrame(arr)
    print(file)
    print_stats(df)

def compute_all(files):
    #read each line in file
    arr = []
    for file in files:
        with open(file, 'r') as f:
            arr += [float(line) for line in f]
    #convert to dataframe
    df = pd.DataFrame(arr)
    print("Combined")
    print_stats(df)

def print_stats(arr: pd.DataFrame):
    print(f"mean: {arr.mean().values[0]}")
    print(f"std: {arr.std().values[0]}")
    print(f"min: {arr.min().values[0]}")
    print(f"max: {arr.max().values[0]}")

if __name__ == "__main__":
    #get all names of files
    files = sys.argv[1:]
    #by filtering this way, the whole program won't crash from one bad txt file
    valid_files = []
    for fn in files:
        if verify_input(fn):
            compute(fn)
            valid_files.append(fn)
        else:
            print(f"File {fn} contains invalid data.")
    compute_all(valid_files)