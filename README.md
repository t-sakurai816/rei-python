# pythonDocker

最新版のPython3環境が使えます。  
使い方のメモは[Wiki](https://github.com/t-sakurai816/pythonDocker.wiki.git)にかきました。

## コマンドメモ

### 起動

```
docker-compose up -d --build
```

### コンテナの中に入る

```
docker compose exec python3 bash
```

以降は下記のようなコマンドでPythonが実行できます

```
python opt/sample.py
```

しかし`opt/`といちいち打つのはめんどくさいので、`opt`に移動してから`python sample.py`のほうが楽かもしれません

### コンテナ終了

```
docker compose down
```
