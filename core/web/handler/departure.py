from flask import current_app, jsonify

from web.repository import departure_repository


@current_app.route('/departures/<stop_tag>', methods=['GET'])
def get_departures(stop_tag):
    departures = departure_repository.get_stop_schedule(stop_tag)
    return jsonify(departures=[d.serialize for d in departures])
