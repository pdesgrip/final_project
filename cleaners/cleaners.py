#function to clean all white spaces and upper cases in DFs

def clean_column_label(label):
    """
    removes white spaces from the beginning and end of a string label, 
    replace white spaces within the string with underscores,
    and convert the string to lower case.

    Input:
    - label (str): Input column label

    Output:
    - str: Cleaned column label
    """
    return label.strip().replace(' ', '_').lower()

def clean_dataframe_columns(df):
    """
    Clean the column labels of a pandas DataFrame by removing white spaces 
    from the beginning and end, replacing white spaces within the labels 
    with underscores, and converting them to lower case.

    Parameters:
    - df (pd.DataFrame): Input DataFrame

    Returns:
    - pd.DataFrame: DataFrame with cleaned column labels
    """
    df.columns = [clean_column_label(col) for col in df.columns]
    return df


# function to clean all white spaces and upper cases EVERYWHERE in DF

def clean_string(s):
    """
    removes white spaces from the beginning and end of a string 
    and converts to lower case

    Input:
    - s (str or any type): Input string or value

    Output:
    - str: Cleaned string if input is a string
    - any type: Original value if input is not a string
    """
    if isinstance(s, str):
        return s.strip().lower()
    return s

def clean_dataframe(df):
    """
    Apply cleaning to all elements of a pandas DataFrame by removing white spaces 
    from the beginning and end of strings and converting them to lower case.

    Parameters:
    - df (pd.DataFrame): Input DataFrame

    Returns:
    - pd.DataFrame: DataFrame with cleaned strings
    """
    return df.applymap(clean_string)
    
    
 

def unique_values_count(df, column):
    # check if column exists
    if column not in df.columns:
        return f"Column '{column}' not found in the DataFrame."

    # count the unique values and their instances
    unique_counts = df[column].value_counts(dropna=False)
    
    # count NaN or null values
    nan_count = df[column].isna().sum()

    return {'unique_value_counts': unique_counts,'nan_count': nan_count}
    
    
def n_counts_and_values(df):
    # prompt user for n
    try:
        n = int(input("Enter the number of columns to analyze (n): "))
        # ensure n is not greater than the total number of columns
        n = min(n, len(df.columns))

        results = {}

        for column in df.columns[:n]:
            # count the unique values and their instances
            unique_counts = df[column].value_counts(dropna=False)

            # count NaN or null values
            nan_count = df[column].isna().sum()

            results[column] = {'unique_value_counts': unique_counts, 'nan_count': nan_count}

        return results

    except ValueError:
        print("Please enter a valid number for n.")
        return {}







