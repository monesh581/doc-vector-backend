import uuid
from app.db import get_connection
from app.embeddings import generate_embedding


def store_text(text: str):
    embedding = generate_embedding(text)

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO documents (id, content, embedding)
        VALUES (%s, %s, %s)
        """,
        (
            str(uuid.uuid4()),
            text,
            embedding
        )
    )

    conn.commit()
    cur.close()
    conn.close()


def store_chunks(chunks: list[str]):
    for chunk in chunks:
        store_text(chunk)


def semantic_search(query: str, top_k: int = 3):
    query_embedding = generate_embedding(query)

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT content
        FROM documents
        ORDER BY embedding <-> %s::vector
        LIMIT %s
        """,
        (query_embedding, top_k)
    )

    results = [row[0] for row in cur.fetchall()]

    cur.close()
    conn.close()

    return results
