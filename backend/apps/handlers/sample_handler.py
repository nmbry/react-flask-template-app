import json

from flask import Blueprint

from apps.models import sample_model

sample = Blueprint('sample', __name__)


@sample.route('/', methods=['GET'])
def index():
    result_dict = sample_model.get_sample_data()

    return json.dumps(result_dict)
