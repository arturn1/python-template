from system.blueprints.schedule.scheme.reports import work_blueprint


def init_app(app):
    app.register_blueprint(work_blueprint)
