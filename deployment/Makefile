export COMPOSE_PROJECT_NAME=ford3
export COMPOSE_FILE=docker-compose.yml$(shell if [ -f docker-compose.override.yml ]; then echo ":docker-compose.override.yml"; fi):scripts/travis/selenium-compose.yml
export ANSIBLE_PROJECT_SETUP_DIR=ansible

SHELL := /bin/bash

# ----------------------------------------------------------------------------
#    S E T U P     C O M M A N D S
# ----------------------------------------------------------------------------

ansible-check:
	@echo "Check ansible command"
	@ansible -i ${ANSIBLE_PROJECT_SETUP_DIR}/development/hosts all -m ping
	@ansible-playbook -i ${ANSIBLE_PROJECT_SETUP_DIR}/development/hosts ${ANSIBLE_PROJECT_SETUP_DIR}/development/site.yml --list-tasks --list-hosts $(ANSIBLE_ARGS)

setup-ansible:
	@echo "Setup configurations using ansible"
	@ansible-playbook -i ${ANSIBLE_PROJECT_SETUP_DIR}/development/hosts ${ANSIBLE_PROJECT_SETUP_DIR}/development/site.yml $(ANSIBLE_ARGS)

# ----------------------------------------------------------------------------
#    P R O D U C T I O N     C O M M A N D S
# ----------------------------------------------------------------------------
default: web
run: build permissions web migrate collectstatic

build:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Building in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose build base_uwsgi
	@docker-compose build uwsgi

web:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose up -d web
	@# Dont confuse this with the dbbackup make command below
	@# This one runs the postgis-backup cron container
	@# We add --no-recreate so that it does not destroy & recreate the db container
	@docker-compose up --no-recreate --no-deps -d dbbackups
	@docker-compose up -d btsync-db
	@docker-compose up -d btsync-media

up: web
	# Synonymous with web

down:
	@docker-compose down

permissions:
	# Probably we want something more granular here....
	# Your sudo password will be needed to set the file permissions
	# on logs, media, static and pg dirs
	@if [ ! -d "logs" ]; then mkdir logs; fi
	@if [ ! -d "media" ]; then mkdir media; fi
	@if [ ! -d "static" ]; then mkdir static; fi
	@if [ ! -d "backups" ]; then mkdir backups; fi
	@if [ -d "logs" ]; then sudo chmod -R a+rwx logs; fi
	@if [ -d "media" ]; then sudo chmod -R a+rwx media; fi
	@if [ -d "static" ]; then sudo chmod -R a+rwx static; fi
	@if [ -d "pg" ]; then sudo chmod -R a+rwx pg; fi
	@if [ -d "backups" ]; then sudo chmod -R a+rwx backups; fi

db:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running db in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose up -d db

wait-for-db:
	@docker-compose exec dbbackups /bin/bash -c "until psql -l -d gis; do echo 'Waiting for databases.'; sleep 5; done"

generate-django-secret:
	@echo "Generating Django Secret Key"
	@docker-compose exec uwsgi /bin/bash -c "echo -e \"from core.settings.utils import ensure_secret_key_file\\nensure_secret_key_file()\" | python manage.py shell"

nginx:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running nginx in production mode"
	@echo "Normally you should use this only for testing"
	@echo "In a production environment you will typically use nginx running"
	@echo "on the host rather if you have a multi-site host."
	@echo "------------------------------------------------------------------"
	@docker-compose up -d nginx
	@echo "Site should now be available at http://localhost"

migrate:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running migrate static in production mode"
	@echo "------------------------------------------------------------------"
	@#http://stackoverflow.com/questions/29689365/auth-user-error-with-django-1-8-and-syncdb-migrate
	@#and
	@#http://stackoverflow.com/questions/3143635/how-to-ignore-mv-error
	@# We add the '-' prefix to the next line as the migration may fail
	@# but we want to continue anyway.
	@#We need to migrate accounts first as it has a reference to user model
	-@docker-compose exec uwsgi python manage.py migrate auth
	@docker-compose exec uwsgi python manage.py migrate

update-migrations:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running update migrations in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose exec uwsgi python manage.py makemigrations

