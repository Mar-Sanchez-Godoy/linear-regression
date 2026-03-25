import pandas as pd

def load_csv(file_path):
    """Load a CSV file into a DataFrame."""
    return pd.read_csv(file_path)


def clean_data(df):
    """Remove duplicates and null values from the DataFrame."""
    df = df.drop_duplicates()
    df = df.dropna()
    return df


def organize_time_series(df, date_column):
    """Convert a column to datetime and set as index."""
    df[date_column] = pd.to_datetime(df[date_column])
    df = df.set_index(date_column)
    return df

class DataProcessor:
    """Class for processing CSV data."""

    def __init__(self, file_path, date_column):
        self.file_path = file_path
        self.date_column = date_column
        self.data = self.load_data()

    def load_data(self):
        return load_csv(self.file_path)

    def clean(self):
        self.data = clean_data(self.data)

    def organize_time_series(self):
        self.data = organize_time_series(self.data, self.date_column)
