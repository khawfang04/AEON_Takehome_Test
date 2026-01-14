"""
Task: Combined Data Manipulation

Input Files (located in `sample_data/`):
1. `q1_raw_sales.csv` — Contains raw sales transaction data.
2. `q1_dim_branch.json` — Contains metadata about each branch.

Requirements:

1. Prepare Data:
   - Ensure all fields in `q1_raw_sales.csv` are correctly formatted:
   - Mask sensitive `card_no` to this format `**** **** **** 9091`	.
   - Perform any additional cleaning steps needed to prepare the data for analysis.
   - return pandas dataframe

2. Group By Data:
   - Using the cleaned data and branch metadata, calculate the total sales `amount` grouped by province.
   - Sort the result in descending order of total sales amount.

    Expected Output: 
    [
      {
        "province": "กรุงเทพมหานคร",
        "amount": 33670.57
      },
      {
        "province": "ปทุมธานี",
        "amount": 30416.41
      }
    ]
"""
import pandas as pd
import json
from decimal import Decimal, getcontext
# precision for decimal
getcontext().prec = 36

def prep_data() -> pd.DataFrame:
    """
    could only read and perform data cleaning steps for q1_raw_sales.csv file.
    return dataframe what to improve is make a config for data types and what to convert
    """
    # load raw sales data
    df = pd.read_csv('./sample_data/q1_raw_sales.csv')

    df["sales_id"] = df["sales_id"].astype(str)
    df["sales_date"] =  pd.to_datetime(df["sales_date"], format="%Y%m%d")
    df["cust_id"] = df["cust_id"].astype(str)
    # Mask sensitive `card_no` to this format `**** **** **** 9091`.
    df["card_no"] = df["card_no"].astype(str).apply(lambda x: "**** **** **** " + x[-4:])
    df['branch_code'] = df['branch_code'].astype(str).str.zfill(4)
    # cast amount to Decimal(36,2)
    df["amount"] = df["amount"].apply(lambda x: Decimal(x).quantize(Decimal("0.00")))
    return df
    
    return


def group_by_data():
    """
    Merges cleaned sales data with branch metadata, calculates total sales 
    grouped by province, and return the result sorted by amount descending.
    """

    sales_df = prep_data()
    
    # Load branch metadata
    with open('./sample_data/q1_dim_branch.json', 'r', encoding='utf-8') as f:
        branch_data = json.load(f)
    
    branch_df = pd.DataFrame(branch_data)

    # join sales data with branch metadata on branch_code
    merged_df = pd.merge(sales_df, branch_df, on='branch_code', how='left')
    
    # calculate the total sales `amount` grouped by province.
    result_df = merged_df.groupby('province')['amount'].sum().reset_index()
    
    # Sort the result in descending order of total sales amount
    result_df = result_df.sort_values(by='amount', ascending=False)
    # removes the Decimal(...) wrapper when printed
    result_df['amount'] = result_df['amount'].apply(lambda d: format(d, 'f')) 
    result = result_df.to_dict(orient='records')
    
    return result
    

if __name__ == "__main__":
    try:
        result = group_by_data()
        print(result)
    except Exception as e:
        print(f"Error occurred in main: {e}")