class Config:
    def __init__(self, env):

        self.base_url = {
            'dev': 'https://yandex.ru',
            'stage': 'https://google.com',
            'prod': 'https://mcdonalds.ru'
        }[env]