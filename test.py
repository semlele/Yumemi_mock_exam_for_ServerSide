import sys
import pandas as pd

args = sys.argv
df = pd.read_csv(args[1])

#player_idごとの平均スコアを算出 & 四捨五入し、降順で表示
df_ranking = df.groupby("player_id", as_index=False).mean().round().sort_values(by="score", ascending=False).reset_index(drop=True)
df_ranking["score"] = df_ranking["score"].astype(int)

#実行時間削減のため、順位付けの前に必要となるデータのみに絞り込む
for i in range(10,len(df_ranking)):
    if (df_ranking["score"][i-1] != df_ranking["score"][i]):
        df_ranking_top = df_ranking.head(i)
        break

#rankメソッドで順位付けし、先頭にrank列を追加
df_ranking_top.insert(0, "rank", df_ranking_top["score"].rank(ascending=False, method='min').astype(int))

#3列のCSV形式で出力
df_ranking_top.to_csv("output.csv", index=False)