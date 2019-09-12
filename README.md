Дисклеймер: Этот джупитер ноутбук, а также модули vkparser и myplots были созданы единственно с целью появления на гитхабе минимального демонстрационного куска кода. 

# MyVKParser

Идея: посмотреть на стату по друзьям некоторого пользователя: пол, возраст, ВУЗы.
Класс MyVKParser позволяет подключиться к API ВКонтакте и получить общую информацию по друзьям выбранного пользователя для сбора статистики.

## Структура
* [Parsing VK friends list.ipynb](https://github.com/bendiwise/My-VK-Parser/blob/master/Parsing%20VK%20friends%20list.ipynb) - пример использования MyVKParser: подключение к ВК, получение информации по друзьям, графики.
* [vkparser.py](https://github.com/bendiwise/My-VK-Parser/blob/master/vkparser.py) - модуль, содержащий класс MyVKParser
* [myplots.py](https://github.com/bendiwise/My-VK-Parser/blob/master/myplots.py) - графические инструменты (на самом деле там всего одна функция, но не суть)

## Сторонние библиотеки

* [vk_api](https://github.com/python273/vk_api) - инструменты подключения к API Вконтакте
* [seaborn](https://seaborn.pydata.org/) - графики
