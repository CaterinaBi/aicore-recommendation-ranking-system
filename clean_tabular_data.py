import pandas as pd

pd.set_option('display.max_columns', None)
products_df = pd.read_csv("products.cvs", sep="|")