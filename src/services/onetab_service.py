"""onetab service"""
#########################################################
# Builtin packages
#########################################################
import csv
import sys
# (None)

#########################################################
# 3rd party packages
#########################################################
# (None)

#########################################################
# Own packages
#########################################################
from common.log import (
    info
)
from repositories.read_laters import CsvReadLaterRepository
from repositories.read_laters import GssReadLaterRepository
from utils import get_now_jst


class OnetabService(object):
    """onetab service"""

    ONETAB_FILE_PATH = "/opt/work/src/text/onetabs.txt"
    ERR_400 = ["400 Request Header Or Cookie Too Large"]
    ERR_404 = ["The page you were looking for doesn't exist",
               "404 Not Found - Qiita"]

    def __init__(self):
        self.csv_repo = CsvReadLaterRepository()
        self.gss_repo = GssReadLaterRepository()

    def get_new_data(self) -> list:
        """_summary_

        Returns:
            list: _description_
        """
        onetabs = self.__get_onetab_txt()
        read_laters = self.csv_repo.all()
        try:
            id_ = int(read_laters[-1][self.csv_repo.KEY_ID])
        except IndexError:
            # if there is no data in repo, id is 0
            id_ = 0
        create_at = get_now_jst()

        new_onetabs = []
        for onetab in onetabs:
            # there some "\n" values in texts from onetab and avoid them
            if onetab == "\n":
                continue

            splitted_onetab = onetab.split("|")
            url = splitted_onetab[0].replace("\n", "")
            title = "".join(splitted_onetab[1:]).replace("\n", "").lstrip()

            # sometimes title is error_title which is not legit
            if any(err in title for err in self.ERR_400):
                print(f"break since 400 error. title: {title}, url: {url}")
                sys.exit(1)
            if any(err in title for err in self.ERR_404):
                print(f"skip since 404 error. title: {title}, url: {url}")
                continue
            # skip if duplicated data with onetab
            if any(url == new_onetab["url"] for new_onetab in new_onetabs):
                continue
            # skip if url exists in the csv
            if any(url == read_later["url"] for read_later in read_laters):
                continue

            id_ += 1
            read_later = {
                self.csv_repo.KEY_ID: id_,
                self.csv_repo.KEY_TITLE: title,
                self.csv_repo.KEY_URL: url,
                self.csv_repo.KEY_CREATE_AT: create_at}
            new_onetabs.append(read_later)

        info("new onetabs: {0}", len(new_onetabs))
        return new_onetabs

    @classmethod
    def __get_onetab_txt(cls) -> list:
        """_summary_

        Returns:
            list: _description_
        """
        with open(cls.ONETAB_FILE_PATH, encoding="utf-8") as f:
            onetabs = f.readlines()
            onetabs.reverse()

        return onetabs

    def add(self, onetabs: list) -> None:
        """_summary_
        """
        for onetab in onetabs:
            info("add onetab: {0}", onetab)
            self.csv_repo.add(onetab)
            self.gss_repo.add(onetab)
