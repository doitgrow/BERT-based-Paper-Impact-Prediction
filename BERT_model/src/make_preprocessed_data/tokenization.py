import collections
import unicodedata
import tensorflow as tf

def printable_text(text):
    """Returns text encoded in a way suitable for print or `tf.logging`."""

    if isinstance(text, str):
        return text
    elif isinstance(text, bytes):
        return text.decode('utf-8', "ignore")
    else:
        raise ValueError("Unsupported string type: %s" % (type(text)))

    



    