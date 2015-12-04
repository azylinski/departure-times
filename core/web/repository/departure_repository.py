import datetime
from sqlalchemy import and_
from flask import current_app

from web.model.departure import Departure


def get_stop_schedule(stop_tag):
    """ Sample query:
    SELECT *
    FROM departures
    WHERE stop_tag = '759499' AND departure_at > now()
    ORDER BY departure_at
    LIMIT 20;
    """

    now = datetime.datetime.utcnow()
    condition = and_(Departure.stop_tag == stop_tag, Departure.departure_at > now)
    max_display = current_app.config.get('DEPARTURES_DISPLAY_AMOUNT', 20)

    results = Departure.query.\
        filter(condition).\
        order_by(Departure.departure_at).\
        limit(max_display)

    return results
