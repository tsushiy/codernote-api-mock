import requests
import json
import os
import urllib


def fetchAtcoderData():
  BASE_FILEPATH = "./api/"
  HOSTNAME = "atcoder-"
  BASE_API_URL = "https://kenkoooo.com/atcoder/resources/"
  API_PATH_LIST = ["contests.json", "problems.json", "merged-problems.json", "contest-problem.json"]

  for path in API_PATH_LIST:
    api_url = urllib.parse.urljoin(BASE_API_URL, path)
    filename = HOSTNAME + os.path.basename(path)

    response = requests.get(api_url)
    jsonData = response.json()

    filepath = os.path.join(BASE_FILEPATH, filename)
    file = open(filepath, 'w')
    file.write(json.dumps(jsonData, ensure_ascii=False))
    file.close()


os.makedirs('./api', exist_ok=True)
fetchAtcoderData()
