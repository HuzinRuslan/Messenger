Common package
=================================================

Пакет общих утилит, использующихся в разных модулях проекта.

Скрипт errors.py
---------------------

.. automodule:: common.errors
   :members:

Скрипт decos.py
---------------------

.. automodule:: common.decos
   :members:

Скрипт descriptors.py
---------------------

.. automodule:: common.descriptors
   :members:

Скрипт metaclasses.py
---------------------

.. automodule:: common.metaclasses
   :members:

utils.py
---------------------

common.utils. **get_message** (client)


	Функция приёма сообщений от удалённых компьютеров. Принимает сообщения JSON,
	декодирует полученное сообщение и проверяет что получен словарь.

common.utils. **send_message** (sock, message)


	Функция отправки словарей через сокет. Кодирует словарь в формат JSON и отправляет через сокет.


vars.py
---------------------

Содержит разные глобальные переменные проекта.