collectstatic:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Collecting static in production mode"
	@echo "------------------------------------------------------------------"
	#@docker-compose run uwsgi python manage.py collectstatic --noinput
	#We need to run collect static in the same context as the running
	# uwsgi container it seems so I use docker exec here
	# no -it flag so we can run over remote shell
	@docker-compose exec uwsgi python manage.py collectstatic --noinput

reload:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Reload django project in production mode"
	@echo "------------------------------------------------------------------"
	# no -it flag so we can run over remote shell
	@docker-compose exec uwsgi uwsgi --reload  /tmp/django.pid

status:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Show status for all containers"
	@echo "------------------------------------------------------------------"
	@docker-compose ps

kill:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Killing in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose kill
	@docker-compose kill btsync-db
	@docker-compose kill btsync-media

rm: dbbackup rm-only


rm-only: kill
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Removing production instance!!! "
	@echo "------------------------------------------------------------------"
	@docker-compose rm

logs:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Showing uwsgi logs in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose logs -f --tail=50 uwsgi

dblogs:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Showing db logs in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose logs -f --tail=50 db

nginxlogs:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Showing nginx logs in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose logs -f --tail=50 web

shell:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Shelling in in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose exec uwsgi /bin/bash

superuser:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Creating a superuser in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose exec uwsgi python manage.py createsuperuser

dbbash:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Bashing in to production database"
	@echo "------------------------------------------------------------------"
	@docker-compose exec db /bin/bash

dbsnapshot:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Grab a quick snapshot of the database and place in the host filesystem"
	@echo "------------------------------------------------------------------"
	@docker-compose exec db /bin/bash -c "PGPASSWORD=docker pg_dump -Fc -h localhost -U docker -f /tmp/$(COMPOSE_PROJECT_NAME)-snapshot.dmp gis"
	@docker cp $(COMPOSE_PROJECT_NAME)_db_1:/tmp/$(COMPOSE_PROJECT_NAME)-snapshot.dmp .
	@docker-compose exec db /bin/bash -c "rm /tmp/$(COMPOSE_PROJECT_NAME)-snapshot.dmp"
	@ls -lahtr *.dmp

dbschema:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Print the database schema to stdio"
	@echo "------------------------------------------------------------------"
	@docker-compose exec db pg_dump -s -h localhost -U docker gis

dbshell:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Shelling in in production database"
	@echo "------------------------------------------------------------------"
	@docker-compose exec db psql -U docker -h localhost gis

dbrestore:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Restore dump from backups/latest.dmp in production mode"
	@echo "------------------------------------------------------------------"
	@# - prefix causes command to continue even if it fails
	@echo "stopping uwsgi container"
	@docker-compose stop uwsgi
	@echo "dropping gis"
	@docker-compose exec db dropdb gis
	@echo "creating gis"
	@docker-compose exec db createdb -O docker -T template_postgis gis
	@echo "restoring gis"
	@# Because we pipe from one docker command to another and we are going
	@# to execute this Make command from a remote server at times, we need to using use interactive mode (-i)
	@# in the first command and not use terminal (-t) in the second. Please do not change these!
	@docker-compose exec db /bin/bash -c "pg_restore /backups/latest.dmp | psql gis"
	@docker-compose start uwsgi
	@echo "starting uwsgi container"

dbbackup:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Create `date +%d-%B-%Y`.dmp in production mode"
	@echo "Warning: backups/latest.dmp will be replaced with a symlink to "
	@echo "the new backup."
	@echo "------------------------------------------------------------------"
	@# - prefix causes command to continue even if it fails
	@# Explicitly don't use -it so we can call this make target over a remote ssh session
	@docker-compose exec dbbackups /backups.sh
	@docker-compose exec dbbackups cat /var/log/cron.log | tail -2 | head -1 | awk '{print $4}'
	# Force create new symlinks. Overwriting the previous one if any.
	@ln -sf `date +%Y`/`date +%B`/PG_$(COMPOSE_PROJECT_NAME)_gis.`date +%d-%B-%Y`.dmp backups/latest.dmp
	@echo "Backup should be at: backups/`date +%Y`/`date +%B`/PG_$(COMPOSE_PROJECT_NAME)_gis.`date +%d-%B-%Y`.dmp"

