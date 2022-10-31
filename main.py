class Student:

    def __init__(self, name):
        self.name = name
        self.progress = 0
        self.gladness = 50
        self.money = 7
        self.alive = True



    def to_study(self):
        print('Time to study')
        self.progress += 0.5
        self.gladness -= 2

    def to_sleep(self):
        print('Time to sleep')
        self.gladness += 4

    def to_chill(self):
        print('Time to rest')
        self.progress -= 2
        self.gladness += 1
        self.money -= 0.7

    def work(self):
        print('Time to work')
        self.progress += 1
        self.gladness -= 0.1
        self.money += 4



    def nomoney(self):
        print('You have little money, go to work')
        self.progress += 0.5
        self.gladness -= 1
        self.money += 3

    def nostudy(self):
        print('You have not studied in a long time, you need to study')
        self.progress += 0.5
        self.gladness -= 3

    def nochill(self):
        print('You need to get some rest')
        self.progress -= 1.7
        self.gladness += 1
        self.money -= 0.7

    def nosleep(self):
        print('You need to sleep')
        self.gladness += 3



    def is_alive(self):
        if self.progress < -0.5:
            self.alive = False

        elif self.gladness <= 0:
            print('Depression')
            self.alive = False

    def end_of_day(self):
        print(f'Gladness = {self.gladness}')
        print(f'Progress = {self.progress}')




class Cat:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.alive = True

    def sleep(self):
        print('Time to sleep')
        self.gladness += 4

    def eat(self):
        print('Time to eat')
        self.gladness += 2

    def solitude(self):
        print('You are lonely')
        self.gladness -= 3

    def gladness(self):
        if self.gladness == 0:
            play = input('Go to play?')
            if play == 'yes':
                self.gladness += 5
        else:
            self.alive = False