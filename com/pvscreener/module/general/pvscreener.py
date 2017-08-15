# coding=utf-8
from sys import stdin
import sys
import __builtin__


class PVscreener(object):
    # Переменная для проверки авторизации:
    __builtin__.AUTH = False

    # Инициализируем систему (точка входа):
    def __init__(self):
        # Временный ассоциативный массив для авторизации.
        # В перспективе - целый модуль или класс безопасности.
        self.users = { "alexandr" : "p10V-scr", "tohrul" : "ee4n3r"}
        print('Hi :) Welcome to PVscreener!' + '\n')

        print('Please enter your login: ')
        username = stdin.readline()
        # we use strip because readline()
        # grabs a newline character
        username = username.strip()
#        print('You entered %s' % username)

        print('\n' + 'Now please enter your password: ')
        password = stdin.readline()
        password = password.strip()
#        print('You entered %s' % password)

        self.authenticate(username, password, self.users)

        # Считываем команду и обрабатываем её:
        command = ''
        while command != 'exit':
            print('\n' + 'Enter command:')
            command = stdin.readline()
            command = command.strip()
            self.processCommand(command)

    # Логика аутентификации пользователей:
    def authenticate(self, username, password, usersList):
        isInBase = username in usersList
        passMatch = usersList.get(username, 0)

        if isInBase:
            if passMatch == password:
                __builtin__.AUTH = True
                print('\n' + 'Authentication successful!')
                return

        print('\n' + 'Authentication failed!')
        sys.exit()

    # Логика для обработки различных комманд:
    # 1. Операции поиска и фильтрации данных.
    # 2. Операции импорта и обработки данных.
    # 3. Генерация моделей и получение результатов.
    def processCommand(self, command):
        if command != 'exit':
            print('Sorry! This command is not supported.')
            return


pv = PVscreener()