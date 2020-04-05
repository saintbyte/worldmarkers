# world markers
Проект на джанго с REST

## Установка
1. git clone https://github.com/saintbyte/worldmarkers.git
2. pip install -r requirements.txt
3. npm install
4. Настроить подключение к базе postgres с postgis
5. ./manage.py migrate
6. установка данных стран
6.1 wget https://thematicmapping.org/downloads/TM_WORLD_BORDERS-0.3.zip
6.2 unzip TM_WORLD_BORDERS-0.3.zip
6.3 ./manage.py import_countries --file="./TM_WORLD_BORDERS-0.3.shp"
7. Установка данных городов
7.1 wget https://download.geonames.org/export/dump/cities15000.zip
7.2 unzip cities15000.zip
7.3 ./manage.py import_towns --file="./cities15000.txt"
8. Связить города и страны
8.1 ./manage.py connect_towns2country
9. Собрать статику
9.1 npm run build
10. Проверить что работает
10.1 ./manage.py runserver

Icons for markers:
Museum icon: https://icons8.com/icons/set/museum--v1 
icon by Icons8 https://icons8.com 