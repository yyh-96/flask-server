# -*- coding: utf-8 -*-
from common.api_base import ResourceBase, APIBase
from common.db_extension import db
from backends.user.model import UserModel
from common import provider

PROVIDER = provider.ProviderAPIs

class UserResource(ResourceBase):

    _urls = ['/user', '/user/<string:user_id>']

    def get(self, user_id=None):
        if user_id is not None:
            return self._get_user(user_id)
        return self._list_users()

    def _get_user(self, user_id):
        return PROVIDER.user_api.get_user(user_id)

    def _list_users(self):
        return PROVIDER.user_api.get_users()

    def post(self):
        pass

    def patch(self, user_id):
        pass

    def delete(self, user_id):
        pass

class UserAPI(APIBase):
    _bp_name = 'user'
    _import_name = __name__
    _resources = [
        UserResource
    ]

APIs = (UserAPI,)