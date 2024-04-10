import pandas as pd
class DataLoader:
    def __init__(self, preprocessor=None):
        """
        DataLoader initialization.
        :param preprocessor: An instance of Preprocessor class or similar, with a preprocess method. If None, preprocessing is skipped.
        """
        self.preprocessor = preprocessor
    
    def load_data(self, file_path):
        """
        Loads data from a CSV file.
        :param file_path: Path to the CSV file.
        :return: A pandas DataFrame with the processed articles.
        """
        # Load the CSV file into a DataFrame
        data = pd.read_csv(file_path, usecols=[0], header=None)
        data.columns = ['article'] 
        
        return data