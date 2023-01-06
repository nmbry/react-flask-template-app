import logging

from flask import Blueprint, make_response, jsonify

from apis.models import sample_model

api = Blueprint('sample', __name__)

logger = logging.getLogger(__name__)


@api.route('/', methods=['GET'])
def index():
    """ サンプルJSONを返却する。 """
    sample_dict = sample_model.get_sample_data()

    logger.info('アクセスがきました。')

    return make_response(jsonify(sample_dict), 200)
