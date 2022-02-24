import pytest
from odiogarpa.preprocessing import preprocess_comment

def test_it_truncates_repetitions():
    comment = "aaaaaaaaahhhh"

    assert preprocess_comment(comment) == "aaahhh"

def test_it_converts_emojis():
    comment = "😃 genial!"

    assert preprocess_comment(comment) == "cara sonriendo con ojos grandes genial!"
    
def test_it_erases_html():
    comment = "ºº<br>----"
    
    assert preprocess_comment(comment) == "<br>---"

def test_it_converts_emoticon():
    comment = "XD xd buenísimo mal"
    
    assert preprocess_comment(comment) == 'riendo riendo buenísimo mal'
    
def test_it_solves_empty_comments():
    comment = ""
    
    assert preprocess_comment(comment) == "--"


