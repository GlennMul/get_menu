import pandas as pd


def upload_menu(menu):
    df = pd.DataFrame(menu)
    print(df)
    return df
