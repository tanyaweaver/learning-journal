def includeme(config):
    config.add_route('lists', '/')
    config.add_route('create', '/journal/new-entry')
    config.add_route('detail', '/journal/1')
    config.add_route('update', '/journal/1/edit-entry')
    config.add_static_view('static', 'static', cache_max_age=3600)
