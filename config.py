import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb+srv://madhavi:ammu1509@cluster1.mtgz6wq.mongodb.net/expense_tracker?retryWrites=true&w=majority')
