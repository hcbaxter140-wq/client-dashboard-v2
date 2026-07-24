import pandas as pd

def load_and_sanitize(filepath, required_columns=None):
    """Safely reads a CSV and standardizes the headers."""
    try:
        df = pd.read_csv(filepath, encoding='utf-8-sig')
    except UnicodeDecodeError:
        df = pd.read_csv(filepath, encoding='latin1')
    except FileNotFoundError:
        print(f"ERROR: Could not find {filepath}")
        return pd.DataFrame()
    
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    if required_columns:
        normalized_required = [col.strip().lower().replace(' ', '_') for col in required_columns]
        missing = [col for col in normalized_required if col not in df.columns]
        if missing:
            raise ValueError(f"CRITICAL ERROR: Data is missing these columns: {missing}")
            
    return df

def force_numeric(df, column_name):
    """Forces a column to be numbers. Turns 'N/A' or blanks into 0."""
    if column_name in df.columns:
        df[column_name] = pd.to_numeric(df[column_name], errors='coerce').fillna(0)
    return df

def clean_text(df, column_name):
    """Standardizes messy text by stripping spaces and forcing UPPERCASE."""
    if column_name in df.columns:
        df[column_name] = df[column_name].astype(str).str.strip().str.upper()
    return df
