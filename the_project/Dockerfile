FROM nginx

ENV PORT=8088
COPY ./default.conf.template /etc/nginx/templates/
COPY static-html /usr/share/nginx/html
COPY ./start.sh /docker-entrypoint.d/start.sh
