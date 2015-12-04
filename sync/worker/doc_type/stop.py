class Stop(object):
    __es_index__ = 'next_bus'
    __es_doc_type__ = 'stop'

    @property
    def mappings(self):
        return {
            "properties": {
                "tag": {
                    "type": "string"
                },
                "title": {
                    "type": "string"
                },
                "location": {
                    "type": "geo_point"
                }
            },
            "_all": {
                "enabled": False
            }
        }
