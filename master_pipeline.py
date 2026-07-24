import pandas as pd
import cleaner # Make sure cleaner.py is in the same folder!

def transform_data(df_raw):
    """
    STEP 2: THE BUSINESS LOGIC
    This function catches the dataframe from the Streamlit uploader,
    runs the business logic, and hands it right back to Streamlit.
    """
    
    # 1. Clean the columns (Example using your cleaner tool)
    # df_raw = cleaner.force_numeric(df_raw, 'cost')
    
    # 2. Run the client's math (Example)
    # df_raw['profit'] = df_raw['revenue'] - df_raw['cost']
    
    # For the master template, we just pass the data straight through
    df_clean = df_raw.copy()
    
    return df_clean
