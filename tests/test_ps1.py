from problemSet1.ps1 import load_cows, greedy_cow_transport


def test_dictionary():
    data = "problemSet1/ps1_cow_data.txt"
    assert load_cows(data) == {'Maggie': 3, 'Herman': 7, 'Betsy': 9, 'Oreo': 6, 'Moo Moo': 3,
                               'Milkshake': 2, 'Millie': 5, 'Lola': 2, 'Florence': 2, 'Henrietta': 9}


def test_sort_cows_by_weight():
    cows = {'Maggie': 3, 'Herman': 7, 'Betsy': 9, 'Oreo': 6, 'Moo Moo': 3,
            'Milkshake': 2, 'Millie': 5, 'Lola': 2, 'Florence': 2, 'Henrietta': 9}
    assert greedy_cow_transport(cows, limit=10) == [
        ["Betsy"], ["Henrietta"], ["Herman"]]
