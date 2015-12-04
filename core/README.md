# Core module

Find schedule data for given stop_tag. Fetching prepared (preprocessed by sync module) data from PostgreSQL.

### Better data

Since the entire data is based on San Francisco, the default view (nearest stop to browser geo_location (Europe)), might not be that interesting, try:

http://188.166.69.145/api/v1/core/departures/SturgisSchoolWest
http://188.166.69.145/api/v1/core/departures/WMain28Centerville
http://188.166.69.145/api/v1/core/departures/MashpeeCommons
