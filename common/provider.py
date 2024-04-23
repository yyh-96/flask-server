# -*- coding: utf-8 -*-

class ProviderApi():

    _api_providers = {}
    _locked = False

    def __getattr__(self, item):
        try:
            return self._api_providers[item]
        except KeyError:
            raise AttributeError(
                "'ProviderAPIs' has no attribute %s" % item)

    def register_provider_api(self, name, obj):

        if self._locked:
            raise("The provider api registry has been locked")
        
        if name in self._api_providers:
            raise("The api %s has been register" % name)
        
        self._api_providers[name] = obj

    def lock_register(self):
        self._locked = True

        
ProviderAPIs = ProviderApi()