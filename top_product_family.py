import argparse
import datetime
from pathlib import Path
from metrics import analytics

"""
Example for how to use the function top_product_family_on_period.
This can be called from the command line. Type
python top_product_family_on_period.py -h for a hint
"""

parser = argparse.ArgumentParser(description='Calculate the top produc family by sales for a given time interval')
parser.add_argument('-p', '--path',  required=True, type=str, help='path to where data csv files are')
parser.add_argument('-b', '--begin-date', required=True, type=str, help='begin date on format YYYY/MM/DD')
parser.add_argument('-e', '--end-date', required=True, type=str, help='end date on format YYYY/MM/DD')
parser.add_argument('-s', '--sales-filename', required=True, type=str, help='csv sales filename')
parser.add_argument('-t', '--product-filename', required=True, type=str, help='csv product filename')

args = parser.parse_args()
begin_date = datetime.datetime.strptime(args.begin_date, '%Y/%m/%d')
end_date = datetime.datetime.strptime(args.end_date, '%Y/%m/%d')
path = Path(args.path)
top_family = analytics.top_product_family_on_period(
        path,
        args.sales_filename,
        args.product_filename,
        begin_date,
        end_date
    )
print(top_family)