import psycopg2
import random

# Connect to the database
conn = psycopg2.connect(
    dbname="your_db_name",
    user="your_db_user",
    password="your_db_password",
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

# generate_statistics.py

import psycopg2
import random

# Connect to the database
conn = psycopg2.connect(
    dbname="your_db_name",
    user="your_db_user",
    password="your_db_password",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Get all companies
cur.execute("SELECT id FROM api_company")
companies = cur.fetchall()

# Generate random statistics for each company
for company_id in companies:
    mean = round(random.uniform(1, 5), 2)
    std_dev = round(random.uniform(0.5, 1.5), 2)
    
    # Check if statistics already exist for the company
    cur.execute("SELECT id FROM api_statistics WHERE company_id = %s", (company_id[0],))
    existing_stats = cur.fetchone()
    
    if existing_stats:
        # Update existing statistics
        cur.execute(
            "UPDATE api_statistics SET mean = %s, standard_deviation = %s WHERE company_id = %s",
            (mean, std_dev, company_id[0])
        )
    else:
        # Insert new statistics
        cur.execute(
            "INSERT INTO api_statistics (company_id, mean, standard_deviation) VALUES (%s, %s, %s)",
            (company_id[0], mean, std_dev)
        )

conn.commit()
cur.close()
conn.close()

print("Statistics generated successfully.")