
"""utils helper"""
#########################################################
# Builtin packages
#########################################################
import datetime

#########################################################
# 3rd party packages
#########################################################
# (None)

#########################################################
# Own packages
#########################################################
# (None)


def get_now_jst():
    """_summary_

    Returns:
        _type_: _description_
    """
    t_delta = datetime.timedelta(hours=9)
    jst = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(jst)
    d = now.strftime('%Y/%m/%d %H:%M:%S')
    return d
