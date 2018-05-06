from github_manager import GithubManager
from repo_query_params import RepoQueryParams, RepoQueryParamsEnum, RepoSortParamsEnum, RepoQueryParamsOperator

class Crawler:
    def __init__(self):
        self._github_mgr = GithubManager()

    def fetch_repositories_with_stars_greater_than(self, num_stars: int):
        repo_params = RepoQueryParams()
        repo_params\
            .add_range_param(RepoQueryParamsEnum.STARS, 1, num_stars)\
            .add_param(RepoQueryParamsEnum.FORK, RepoQueryParamsOperator.NO_OP, False)

        repos = self._github_mgr.search_repos(repo_params.resolve(), RepoSortParamsEnum.STARS)
        return repos
