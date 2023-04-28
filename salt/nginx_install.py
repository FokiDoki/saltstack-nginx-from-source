import os
import sys
import subprocess

if len(sys.argv) != 2:
    print("Неверное количество аргументов")
    print("Пример: python nginx_install.py <clientID>")
    sys.exit(1)

clientID = sys.argv[1]
print("Начинаю установку Nginx для "+clientID)
print("Внимание, прцоесс установки может занять некоторое время...")
process = subprocess.Popen(['sudo', 'salt', clientID, 'state.apply', 'nginx_install'],
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
out = stdout.decode("utf-8")
if stderr:
    print("Ошибка установки "+clientID)
    err = stderr.decode("utf-8")
    print("Логи запишутся в файл /var/log/salt/error.log")
    with open("/var/log/salt/transfer_file.log", "w") as file:
        file.write(err)
        file.write(out)
    print(err)
    print(out)
    sys.exit(1)
print("Перенос установка Nginx для "+clientID+" успешно завершена!")
sys.exit(0)
