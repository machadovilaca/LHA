import logging
from typing import Dict

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from actions.action import Action


class ActionCalculator:
    actions: Dict[str, Action]
    model: TfidfVectorizer
    threshold: float

    def __init__(self, actions: Dict[str, Action], threshold: float = 0.4):
        self.actions = actions
        self.model = TfidfVectorizer()
        self.threshold = threshold

    def train_model(self, data):
        return self.model.fit_transform(data)

    def get_all_tags(self):
        tags_list = []
        for action in list(self.actions.values()):
            tags_list.append(action.tags)
        return [' '.join(tag) for tag in tags_list]

    def select_action_to_execute(self, transcript: str):
        train = self.train_model(self.get_all_tags())
        test = self.model.transform([transcript.lower()])

        similarities = cosine_similarity(train, test)
        closest_action = similarities.argsort(axis=None)[-1]

        logging.info("Similaridade: {} (mínimo: {})"
                      .format(similarities[closest_action][0], self.threshold))

        if similarities[closest_action] >= self.threshold:
            return list(self.actions.values())[closest_action]
        else:
            return None
