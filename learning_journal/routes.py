def includeme(config):
    config.add_route('lists', '/')
    config.add_route('create', '/journal/new-entry')
    config.add_route('detail1', r'/journal/{id:\d+}')
    config.add_route('detail2', r'/journal/{id:\d+}')
    config.add_route('update', r'/journal/{id:\d+}/edit-entry')
    config.add_static_view('static', 'static', cache_max_age=3600)
