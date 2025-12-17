import streamlit as st
from langchain_app.sql_agent import run_sql_query
from langchain_app.vector_search import search_products
from utils.helpers import clean_text, detect_intent, format_vector_results

st.set_page_config(page_title="NL Search PostgreSQL")

st.title("🔍 Natural Language Search")

query = st.text_input("Ask a question about employees, orders, or products")

if st.button("Search"):
    if "product" in query.lower():
        results = search_products(query)
        st.subheader("Product Results")
        st.table(results)
    else:
        result = run_sql_query(query)
        st.subheader("Query Result")
        st.write(result)
