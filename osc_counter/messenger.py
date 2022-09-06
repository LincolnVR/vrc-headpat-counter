import json

class Messenger:

    def __init__ (self, timer):
        self.timer = timer

    def format_message(self, tracker: dict) -> str:

        message =  ""
        for contact_name in tracker.keys():
            n_ctx = self.format_number(tracker[contact_name]['current_count'])
            message += f"{contact_name.capitalize()}: {n_ctx}, "

        if len(tracker.keys()) >= 1:
            message = message[:-2]
        
        return message

    def format_number(self, number: int) -> str:
        return "{:,}".format(number)

    def has_new_content(self, tracker: dict) -> bool:

        ctx_inc = [False]*len(tracker.keys())

        for n, contact_name in enumerate(tracker.keys()):
            new_ctx = tracker[contact_name]['current_count']
            old_ctx = tracker[contact_name]['last_count']
            ctx_inc[n] = new_ctx > old_ctx
        
        return any(ctx_inc)

