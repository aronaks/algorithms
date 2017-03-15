from algorithms.gfg_strings5 import remove_spaces1, remove_spaces2


def test_remove_spaces_var1():
    input_str = "g  eeks   for ge  eeks  "
    new_str = remove_spaces1(input_str)
    expected_output = "geeksforgeeeks"
    assert new_str == expected_output


def test_remove_spaces_var2():
    input_str = "g  eeks   for ge  eeks  "
    new_str = remove_spaces2(input_str)
    expected_output = "geeksforgeeeks"
    assert new_str == expected_output
