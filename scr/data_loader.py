import pandas as pd

def load_farma_go(path):
    df = pd.read_json(path, encoding="utf-8")
    return pd.json_normalize(
        df["medicamentos"],
        record_path="farmacias",
        meta=["nome", "categoria"],
        meta_prefix="medicamento_")