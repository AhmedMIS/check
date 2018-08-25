import pandas as pd


def main():
    '''This code is just an overview of combining required coulumn from two different CSV files with using Panda
    library'''
    df = pd.read_csv("Example.csv", nrows=3)
    df1 = pd.read_csv("name.csv", nrows=3)
    print("Loaded File 1", df1)
    print("Checking the shape of loaded file", df.shape)
    # Reshaping the Loaded file and droping the columns in the loaded file
    df = df.loc[:, ["policyID", "statecode"]]
    # Joining the Column needed from file1 and File 2 into one file.
    df3 = pd.concat([df1, df], axis=1, join='inner').sort_index()
    # Storing the data into the new file
    df3.to_csv("New.csv", sep='\t')
    print(df3)


if __name__ == '__main__':
    main()
