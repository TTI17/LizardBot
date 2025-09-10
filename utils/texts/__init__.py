import importlib

def get_lang(lang: str):
    return importlib.import_module(f"utils.texts.{lang}")