import requests


RAG_API_URL = "http://localhost:8000/ask"


def ask_rag(question: str, department: str):

    response = requests.post(
        RAG_API_URL,
        json={
            "question": question,
            "department": department
        }
    )

    response.raise_for_status()

    return response.json()