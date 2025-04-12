"""repositories.read_laters.csv_read_later_repository"""
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
from repositories import CsvBaseRepository


class CsvReadLaterRepository(CsvBaseRepository):
    """csv read later repository"""
    CSV_FILE_PATH = "/opt/csv/read_laters.csv"

    KEY_ID = "id"
    KEY_TITLE = "title"
    KEY_URL = "url"
    KEY_CREATE_AT = "create_at"
    HEADER = [KEY_ID, KEY_TITLE, KEY_URL, KEY_CREATE_AT]

    def __init__(self):
        super().__init__(self.CSV_FILE_PATH, self.HEADER)
