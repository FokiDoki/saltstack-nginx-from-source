import os
import sys
import subprocess

if len(sys.argv) != 2:
    print("Неверное количество аргументов")
    print("Пример: python nginx_install.py <clientID>")
    sys.exit(1)

clientID = sys.argv[1]
print("Начинаю процесс подмены index.html для "+clientID+ " на index.html из /srv/salt/res/nginx_index.html")
process = subprocess.Popen(['sudo', 'salt', clientID, 'state.apply', 'nginx_index_replace'],
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
out = stdout.decode("utf-8")
if stderr:
    print("Ошибка подмены "+clientID)
    err = stderr.decode("utf-8")
    print("Логи запишутся в файл /var/log/salt/error.log")
    with open("/var/log/salt/transfer_file.log", "w") as file:
        file.write(err)
        file.write(out)
    print(err)
    print(out)
    sys.exit(1)
print("Подмена успешна для "+clientID+"!")
sys.exit(0)
