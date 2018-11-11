# BMSTU
## Modeling
* lab1 Моделирование ФПРВ и ФРВ случайных величин
Равномерное и Экспоненциальное распределения.
* lab2 Разработка способа оценки псевдослучайных величин
## WEB
* lab1 Изучение протокола HTTP
    *  1. 	Базовая часть работы

    *  1.1.  Цель данной работы – ознакомится с применением протокола HTTP на практике, в реальных системах. Каждый из рассмотренных типов запросов предлагается отправить на несколько известных интернет-сервисов. Впрочем, сервисы указаны лишь как примеры и при желании вы можете выбрать другие (социальные сети, почта, облака, новостные сайты и т.д.).  

    *  1.2.  С помощью специального ПО (Postman, либо многочисленные аналоги, например, Restlet Clent - расширение для Chrome) вручную отправить следующие запросы и ответить на предлагаемые вопросы.
 

    *  1.2.1.   Запрос OPTIONS. Отправьте запрос на http://mail.ru, http://ya.ru, www.rambler.ru, https://www.google.ru, https://github.com/,   www.apple.com/.
Для чего используется запрос OPTIONS? Какие коды ответов приходят при этом запросе? Какие сайты правильно обработали запрос и вернули ожидаемые данные?
    *  1.2.2.   Запрос HEAD.  vk.com, www.apple.com, www.msn.com.
