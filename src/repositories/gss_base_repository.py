"""repositories.gss_base_repository"""
#########################################################
# Builtin packages
#########################################################
# (None)

#########################################################
# 3rd party packages
#########################################################
# (None)

#########################################################
# Own packages
#########################################################
from repositories import BaseRepositoryInterface


class GssBaseRepository(BaseRepositoryInterface):
    """gss base repository"""

    def __init__(self):
        pass

    def all(self) -> list:
        pass

    def find_by_id(self, id_: int) -> dict:
        pass

    def add(self, data: dict) -> None:
        pass

    def delete_by_id(self, id_: int) -> None:
        pass
