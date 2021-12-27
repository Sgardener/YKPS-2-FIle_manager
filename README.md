Лабораторная работа №2 по Управлению качеством программных систем

Для выполнения данной работы были использованы программы: IDE PyCharm, Python 3.8. 
Для выполнения заданий из данной работы, нам нужно будет воспользоваться модулем PyTest. Для того, чтобы его установить, я создаю файл requirements.txt, в который записываю необходимый модуль и его версию, а после уже загружаю модуль нажатием на кнопку "Install requirement":

![image](https://user-images.githubusercontent.com/72302486/147509854-f61b3a5a-c4c1-49ee-8649-a0fbffa3d63e.png)

![image](https://user-images.githubusercontent.com/72302486/147509891-65dca728-403f-4f34-93f2-ddf916df5fe8.png)

Теперь нужно создать папку внутри проекта, в которой будут хранится все тесты, ее обязательное имя – tests. Внутри папки создается файл .py, в котором будет содержаться код тестировки.

![image](https://user-images.githubusercontent.com/72302486/147509934-eb257b01-e5fe-4e27-b8ff-9c04990bd2ff.png)

Чтобы все работало корректно, нужно настроить pytest через конфигурацию. Заходим в изменение конфигураций, выбираем pytest.

Добавляем pytest с помощью иконки "+".

Таким образом, была настроена рабочую область. Теперь добавляем код файлового менеджера "main.py" и дополнительный код с настройками для файлового менеджера "settings.py". Алгоритм тестировки будет проводиться с использованием фикстур, а также тест фикстур:

![image](https://user-images.githubusercontent.com/72302486/147510046-ee06e29a-5d2b-4629-9ed7-71ca866acdf9.png)

![image](https://user-images.githubusercontent.com/72302486/147510055-a3d6cb1c-e2dc-4edd-bbfb-b47853943c41.png)

Суть алгоритма – вернуть значение True в случае положительного прохождения тестов и сравнить ее с предустановленным значением:

![image](https://user-images.githubusercontent.com/72302486/147510074-561b1e66-1ec0-4a42-b234-02eb54b70840.png)

Эти тесты дублирутся в кэше pytest:

![image](https://user-images.githubusercontent.com/72302486/147510094-95dfd750-6c1b-44f4-b402-bb617edf03f0.png)

В качестве вывода можно утверждать, что тестировка программы с помощью pytest очень удобна тем, что ее можно подстраивать под себя как угодно, обобщать тесты, использовать различные декораторы для своих потребностей.
