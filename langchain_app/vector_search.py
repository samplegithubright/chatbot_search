from langchain_openai import OpenAIEmbeddings
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=5432
    )

embeddings = OpenAIEmbeddings()

def search_products(query):
    vector = embeddings.embed_query(query)

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT name, price
        FROM products
        ORDER BY embedding <-> %s
        LIMIT 5
    """, (vector,))

    results = cur.fetchall()
    cur.close()
    conn.close()

    return results
