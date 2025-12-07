import requests
import psycopg2
import os

API_KEY = os.getenv("STOCK_API_KEY")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

SYMBOL = "AAPL"

def fetch_and_store():

    url = (
        "https://www.alphavantage.co/query?"
        f"function=GLOBAL_QUOTE&symbol={SYMBOL}&apikey={API_KEY}"
    )

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()

        quote = data.get("Global Quote", {})

        if not quote:
            print("No data found from API.")
            return

        open_price = float(quote["02. open"])
        high_price = float(quote["03. high"])
        low_price = float(quote["04. low"])
        close_price = float(quote["05. price"])
        volume = int(quote["06. volume"])
        latest_trading_day = quote["07. latest trading day"]

        conn = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            dbname=DB_NAME
        )

        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO stock_data
            (symbol, open_price, high_price, low_price, close_price, volume, latest_trading_day)
            VALUES (%s,%s,%s,%s,%s,%s,%s)
        """, (
            SYMBOL,
            open_price,
            high_price,
            low_price,
            close_price,
            volume,
            latest_trading_day
        ))

        conn.commit()
        cursor.close()
        conn.close()

        print("Stock data inserted successfully.")

    except requests.exceptions.RequestException as e:
        print("API Error:", e)

    except psycopg2.Error as e:
        print("Database Error:", e)

    except Exception as e:
        print("Unexpected Error:", e)

if __name__ == "__main__":
    fetch_and_store()
