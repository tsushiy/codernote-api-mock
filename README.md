APIモックサーバ

```sh
$ npm install -g json-server
```

AtCoderProblemsAPIからjsonをダウンロードして単一ファイルにマージする

```sh
$ python3 fetch_data.py
$ python3 merge_json.py
```

```sh
$ json-server db.json --watch --middlewares middleware.js --routes route.json
```