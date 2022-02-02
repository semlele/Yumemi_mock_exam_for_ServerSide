# Yumemi_mock_exam_for_ServerSide

## 概要
本リポジトリは, [【新卒・中途採用】サーバーサイドエンジニア応募者向けの模試 - 株式会社ゆめみ](https://www.yumemi.co.jp/serverside_recruit) をPython (一応, Jupyterでも) 解いたコードが格納されている.

## ファイル説明
**test.py** ... 模試をPythonで回答したコード
<br>
**test.ipynb** ... 模試をJupyter Notebookで解答したコード
<br>
**create_big_csv.py** ... 疑似的なinput fileの**big_test.csv**を生成するコード
<br>
**big_test.csv** ... **create_big_csv.py**で疑似的に作成したinput file (行数が多いだけなので, その他エラーを考慮したcsvにはなっていない.)
<br>
**output.csv** ... 解答の出力csvファイル
<br>
<br>
<br>
以下の様にして, 適宜input fileを自分好みにカスタマイズできる.
```
python create_big_csv.py
```
<br>
pythonの解答コードは以下の様に動かせば, output.csvが生成される.
```
python test.py big_test.csv
```
