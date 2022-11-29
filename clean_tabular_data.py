import pandas as pd

def obtain_tabular_data(file_path: str, line_terminator: str = ',') -> pd.DataFrame:
    '''A function that imports data from a .cvs file to a pandas data frame, and deletes all incomplete rows.
    Args:
        file_path (str): path from where the data is to be imported
        line_terminator (str): line terminator of the .cvs file, by default a comma (',').
    Returns:
        pd.DataFrame: data frame of all complete contents from the .cvs file
    '''

    products_df = pd.read_csv("products.csv", sep=",")
    products_df.dropna() # deletes columns where at least 1 item is missing
    products_df.head()

    return products_df



if __name__ == "__main__":
    file_path = "tabular_data/products.csv"
    line_terminator = "\n"