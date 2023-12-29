import requests
import pandas as pd


def get_data(n_results: int = 10) -> pd.DataFrame:
    resp = requests.get(f"https://randomuser.me/api/?results={n_results}")
    if not resp.ok:
        raise RuntimeError(
            f"request to https://randomuser.me/api/?results={n_results} failed"
        )

    coords_list = [
        (
            float(x["location"]["coordinates"]["latitude"]),
            float(x["location"]["coordinates"]["longitude"]),
        )
        for x in resp.json()["results"]
    ]

    return pd.DataFrame(coords_list, columns=["lat", "lon"])
