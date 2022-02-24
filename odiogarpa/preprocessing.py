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
    text = re.sub("^[\d ]*", "", text)
    text = re.sub("&quot;", "", text)
    
    ## JOACO: Y acá los miles de emoticonos
    
    text = re.sub("_"," ", text)
    text = re.sub("xd", "riendo", text)
    text = re.sub("xdd", "riendo mucho", text)
    text = re.sub("xddd", "riendo mucho", text)
    text = re.sub("xD", "riendo", text)
    text = re.sub("xDD", "riendo mucho", text)
    text = re.sub("xDDD", "riendo mucho", text)
    text = re.sub("XD", "riendo", text)
    text = re.sub("XDD", "riendo mucho", text)
    text = re.sub("XDDD", "riendo mucho", text)
    text = re.sub("xP", "travieso", text)
    text = re.sub("xp", "travieso", text)
    text = re.sub("XP", "travieso", text)
    text = re.sub("X-P", "travieso", text)
    text = re.sub("UWU", "sonriente", text)
    text = re.sub("uwu", "sonriente", text)
    text = re.sub(re.escape(":)"), "sonrisa", text)
    text = re.sub(re.escape(":))"), "sonrisa intensa", text)
    text = re.sub(re.escape(":‑)"), "sonrisa", text)
    text = re.sub(":3", "sonrisa", text)
    text = re.sub(re.escape("=)"), "sonrisa", text)
    text = re.sub("=D", "sonrisa", text)
    text = re.sub("=DD", "sonrisa", text)
    text = re.sub(":D", "sonrisa", text)
    text = re.sub(":DD", "sonrisa", text)
    text = re.sub("8D", "sonrisa", text)
    text = re.sub("<3", "corazón", text)
    text = re.sub("v.v", "disgusto", text)
    text = re.sub("♡", "corazón", text)
    text = re.sub(">.<", "indeciso", text)
    text = re.sub(re.escape(">:‑)"), "maldad", text)
    text = re.sub(re.escape(":|"), "indeciso", text)
    text = re.sub(re.escape(":/"), "indeciso", text)
    text = re.sub(re.escape(":-/"), "molesto", text)
    text = re.sub(re.escape(";)"), "guiño", text)
    text = re.sub(re.escape(";‑)"), "guiño", text)
    text = re.sub(";D", "guiño", text)
    text = re.sub("D=", "horror", text)
    text = re.sub(">:O", "enojo", text)
    text = re.sub(":‑O", "sorpresa", text)
    text = re.sub(":O", "sorpresa", text)
    text = re.sub(":OO", "sorpresa grande", text)
    text = re.sub(":o", "sorpresa", text)
    text = re.sub(":‑o", "sorpresa", text)
    text = re.sub(":‑oo", "sorpresa grande", text)
    text = re.sub(":0", "sorpresa", text)
    text = re.sub(":-0", "sorpresa", text)
    text = re.sub(re.escape(":'‑)"), "alegría", text)
    text = re.sub(re.escape(":')"), "alegría", text)
    text = re.sub(re.escape(":'‑("), "triste", text)
    text = re.sub(re.escape(":'("), "triste", text)
    text = re.sub(re.escape(":("), "triste", text)
    text = re.sub(re.escape(":(("), "muy triste", text)
    text = re.sub(re.escape(":((("), "muy triste", text)
    text = re.sub(re.escape(":'("), "sorpresa", text)
    text = re.sub(re.escape(">:("), "enojado", text)
    text = re.sub("kk", "caca", text)
    text = re.sub("kkk", "caca", text)
    text = re.sub("ah re", "irónico", text)
    text = re.sub("ahre", "irónico", text)
    text = re.sub("a re", "irónico", text)
    text = re.sub("arhE", "irónico", text)
    text = re.sub("&quot;", "", text)
    text = re.sub("&quot;", "", text)
    
    #FIX: Estaba tirando error por htmls y comentarios que habían quedado vacíos, veamos si así se soluciona
    text = re.sub('<[^<]+?>', '', text)
    
    return text
