import re
from pysentimiento.preprocessing import preprocess_tweet


def preprocess_comment(comment, emoji_wrapper="", **kwargs):
    text = preprocess_tweet(
        comment,
        emoji_wrapper=emoji_wrapper,
        **kwargs
    )

    ## FIX: hago esto porque tiene un pequeño error pysentimiento
    text = re.sub(r"\s+", " ", text)

    return text