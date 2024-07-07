from django.conf import settings
from bson import ObjectId

class Sentiment:
    def __init__(self, text, score=None, created_at=None, _id=None):
        self.text = text
        self.score = score
        self.created_at = created_at
        self._id = str(_id) if _id else None  # Convert ObjectId to string

    @classmethod
    def create(cls, text):
        sentiment = cls(text)
        collection = settings.MONGO_DB['sentiments']
        result = collection.insert_one({
            'text': sentiment.text,
            'score': sentiment.score,
            'created_at': sentiment.created_at
        })
        sentiment._id = str(result.inserted_id)  # Convert ObjectId to string
        return sentiment

    @classmethod
    def get(cls, sentiment_id):
        collection = settings.MONGO_DB['sentiments']
        data = collection.find_one({'_id': ObjectId(sentiment_id)})
        if data:
            return cls(data['text'], data['score'], data['created_at'], str(data['_id']))  # Convert ObjectId to string
        return None

    @classmethod
    def get_all(cls):
        collection = settings.MONGO_DB['sentiments']
        return [cls(data['text'], data['score'], data['created_at'], str(data['_id'])) for data in collection.find()]  # Convert ObjectId to string

    def save(self):
        collection = settings.MONGO_DB['sentiments']
        collection.update_one({'_id': ObjectId(self._id)}, {'$set': {
            'text': self.text,
            'score': self.score,
            'created_at': self.created_at
        }})

    def delete(self):
        collection = settings.MONGO_DB['sentiments']
        collection.delete_one({'_id': ObjectId(self._id)})