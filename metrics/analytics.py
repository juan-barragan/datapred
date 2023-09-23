import datetime
from pathlib import Path
import pandas as pd
from collections import namedtuple

# -*- coding: utf-8 -*-
""" A named class just for sending the answer on a nice readable format
"""
Retailer_Performance = namedtuple('Retailer_Performance', 'retailer_id revenue')


"""
This function reads a csv file containing sales. We slice for a given time interval.

"""
def read_sales_for_period(
        path_to_files: Path,
        sales_filename: str,
        start_date: datetime,
        end_date: datetime
    )->pd.DataFrame:
    sales_ds = pd.read_csv(path_to_files/sales_filename, parse_dates=['date'])
    return sales_ds[
        (sales_ds['date']>=start_date) & (sales_ds['date']<=end_date)
    ]

"""
Best retailers by revenue.
TODO: consider adding a dictionnary with the column names, so as if column names
changes this code will be unaltered and hard coded strings will disapear. 

"""
def top_retailers_on_period(
        path_to_files: Path,
        sales_filename: str,
        stores_filename: str,
        start_date: datetime,
        end_date: datetime,
        num_retailers: int=3
    ) -> list[Retailer_Performance]:

    stores = pd.read_csv(path_to_files/stores_filename)
    sales_on_period = read_sales_for_period(path_to_files, sales_filename, start_date, end_date)
    sales_by_store = pd.merge(sales_on_period, stores, on='store_id')
    total_sales_by_retailer = sales_by_store[['retailer_id', 'revenue']]\
        .groupby('retailer_id').sum()\
            .sort_values(by='revenue', ascending=False).iloc[:num_retailers,:]
    return  [
        Retailer_Performance(ret_id, sales) 
            for ret_id, sales in 
                zip(total_sales_by_retailer.index, total_sales_by_retailer['revenue']) 
    ]

""" Again, a named class just for sending the answer on a nice readable format
"""
product_family_sales_by_day = namedtuple('product_family_sales_by_day', 'date sales')

"""
Top product family by sales.
"""
def top_product_family_on_period(
        path_to_files: Path,
        sales_filename: str,
        product_filename: str,
        start_date: datetime,
        end_date: datetime,
    ) -> list[product_family_sales_by_day]:

    sales_on_period = read_sales_for_period(path_to_files, sales_filename, start_date, end_date)
    products = pd.read_csv(path_to_files/product_filename)
    sales_by_product = pd.merge(sales_on_period, products, on = 'product_id')
    top_products = sales_by_product[['family_id', 'sales']]\
        .groupby('family_id').sum().sort_values(by='sales', ascending=False)
    # Exception?
    if len(top_products) == 0:
        return []
    products_in_family = products[
        products['family_id'] == top_products.index[0]
    ]['product_id'].values
    sales_for_products_in_family = sales_on_period[sales_on_period.product_id.isin(products_in_family)]
    product_family_sales_by_day_ds = sales_for_products_in_family[['date', 'sales']].groupby(by='date').sum()
    return [
        product_family_sales_by_day(date, sales) 
            for date, sales in 
                zip(product_family_sales_by_day_ds.index, product_family_sales_by_day_ds['sales'])
    ]



    


