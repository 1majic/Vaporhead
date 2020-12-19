import vk_api, codecs, gcm
from time import sleep
from random import randint


class Main:
    def __init__(self, login, password, token, file_path, post_id, group_id, user_id, sleep_time):
        self.login = login
        self.password = password
        self.token = token
        self.vk_session = ''

        self.file_path = file_path

        self.post_id = post_id
        self.group_id = group_id
        self.user_id = user_id

        self.sleep_time = sleep_time

    def check_like(self):
        a = self.vk_session.method('likes.isLiked',
                                  {'user_id': 353313939, 'type': 'post', 'owner_id': self.group_id, 'item_id': self.post_id})
        return a['liked']

    def get_liked(self):
        if not self.check_like():
            self.vk_session.method('likes.add',
                                   {'user_id': 353313939, 'type': 'post', 'owner_id': self.group_id, 'item_id': self.post_id})

    def captcha_handler(self, captcha):
        key = gcm.send_captcha(captcha.get_url())

        # Пробуем снова отправить запрос с капчей
        return captcha.try_again(key)

    def autorization(self):
        self.vk_session = vk_api.VkApi(
            login=self.login, password=self.password, token=self.token,
            captcha_handler=self.captcha_handler
        )

    def send_comment(self, post, comment_text, group):
        try:
            self.vk_session.method('wall.createComment',
                              {'owner_id': group, 'post_id': post, 'message': comment_text, 'random_id': 0},
                              captcha_sid=None, captcha_key=None)
        except vk_api.exceptions.Captcha as err:
            print('Отправлен запрос на получение ключа от капчи.')
            key = ''
            if key.lower() == 'стоп':
                exit(-1)
            print('Получен ключ:', key)

            # Обработка неверности ключа капчи
            try:
                self.vk_session.method('wall.createComment',
                                  {'owner_id': group, 'post_id': post, 'message': comment_text, 'random_id': 0},
                                  captcha_sid=((err.get_url().split('=')[1])[:-2]), captcha_key=key)
                print('Ключ успешно отправлен.\n' + '-' * 100 + '\n')
            #               gcm.send_message('Успешно.')
            except:
                print('Произошла ошибка при отправке капчи.\nПерезагрузка.')

    def main(self):
        # Загрзка файла и работа с ним
        with codecs.open(self.file_path, encoding='utf-8') as text:
            for i in text:
                k = i[::]
                self.send_comment(post=self.post_id, comment_text=k, group=self.group_id)
            sleep(self.sleep_time + (randint(1, 30) / 10))

        gcm.send_message('Достигнут конец файла')
        print('Достигнут конец файла')