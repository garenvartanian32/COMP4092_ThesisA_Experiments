def construct_IncomingPhoneNumberContext(sid):
    return twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberContext(sid)
