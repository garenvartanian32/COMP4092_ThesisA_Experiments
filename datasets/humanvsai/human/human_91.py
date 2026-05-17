def win_set_trans(title, trans, **kwargs):
    text = kwargs.get("text", "")
    ret = AUTO_IT.AU3_WinSetTrans(LPCWSTR(title), LPCWSTR(text), INT(trans))
    return ret