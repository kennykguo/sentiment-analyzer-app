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