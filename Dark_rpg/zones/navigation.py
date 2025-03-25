
ZONE_ROUTES = {}

def register_zone(name, func):
    ZONE_ROUTES[name] = func

def go_to(name):
    func = ZONE_ROUTES.get(name)
    if func:
        return func()
    print(f"[ERROR] Zone route '{name}' not registered.")