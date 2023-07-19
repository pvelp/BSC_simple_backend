from flask import Flask, request, jsonify, Response, make_response
from flask_cors import CORS
from core.models.models import FeedBackModel
from core.actions.actions import add_new_feedback
from settings import settings
from database.db_connection import set_settings_file_for_db

app = Flask(__name__)
set_settings_file_for_db(settings)
CORS(app)


def response(status):
    result = "Failed" if status != 200 else "Success"
    res = make_response({"status": status})
    res.headers['Content-Type'] = 'application/json'
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res


@app.post('/feedback')
def feedback():
    request_data = request.get_json()
    print(request_data)
    data = FeedBackModel()
    try:
        data.name = request_data["name"]
        data.phone = request_data["phone"]
    except Exception as e:
        print(e)
    try:
        data.period = request_data["period"]
        data.business = request_data["business"]
    except Exception as e:
        print(e)
    try:
        add_new_feedback(data)
    except Exception as e:
        print(e)
        return response(500)
    return response(200)


if __name__ == '__main__':
    app.run()
