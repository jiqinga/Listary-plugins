from fastapi import FastAPI
import requests
import json

app = FastAPI()  # 创建 api 对象


# 判断是否是中文
def is_all_chinese(strs):
	for _char in strs:
		if not '\u4e00' <= _char <= '\u9fa5':
			return False
	return True


@app.get("/{data}")  # 根路由
def root(data: str):
	print(data)
	if is_all_chinese(data):
		res = fy(data, "auto2en")
	else:
		res = fy(data, "auto2zh")
	return ["", ["翻译结果为👇", res]]


def fy(data, lang):
	url = "http://api.interpreter.caiyunai.com/v1/translator"
	token = "ajh3xltrrtb9oro8z7dd"
	payload = {
		"source": data,
		"trans_type": lang,
		"request_id": "demo",
		"detect": True,
	}
	
	headers = {
		'content-type': "application/json",
		'x-authorization': "token " + token,
	}
	
	response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
	
	print(response.text)
	return json.loads(response.text)["target"]
