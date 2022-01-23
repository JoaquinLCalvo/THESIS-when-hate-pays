import pytest
from odiogarpa.preprocessing import preprocess_comment

def test_it_truncates_repetitions():
    comment = "aaaaaaaaahhhh"

    assert preprocess_comment(comment) == "aaahhh"

def test_it_converts_emojis():
    comment = "😃 genial!"

    assert preprocess_comment(comment) == "cara sonriendo con ojos grandes genial!"



