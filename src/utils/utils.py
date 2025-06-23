import re


def split_camelcase(text: str):
    return re.sub("([A-Z][a-z]+)|_", r" \1", re.sub("([A-Z]+)", r" \1", text)).split()
