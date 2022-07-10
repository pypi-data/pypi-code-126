import requests


def tg_send_message(msgs=(), *, token=None, chat_id=None, conf=None, response='bool'):
    """
    Sends message(s) as bot to specified chat

    :param str|[]str msgs: one or more messages to send
    :param str token: bot token, from @BotFather or bot owner
    :param str chat_id: chat id, may belong to a person or chat/group/whatever.
        There are several ways of getting your hands on one, just google it.
    :param {} conf: dict with token and chat_id, just for convenience.
        if both token and/or chat_id and conf args given - conf will be used.
    :param str response: either 'bool' or 'full'.
        bool - returned result will be true if every msg sent successfully, false otherwise
        full - returned result will be list of response objects from requests lib
    :return:
    """

    _token = None
    _chat_id = None

    if token is not None:
        _token = token

    if chat_id is not None:
        _chat_id = chat_id

    if conf is not None:
        _token = conf['token']
        _chat_id = conf['chat_id']

    if _token is None \
            or _chat_id is None:
        raise Exception('No token or chat id! Check your credentials.')

    send_url = f'https://api.telegram.org/bot{_token}/sendMessage'

    res = []

    if isinstance(msgs, str):
        msgs = [msgs]

    for each_msg in msgs:
        res.append(
            requests.post(send_url, json={'chat_id': _chat_id, 'text': each_msg})
        )

    if response == 'full':
        return res
    elif response == 'bool':
        flag = True

        for el in res:
            if not el.ok:
                flag = False
                break

        return flag


def do_tests():
    """
    used for testing before release
    :return:
    """

    token = input("enter token: ")
    chat_id = input("enter chat_id: ")

    return tg_send_message('test message', token=token, chat_id=chat_id, response='full')
