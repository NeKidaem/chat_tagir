Docs:
https://centrifugal.github.io/centrifugo/server/configuration/

На Linux:

wget https://github.com/centrifugal/centrifugo/releases/download/v2.1.0/centrifugo_2.1.0_linux_amd64.tar.gz
tar -xzf centrifugo_2.1.0_linux_amd64.tar.gz
./centrifugo genconfig

добавляем в config-file
"admin_password":"123456",
"admin_secret":"secret123456"

Запуск:
./centrifugo

Админка centrifugo доступна на localhost:8000

