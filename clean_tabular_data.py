import pandas as pd

def obtain_tabular_data(file_path: str='tabular_data/products.csv', line_terminator: str=',') -> pd.DataFrame:
    '''A function that imports data from a .cvs file to a pandas data frame, and deletes all incomplete rows.
    Args:
        file_path (str): path from where the data is to be imported
        line_terminator (str): line terminator of the .cvs file, by default a comma (',').
    Returns:
        pd.DataFrame: data frame of all complete contents from the .cvs file
    '''

    products_df = pd.read_csv(file_path, line_terminator)
    # print(products_df.head()) # uncomment to see original panda frame
    
    products_df = products_df.dropna() # deletes columns where at least 1 item is missing

    return products_df

def clean_price_column(price_column: pd.Series) -> pd.Series:
    """A function that takes a pandas series containing prices, removes pound symbols (£) and commas, 
    then convert all values to floats.
    Args:
        price_column (pd.Series): pandas series of prices in string format
    Returns:
        pd.Series: pandas series of clean price data in float format
    """
    products_df = obtain_tabular_data()
    price_column = products_df['price']
    
    # cleaning
    price_column = price_column.str.strip('£')
    price_column = price_column.replace(',','', regex=True) # commas need to go to convert price string to float
    price_column = price_column.astype('float64')
    # print(price_column) # uncomment to see cleaning results

    return price_column

if __name__ == "__main__":
    clean_price_column(pd.Series)