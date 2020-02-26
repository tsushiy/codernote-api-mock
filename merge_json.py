import json
import os
import glob


def mergeJson():
  BASE_FILEPATH = "./api/*"
  db = dict()

  filepaths = glob.glob(BASE_FILEPATH)
  for path in filepaths:
    file = open(path, 'r')
    data = json.load(file)
    filename = os.path.splitext(os.path.basename(path))[0]
    db[filename] = data
    file.close()

  MERGED_FILEPATH = "./db.json"
  file = open(MERGED_FILEPATH, 'w')
  file.write(json.dumps(db, ensure_ascii=False))
  file.close()


mergeJson()