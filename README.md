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
    *  1.3.2.3. Ответьте на вопросы: какой код ответа присылается от api? Что содержит тело ответа? В каком формате и какой кодировке содержаться данные? Какой веб-сервер отвечает на запросы? Какая версия протокола HTTP используется?
    *  1.3.3. POST запросы проще отправлять с формы, встроенной в документацию api. Чтобы посмотреть, как выглядит запрос, можно воспользоваться панелью разработчика браузера (F12 в Chrome -> вкладка Hetwork).
    *  1.3.3.1. Отправьте запись на стену любому пользователю/группе и убедитесь, что она пришла. 
    *  1.3.3.2. Ответьте на вопрос: каким образом передаются данные от пользователя к серверу в POST-запросах?
    *  2. Реализуйте небольшое серверное приложение, с использованием любого фреймворка. Лучшего всего для этой цели подойдет NodeJS: решение получится очень компактным и простым.
    * Сервер должен содержать предоставлять API с поддержкой (GET, POST, DELETE, PUT, OPTION). Данные отправлять в формате json. Конкретное содержание запросов - на ваше усмотрение. Подключите фантазию. (Можно сделать простейший CRUD-сервис с хранением данных в RAM).
    *  3. Доп. задание. Статика и маршрутизация.
    *  3.1. Добавьте папку static (классическое название для статически раздаваемой папки).
    *  3.2. В папке static создайте папки html и img.
    *  3.3. В папке static/html создайте файл index.html
    *  3.3. Настройте сервер так, чтобы при запросе из браузера отображалась эта страница.
    *  3.4. Настройте routing (маршрутизацию) на вашем сервере. Например, чтобы путь /hack тоже отдавал файл index.html, а путь /, по умолчанию отдающий index, выдавал дополнительную страницу hack.html.
    *  3.5. Переименуйте hack.html (содержащую теги html) в hack.txt. Что изменилось? Почему? Как сделать так, чтобы страница отображалась корректно?

* lab2 Сконфигурировать nginx сервер
    *  В данной работе вам будет необходимо оценить как изменятся качественные показатели работы веб-сервера после добавления фронтенд-сервера, для этого предлагается воспользоваться утилитой для тестирования сервера: ApacheBenchmark
    *  Замечание. При использовании AB не стоит допускать деградации производительности сервера. Также предлагается изначально зафиксировать общее количество запросов и количество конкурентных запросов для утилиты AB. 
    *  Результаты оформить в виде отчёта .md.
    *  Код и конфигурацию nginx разместить в репозитории в папке lab2.
    *  1.	Замерьте скорость отдачи контента на сервере из лабораторной работы №1 (отдача страниц, картинки, запросов к api). Добавьте логирование приходящих запросов.
    *  a.	django logger
    *  b.	express logger (middleware)
    *  c.	C# NLog
    *  2.	Сконфигурируйте nginx сервер таким образом, чтобы запросы проходили через nginx и перенаправлялись на сервер из лабораторной работы №1.
    *  a.	Гайд для начинающих
    *  3.	Используйте nginx отдачи статического контента. Как изменилось время ответа сервера?
    *  4.	Настройте кеширование и gzip сжатие файлов.  Как изменилось время ответа сервера?
    *  a.	Настройка gzip сжатия
    *  b.	Гайд по настройке кеширования
    *  5.	Запустите еще 2 инстанса вашего сервера из лабораторной работы №1, настройте перенаправление таким образом, чтобы на серверы приходили запросы в соотношении 3:1. 
    *  a.	Гайд по настройке балансировки.
    *  6.	 Напишите еще два мини-сервера. Каждый из них должен обрабатывать два GET-запроса.
    *  a.	по / отдавать страницу с надписью “Добро пожаловать на сервис #1/#2” и ссылкой, ведущей на /temp
    *  b.	по /temp  возвращать произвольный контент
    *  Настройте nginx так, чтобы в дополнение к п.1-5 он перенаправлял запросы по     url /service1 и /service2 на соответствующие сервера. 
    *  7.	Настройте отдачу страницы о состоянии сервера
    *  a.	nginx status
    *  Дополнительные задания:
    *  1.	Настройте https порт на сервере nginx. Используйте самоподписанный сертификат. (Создание сертификата)
    *  2.	Добавьте ServerPush картинки для страницы index.html. Как изменилось время ответа сервера и загрузки страницы?
    *  3.	Для повышения уровня безопасности необходимо скрывать внутреннюю реализацию вашего сервера. Скройте все заголовки Server (nginx можно оставить) из header ответа, а также дополнительные заголовки, которые дописывает ваш сервер, если есть.

