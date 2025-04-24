import glob, json, pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

texts = [json.load(open(p))["text"] for p in glob.glob("data/raw/*.json")]
vec = TfidfVectorizer(stop_words="english", max_features=5000)
X = vec.fit_transform(texts)
pd.DataFrame(X.toarray()).to_csv("data/features.csv", index=False)

