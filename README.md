# Обрезка ссылок с помощью Битли

Скрипт обрезает ссылки с помощью Битли. Если ссылка уже является Bitlink, то выводит количесво переходов по ней.

## Установка

- Скачайте код
- Установите зависимости для работы с проектом

```bash
pip install -r requirements.txt
```

- Зарегестрируйтесь на сайте [Bitly](https://app.bitly.com/Bm5da3Xa4X7/bitlinks/39WUiMU) и получите свой [token](https://app.bitly.com/settings/api/)
- Создайте файд .env и положите в него свой [token](https://app.bitly.com/settings/api/) с названием BITLY_TOKEN. 
Пример содержимого файла .env:
```bash
BITLY_TOKEN=b83315353bd94eabad3n13e0b427ca56ed5k52f7
```


## Запуск

- Запустите скрипт с аргументом

```bash
python main.py ссылка
```
Пример:
```bash
python main.py https://dvmn.org/modules/
```