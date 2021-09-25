# LOL-backend
Backend for LOL

# Run project
* docker build . -t lol
* docker run -it --volume "$(PWD)":/code lol django-admin startproject LOL_backend .
* docker run --rm --volume "$(PWD)":/code -p 8000:8000 --name lol lol
* `docker-compose --env-file=./.env.dev up`
* `docker-compose run  web python manage.py migrate`
* `docker-compose run  web python manage.py createsuperuser --email temp@em.ail --user temp`
