"""repositories.csv_base_repository"""
#########################################################
# Builtin packages
#########################################################
import csv
import sys
from dataclasses import dataclass, field


#########################################################
# 3rd party packages
#########################################################
# (None)

#########################################################
# Own packages
#########################################################
from repositories import BaseRepositoryInterface


@dataclass
class CsvBaseRepository(BaseRepositoryInterface):
    """csv base repository"""

    path: str = None
    header: list = field(init=False, default_factory=list)

    def __init__(self, path, header):
        self.path = path
        self.header = header

    def all(self) -> list:
        """get all data from csv

        Returns:
            list: all data from csv
        """
        if not self.__has_header():
            self.__write_header()

        with open(self.path, encoding="utf-8", mode="r") as f:
            reader = csv.DictReader(f)
            all_data = [row for row in reader]
        return all_data

    def find_by_id(self, id_: int) -> dict:
        pass

    def add(self, data: dict) -> None:
        """add data into the csv file

        Args:
            data (dict): data to add
        """
        if not self.__has_header():
            self.__write_header()

        with open(self.path, encoding="utf-8", mode="a") as f:
            writer = csv.DictWriter(f, fieldnames=self.header)
            writer.writerow(data)

        print(f"added data in the csv file({self.path}).")

    def delete_by_id(self, id_: int) -> None:
        pass

    def __has_header(self) -> bool:
        """check the csv file has header or not

        Returns:
            bool: the csv file has header or not
        """
        with open(self.path, encoding="utf-8", mode="r") as f:
            reader = csv.DictReader(f)

            header = reader.fieldnames
            if header is None:
                print(f"header is None in the csv file({self.path}).")
            elif header != self.header:
                print(f"invalid header in the csv file({self.path}): {header}, expected header: {self.header}")
                sys.exit(1)

        return bool(header)

    def __write_header(self) -> None:
        """write header
        """
        with open(self.path, encoding="utf-8", mode="w") as file:
            writer_ = csv.DictWriter(file, fieldnames=self.header)
            writer_.writeheader()
            print(f"write header in the csv file({self.path}). header: {self.header}")
