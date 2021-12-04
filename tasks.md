1. Подготовка голосования
  1. Создание голосования
    1. Написать название голосования
    2. Вставить список электронных адресов удаленных участников
    3. Отметить примерное количество очных участников
    4. Сохранить
  2. Внесение электронных адресов удаленных участников
    1. Добавить электронные адреса
    2. Сохранить
  3. Добавление примерного количества очных участников
    1. Изменить количество
    2. Сохранить
  4. Генерация ключевых слов голосования
    1. Из списка неназначенных слов взять необходимое количество
    2. Назначить
    3. ИЛИ
    4. Взять последние лишние слова из назначенных
    5. Отменить назначение
  5. Печать памяток для очных участников
    1. Достать все пары ключевых слов для очных участников
    2. Подставить в шаблон памятки
    3. Памятки подставить в шаблон документа
2. Объявление начала голосования
  1. Отправка электронных писем с памятками удаленным участникам
    1. Достать все пары ключевых слов для удаленных участников
    2. Подставить в шаблон памятки
    3. Отправить письма на электронные адреса 
  2. Фиксация не использованных памяток
    1. Отметить количество неиспользованных памяток для очного голосования
    2. Отметить количество отсутствующих удаленных участников
3. Голосование
  1. Получение голоса
    1. Получить СМС, сохранить
    2. Определить тип смс:
      1. Если ЗА, заблокировать бюллетень, перевести бюллетень в состояние ЗА, отправить ответное СМС
      2. Если ПРОТИВ, заблокировать бюллетень, перевести бюллетень в состояние ПРОТИВ, отправить ответное СМС
      3. Иначе, отправить сообщение об ошибке
4. Объявление окончания голосования
  1. Блокировка голосования
  2. Подсчет результатов
    1. Посчитать количество ЗА
    2. Посчитать количество ПРОТИВ
    3. Посчитать количество недействительных = ОБЩЕЕ - ЗА - ПРОТИВ
  3. Печать результатов
    1. Подставить результаты в шаблон документа

## Операторы SMS
- https://sigmasms.ru/priem/
- https://onlinesim.ru/ -- Не подходит, нет автоматизации
- https://www.smsfeedback.ru/priem-sms-na-federalnom-nomere.php -- Только для ЮрЛиц
- https://smsc.ru/tariffs/#phones -- Подходит, отправка только для ЮрЛиц

### TODO
- 
- поставить pypandoc
- отправка писем очень медленная, нужно распараллелить
- Записать настройки в ансибл
- Сделать чтобы все поля показывались
- поставить условия на серверной части кнопок
- поставить условие суперюзер на рестарт клиент|сервер
- построить базовый шаблон для красоты
