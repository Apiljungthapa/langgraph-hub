import os
from dotenv import load_dotenv
from pinecone import Pinecone
from utils.getLLM import get_llm_embedings
load_dotenv()
pinecone_api = os.getenv('PINECONE_API_KEY')

embeddings_model = get_llm_embedings('open_ai').get('embedding')

pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))

def get_vector_store_result(query: str, index_name: str, name_space: str, k: int = 5, embeddings_model=embeddings_model):
    if not pc.has_index(index_name):
        raise ValueError(f"Index '{index_name}' does not exist in Pinecone.")
    
    index = pc.Index(index_name)

    if embeddings_model is None:
        raise ValueError("Embeddings model must be provided.")

    query_embeddings = embeddings_model.embed_query(query)

    pc_data = index.describe_index_stats()
    
    if name_space not in pc_data.get('namespaces', {}):
        raise ValueError(f"Namespace '{name_space}' not found in index '{index_name}'.")

    results = index.query(
        namespace=name_space,
        vector=query_embeddings,
        top_k=k,
        include_values=False,
        include_metadata=True
    )

    
    
    final_results = "".join(entry['metadata']['text'] for entry in results['matches']).replace("\n"," ")

    return final_results