sentry:
	@echo
	@echo "--------------------------"
	@echo "Running sentry production mode"
	@echo "--------------------------"
	@docker-compose up -d sentry

maillogs:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Showing smtp logs in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose exec smtp tail -f /var/log/mail.log

mailerrorlogs:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Showing smtp error logs in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose exec smtp tail -f /var/log/mail.err

mediasync:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Syncing media files and secret.py from live server"
	@echo "------------------------------------------------------------------"
	# This section needs to be adapted for ford3 central backups
	#@rsync -av --progress changelog.kartoza.com:/home/projecta/deployment/media/ media
	#@rsync -av --progress changelog.kartoza.com:/home/projecta/django_project/core/settings/secret.py ../django_project/core/settings/
	#@rsync -av --progress changelog.kartoza.com:/home/projecta/deployment/btsync-db.env btsync-db.env.PRODUCTION
	#@rsync -av --progress changelog.kartoza.com:/home/projecta/deployment/btsync-media.env btsync-media.env.PRODUCTION

dbsync:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Syncing database files from live server"
	@echo "------------------------------------------------------------------"
	# This section needs to be adapted for ford3 central backups
	#-@ssh changelog.kartoza.com "cd /home/projecta/deployment; make dbbackup"
	#@rsync -av --progress changelog.kartoza.com:/home/projecta/deployment/backups/ backups

staging-sync:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Syncing database and media files from this host to staging server"
	@echo "Then doing a dbrestore and migrate on the staging server"
	@echo "------------------------------------------------------------------"
	# This section needs to be adapted for ford3 central backups
	#@rsync -av --progress --exclude=.sync --exclude=.DS_Store backups staging.changelog.kartoza.com:/home/projecta/deployment
	#@rsync -av --progress --exclude=.sync --exclude=.DS_Store media staging.changelog.kartoza.com:/home/projecta/deployment
	#-@ssh staging.changelog.kartoza.com "cd /home/projecta/deployment; make dbrestore; make migrate; make collectstatic"

create-machine:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Creating a docker machine."
	@echo "------------------------------------------------------------------"
	@docker-machine create -d virtualbox $(COMPOSE_PROJECT_NAME)

enable-machine:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Enabling docker machine."
	@echo "------------------------------------------------------------------"
	@echo "eval \"$(docker-machine env projecta)\""

# ----------------------------------------------------------------------------
#    DEVELOPMENT C O M M A N D S
# --no-deps will attach to prod deps if running
# after running you will have ssh and web ports open (see dockerfile for no's)
# and you can set your pycharm to use the python in the container
# Note that pycharm will copy in resources to the /root/ user folder
# for pydevd etc. If they dont get copied, restart pycharm...
# ----------------------------------------------------------------------------

devweb: db
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running in DEVELOPMENT mode"
	@echo "------------------------------------------------------------------"
	@docker-compose up --no-deps -d devweb

build-devweb: db
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Building devweb"
	@echo "------------------------------------------------------------------"
	@docker-compose build devweb

flake8:
	@docker-compose exec uwsgi flake8 --version
	@docker-compose exec uwsgi flake8

update-translation-strings:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Update strings for translation."
	@echo "------------------------------------------------------------------"
	@docker-compose exec uwsgi python manage.py makemessages

compile-translation-strings:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Compile strings for translation."
	@echo "------------------------------------------------------------------"
	@docker-compose exec uwsgi python manage.py compilemessages

push-translation-source:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Push translation to transifex."
	@echo "You need to set up your transifex client first."
	@echo "------------------------------------------------------------------"
	@tx push -s -t

pull-translation-source:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Pull all translation from transifex."
	@echo "You need to set up your transifex client first."
	@echo "------------------------------------------------------------------"
	@tx pull -a -f

selenium-up:
	@docker-compose up -d firefox-debug

selenium-down:
	@docker-compose stop hub firefox-debug

test:
	@docker-compose exec uwsgi python manage.py test

coverage-test:
	@docker-compose exec uwsgi coverage run manage.py test

import-saqa-qualifications:
	@docker-compose exec uwsgi python manage.py import_saqa_qualifications

create-provinces-group:
	@docker-compose exec uwsgi python manage.py loaddata provinces_group.json

