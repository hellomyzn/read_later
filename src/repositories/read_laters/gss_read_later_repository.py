"""repositories.read_laters.gss_read_later_repository"""
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
from repositories import GssBaseRepository


class GssReadLaterRepository(GssBaseRepository):
    """gss read later repository"""

    SHEET_NAME = "read laters"

    KEY_ID = "id"
    KEY_TITLE = "title"
    KEY_URL = "url"
    KEY_CREATE_AT = "create_at"
    KEY_READ = "read"
    KEY_READ_AT = "read_at"
    COLUMNS = [KEY_ID, KEY_TITLE, KEY_URL, KEY_CREATE_AT, KEY_READ, KEY_READ_AT]

    def __init__(self):
        super().__init__(self.SHEET_NAME, self.COLUMNS)
