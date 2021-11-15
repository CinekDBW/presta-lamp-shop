# presta-lamp-shop

A Simple online shop with lamps based on Prestashop. 
The whole project is containerized using Docker.
The project was created for Electronic Business classes only for for educational purposes.
The products are the results of web-scraping the shop called [Manufaktura Oświetlenia](https://manufakturaoswietlenia.pl/)

Contributors:
- Maciej
- Patryk
- Radek
- Karol

# Build

To run the app on your local machine:
1. just clone the whole repository
2. build the docker image with command `docker build .` inside your working directory
3. get the image id by `docker images`
4. change the image id in the docker-compose.yaml file at line #18 to contain your image's id
5. run containers by command `docker compose up -d`
6. your app will be deployed on the `https://localhost' and also 'http://localhost:8080' which will redirect you to HTTPS address.