* lab3 Разработка архитектуры web приложения
    *  Задача: Вам необходимо разбиться на пары по 2 человека (большее количество людей возможно только при доказательстве сложности проекта и согласовании с преподавателями). Разработка данного проекта планируется на протяжении всего семестра. В данной лабораторной работе необходимо спланировать архитектуру разрабатываемого приложения.

    *  Замечание: приложение должно включать frontend и backend(возможно с базой), запрещается в качестве frontend использовать vk или tg ботов.


    *  Для сдачи лабораторной работы необходимо предоставить отчет в виде .md файла в репозитории. Отчет может включать изображения, по-возможности используйте векторные (либо растр с хорошим сжатием без потерь: png).


    *  1.	Название проекта

    *  2.	Краткое описание проблемной области и актуальности

    *  a.	Какая проблема

    *  b.	Как решаем

    *  3.	Описание ролей пользователя

    *  a.	Use-Case диаграмма (основные кейсы)

    *  b.	Назначение ролей пользователя

    *  4.	Сущности предметной области

    *  a.	ER-диаграмма сущностей

    *  5.	Прототип интерфейса (sketch) со всеми страницами. (Можно использовать MockFlow  или любой другой специализированный инструмент, paint/photoshop, салфетку и карандаш). Краткое описание основных функциональных действий.

    *  6.	Архитектура приложения

    *  a.	Выбор архитектуры (MPA-SPA)

    *  b.	Диаграмма взаимодействия Backend-Frontend

    *  c.	Описание протокола взаимодействия Backend-Frontend / Rest API - при наличии 

    *  d.	Структура модулей/классов для Backend и Frontend

    *  7.	Техническое решение

    *  a.	Выбор Backend- и Frontend-стеков


    *  Требования к приложению.

    *  1.	Минимум - 3 экрана с данными. Т.е. экран - это не просто html ”об авторе”. А вполне целостная страница, со списком каких-нибудь данных. Пример такого приложения: Интернет магазин (страница списка товаров, детальный просмотр товара, корзина)

    *  2.	На каждом экране должна быть минимум одна пользовательская активность (кроме пассивного просмотра информации). Продолжая пример с интернет-магазином: Поиск товара и добавление в корзину на списке товаров, Добавление в корзину при детальном просмотре, Покупка в корзине.

    *  3.	В проекте должны быть данные. Это могут быть данные, хранящиеся в виде файлов в файловом хранилище, может быть SQL/NoSQL база данных, может быть внешняя система, с которой ваш проект взаимодействует по некому API (например, vk, twitter и т.д.).

    *  4.	Тема - может быть абсолютно любой. Темы можно обсуждать в телеграме. Если будет кризис идей - пишите. Что-нибудь придумаем ;)


## Computer Networks (+ course work)
* lab1 UDP Sockets
* lab2 TCP Sockets
* lab3 UDP File

## Information Security
* lab1 
    *  Protect program from unauthorised access using CPUID check. This program should be done in two parts: first is the installer which contains license calculating, the second part is the "program" itself, which is basically a sum check.
    *  ./installer binary generates a license file based on md5 hash of /proc/cpuinfo (system-profiler in macOS case) which is to be placed into the same directory with the ./program binary.
    *  ./program binary generates the current cpuinfo md5 hash and compares it with the same of the file.
* lab2 Engima
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
