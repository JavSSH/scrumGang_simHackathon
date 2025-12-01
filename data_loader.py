import pandas as pd
import os

DATA_FOLDER = "data"

def load_nutrition_data():
    dfs = []

    # Recursively find all CSV files in DATA_FOLDER and subfolders
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

    # unify column names
    df.columns = df.columns.str.lower().str.strip()

    # create a search field if dataset contains 'description' or 'name'
    if "description" in df.columns:
        df["search_text"] = df["description"].fillna("").str.lower()
    elif "name" in df.columns:
        df["search_text"] = df["name"].fillna("").str.lower()
    else:
        df["search_text"] = ""

    return df


