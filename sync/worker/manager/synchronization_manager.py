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

        # move to separate RabbitMQ tasks
        for agency in agencies:
            sleep(3)
            routes = self.next_bus_client.get_agency_route_list(agency_tag=agency['tag'])

            for route in routes:
                sleep(1)
                schedule_list = self.next_bus_client.get_schedule(agency_tag=agency['tag'], route_tag=route['tag'])

                # TODO: move to Repository
                for schedule_desc in schedule_list:
                    departure = Departure(**schedule_desc)
                    db.session.add(departure)

                db.session.commit()

                sleep(1)
                stops_list = self.next_bus_client.get_route_config(agency_tag=agency['tag'], route_tag=route['tag'])

                # TODO: move to Repository
                for uuid, doc in stops_list.items():
                    es.index(index="next_bus", doc_type='stop', id=uuid, body=doc)
