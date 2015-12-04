from flask import abort

from utils.elasticsearch import es


__INDEX__ = 'next_bus'
__DOC_TYPE__ = 'stop'


def find_nearest_stop(lat, lng):
    query = {
        "sort": [
            {
                "_geo_distance": {
                    "location": [lng, lat],
                    "order": "asc",
                    "unit": "km"
                }
            }
        ],
        "size": 1
    }

    response = es.search(index=__INDEX__, doc_type=__DOC_TYPE__, body=query)

    results = response['hits']['hits']

    if len(results) == 0:
        raise abort(404)

    result = results[0]
    stop = {
        'id': result['_id'],
        'tag': result['_source']['tag'],
        'title': result['_source']['title'],
        'location': result['_source']['location'],
        'distance': result['sort'][0]
    }

    return stop
