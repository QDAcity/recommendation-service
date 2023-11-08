
from abc import ABC, abstractmethod
from datasets import load_dataset
import pandas as pd


class TextDataPipeline(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def load_train_data(self) -> pd.DataFrame:
        pass
    
    @abstractmethod
    def load_test_data(self) -> pd.DataFrame:
        pass

    @abstractmethod
    def preprocess_data(self) -> pd.DataFrame:
        pass
    
    @abstractmethod
    def get_label_map(self) -> dict:
        pass



class HuggingFaceTCFD(TextDataPipeline):
    def __init__(self, dataset_name= "climatebert/tcfd_recommendations"):
        # super().__init__(dataset_name)
        self.data_path = dataset_name
        self.label_map = {0: 'none', 1: 'metrics', 2: 'strategy', 3: 'risk', 4: 'governance'}

    def load_train_data(self) -> pd.DataFrame:
        # Load data from data_path
        """Load dataset from HuggingFace Datasets Hub.
        Args:
            dataset_name (str): Name of the dataset to load.
            split (str): Name of the split to load.
        Returns:
            dataset (pandas.DataFrame): Pandas DataFrame containing the dataset.
        """
        dataset = load_dataset(self.dataset_name, split="train").to_pandas()
        return dataset
    
    def load_test_data(self) -> pd.DataFrame:
        # Load data from data_path
        """Load dataset from HuggingFace Datasets Hub.
        Args:
            dataset_name (str): Name of the dataset to load.
            split (str): Name of the split to load.
        Returns:
            dataset (pandas.DataFrame): Pandas DataFrame containing the dataset.
        """
        dataset = load_dataset(self.dataset_name, split="test").to_pandas()
        return dataset

    def get_label_map(self) -> dict:
        """Get label map for the TCFD recommendation dataset.
        Returns:
            label_map (dict): Dictionary mapping label indices to label names.
        """
        return self.label_map

    def preprocess_data(self):
        """Preprocess data."""
        # Preprocess data
        pass



    
    

