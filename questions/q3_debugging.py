"""
Task: Debugging Challenge

- Identify and fix any bugs or errors in the code.
- Ensure the code runs correctly and handles various cases gracefully.
"""

""" developer comment:normally i would report this back to source data contact point
**** in original file ****
in line 9, 378282246310005,Sarah,Wilson,03/25,567,American Express 

- Identify and fix any bugs or errors in the code > code seems fine except for data issue
I'm gonna assume ',' Sarah,Wilson should be ' Sarah Wilson' (space instead of comma)"""
import pandas as pd
# import outside of function so we don't have to reload everytime function is called
# this function could only deal with this file
def read_csv_file(input_path):
    try:
        df = pd.read_csv(input_path)
        
        df.columns = list(map(str.lower, df.columns))
        # add .strip() to remove leads/trails
        df['cardholdername'] = df['cardholdername'].str.strip()
        # I've never seen anyone dealing with  middle name so n=1 is probably fine
        name_split = df['cardholdername'].str.split(' ', n=1, expand=True) 
        #add .replace(['', None], '-') in case of missing first or last name and replace with '-' for clarity
        df['firstname'] = name_split[0].replace(['', None], '-')
        df['lastname'] = name_split[1].replace(['', None], '-')
        df = df.drop(columns=['cardholdername'])
        
        cols = list(df.columns)
        
        cols.remove('firstname')
        cols.remove('lastname')
        new_order = [cols[0], 'firstname', 'lastname'] + cols[1:]
        
        df = df[new_order]
        # return result of function
    except Exception as e:
        print(f"Error occurred while reading CSV file: {e}")
    return df

if __name__ == "__main__":
    try:
        df = read_csv_file('./sample_data/q3_credit_card.csv')
        # return result of function do what you want with it in main instead
        print(df)
    except Exception as e:
        print(f"Error occurred in main: {e}")