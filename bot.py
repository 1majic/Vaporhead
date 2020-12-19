import vk_api, codecs, gcm, bot2
from time import sleep
from random import randint

# Авторизация
def captcha_handler(captcha):
    key = gcm.send_captcha(captcha.get_url())

    # Пробуем снова отправить запрос с капчей
    return captcha.try_again(key)

login, password = '89964020490', 'Wikutorrent21'
vk_session = vk_api.VkApi(
    login, password, token='c03ed8423b7acb42ea464d97f7f07991b634e430efc029a7ca3562b98e867ab787203721614d3dc31f400',
    captcha_handler=captcha_handler  # функция для обработки капчи
)

# Загрзка файла и работа с ним
with codecs.open('hokku.txt', encoding='utf-8') as text:
    # def check_like(post_id):
    #     a = vk_session.method('likes.isLiked',
    #                           {'user_id': 353313939, 'type': 'post', 'owner_id': -193376219, 'item_id': post_id})
    #     return a['liked']
    #
    #
    # def get_liked(post_id):
    #     if not check_like(post_id):
    #         sleep(4)
    #         vk_session.method('likes.add',
    #                           {'user_id': 353313939, 'type': 'post', 'owner_id': -193376219, 'item_id': post_id})



    # Функция отправки коментария
    def send_comment(post, comment_text, group=-92597394):
        # get_liked(post)
        try:
            vk_session.method('wall.createComment',
                              {'owner_id': group, 'post_id': post, 'message': comment_text, 'random_id': 0})
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
                print('Ключ успешно отправлен.\n' + '-' * 100 + '\n')
            #               gcm.send_message('Успешно.')
            except:
                print('Произошла ошибка при отправке капчи.\nПерезагрузка.')


    k = ''
    for i in text:
        # Нахождение последнего поста
        try:
            # all_wall = (vk_session.method('wall.get', {'owner_id': -193376219, 'count': 2})).values()
            # last_post_id = (list(list(all_wall)[1])[1])['id']
            last_post_id = 451402
        except:
            pass
            # all_wall = (vk_session.method('wall.get', {'owner_id': -193376219, 'count': 2})).values()
            # last_post_id = (list(list(all_wall)[1])[1])['id']

        if i == '\r\n':
            send_comment(last_post_id, k)
            k = ''
        else:
            k += i

        sleep(0.5 + (randint(1, 23) / 10))

gcm.send_message('Достигнут конец файла')
print('Достигнут конец файла')