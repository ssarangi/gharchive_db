from github import Github, GithubObject
from env import GITHUB_ACCESS_TOKEN
from repo_query_params import RepoQueryParams, RepoSortParamsEnum

class GithubManager:
    def __init__(self):
        self._github_client = Github(GITHUB_ACCESS_TOKEN)

    def search_repos(self, repo_params: RepoQueryParams, sort_param: RepoSortParamsEnum):
        repos = self._github_client.search_repositories(repo_params, sort_param.STARS.name.lower())
        for page in range(repos.totalCount):
            page = repos.get_page(page)
            print(page)
        return repos