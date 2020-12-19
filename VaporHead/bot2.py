# -*- coding: utf-8 -*-
import vk_api, gcm

def captcha_handler(captcha):
    key = gcm.send_captcha(captcha.get_url())

    # Пробуем снова отправить запрос с капчей
    return captcha.try_again(key)

# Авторизация
login, password = '89964020490', 'Wikutorrent21'
vk_session = vk_api.VkApi(
    login, password,
    captcha_handler=captcha_handler  # функция для обработки капчи
)

try:
    vk_session.auth()
except vk_api.AuthError as error_msg:
    print(error_msg)


# def get_liked(post_id):
#     if not check_like(post_id):
#         vk_session.method('likes.add',
#                           {'user_id': 295288929, 'type': 'post', 'owner_id': -193376219, 'item_id': post_id})
#
#
# def check_like(post_id):
#     a = vk_session.method('likes.isLiked',
#                           {'user_id': 295288929, 'type': 'post', 'owner_id': -193376219, 'item_id': post_id})
#     return a['liked']

# Функция отправки коментария
def send_comment(post, comment_text, group=-95908464):
    # get_liked(post)
    try:
        vk_session.method('wall.createComment', {'owner_id': group, 'post_id': post, 'message': comment_text, 'random_id': 0}, captcha_sid=None, captcha_key=None)
    except vk_api.exceptions.Captcha as err:
        print('Отправлен запрос на получение ключа от капчи.')
        key = ''
        if key.lower() == 'стоп':
            exit(-1)
        print('Получен ключ:', key)

        # Обработка неверности ключа капчи
        try:
            vk_session.method('wall.createComment',
                            {'owner_id': group, 'post_id': post, 'message': comment_text, 'random_id': 0},
                            captcha_sid=((err.get_url().split('=')[1])[:-2]), captcha_key=key)
            print('Ключ успешно отправлен.\n' + '-'*100 + '\n')
#               gcm.send_message('Успешно.')
        except:
            print('Произошла ошибка при отправке капчи.\nПерезагрузка.')





