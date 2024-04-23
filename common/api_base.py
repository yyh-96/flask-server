import abc

from flask import Blueprint
import flask_restful

class APIBase(object, metaclass=abc.ABCMeta):

    @property
    @abc.abstractmethod
    def _bp_name(self):
        """Override with an attr consisting of the API Name, e.g 'users'."""
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def _import_name(self):
        """Override with an attr consisting of the value of `__name__`."""
        raise NotImplementedError()
    
    @property
    def _bp_prefix(self):
        return '/'
    
    @property
    def _api_prefix(self):
        return ''
    
    @property
    def _resources(self):
        return []
    
    @property
    def api(self):
        return self.__api

    @property
    def blueprint(self):
        return self.__blueprint

    def __init__(self):
        self.__blueprint = Blueprint(
            name=self._bp_name, import_name=self._import_name,
            url_prefix=self._bp_prefix)
        self.__api = flask_restful.Api(
            app=self.blueprint, prefix=self._api_prefix)
        self._add_resources()

    def _add_resources(self):
        for r in self._resources:
            urls = r._urls
            self.api.add_resource(r, *urls)

    @classmethod
    def register_to_app(cls, app):
        inst = cls()
        app.register_blueprint(inst.blueprint)
        return inst

class ResourceBase(flask_restful.Resource):

    @property
    def _urls(self):
        raise NotImplementedError()
    