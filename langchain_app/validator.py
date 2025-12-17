def validate_sql(query: str) -> bool:
    blocked = ["DROP", "DELETE", "TRUNCATE", "ALTER"]
    return not any(word in query.upper() for word in blocked)
