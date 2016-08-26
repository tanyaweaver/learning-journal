from pyramid.config import Configurator

import os

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_jinja2_renderer('.html')
    config.include('.routes')
    # config.include('.views')
    config.scan()
    return config.make_wsgi_app()
