# Stop Finder module

Find nearest stop, for given coordinates:

Example (San Francisco middle point):
```
GET http://188.166.69.145/api/v1/stop_finder/stops/?lat=37.7576793&lng=-122.50764
```

### Behind the scenes

Module is making a query to Elasticsearch which is storing cached version of ```NextBus``` stops data.


### Known issues

Since the current demo is placed on smallest (512MB) Digitalocean image, it's not enough to build a working Elasticsearch container. Instead, I used "Elasticsearch as a Service" (https://found.elastic.co/).
