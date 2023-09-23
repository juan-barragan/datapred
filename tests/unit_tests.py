import unittest
import datetime
from pathlib import Path
from metrics import analytics

class TestMetrics(unittest.TestCase):
    path = Path('files')
    sales_file = 'sales_data.csv'
    stores_file = 'stores.csv'
    product_file = 'products.csv'
    begin_date = datetime.datetime(2016, 1, 1)
    end_date = datetime.datetime(2016, 2, 1)

    def test_retailers(self):    
        top_retailers = analytics.top_retailers_on_period(
            self.path,
            self.sales_file,
            self.stores_file,
            self.begin_date,
            self.end_date
        )
        self.assertTrue(len(top_retailers)>0)
        best_retailer = top_retailers[0]
        self.assertEqual(
            best_retailer, 
            analytics.Retailer_Performance(2, 910035355.35)
        )

    def test_top_product_familty(self):
        top_product_family = analytics.top_product_family_on_period(
            self.path,
            self.sales_file,
            self.product_file,
            self.begin_date,
            self.end_date
        )
        self.assertTrue(len(top_product_family)>0)
        ranked_by_sales = sorted(
            top_product_family, key = lambda x:x.sales
        )
        best_sales = ranked_by_sales[0]
        self.assertEqual(
            best_sales, 
            analytics.product_family_sales_by_day(
                datetime.datetime(2016,1,27),
                121551
            )
        )

if __name__ == '__main__':
    unittest.main()