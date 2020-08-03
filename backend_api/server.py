import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import random



# configuration
DEBUG = True

with open('./data/data_combined.json') as f:
  HEALTH_RECORDS = json.load(f)
  # to demonstrate the table client-side filter
  random.shuffle(HEALTH_RECORDS)


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})




# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/health_records', methods=['GET', 'POST'])
def all_health_records():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        print(post_data)
        selectedTags = [t['name'] for t in post_data['tags']]
        res = []
        if selectedTags:
            for hrow in HEALTH_RECORDS:
                if hrow['icd1010_code'] in selectedTags:
                    res.append(hrow)
            response_object['health_records'] = res
            response_object['cpt_categories'] = [{'name': r['icd1010_code'], 'detail': r['icd_desc']} for r in HEALTH_RECORDS[:500]]
        else:
            response_object['health_records'] = HEALTH_RECORDS[:500]
            response_object['cpt_categories'] = [{'name': r['icd1010_code'], 'detail': r['icd_desc']} for r in HEALTH_RECORDS[:500]]

    else:
        response_object['health_records'] = HEALTH_RECORDS[:500]
        response_object['cpt_categories'] = [{'name': r['icd1010_code'], 'detail': r['icd_desc']} for r in HEALTH_RECORDS[:500]]
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()