from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer
from typing import Any, List
import numpy as np
import torch
import json


class EvalHandler:
    def __init__(self, model_path:str = "./code_recommandation", thresholds:float = 0.5, device:str = "cpu", max_length=512):
        self.model_path = model_path
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_path,
                                                           problem_type="multi_label_classification",)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        self.id2label = self.get_id2label(self.model_path)
        self.device = device
        self.max_length = max_length
        self.thresholds = thresholds

    def get_id2label(self, model_path:str):
        with open(model_path+"/id2label.json", 'r') as file:
            data = json.load(file)
        return data
    

    def predict(self, text) -> dict[list[Any], list[Any]]:
        encoding = self.tokenizer(text, return_tensors="pt", padding="max_length", truncation=True, max_length=512)
        encoding = {k: v.to(self.model.device) for k,v in encoding.items()}
        outputs = self.model(**encoding)
        logits = outputs.logits

        # apply sigmoid + threshold
        sigmoid = torch.nn.Sigmoid()
        probs = sigmoid(logits.squeeze().cpu())
        predictions = np.zeros(probs.shape)
        predictions[np.where(probs >= self.thresholds)] = probs.detach().numpy()[np.where(probs.detach().numpy() >= self.thresholds)]

        # turn predicted id's into actual label names
        predicted_labels = [self.id2label[str(idx)] for idx, label in enumerate(predictions) if label != 0.0]
        # select only scores != 0
        predictions = predictions[predictions != 0.0]

        # Combine the lists and sort them
        # Sort in descending order based on probabilities
        combined = zip(predictions.tolist(), predicted_labels)
        sorted_combined = sorted(combined, reverse=True) 
        # Unzip the sorted pairs back into two lists
        sorted_predictions, sorted_labels = zip(*sorted_combined) 

        # result = { 'text' : text, 'predicted_labels': predicted_labels, 'score': predictions.tolist() }
        result = {'predicted_labels': list(sorted_labels), 'score': list(sorted_predictions)}
        return result

    def predict_batch(self, texts):
        encoded_input = self.tokenizer(texts, return_tensors='pt', padding=True).to(self.device)
        output = self.model(**encoded_input)
        scores = output[0].detach().cpu().numpy()
        return scores
    

# if __name__ == "__main__":
#     from pprint import pprint
#     handler = EvalHandler(model_path="/Users/ariyanhasan/Documents/Hasan/project/recommendation-service/src/code_recommandation")
#     with open("/Users/ariyanhasan/Documents/Hasan/project/recommendation-service/data/cleandata/test.json", 'r') as file:
#         data = json.load(file)
#     text = data['5319479688953856']['documents']
#     result = handler.predict(text)
#     pprint(result)