create-providers-group:
	@docker-compose exec uwsgi python manage.py loaddata providers_group.json

create-campus-group:
	@docker-compose exec uwsgi python manage.py loaddata campus_group.json


load-initial-data:
	@docker-compose exec uwsgi python manage.py loaddata occupation.json
	@docker-compose exec uwsgi python manage.py loaddata subject.json
	@docker-compose exec uwsgi python manage.py loaddata interest.json
	@docker-compose exec uwsgi python manage.py loaddata provinces_group.json
	@docker-compose exec uwsgi python manage.py loaddata providers_group.json
	@docker-compose exec uwsgi python manage.py loaddata campus_group.json
	@docker-compose exec uwsgi python manage.py import_saqa_qualifications -f


# --------------- help --------------------------------

help:
	@echo "* **build** - builds all required containers."
	@echo "* **build-devweb** - build the development container. See [development notes](README-dev.md)."
	@echo "* **collectstatic** - run the django collectstatic command."
	@echo "* **create-machine** ."
	@echo "* **db** - build and run the db container."
	@echo "* **dbbackup** - make a snapshot of the database, saving it to deployments/backups/YYYY/MM/project-DDMMYYYY.dmp. It also creates a symlink to backups/latest.dmp for the latest backup."
	@echo "* **dbbash** - open a bash shell inside the database container."
	@echo "* **dblogs** - view the database logs."
	@echo "* **dbrestore** - restore deployment/backups/latest.dmp over the active database. Will delete any existing data in your database and replace with the restore, so **use with caution**."
	@echo "* **dbschema** - dump the current db schema (without data) to stdio. Useful if you want to compare changes between instances."
	@echo "* **dbshell** - get a psql prompt into the db container. "
	@echo "* **dbsnapshot** - as above but makes the backup as deployment/snapshot.smp - replacing any pre-existing snapshot."
	@echo "* **dbsync** - use this from a development or offsite machine. It will rsync all database backups from deployment/backups to your offsite machine."
	@echo "* **staging-sync** - sync database and media files from this host to staging server, then do a dbrestore and migrate on the staging server"
	@echo "* **default** ."
	@echo "* **deploy** ."
	@echo "* **devweb** - create an ssh container derived from uwsgi that can be used as a remote interpreter for PyCharm. See [development notes](README-dev.md)."
	@echo "* **enable-machine** - "
	@echo "* **kill** - kills all running containers. Does not remove them."
	@echo "* **logs** - view the logs of all running containers. Note that you can also view individual logs in the deployment/logs directory."
	@echo "* **mailerrorlogs** - View the error logs from the mail server."
	@echo "* **maillogs** - view the transaction logs from the mail server."
	@echo "* **mediasync** - use this from a development or offsite machine. It will rsync all media backups from deployment/media to your offsite machine."
	@echo "* **migrate** - run any pending migrations. "
	@echo "* **nginx** - builds and runs the nginx container."
	@echo "* **nginxlogs** - view just the nginx activity logs."
	@echo "* **permissions** - Update the permissions of shared volumes. Note this will destroy any existing permissions you have in place."
	@echo "* **reload** - reload the uwsgi process. Useful when you need django to pick up any changes you may have deployed."
	@echo "* **rm** - remove all containers."
	@echo "* **rm-only** - remove any containers without trying to kill them first. "
	@echo "* **run** - builds and runs the complete orchestrated set of containers."
	@echo "* **sentry** - **currently not working I think.** The idea is to spin up a sentry instance together with your app for fault reporting."
	@echo "* **shell** - open a bash shell in the uwsgi (where django runs) container."
	@echo "* **status** - show status for all containers."
	@echo "* **superuser** - create a django superuser account."
	@echo "* **update-migrations** - freshen all migration definitions to match the current code base."
	@echo "* **web** - same as **run** - runs the production site."
	@echo "* **pep8** - Run Python PEP8 check."
	@echo "* **update-translation-strings** - Update strings for translation."
	@echo "* **compile-translation-strings** - Compile strings for translation."
	@echo "* **push-translation-source** - Push translation to transifex."
	@echo "* **pull-translation-source** - Pull translation from transifex."
