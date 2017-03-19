
class callObjectAsFunction():
        def __init__(self):
            self.i = 1

        def __call__(self, *args, **kwargs):
                self.i = self.i + 1
                return self.i

obj = callObjectAsFunction()
print(obj()) ## 2
print(obj()) ## 3

