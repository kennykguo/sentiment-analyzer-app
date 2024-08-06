import psycopg2
import random

# Connect to the database
conn = psycopg2.connect(
    dbname="sentiment_app",
    user="kennykguo",
    password="rex25244",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Get all companies
cur.execute("SELECT id FROM api_company")
companies = cur.fetchall()

# Sample sentiments
sample_sentiments = [
    "Great product, highly recommended!",
    "Terrible experience, would not buy again.",
    "Average service, nothing special.",
    "Exceeded my expectations, will definitely return.",
    "Needs improvement in customer support."
]

# Import sentiments for each company
for company_id in companies:
    num_sentiments = random.randint(5, 20)
    for _ in range(num_sentiments):
        sentiment = random.choice(sample_sentiments)
        cur.execute(
            "INSERT INTO api_sentiment (company_id, review) VALUES (%s, %s)",
            (company_id[0], sentiment)
        )

conn.commit()
cur.close()
conn.close()

print("Sentiments imported successfully.")