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


if __name__ == "__main__":
    main()