Для чего нужен запрос HEAD? Какой сайт прислал ожидаемый ответ?
    *  1.2.3.   Запросы GET и POST. Отправьте по запросу на yandex.ru, google.com и apple.com. Что они вернули? Что содержится в теле ответа?
    *  1.3.          Работа с api сайта. Многие крупные сервисы предоставляют открытое api. Как правило, оно реализовано на подходе REST, но это необязательно. Такое api используется сторонними сервисами и приложениями, которые хотят воспользоваться услугами предоставляющего такое api сервиса. Рассмотрим такое api на примере сайта vk.com (при желании можно выбрать другой подходящий сервис).

    *  1.3.1.   Зайдите на https://vk.com/dev/api_requests и посмотрите структуру запросов к данному api.

    *  1.3.2.   Используя документацию (https://vk.com/dev/methods) выполните следующие задания (обратите внимание, запросы нужно отправлять не из предложенной на сайте формы, а как в предыдущем задании):

    *  1.3.2.1.        Получите список всех факультетов МГТУ им. Н.Э.Баумана.

    *  1.3.2.2.        Получите свою аватарку.

    *  1.3.2.3.       Ответьте на вопросы: какой код ответа присылается от api? Что содержит тело ответа? В каком формате и какой кодировке содержаться данные? Какой веб-сервер отвечает на запросы? Какая версия протокола HTTP используется?

    *  1.3.3.  POST запросы проще отправлять с формы, встроенной в документацию api. Чтобы посмотреть, как выглядит запрос, можно воспользоваться панелью разработчика браузера (F12 в Chrome -> вкладка Hetwork).

    *  1.3.3.1.        Отправьте запись на стену любому пользователю/группе и убедитесь, что она пришла. 

    *  1.3.3.2.        Ответьте на вопрос: каким образом передаются данные от пользователя к серверу в POST-запросах?
 

    *  2.       Реализуйте небольшое серверное приложение, с использованием любого фреймворка. Лучшего всего для этой цели подойдет NodeJS: решение получится очень компактным и простым.

    *    Сервер должен содержать предоставлять API с поддержкой (GET, POST, DELETE, PUT, OPTION). Данные отправлять в формате json. Конкретное содержание запросов - на ваше усмотрение. Подключите фантазию. (Можно сделать простейший CRUD-сервис с хранением данных в RAM).


    *  3. Доп. задание. Статика и маршрутизация.


    *  3.1.   Добавьте папку static (классическое название для статически раздаваемой папки).

    *  3.2.   В папке static создайте папки html и img.

    *  3.3.   В папке static/html создайте файл index.html со следующим содержанием (или любым другим):
```
<head></head>
<body>
<h1>Hello, world!</h1>
<img src=”/img/image.jpg”>
</body>
```
 

    *  3.3.   Настройте сервер так, чтобы при запросе из браузера отображалась эта страница.

    *  3.4.          Настройте routing (маршрутизацию) на вашем сервере. Например, чтобы путь /hack тоже отдавал файл index.html, а путь /, по умолчанию отдающий index, выдавал дополнительную страницу hack.html.

    *  3.5.          Переименуйте hack.html (содержащую теги html) в hack.txt. Что изменилось? Почему? Как сделать так, чтобы страница отображалась корректно?

* lab2 Сконфигурировать nginx сервер
* lab3 Разработка архитектуры web приложения
## Computer Networks (+ course work)
## Information Security
## Software Testing And Debuging
* lab1 Модульное и интеграционное тестирование.
    *  Разработать тестовый проект модульного и интеграционного тестирования. Требования : не менее 10 модульных и 5 интеграционных тестов. Обязательно использовать заглушки и Mock – объекты при поведенческом тестировании ( не менее 5 ) . Принцип AAA должен быть продемонстрирован. Nunit, Xunit, Mstests.
    *  Дополнительно, можно использовать технологию TDD. Для интеграционного тестирования интерфейса Web приложения использовать Selenium. При интеграционных тестах с базой данных использовать Fake-объекты. Работа с репозиторием включает тесты на основные операции : добавить, удалить, вставить, выбрать.
* lab2 Регрессионное тестирование.
    *  Подготовить управляющий граф программы ( Control Flow Graph). Программа для тестирования может представлять модуль авторизации. Необходимо построить тестовый вектор и на 5 исправлениях исходного кода показать как провести регрессионное тестирование, не потеряв тестового покрытия. Виды тестового покрытия.
* lab3 Системное и функциональное тестирование.
    *  Необходимо представить спецификацию на ПО и разработать функциональные тесты  исходя из принципа классов эквивалентности и граничных значений. Посчитать покрытие ( использовать различные критерии покрытия). Необходимо не менее 20  тестов. В качестве примера можно взять Web – приложение с использованием MVC.
* lab4 Автоматизированное тестирование.
    *  Написать скрипт для запуска набора тестов. Наборы тестов могут использоваться в многопоточном приложении. 

* Требования:
    * Примеры приложений для тестирования. Приложение может быть одно для выполнения всех лабораторных работ.
    *  1. Диспетчер процессов.
    *  1.1. Программа должна выводить на экран процессы в формате : идентификатор, название, размер, приоритет, количество потоков.
    *  1.2. Удалять процессы из памяти.
    *  1.3. Запускать задачу.
    *  1.4. Отслеживать попытку несанкционированного снятия процесса.
    *  2. Работа с многопоточным приложением.
    *  2.1. Запуск процессов в разных потоках, метод Invoke.
    *  2.2. Продемонстрировать запуск, остановку и выполнение процессов с помощью элемента ProgressBar.
    *  3. Web – приложение с использованием технологии MVC.
    *  3.1 Спроектировать интернет-приложение( интернет-магазин) в виде ORM системы.
При проектировании использовать технологию Code First. В качестве репозитория выбрать EntityFramework или аналогичный программный продукт.
    *  3.2. Сформированная база данных должна иметь не менее 2 таблиц.
    *  3.3. Должны быть реализованы роли системного администратора, пользователя и гостя.
    *  3.4. При использовании технологии MVC нужно показать ее  преимущества или недостатки.
    *  3.5. В отчете должна быть отражена разница между ASP.net и MVC  ASP.net
    *  4. Программа распознавания цифр на основе однослойной нейронной сети (перцептрон Розенблата).
    *  4.1 Обучение проводить с учителем.
    *  5. Продукционный прямой и обратный вывод.
    *  Показать работу на примере определения степени родства.
   
## System programming (driver course work)
