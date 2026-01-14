"""
Task: Debugging Challenge

- Identify and fix any bugs or errors in the code.
- Ensure the code runs correctly and handles various cases gracefully.
"""

def read_csv_file():
    
    import pandas as pd

    df = pd.read_csv('sample_data/q3_credit_card.csv')
    
    df.columns = list(map(str.lower, df.columns))
    
    name_split = df['cardholdername'].str.split(' ', n=1, expand=True)
    df['firstname'] = name_split[0]
    df['lastname'] = name_split[1]
    df = df.drop(columns=['cardholdername'])
    
    cols = list(df.columns)
    
    cols.remove('firstname')
    cols.remove('lastname')
    new_order = [cols[0], 'firstname', 'lastname'] + cols[1:]
    
    df = df[new_order]

    print(df)

if __name__ == "__main__":
    read_csv_file()