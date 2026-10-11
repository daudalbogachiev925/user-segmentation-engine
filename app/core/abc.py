def abc_classify(users):
    sorted_users = sorted(users, key=lambda u: -u.monetary)
    total = sum(u.monetary for u in sorted_users)
    if total == 0:
        return ["C"] * len(users)
    cum = 0
    classes = []
    for u in sorted_users:
        cum += u.monetary
        pct = cum / total
        if pct <= 0.8: classes.append("A")
        elif pct <= 0.95: classes.append("B")
        else: classes.append("C")
    mapping = {u.id: c for u, c in zip(sorted_users, classes)}
    return mapping
