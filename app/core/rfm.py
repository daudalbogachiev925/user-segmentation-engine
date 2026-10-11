def r_score(r):
    if r <= 30: return 5
    if r <= 60: return 4
    if r <= 120: return 3
    if r <= 240: return 2
    return 1

def f_score(f):
    if f >= 30: return 5
    if f >= 15: return 4
    if f >= 7: return 3
    if f >= 3: return 2
    return 1

def m_score(m):
    if m >= 300: return 5
    if m >= 150: return 4
    if m >= 70: return 3
    if m >= 25: return 2
    return 1

def segment(r, f, m):
    if r >= 4 and f >= 4 and m >= 4: return "Champions"
    if r >= 3 and f >= 3 and m >= 3: return "Loyal"
    if r >= 4 and f <= 2: return "New Customers"
    if r >= 3 and f >= 2 and m >= 2: return "Potential Loyalist"
    if r <= 2 and f >= 3 and m >= 3: return "At Risk"
    if r <= 2 and f >= 4 and m >= 4: return "Cant Lose Them"
    if r <= 1 and f <= 2: return "Lost"
    return "Others"
