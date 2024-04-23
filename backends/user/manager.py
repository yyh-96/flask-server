from common import provider
from common.manager_base import ManagerBase
from backends.user.model import UserModel

PROVIDER = provider.ProviderAPIs


class UserManager(ManagerBase):
    _provides_api = "user_api"

    def __init__(self):
        super(UserManager, self).__init__()

    def get_user(self, user_id):
        return UserModel.query.filter_by(name=user_id).all()
    
    def get_users(self):
        return UserModel.query.all()
    
