import twilio
from twilio.rest import Client

class MyClass:
    def __init__(self):
        self.client = Client("your_account_sid", "your_auth_token")

    def get(self, sid):
        """Constructs a IncomingPhoneNumberContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberContext
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberContext"""

        return self.client.api.v2010.account.incoming_phone_number.IncomingPhoneNumberContext(sid)