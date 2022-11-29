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

def clean_price_column(price_column: pd.Series) -> pd.Series:
    """A function that takes a pandas series containing prices, removes pound symbols (£) and commas, 
    then convert all values to floats.
    Args:
        price_column (pd.Series): pandas series of prices in string format
    Returns:
        pd.Series: pandas series of clean price data in float format
    """
    
    products_df['price'] = products_df['price'].str.strip('£')
    products_df = products_df.replace(',','', regex=True) # commas need to go to convert price string to float
    products_df['price'] = products_df['price'].astype('float64')
    price_column = products_df['price']

    return price_column


if __name__ == "__main__":
    file_path = "tabular_data/products.csv"
    line_terminator = "\n"

    obtain_tabular_data(file_path, line_terminator)
    clean_price_column()