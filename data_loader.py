import pandas as pd
import ast

def load_recipes(path="RAW_recipes.csv"):
    df = pd.read_csv(path)

    def parse_list(x):
        try:
            return ast.literal_eval(x)
        except:
            return []

    df["tags"] = df["tags"].apply(parse_list)
    df["ingredients"] = df["ingredients"].apply(parse_list)
    df["nutrition"] = df["nutrition"].apply(parse_list)

    df["text"] = (
        df["name"].fillna("") + " " +
        df["description"].fillna("") + " " +
        df["ingredients"].apply(lambda x: " ".join(x)) + " " +
        df["tags"].apply(lambda x: " ".join(x))
    )

    return df
