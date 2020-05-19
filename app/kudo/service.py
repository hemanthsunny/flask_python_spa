from ..repository import Repository
from ..repository.mongo import MongoRepository
from .schema import KudoSchema

class Service(object):
    def __init__(self, user_id, repo_client=Repository(adapter=MongoRepository)):
        self.repo_client = repo_client
        self.user_id = user_id
        if not user_id:
            raise Exception('User id not provided')

    def find_all_kudos(self):
        kudos = self.repo_client.find_all({'user_id': self.user_id})
        return [self.dump(kudo) for kudo in kudos]

    def find_kudo(self, repo_id):
        kudo = self.repo_client.find({'user_id': self.user_id, 'repo_id': repo_id})
        return self.dump(kudo)

    def create_kudo(self, github_repo):
        self.repo_client.create(self.prepare_kudo(github_repo))
        return self.dump(github_repo.data)

    def update_kudo(self, repo_id, github_repo):
        kudo = self.repo_client.update({'user_id': self.user_id, 'repo_id': repo_id}, self.prepare_kudo(github_repo))
        return kudo > 0

    def delete_kudo(self, repo_id):
        deleted_kudo = self.repo_client.delete({'user_id': self.user_id, 'repo_id': repo_id})
        return deleted_kudo > 0

    def dump(self, data):
        return KudoSchema(exclude=['_id']).dump(data).data

    def prepare_kudo(self, github_repo):
        data = github_repo.data
        data['user_id'] = self.user_id
        return data