# -*- coding: utf-8 -*-
from common.provider import ProviderAPIs

class ManagerBase():

    _provides_api = None

    def __init__(self):
        if self._provides_api is None:
            raise
        self.__register_provider_api()

    def __register_provider_api(self):
        ProviderAPIs.register_provider_api(
            name=self._provides_api, obj=self)
