# Get vacancies by API
## Получение данных вакансий с двух порталов:
+ ### HeadHunter.ru
+ ### SuperJob.ru
## Установка зависимостей:
+ ### pip install -r requirements.txt
+ ### poetry add $( cat requirements.txt )
## Использование:
+ ### Исполняемый файл `main` расположен в директории `src`
+ ### При запуске `main` начинается интерактив с пользователем
+ ### Запрашивается ключевое слово для поиска вакансий
+ ### В случае успеха программа предлагает неск-ко вариантов:
  1) #### Вывод списка всех вакансий по убыванию ЗП
  2) #### Вывод топ-10 вакансий
  3) #### Вывода вакансий по желаемой зарплате
  4) #### Начать новый поиск
  5) #### Выход из программы
+ ### Если результат не найден, программа предлагает ввести поисковый запрос заново
## Структура:
+ ### Директория `json` - место сохранения файла вакансий
+ ### `src` - Основной рабочий каталог, содержащий:
  + ### Классы `HeadHunterAPI` и `SuperJobAPI` для работы с API данных порталов на основе абстрактного класса Engine
  + ### Класс `JSONSaver` - читает, записывает данные в файл vacancies.json, получает экземпляры класса `Vacancy` на основе этих данных
  + ### Файл `utils` содержит вспомогательные функции (сортировка вакансий и вывод в консоль)