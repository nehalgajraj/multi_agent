import chromadb

class MemoryAccess:
    def __init__(self, collection_name):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(collection_name)

    def add(self, document, metadata, ids):
        self.collection.add(documents=document, metadatas=metadata, ids=ids)

    def get(self, query, n_results=1, where=None):
        return self.collection.query(query_texts=query, n_results=n_results)
