from flask import current_app, request, jsonify

from web.repository import stop_repository


@current_app.route('/stops/', methods=['GET'])
def find_nearest_stop_by_geo_point():
    try:
        lat = float(request.args.get('lat'))
        lng = float(request.args.get('lng'))
    except (TypeError, ValueError):
        response = jsonify({'message': 'Invalid url params'})
        response.status_code = 400
        return response

    return jsonify(stop_repository.find_nearest_stop(lat, lng))
    # departures = departure_repository.get_stop_schedule(stop_tag)
    # return jsonify(departures=[d.serialize for d in departures])
