from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


class PersonalInfo(Section):
    def describe(self):
        print("describe: personal info")


class Story(Section):
    def describe(self):
        print("describe: stories")
