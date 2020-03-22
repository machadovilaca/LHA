from sklearn.feature_extraction.text import TfidfVectorizer
from typing import List
from sklearn.metrics.pairwise import cosine_similarity
from Action import Action

class ActionCalculator:
    actions: List[Action]
    model: TfidfVectorizer
    threshold: float


    def __init__(self, actions: List[Action], threshold :float = 0.5):
        self.actions = actions
        self.model = TfidfVectorizer()
        self.threshold = threshold

    def train_model(self, data):
        return self.model.fit_transform(data)

    def select_action_to_execute(self, transcript):
        tags = [a.tags for a in self.actions]
        data = [val for sublist in tags for val in sublist]
        train = self.train_model(data)
        test = self.model.transform([transcript])

        similarities = cosine_similarity(train,test)
        closest_action = similarities.argsort(axis=None)[-1]
        if similarities[closest_action] >= self.threshold:
            s = data[closest_action]
            return [a for a in self.actions if s in a.tags]
        else:
            return None