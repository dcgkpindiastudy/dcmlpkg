

def dcshape(X_train, X_test, y_train, y_test):
    """
    Display the shape (number of rows and columns) of input arrays.

    Parameters:
    - X_train (array-like): Training input features.
    - X_test (array-like): Testing input features.
    - y_train (array-like): Training target labels.
    - y_test (array-like): Testing target labels.

    Returns:
    None

    Example:
    >>> X_train_data = [[1, 2], [3, 4]]
    >>> X_test_data = [[5, 6], [7, 8]]
    >>> y_train_data = [0, 1]
    >>> y_test_data = [1, 0]
    >>> dcshape(X_train_data, X_test_data, y_train_data, y_test_data)
    The rows and columns in X_train are : (2, 2)
    The rows and columns of X_test are: (2, 2)
    The rows and columns of y_train are: (2,)
    The rows and columns of y_test are: (2,)
    """
    print("The rows and columns in X_train are :\t", X_train.shape)
    print("The rows and columns of X_test are:\t", X_test.shape)
    print("The rows and columns of y_train are:\t", y_train.shape)
    print("The rows and columns of y_test are:\t", y_test.shape)

    
def dcsample(df, rw=10):
    """
    Randomly samples rows from a DataFrame.

    Parameters:
    - df (pd.DataFrame): The input DataFrame from which rows will be sampled.
    - rw (int, optional): The number of rows to sample. Default is 10. If None is provided, it defaults to 10.

    Returns:
    pd.DataFrame: A DataFrame containing randomly sampled rows from the input DataFrame.

    Example:
    >>> import pandas as pd
    >>> data = {'feature1': [1, 2, 3, 4, 5], 'feature2': [6, 7, 8, 9, 10]}
    >>> df = pd.DataFrame(data)
    >>> sampled_df = dcsample(df, rw=3)
    >>> print(sampled_df)
       feature1  feature2
    1         2         7
    3         4         9
    0         1         6
    """
    import pandas as pd
    
    if rw is None:
        rw = 10
    
    return df.sample(rw)

def DC_describe_categorical(X):
    """
    Just like .decribe(), but returns the results for categorical variables only.
    """
    from IPython.display import display, HTML
    display(HTML(X[X.columns[X.dtypes == "object"]].describe().to_html()))
    
