"""Entry point"""
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
from controllers import ReadLaterController
from common.log import initialize_logger


def main():
    """main"""
    initialize_logger()
    controller = ReadLaterController()
    controller.add()
    # TODO: reads csvを用意して、google spread sheetからデータを取得し、ローカルcsv に同期して、githubで管理する


if __name__ == "__main__":
    main()
