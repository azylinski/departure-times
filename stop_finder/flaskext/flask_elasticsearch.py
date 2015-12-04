# Based on: https://github.com/chiangf/Flask-Elasticsearch

from elasticsearch import Elasticsearch


# Find the stack on which we want to store the database connection.
# Starting with Flask 0.9, the _app_ctx_stack is the correct one,
# before that we need to use the _request_ctx_stack.
try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack


class FlaskElasticsearch(object):
    def __init__(self, app=None, **kwargs):
        self.app = app
        if app is not None:
            self.init_app(app, **kwargs)

    def init_app(self, app, **kwargs):
        app.config.setdefault('ES_HOSTS', ['localhost'])

        self.es_options = kwargs

        # Use the newstyle teardown_appcontext if it's available,
        # otherwise fall back to the request context
        if hasattr(app, 'teardown_appcontext'):
            app.teardown_appcontext(self.teardown)
        else:
            app.teardown_request(self.teardown)

    def __getattr__(self, item):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'es'):
                ctx.es = Elasticsearch(hosts=ctx.app.config.get('ES_HOSTS'), **self.es_options)

            return getattr(ctx.es, item)

    def teardown(self, exception):
        ctx = stack.top
        if hasattr(ctx, 'es'):
            ctx.es = None