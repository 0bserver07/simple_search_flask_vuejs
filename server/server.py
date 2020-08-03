import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import random



# configuration
DEBUG = True

# Database
with open('./data/data_combined.json') as f:
  HEALTH_RECORDS = json.load(f)
  # to demonstrate the table client-side filter
  random.shuffle(HEALTH_RECORDS)


## FIXME HACKY solution
def icd_index_loader(records):
    """[summary]
        A temporary function to load the indices of the icd codes
    Args:
        records ([dict]): [description] a dictionary containing several items, we extract icd1010_code to map it the description

    Returns:
        [list]: [description]
    """

    # reduce look up time (ideally redis or ES)
    icd_dict = {r['icd1010_code']: r['icd_desc'] for r in records[:500]}

    # prepare the list
    icd_list = [{'name': r, 'detail': icd_dict[r]} for r in icd_dict]

    return icd_list






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

        selectedTags = [t['name'] for t in post_data['tags']]
        res = []

        if selectedTags:
            for hrow in HEALTH_RECORDS:
                if hrow['icd1010_code'] in selectedTags:
                    res.append(hrow)
            response_object['health_records'] = res
            response_object['icd_index'] = icd_index_loader(HEALTH_RECORDS)
        else:
            response_object['health_records'] = HEALTH_RECORDS[:500]
            response_object['icd_index'] = icd_index_loader(HEALTH_RECORDS)

    else:
        response_object['health_records'] = HEALTH_RECORDS[:500]
        response_object['icd_index'] = icd_index_loader(HEALTH_RECORDS)
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()