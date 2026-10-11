import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

FEATURES = ["recency_days", "frequency", "monetary", "tenure_days"]

def fit_clusters(users, k=5):
    X = np.array([[u.recency_days, u.frequency, u.monetary, u.tenure_days]
                  for u in users])
    X = StandardScaler().fit_transform(X)
    km = KMeans(n_clusters=k, random_state=0, n_init=10).fit(X)
    return km.labels_, km
