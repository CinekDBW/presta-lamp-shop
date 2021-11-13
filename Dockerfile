FROM prestashop/prestashop:latest

RUN rm -rf /var/www/html/*
COPY ./html /var/www/html
RUN chmod -R 777 /var/www/html

COPY ./config/apache-selfsigned.key /etc/ssl/private/apache-selfsigned.key
COPY ./config/apache-selfsigned.crt /etc/ssl/certs/apache-selfsigned.crt

COPY ./config/php.ini /usr/local/etc/php/php.ini

COPY ./config/ssl-params.conf /etc/apache2/conf-available/ssl-params.conf
COPY ./config/default-ssl.conf /etc/apache2/sites-available/default-ssl.conf
COPY ./config/000-default.conf /etc/apache2/sites-available/000-default.conf

RUN a2enmod ssl
RUN a2enmod headers
RUN a2ensite default-ssl
RUN a2enconf ssl-params
RUN echo apache2ctl configtest
RUN service apache2 restart
