# りーどみー

使い方のイメージ

```cmd
C:\...>tree /f
フォルダー パスの一覧:  ボリューム OS
ボリューム シリアル番号は ****-**** です
C:.
│  .gitignore
│  main.py
│  README.md
│
├─dst
│      .gitkeep
│
└─src
        sample.jpg
        sample360.jpg


C:\...>python main.py src dst
カレントディレクトリ： C:\...
　　入力ディレクトリ： C:\...\src
　　出力ディレクトリ： C:\...\dst
C:\...\src\sample.jpgを処理中...
C:\...\src\sample360.jpgを処理中...

C:\...>tree /f
フォルダー パスの一覧:  ボリューム OS
ボリューム シリアル番号は ****-**** です
C:.
│  .gitignore
│  main.py
│  README.md
│
├─dst
│      .gitkeep
│      sample360_00.jpg
│      sample360_01.jpg
│      sample360_02.jpg
│      sample360_03.jpg
│      sample360_04.jpg
│      sample360_05.jpg
│      sample360_06.jpg
│      sample360_07.jpg
│      sample360_08.jpg
│      sample360_09.jpg
│      sample360_10.jpg
│      sample360_11.jpg
│      sample360_12.jpg
│      sample360_13.jpg
│      sample360_14.jpg
│      sample360_15.jpg
│      sample_00.jpg
│      sample_01.jpg
│      sample_02.jpg
│      sample_03.jpg
│      sample_04.jpg
│      sample_05.jpg
│      sample_06.jpg
│      sample_07.jpg
│      sample_08.jpg
│      sample_09.jpg
│      sample_10.jpg
│      sample_11.jpg
│      sample_12.jpg
│      sample_13.jpg
│      sample_14.jpg
│      sample_15.jpg
│
└─src
        sample.jpg
        sample360.jpg
```

コマンドライン引数は省略可。

0. python main.py
0. python main.py 入力ディレクトリ
0. python main.py 入力ディレクトリ 出力ディレクトリ

入力／出力ディレクトリはデフォルトでカレントディレクトリ。