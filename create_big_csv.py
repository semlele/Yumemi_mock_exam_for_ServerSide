import pandas as pd
import numpy as np

data_length = 10000 #適当な長さのデータを生成 (今回は1万行)
df = pd.DataFrame(columns=["create_timestamp","player_id","score"] )

# ランダムな日時を生成する関数
def random_dates(start, end, n, unit='D', seed=None):
    if not seed:  
        np.random.seed(0)
    ndays = (end - start).days + 1
    random_dt = pd.to_timedelta(np.random.rand(n) * ndays, unit=unit) + start
    random_dt_str = random_dt.astype(str)
    return list(map(lambda x: x[:16], random_dt_str)) # 日時をminuteまでスライス

np.random.seed(0)
start = pd.to_datetime('2001-01-01') # 適当に日付 (start, end) を指定
end = pd.to_datetime('2022-12-31')
df["create_timestamp"] = random_dates(start, end, data_length)

# 重複ありで、ランダムなidを生成
id_range = list(range(1000, 9999)) # playerの後に続く数値を1000~9999で指定
id_random = np.random.choice(id_range, data_length).astype(str)
id = "player" + id_random.astype(object)
df["player_id"] = id

#重複ありで、ランダムなscore生成 (今回は0~999の範囲指定)
df['score'] = pd.Series( np.random.randint(0,1000, len(df) ), index=df.index) 

df.to_csv("big_test.csv", index=False)
