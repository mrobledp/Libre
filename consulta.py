import requests
import pandas as pd
import time
import sys

SQLPAD_URL = "http://localhost:3000"
USERNAME = "admin"
PASSWORD = "admin"

def run_query(sql_text: str):
    session = requests.Session()

    # 1. Login
    resp = session.post(
        f"{SQLPAD_URL}/api/signin",
        json={"email": USERNAME, "password": PASSWORD},
        headers={"Accept": "application/json"}
    )
    resp.raise_for_status()
    print("Login OK", session.cookies.get_dict())

    # 2. Crear batch
    query_payload = {
        "connectionId": "pgdb",
        "batchText": sql_text,
        "selectedText": "",
        "name": "consulta desde script",
        "chart": {"chartType": "", "fields": {}}
    }
    resp = session.post(f"{SQLPAD_URL}/api/batches", json=query_payload)
    resp.raise_for_status()
    batch = resp.json()
    batch_id = batch["id"]
    statement_id = batch["statements"][0]["id"]
    print("Batch:", batch_id, "Statement:", statement_id)

    # 3. Polling hasta que termine
    while True:
        resp = session.get(f"{SQLPAD_URL}/api/batches/{batch_id}")
        resp.raise_for_status()
        batch_status = resp.json()
        print("Estado batch:", batch_status.get("status"))
        if batch_status.get("status") == "finished":
            break
        time.sleep(1)

    # 4. Obtener resultados del statement
    resp = session.get(f"{SQLPAD_URL}/api/statements/{statement_id}/results")
    resp.raise_for_status()
    results = resp.json()

    # results es una lista de listas (filas crudas)
    if isinstance(results, list):
        rows = results
    else:
        rows = []

    # Convertir a DataFrame
    df = pd.DataFrame(rows)
    return df

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python consulta.py \"SELECT * FROM tabla\"")
        sys.exit(1)

    sql_text = sys.argv[1]
    df = run_query(sql_text)
    print(df.head())