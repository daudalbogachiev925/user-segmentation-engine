from app.core.rfm import r_score, f_score, m_score, segment

def test_r_score():
    assert r_score(10) == 5
    assert r_score(30) == 5
    assert r_score(31) == 4
    assert r_score(300) == 1

def test_segment_champion():
    assert segment(5, 5, 5) == "Champions"

def test_segment_lost():
    assert segment(1, 1, 1) == "Lost"
