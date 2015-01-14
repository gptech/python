__author__ = 'jason'
import sys

class MySingleton(object):
    __instance = None
    def __new__(self):
        if not self.__instance:
            self.__instance=super(MySingleton, self).__new__(self)

            self.count=0
        else:
            self.count+=1

        return self.__instance

x = MySingleton()

print(x.count)

x = MySingleton()

print(x.count)

x = MySingleton()

print(x.count)


def main():
    """Main entry point for the script."""

if __name__ == '__main__':
    sys.exit(main())