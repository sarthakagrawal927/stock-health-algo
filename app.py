
from flask import Flask,request
from flask_cors import CORS
from main import makeData
import json

app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET','POST'])
def names():
	user_json = request.get_json()
	stocks_data = user_json.get('stocks')
	timeframe = user_json.get('timeframe')
	result = makeData(stocks_data,timeframe)
	print(result)
	return result

@app.route('/hi',methods=['GET','POST'])
def hello_world():
	return 'Hello Word!, sup'

if __name__ == "__main__":
	app.run()

