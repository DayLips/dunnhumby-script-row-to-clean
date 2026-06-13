from sqlalchemy import text

def run_sql_file(conn, filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        sql = f.read()
    for statement in sql.split(';'):
        stmt = statement.strip()
        if stmt:
            conn.execute(text(stmt))
    conn.commit()