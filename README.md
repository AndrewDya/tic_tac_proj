# Крестики-нолики

Это простая реализация игры "Крестики-нолики" на языке Python. Игра позволяет двум игрокам соревноваться друг с другом, ставя крестики и нолики на игровом поле. Целью игры является заполнение горизонтальной, вертикальной или диагональной линии из трех одинаковых символов.

## Инструкции

1. Установите Python, если у вас его нет.
2. Запустите файл `main.py` для начала игры.
3. Игроки по очереди вводят номера клеток, чтобы сделать ход.
4. Первый игрок использует символ "X", а второй игрок - символ "O".
5. Если один из игроков собирает три своих символа в ряд, он побеждает.
6. Если все клетки на поле заполнены и победителя нет, игра заканчивается вничью.
7. После окончания игры вы можете выбрать, хотите ли вы сыграть еще раз.

## Описание классов

1. **Cell** - представляет клетку на игровом поле. Содержит атрибуты `number` (номер клетки), `is_occupied` (занята ли клетка) и `symbol` (символ, который клетка хранит). Метод `occupy` используется для занятия клетки символом.

2. **Board** - представляет игровое поле. Содержит список объектов `Cell`. Метод `display` выводит текущее состояние поля на экран.

3. **Player** - представляет игрока. Содержит атрибуты `name` (имя игрока) и `wins` (количество побед игрока). Метод `make_move` запрашивает у игрока номер клетки для хода.

4. **Game** - управляет процессом игры. Содержит объекты `Board` и двух игроков. Метод `start_game` осуществляет ходы игроков и проверяет наличие победителя или ничью. Метод `check_win` проверяет, выполнено ли условие победы. Метод `play_game` запускает игру и обрабатывает раунды. Метод `print_score` выводит текущий счет игроков. Метод `play_again` запрашивает у игроков, хотят ли они сыграть еще раз.

## Расширения

Вы можете расширить игру, добавив следующие функции:

- Добавьте возможность игры против компьютера.
- Реализуйте визуализацию игрового поля с помощью графического интерфейса пользователя (GUI).
- Добавьте режим сетевой игры, позволяющий играть с другими игроками по сети.

Приятной игры!