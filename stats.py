import sys
import pandas as pd

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
    fn = sys.argv[1]
    compute(fn)