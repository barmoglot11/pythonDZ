# Your Vacancies

## Описание
Данное приложение будет выдавать подходящие соискателю вакансии на выгруженное в приложение резюме.

## Установка и запуск
Установка не требуется. Запуск происходит через `.exe` файл в папке.

## Работа приложения
Пользователь загружает в приложение файл резюме(`.docx` или `.pdf`). 
После этого приложение, найдя соответствие в базе данных по таблице `Cluster`, выводит отнесенные к этому кластеру профессии из таблицы `Vacancies`
Также имеется возможность изменить название кластера[^1] на соответствующей странице. Также можно изменить данные вакансий на странице Профессии.

## Используемые технологии
 - PyQt5
 - PySide6
 - SQLite3
 - QtDesigner
 - Стандартные библиотеки Python

## Сведения об авторах
Группа ИСТ-211
@barmoglot11 Абрамов Данил - Backend-разработка

@shanez4ka Стариков Александр - Frontend-разработка

[^1]: Кластер - это группа названий различных профессий по одному направлению
