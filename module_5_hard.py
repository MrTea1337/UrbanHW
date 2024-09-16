from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(cls, nickname, password):
        for user in cls.users:
            if user.nickname == nickname:
                if user.password == hash(password):
                    cls.current_user = user

    def register(cls, nickname, password, age):
        if cls.users == []:
            temp_user = User(nickname, password, age)
            cls.users.append(temp_user)
            cls.current_user = temp_user
            return
        for user in cls.users:
            if user.nickname != nickname or cls.users == []:
                temp_user = User(nickname, password, age)
                cls.users.append(temp_user)
                cls.current_user = temp_user
                return
            elif user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return

    def log_out(cls):
        cls.current_user = None

    def add(cls, *args):
        for new_video in args:
            if cls.videos == []:
                cls.videos.append(new_video)
            else:
                for video in cls.videos:
                    if video.title == new_video.title:
                        break
                    elif video.title != new_video.title:
                        cls.videos.append(new_video)

    def get_videos(cls, user_input):
        video_list = []
        for video in cls.videos:
            if user_input.lower() in video.title.lower():
                video_list.append(video.title)
        return video_list

    def watch_video(cls, user_input):
        for video in cls.videos:
            if video.title == user_input:
                if not cls.current_user:
                    print("Войдите в аккаунт, чтобы смотреть видео")
                elif video.adult_mode is True and cls.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    while video.time_now < video.duration:
                        sleep(1)
                        video.time_now += 1
                        print(video.time_now, end=' ')
                    print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
