from web.app import create_app


app = create_app()


with app.app_context():
    import web.handler


app.run(host="0.0.0.0")
