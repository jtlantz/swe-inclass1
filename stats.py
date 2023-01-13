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
    print(f"mean: {df.mean().values[0]}")
    print(f"std: {df.std().values[0]}")
    print(f"min: {df.min().values[0]}")
    print(f"max: {df.max().values[0]}")

if __name__ == "__main__":
    #take the first name
    files = sys.argv[1:]
    #by filtering this way, the whole program won't crash from one bad txt file
    for fn in files:
        if verify_input(fn):
            compute(fn) 
        else:
            print(f"File {fn} contains invalid data.")