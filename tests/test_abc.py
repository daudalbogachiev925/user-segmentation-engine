from app.core.abc import abc_classify

class U:
    def __init__(self, id, monetary):
        self.id = id
        self.monetary = monetary

def test_abc():
    users = [U(1, 1000), U(2, 500), U(3, 100), U(4, 50), U(5, 10)]
    result = abc_classify(users)
    assert result[1] == "A"
    assert result[5] in ("B", "C")
