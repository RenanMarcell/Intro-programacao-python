import os

if __name__ == '__main__':
    os.chdir('files')
    print(os.getcwd())
    os.chdir('..')
    print(os.getcwd())
