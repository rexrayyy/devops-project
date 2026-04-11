# Небольшой проект для обучения
## Веб-приложение "угадай чиcло"
____
## Стек
- **Python/Flask**
- **Docker**
- **Jenkins**
- **GitHub**
- **pytest**
___

#### Пайплайн

Push - Jenkins - Build - Test - Deploy

___

#### Локальный запуск
 ``` bash 
 docker build -t myapp:1.0 .
 ducker run -d -p 5000:5000 myapp:1.0
 ```

