# Yumemi_mock_exam_for_ServerSide

## 概要
本リポジトリは, [【新卒・中途採用】サーバーサイドエンジニア応募者向けの模試 - 株式会社ゆめみ](https://www.yumemi.co.jp/serverside_recruit) をPython (一応, Jupyterでも) 解いたコードが格納されている.

## ファイル説明
**test.py** ... 模試をPythonで回答したコード
<br>
**test.ipynb** ... 模試をJupyter Notebookで解答したコード
<br>
**test.csv** ... 疑似的に作成したinput file (行数が足りないなどの問題あり)
<br>
**output.csv** ... 解答の出力csvファイル
<br>
<br>
<br>
pythonの解答コードは以下の様に動かせば, output.csvが生成される.
```
python test.py test.csv
```
