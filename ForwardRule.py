from pytg.sender import Sender
from utilities import info


class ForwardRule:
    # RULES

    def __init__(self, from_chat, to_chat, msg_contains=""):
        self._from_chat = from_chat
        self._to_chat = to_chat
        self._msg_contains = msg_contains

    def evaluate(self, telegram_msg):

        if 'text' in telegram_msg and (self._msg_contains in telegram_msg['text'] or self._msg_contains == ""):
            print("msg match")
            if 'sender' in telegram_msg and 'username' in telegram_msg['sender'] and telegram_msg['sender'][
                'id'] == self._from_chat:
                print("FORWARDED")
                sender.fwd(self._to_chat, telegram_msg['id'])

    def __str__(self):
        from_info = info(self._from_chat)
        to_info = info(self._to_chat)
        print(from_info)
        print(to_info)
        return "From " + from_info["print_name"] + " To " + to_info["print_name"]

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self._to_chat == other._to_chat and self._from_chat == other._from_chat


sender = Sender(host="localhost", port=4458)
admin = sender.get_self()
