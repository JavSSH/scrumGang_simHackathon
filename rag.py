from sentence_transformers import SentenceTransformer, util

class NutritionRAG:
    def __init__(self, df):
        self.df = df
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

        # Detect the best text column
        if "description" in df.columns:
            self.text_col = "description"
        elif "name" in df.columns:
            self.text_col = "name"
        elif "food" in df.columns:
            self.text_col = "food"
        elif "search_text" in df.columns:
            self.text_col = "search_text"
        else:
            raise Exception(" No suitable text column found for RAG.")

        print("Using text column:", self.text_col)

        # Build embeddings
        self.embeddings = self.model.encode(
            df[self.text_col].fillna("").astype(str).tolist(),
            convert_to_tensor=True
        )

    def search(self, query):
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        scores = util.cos_sim(query_embedding, self.embeddings)[0]

        top_idx = int(scores.argmax())
        item = self.df.iloc[top_idx]

        return {
            "food": item.get(self.text_col, "Unknown"),
            "calories": item.get("calories", "N/A"),
            "protein": item.get("protein", "N/A"),
            "fat": item.get("fat", "N/A"),
            "carbohydrates": item.get("carbohydrates", "N/A"),
        }
