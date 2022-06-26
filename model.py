from typing import List

from sentence_transformers import SentenceTransformer


class StringToVec:
    def __init__(self):
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    def get_vector_batch(self, string_list: List[str]):
        embeddings = self.model.encode(string_list)
        return embeddings

