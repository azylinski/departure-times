from flask import current_app
import requests
import datetime
import xml.etree.ElementTree as ET
from logging import getLogger


class NextBusClient(object):
    BASE_URL = 'http://webservices.nextbus.com/service/publicXMLFeed'

    def __init__(self):
        self.logger = getLogger(self.__class__.__name__)

    def get_agency_list(self):
        """
        GET http://webservices.nextbus.com/service/publicXMLFeed?command=agencyList
        """
        params = dict(command='agencyList')

        return self._general_extract(self._get(params))

    def get_agency_route_list(self, agency_tag):
        """
        GET http://webservices.nextbus.com/service/publicXMLFeed?command=routeList&a=<agency_tag>
        """
        params = dict(command='routeList', a=agency_tag)

        return self._general_extract(self._get(params))

    def get_route_config(self, agency_tag, route_tag):
        """
        GET http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a=sf-muni&r=N
        """
        params = dict(command='routeConfig', a=agency_tag, r=route_tag)

        body = ET.fromstring(self._get(params))

        results = {}

        for route in body:
            for stop in route.findall('stop'):
                stop_params = stop.attrib
                results[stop_params['tag']] = {
                    'tag': stop_params['tag'],
                    'title': stop_params['title'],
                    'location': "{lat},{lng}".format(lat=stop_params['lat'], lng=stop_params['lon'])
                }

        return results

    def get_schedule(self, agency_tag, route_tag):
        """
        GET http://webservices.nextbus.com/service/publicXMLFeed?command=schedule&a=sf-muni&r=N
        """
        params = dict(command='schedule', a=agency_tag, r=route_tag)

        body = ET.fromstring(self._get(params))

        results = []

        # TODO: move to adapter
        for route in body:
            route_title = route.attrib.get('title')
            route_period = route.attrib.get('serviceClass')

            path = {}

            header = route.find('header')
            for stop in header:
                path[stop.attrib.get('tag')] = stop.text

            for tr in route.findall('tr'):
                destination = None

                for stop in tr:
                    if stop.text != '--':
                        destination = path[stop.attrib.get('tag')]

                for stop in tr:
                    stop_tag = stop.attrib.get('tag')
                    departure_time = stop.text

                    if departure_time == '--':
                        continue

                    d = datetime.date.today()

                    for it in range(0, current_app.config.get('CALCULATE_FOR_NEXT_DAYS', 7)):
                        if self._is_date_within_route_period(d, route_period):
                            t = datetime.datetime.strptime(departure_time, '%H:%M:%S').time()
                            departure_at = datetime.datetime.combine(d, t)

                            results.append({
                                'stop_tag': stop_tag,
                                'departure_at': departure_at,
                                'destination': destination,
                                'route': route_title
                            })

                        d += datetime.timedelta(1)

        return results

    # TODO: move to separate class

    @staticmethod
    def _is_date_within_route_period(day, route_period):
        days_map = {
            0: ['Monday', 'Mo', 'wkd'],
            1: ['Tuesday', 'Tu', 'wkd'],
            2: ['Wednesday', 'We', 'wkd'],
            3: ['Thursday', 'Th', 'wkd'],
            4: ['Friday', 'Fr', 'wkd'],
            5: ['Saturday', 'sat'],
            6: ['Sunday', 'sun']
        }

        weekday_number = day.weekday()
        text_list = days_map[weekday_number]

        for text in text_list:
            if text in route_period:
                return True

        return False

    def _get(self, params=None):
        response = requests.get(self.BASE_URL, params=params)

        if response.status_code != 200:
            self.logger.warning('External server is not responding')
            raise Exception('Wrong status code')

        # TODO: NextBus error messages validation

        return response.content

    @staticmethod
    def _general_extract(body):
        root = ET.fromstring(body)

        result = []

        for child in root:
            result.append(child.attrib)

        return result
