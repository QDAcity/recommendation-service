from abc import ABC, abstractmethod
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from DataHandler.DataPipeline import TextDataPipeline, HuggingFaceTCFD


class TextRecommendationModel(ABC):
    """
    Abstract class for a deep learning model for text recommendation system.
    """

    @abstractmethod
    def __init__(self):
        """
        Constructor for the model.
        """
        pass


    @abstractmethod
    def build_model(self):
        """
        Method to build the deep learning model.
        """
        pass


class TfidfModel(TextRecommendationModel):
    """
    Tfidf model for text recommendation system.
    """

    def __init__(self):
        """
        Constructor for the model.
        """
        pass

    def build_model(self):
        """
        Method to build the tfidf model.
        """
        self.vectorizer = TfidfVectorizer()
        #self.tfidf_matrix = self.vectorizer.fit_transform(self.df['text'])
        return self.vectorizer
    
    

