from sdk.api.message import Message
from sdk.exceptions import CoolsmsException


if __name__ == '__main__':
    api_key = open('apikey').read().strip()
    api_secret = open('apisecret').read().strip()

    params = dict()
    # sms, lms, mms, ata
    params['type'] = 'sms'

    # 문자를 받을 번호
    # 여러개를 보낼땐 ,로 구분
    params['to'] = '01048118411'

    # 발신자 번호
    params['from'] = '01048118411'

    # 메시지
    params['text'] = 'cool sms test message\n한글입력도 되네요.'

    cool = Message(api_key, api_secret)

    try:
        response = cool.send(params)
        print("Success Count :", response['success_count'])
        print("Error Count :", response['error_count'])
        print("Group ID :", response['group_id'])
    except CoolsmsException as e:
        print('Error Code :', e.code)
        print('Error Message :', e.msg)
