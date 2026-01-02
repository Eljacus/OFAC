import pandas as pd


def exportIncomplete(results):
    path = "./excel/Informacion_incompleta.xlsx"
    incomplete = [
        r for r in results
        if r["estadoTransaccion"] == "Informacion incompleta"
    ]

    if not incomplete:
        return

    df = pd.DataFrame(incomplete)
    df.to_excel(path, index=False)