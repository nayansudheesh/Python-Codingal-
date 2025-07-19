from abc import ABC, abstractmethod
class Absclass(ABC):

    def print(self , x):
        print("Passed value:", x)

        @abstractmethod
        def task(self):
            print("We are inside a absclass task")
class  test_class(Absclass):
    def task(self):
        print("We are inside a Test_Class task")

test_obj = test_class()
test_obj.task()
test_obj.print(100)
