<<<<<<< HEAD
# lab2

### Часто используемые команды

```bash
sudo nginx

sudo nginx -t

sudo ngins -s stop

sudo /etc/init.d/nginx restart

uwsgi --socket labs.sock --wsgi-file wsgi.py --chmod-socket=666

uwsgi --http :8000 --wsgi-file wsgi.py

sudo nginx -V 2>&1 | grep -o with-http_stub_status_module

```


|Контент|Время отдачи |
|---|---|
|Cтраница| 33 ms |
|Картинка| 61 ms |
|API (GET)| 111 ms |
|API (POST)| 40 ms |
|API (DELETE)| 35 ms|
|API (PUT)| 42 ms |
|API (OPTION)| 51 ms |
|API (HEAD)| 13 ms |

### Сервер из лабораторной работы 1

```bash
(venv) savital@savital-VM:~/repos/BMSTU/WEB/labs$ ab -c 10 -n 100 http://localhost:8000/
This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        WSGIServer/0.2
Server Hostname:        localhost
Server Port:            8000

Document Path:          /
Document Length:        3216 bytes

Concurrency Level:      10
Time taken for tests:   0.704 seconds
Complete requests:      100
Failed requests:        0
Total transferred:      356900 bytes
HTML transferred:       321600 bytes
Requests per second:    141.98 [#/sec] (mean)
Time per request:       70.434 [ms] (mean)
Time per request:       7.043 [ms] (mean, across all concurrent requests)
Transfer rate:          494.84 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       0
Processing:     6   68  19.0     69     115
Waiting:        5   61  16.4     63     103
Total:          6   68  19.0     69     115

Percentage of the requests served within a certain time (ms)
  50%     69
  66%     76
  75%     82
  80%     83
  90%     91
  95%    102
  98%    109
  99%    115
 100%    115 (longest request)

```


### После добавления nginx + uwsgi

|Контент|Время отдачи |
|---|---|
|Cтраница| 31 ms |
|Картинка| 21 ms |
|API (GET)| 89 ms |
|API (POST)| 33 ms |
|API (DELETE)| 21 ms|
|API (PUT)| 36 ms |
|API (OPTION)| 42 ms |
|API (HEAD)| 11 ms |

```bash
(venv) savital@savital-VM:~/repos/BMSTU/WEB/labs$ ab -c 10 -n 100 http://localhost:8000/
This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        nginx/1.14.0
Server Hostname:        localhost
Server Port:            8000

Document Path:          /
Document Length:        3216 bytes

Concurrency Level:      10
Time taken for tests:   0.348 seconds
Complete requests:      100
Failed requests:        0
Total transferred:      358000 bytes
HTML transferred:       321600 bytes
Requests per second:    287.51 [#/sec] (mean)
Time per request:       34.781 [ms] (mean)
Time per request:       3.478 [ms] (mean, across all concurrent requests)
Transfer rate:          1005.16 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.2      0       1
Processing:     4   33   5.4     34      38
Waiting:        4   33   5.4     34      38
Total:          5   33   5.2     34      38

Percentage of the requests served within a certain time (ms)
  50%     34
  66%     34
  75%     35
  80%     35
  90%     36
  95%     37
  98%     38
  99%     38
 100%     38 (longest request)

```
=======
# Отчет по лабораторной работе №3
# Курс: "WEB"
# Тема: "Сконфигурировать nginx сервер"

Цель - оценить как изменятся качественные показатели работы веб-сервера после добавления фронтенд-сервера

1.	Замерить скорость отдачи контента на сервере отдача страниц, картинки, запросов к api. Добавить логирование приходящих запросов.

2.	Сконфигурировать nginx сервер таким образом, чтобы запросы проходили через nginx и перенаправлялись на сервер.

3.	Использовать nginx для отдачи статического контента.

4.	Настройте кеширование и gzip сжатие файлов. Оценить время ответа.

5.	Запустите дополнительные 2 инстанса сервера, настроить перенаправление таким образом, чтобы на серверы приходили запросы в соотношении 3:1.

6.	 Написать допольнительные 2 мини-сервера. Каждый из них должен обрабатывать два GET-запроса.
a.	по / отдавать страницу с надписью “Добро пожаловать на сервис #1/#2” и ссылкой, ведущей на /temp
b.	по /temp  возвращать произвольный контент
Настройте nginx так, чтобы в дополнение к п.1-5 он перенаправлял запросы по     url /service1 и /service2 на соответствующие сервера.

7.	Настроить отдачу страницы о состоянии сервера

Дополнительные задания:

1.	Настроить https порт на сервере nginx. Использовать самоподписанный сертификат.

2.	Добавить ServerPush картинки для страницы index.html. Оценить время ответа сервера и время загрузки страницы.

3.	Скрыть все заголовки Server (nginx можно оставить) из header ответа, а также дополнительные заголовки, которые дописывает сервер, если есть.
>>>>>>> master
