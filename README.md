# Saltstack nginx from source
## Набор инструкций и скриптов которые позволяют скомпилировать и установить nginx у клиентов 

## Установка


Устанавливаем GPG ключи на сервере и на клиенте
```sh
mkdir /etc/apt/keyrings
```
```sh
wget -O /etc/apt/keyrings/salt-archive-keyring.gpg https://repo.saltproject.io/salt/py3/ubuntu/22.04/amd64/SALT-PROJECT-GPG-PUBKEY-2023.gpg
```
```sh
echo "deb [signed-by=/etc/apt/keyrings/salt-archive-keyring.gpg arch=amd64] https://repo.saltproject.io/salt/py3/ubuntu/22.04/amd64/latest jammy main" | sudo tee /etc/apt/sources.list.d/salt.list
```
```sh
sudo apt update
```
##### Сервер



Устанавливаем Salt-msater
```sh
sudo apt-get install salt-master
```

Настраиваем 
```sh
nano /etc/salt/master.d/network.conf
```

![image](https://user-images.githubusercontent.com/23121394/235133396-dbfa1fe3-fdd3-4c90-a09f-81382c9d8403.png)

Меняем `172.17.96.2` на адрес сервера на котором вы находитесь (Используйте `ip a` чтобы узнать адреса интерфейсов)

Копируем файлы и скрипты
```sh
apt-get install git
cd /tmp
git clone https://github.com/FokiDoki/saltstack-nginx-from-source.git
mv saltstack-nginx-from-source/salt /srv/salt
```

Запускаем Salt-master
```
sudo systemctl enable salt-master && sudo systemctl start salt-master
```

---------------

##### Клиент


Добавляем адрес Salt-master
```sh
nano /etc/salt/minion.d/master.conf
```
![image](https://user-images.githubusercontent.com/23121394/235138078-9702e8d0-1595-4818-8a70-227bea8c3beb.png)
Замените `172.17.96.2` на адрес который указали при настройке salt-master


Устанавливаем id клиента
```sh
nano /etc/salt/minion.d/id.conf
```
![image](https://user-images.githubusercontent.com/23121394/235138511-f0a411d7-583a-423d-aa5b-6faa60945240.png)
Замените `min_1` на желаемое имя
```
sudo systemctl enable salt-minion && sudo systemctl start salt-minion
```

##### Обмен ключами

Чтобы связать клиент и сервер нужно принять ключь от клиента. Для этого `на сервере` напишите следующую команду:
```
salt-key -a min_1
```
Где `min_1` - имя клиента которое вы установили ранеее

### Использование

Во всех командах будет использоваться `min_1` как имя клиента, вам необходимо будет заменить его на своё 
##### Передача установочных файлов

```sh
sudo python3 /srv/salt/nginx_files_send.py min_1
```

##### Установка
```sh
sudo python3 /srv/salt/nginx_install.py min_1
```

##### Подмена файла index.html
```sh
sudo python3 /srv/salt/nginx_index_replace.py min_1
```

