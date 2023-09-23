import argparse
import datetime
from pathlib import Path
from metrics import analytics

"""
Example on how to use the function top_retailers_on_period.
This can be called from the command line. Type
python top_retailers.py -h for a hint
"""
parser = argparse.ArgumentParser(description='Calculate the top retailers by revenu for a given time interval')
parser.add_argument('-p', '--path',  required=True, type=str, help='path to where data csv files are')
parser.add_argument('-b', '--begin-date', required=True, type=str, help='begin date on format YYYY/MM/DD')
parser.add_argument('-e', '--end-date', required=True, type=str, help='end date on format YYYY/MM/DD')
parser.add_argument('-s', '--sales-filename', required=True, type=str, help='csv sales filename')
parser.add_argument('-t', '--stores-filename', required=True, type=str, help='csv stores filename')

args = parser.parse_args()
begin_date = datetime.datetime.strptime(args.begin_date, '%Y/%m/%d')
end_date = datetime.datetime.strptime(args.end_date, '%Y/%m/%d')
path = Path(args.path)
retailers = analytics.top_retailers_on_period(
        path,
        args.sales_filename,
        args.stores_filename,
        begin_date,
        end_date
    )
print(retailers)