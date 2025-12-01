from sentence_transformers import SentenceTransformer, util

class NutritionRAG:
    def __init__(self, df):
        self.df = df
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

        self.embeddings = self.model.encode(
            df["description"].fillna("").tolist(), convert_to_tensor=True
        )

    def search(self,query):
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        scores  = util.cos_sim(query_embedding, self.embeddings)[0]

        top_idx = int(scores.argmax())
        item = self.df.iloc[top_idx]

        return {
            "food" : item.get("description", "Unknown"),
            "calories": item.get("calories", "N/A"),
            "protein": item.get("protein", "N/A"),
            "fat": item.get("fat", "N/A"),
            "carbohydrates": item.get("carbohydrates", "N/A"),
            
        }