import subprocess

args = ['ping', None]
userinput = None

while userinput not in ('1', '2'):
    userinput = input('Что пингуем (1 - , 2 - youtube.com): ')
    if userinput == '1':
        args[1] = 'yandex.ru'
    elif userinput == '2':
        args[1] = 'youtube.com'
    else:
        print('Неверная команда, повторите ввод.')

subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

for line in subproc_ping.stdout:
    print(line.decode('utf-8'))  # на Linux Mint работает в этой кодировке
