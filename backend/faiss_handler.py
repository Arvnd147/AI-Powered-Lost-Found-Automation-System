import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

d = 384  # Embedding size
faiss_index = faiss.IndexFlatL2(d)
stored_grievances = []

def add_grievance_to_faiss(grievance_text, grievance_id):
    global stored_grievances
    vector = embedding_model.encode(grievance_text).reshape(1, -1)
    faiss_index.add(vector)
    stored_grievances.append({"id": grievance_id, "text": grievance_text})

def retrieve_similar_grievance(query_text):
    query_embedding = embedding_model.encode(query_text).reshape(1, -1)
    if faiss_index.ntotal > 0:
        _, idx = faiss_index.search(query_embedding, k=1)
        return stored_grievances[idx[0][0]] if idx[0][0] != -1 else None
    return None