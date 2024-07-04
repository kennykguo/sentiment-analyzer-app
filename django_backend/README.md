Start MongoDB service - mongod

use sentiment_analysis_db

Run Django server - python manage.py runserver

Run FastAPI server - python manage.py runfastapi

Testing setup - curl -X POST "http://127.0.0.1:8000/sentiment/" -H "accept: application/json" -H "Content-Type: application/json" -d '{"text":"I love this product!","sentiment":"positive"}'

Retrieve a sentiment entry - curl -X GET "http://127.0.0.1:8000/sentiment/<id>" -H "accept: application/json"
