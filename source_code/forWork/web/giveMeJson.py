from http import HTTPStatus
from flask import Flask, jsonify, redirect, render_template, request, url_for

app = Flask(__name__)


data = {
	"LOT" : "",
	"DBLINK" : ""
}

RepliedLotInfo = {
	"PART_NO":"300380450018D000",
	"LOT":"KD33009600",
	"PART_NAME":"BDQQ00201208R24MCA",
	"PARA_NAME":"AOI程式",
	"VALUE":"201208"
}

@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/1', methods = ['POST', 'GET'])
def LotInfomation():
	# if(request.is_json()):
	# 	data = request.get_json()
	# 	if RepliedLotInfo["LOT"] == data["LOT"]:
	# 		return RepliedLotInfo
	# else:
	# 	return "Good"


	return jsonify(RepliedLotInfo)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080, debug=True)


