from time import sleep

from utils.sql import db
from utils.elasticsearch import es
from worker.client.next_bus import NextBusClient
from worker.model.departure import Departure


class SynchronizationManager(object):
    def __init__(self):
        self.next_bus_client = NextBusClient()

    def run(self):
        agencies = self.next_bus_client.get_agency_list()

        for agency in agencies[:3]:
            sleep(5)
            routes = self.next_bus_client.get_agency_route_list(agency_tag=agency['tag'])

            # TODO: move to Repository
            stops_list = self.next_bus_client.get_route_config(agency_tag=agency['tag'], route_tag=routes[1]['tag'])
            for uuid, doc in stops_list.items():
                es.index(index="next_bus", doc_type='stop', id=uuid, body=doc)

            for route in routes[:3]:
                sleep(3)
                schedule_list = self.next_bus_client.get_schedule(agency_tag=agency['tag'], route_tag=route['tag'])

                # TODO: move to Repository
                for schedule_desc in schedule_list:
                    departure = Departure(**schedule_desc)
                    db.session.add(departure)

            db.session.commit()
