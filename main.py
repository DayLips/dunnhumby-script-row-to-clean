from database import init_db, engine
from tools import run_sql_file, clean_product
import os

def main():
    init_db()
    
    clean_product(engine)

    sql_files = [
        "sql/clean_hh_demographic.sql",
        "sql/clean_campaign_desc.sql",
        "sql/clean_campaign_table.sql",
        "sql/clean_coupon.sql",
        "sql/clean_coupon_redempt.sql",
        "sql/clean_transaction_data.sql"
    ]

    with engine.connect() as conn:
        for filepath in sql_files:
            if not os.path.exists(filepath):
                print(f"Файл {filepath} не найден, пропускаем")
                continue
            print(f"Выполняется {filepath}...")
            run_sql_file(conn, filepath)

if __name__ == '__main__':
    main()