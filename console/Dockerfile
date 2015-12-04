FROM node:5.1

MAINTAINER Artur Zylinski (@ArturZylinski)

ENV PATH /usr/local/bin:$PATH

RUN npm install -g gulp

# use changes to package.json to force Docker not to use the cache
# when we change our application's nodejs dependencies:
ADD package.json /tmp/package.json
RUN cd /tmp && npm install
RUN mkdir -p /code/console && cp -a /tmp/node_modules /code/console/

WORKDIR /code/console
ADD . /code/console

CMD ["gulp", "serve"]
