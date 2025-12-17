import re
from typing import Any, List, Tuple


# =========================
# Text Utilities
# =========================

def clean_text(text: str) -> str:
    """
    Clean user input by removing extra spaces and special characters.
    """
    if not text:
        return ""
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text


def detect_intent(query: str) -> str:
    """
    Detect intent from user query.
    Used to route between SQL search and vector search.
    """
    query = query.lower()

    product_keywords = ["product", "price", "cost", "item"]
    employee_keywords = ["employee", "salary", "department", "staff"]
    order_keywords = ["order", "customer", "sales"]

    if any(word in query for word in product_keywords):
        return "product_search"
    elif any(word in query for word in employee_keywords):
        return "employee_search"
    elif any(word in query for word in order_keywords):
        return "order_search"
    else:
        return "general_sql"


# =========================
# Result Formatting
# =========================

def format_sql_result(result: Any) -> Any:
    """
    Normalize SQL agent output for Streamlit display.
    """
    if result is None:
        return "No results found."

    if isinstance(result, list) and len(result) == 0:
        return "No results found."

    return result


def format_vector_results(results: List[Tuple]) -> List[dict]:
    """
    Convert vector search results into readable dictionaries.
    """
    formatted = []
    for row in results:
        formatted.append({
            "name": row[0],
            "price": float(row[1])
        })
    return formatted


# =========================
# Security Helpers
# =========================

def contains_sql_injection(text: str) -> bool:
    """
    Basic SQL injection pattern detection.
    """
    dangerous_patterns = [
        r";",
        r"--",
        r"/\*",
        r"\*/",
        r"drop\s+table",
        r"delete\s+from",
        r"truncate\s+table",
        r"alter\s+table"
    ]

    for pattern in dangerous_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return True

    return False


# =========================
# Logging Helpers
# =========================

def log_query(query: str, intent: str) -> None:
    """
    Simple console logger (can be replaced with file/DB logging).
    """
    print(f"[QUERY] {query}")
    print(f"[INTENT] {intent}")
