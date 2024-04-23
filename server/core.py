from backends.user.manager import UserManager
from common import provider
def load_backends():
    managers = [UserManager]

    drivers = {d._provides_api: d() for d in managers}

    provider.ProviderAPIs.lock_register()

    return drivers

