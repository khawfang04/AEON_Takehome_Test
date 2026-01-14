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


def prep_data() -> pd.DataFrame:
    """
    Write Your Code Here.
    """
    
    return


def group_by_data():
    """
    Write Your Code Here.
    """
    
    return 
    