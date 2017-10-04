import chemkin
def test_progress_rate():
    assert chemkin.progress_rate([3.0,1.0,1.0],[1.0,2.0,3.0],10) == [60.0]
test_progress_rate()

def test_reaction_rate():
    assert chemkin.reaction_rate([[3.0,1.0,1.0]],[[1.0,2.0,1.0]],[1.0,2.0,3.0],10) == [-10.0]
test_reaction_rate()