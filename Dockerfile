FROM nginx:1.27-alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY index.html about.html team.html careers.html contacts.html \
     freight-brokerage.html managed-transportation.html warehousing.html \
     cross-border.html ship-international.html become-shipper.html become-carrier.html \
     favicon.svg /usr/share/nginx/html/
COPY css /usr/share/nginx/html/css
COPY js /usr/share/nginx/html/js
COPY assets /usr/share/nginx/html/assets

EXPOSE 80
