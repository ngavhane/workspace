from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('submit_crash_form', '/submit_crash_form')
    config.add_route('submit_crash', '/submit_crash')
    config.add_route('list_crashes', '/list_crashes')
    config.add_route('delete_crashes', '/delete_crashes')

    config.add_route('submit_signature_form', '/submit_signature_form')
    config.add_route('submit_signature', '/submit_signature')
    config.add_route('list_signatures', '/list_signatures')
    config.scan()
    return config.make_wsgi_app()
