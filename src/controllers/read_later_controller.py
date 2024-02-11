"""read_later controller"""
#########################################################
# Builtin packages
#########################################################
import sys

#########################################################
# 3rd party packages
#########################################################
# (None)

#########################################################
# Own packages
#########################################################
from services import OnetabService


class ReadLaterController(object):
    """onetab controller"""

    def add(self):
        service = OnetabService()
        onetabs = service.get_new_data()
        if not onetabs:
            print("no new onetabe data")
            sys.exit(1)
        service.add(onetabs)
