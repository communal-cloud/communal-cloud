FROM nginx:latest

ADD nginx.conf /etc/nginx/nginx.conf

WORKDIR /api/static
RUN chown -R nginx:nginx /api/static
