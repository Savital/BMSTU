# Тестирование и отладка программного обеспечения
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
