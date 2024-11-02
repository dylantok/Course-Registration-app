import sqlite3
import pandas as pd

# 元データベース (aadb.sqlite3) に接続
conn_source = sqlite3.connect('aadb.sqlite3')

# 移行先データベース (db.sqlite3) に接続
conn_target = sqlite3.connect('db.sqlite3')

# コピーするテーブル名
table_name = 'hantei_subjecttable'

try:
    # 元データベースからテーブルを読み込む
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn_source)
    
    # 移行先データベースにデータを書き込む
    df.to_sql(table_name, conn_target, if_exists='replace', index=False)
    print(f"Table '{table_name}' copied successfully!")
except Exception as e:
    print(f"Failed to copy table '{table_name}': {e}")

# 接続を閉じる
conn_source.close()
conn_target.close()
