import re
import pandas as pd
from sqlalchemy import text

def parse_size(raw: str):
    if not isinstance(raw, str) or raw.strip() == '':
        return None, None
    s = raw.strip().upper()
    s = re.sub(r'^[A-Z]{2,}\s+', '', s)
    s = re.sub(r'^[A-Z]\s+[A-Z]\s+[A-Z]\s+', '', s)
    s = re.sub(r'^[A-Z]\s+[A-Z]\s+', '', s)
    match = re.search(r'(\d*\.?\d+)', s)
    if not match:
        return None, None
    numeric = float(match.group(1))
    rest = s.replace(match.group(0), '').strip()
    if rest.startswith('/') or rest.startswith('-'):
        rest = rest[1:].strip()
    unit = None
    for known in ['SQ FT', 'LOAD', 'BAG', 'CTN', 'PC', 'PK', 'CT', 'OZ', 'LB', 'LTR', 'PT', 'QT', 'GAL']:
        if known in rest:
            unit = known
            break
    else:
        words = re.findall(r'[A-Z]{2,}', rest)
        if words:
            unit = words[-1]
    if unit == 'OZ.':
        unit = 'OZ'
    elif unit == 'LTR':
        unit = 'L'
    return numeric, unit

def clean_product(engine):
    df = pd.read_sql("SELECT * FROM raw.products", engine)
    df = df[df['manufacturer'].notna() & (df['manufacturer'] > 0)]
    df = df.drop_duplicates(subset=['product_id'], keep='first')

    parsed = df['curr_size_of_product'].apply(parse_size)
    df['size_numeric'] = parsed.apply(lambda x: x[0])
    df['size_unit'] = parsed.apply(lambda x: x[1])

    if 'brand' in df.columns:
        df['brand'] = df['brand'].apply(lambda x: x.value if hasattr(x, 'value') else x)
    df.rename(columns={'manufacturer': 'manufacturer_id'}, inplace=True)

    df_clean = df[[
        'product_id', 'manufacturer_id', 'department', 'brand',
        'commodity_desc', 'sub_commodity_desc', 'curr_size_of_product',
        'size_numeric', 'size_unit'
    ]].copy()

    for col in ['department', 'brand', 'commodity_desc', 'sub_commodity_desc', 'curr_size_of_product', 'size_unit']:
        df_clean[col] = df_clean[col].where(pd.notnull(df_clean[col]), None)
        df_clean[col] = df_clean[col].apply(lambda x: None if isinstance(x, str) and x.strip() == '' else x)

    with engine.connect() as conn:
        conn.execute(text("TRUNCATE TABLE clean.products RESTART IDENTITY"))
        conn.commit()

    df_clean.to_sql('products', engine, schema='clean', if_exists='append', index=False, method='multi')
    print(f"Загружено {len(df_clean)} продуктов в clean.products")