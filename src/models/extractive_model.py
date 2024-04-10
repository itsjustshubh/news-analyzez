from model import SummarizationModel


class ExtractiveModel(SummarizationModel):

    def __init__(self):
        super().__init__("ExtractiveModel")
        # Initialize your extractive model here

    def train(self, train_data):
        # Implement training logic
        pass

    def generate_summary(self, input_text):
        # Implement summary generation logic
        pass

    def save_model(self, file_path):
        # Implement model saving logic
        pass

    def load_model(self, file_path):
        # Implement model loading logic
        pass

    def evaluate(self, test_data):
        # Implement evaluation logic
        pass
