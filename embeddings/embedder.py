from langchain_openai import OpenAIEmbeddings
import psycopg2
import os


def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=5432
    )

embeddings = OpenAIEmbeddings()

def store_product_embeddings():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM products")
    rows = cur.fetchall()

    for pid, name in rows:
        vector = embeddings.embed_query(name)
        cur.execute(
            "UPDATE products SET embedding = %s WHERE id = %s",
            (vector, pid)
        )

    conn.commit()
    cur.close()
    conn.close()
