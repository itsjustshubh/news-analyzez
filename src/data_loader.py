import pandas as pd
import time


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
        :return: A pandas DataFrame with the processed Articles.
        """
        # Load the CSV file into a DataFrame
        data = pd.read_csv(file_path)

        # Apply preprocessing if a preprocessor is provided
        if self.preprocessor is not None:
            data = self.preprocessor.preprocess(data)

        return data


# Testing the DataLoader class and measuring load time
if __name__ == "__main__":
    loader = DataLoader()

    start_time = time.time()
    # Adjusted file path for the environment
    data = loader.load_data("/mnt/data/data.csv")
    end_time = time.time()

    print(data.head())  # Display the first few rows of the DataFrame
    print(f"Time taken to load data: {end_time - start_time} seconds")
