import pandas as pd
import os

DATA_FOLDER = "data" 

def load_nutrition_data():
    dfs = []

    
    for root, dirs, files in os.walk(DATA_FOLDER):
        for file in files:
            if file.endswith(".csv"):
                path = os.path.join(root, file)
                if os.path.getsize(path) == 0:
                    print("Skipping empty file:", path)
                    continue
                print("Loading:", path)
                dfs.append(pd.read_csv(path))
    
    if not dfs:
        raise Exception(f"No CSV files found in '{DATA_FOLDER}' or its subfolders!")

    df = pd.concat(dfs, ignore_index=True)

    
    df.columns = df.columns.str.lower().str.strip()

    
    if "description" in df.columns:
        df["search_text"] = df["description"].fillna("").str.lower()
    elif "name" in df.columns:
        df["search_text"] = df["name"].fillna("").str.lower()
    else:
        df["search_text"] = ""

    return df


