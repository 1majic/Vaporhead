from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api

token = "74ceaa4450622c8a660be23cd227fc7c572e9553804fb982031821652c02759b896492adfaa3410ff974d"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


def send_message(text):
    vk_session.method('messages.send', {'user_id': 353313939, 'message': str(text), 'random_id': 0})


def send_captcha(text):
    # key = download_img(text)
    # send_message(key)
    # for event in longpoll.listen():
    #     if event.type == VkEventType.MESSAGE_NEW:
    #         return event.text
    #  620608207
   vk_session.method('messages.send', {'user_id': 353313939, 'message': str(text), 'random_id': 0})

   for event in longpoll.listen():
       if event.type == VkEventType.MESSAGE_NEW and event.user_id == 353313939 and event.from_user and not event.from_me:
           return event.text