# README #

This README would normally document whatever steps are necessary to get your application up and running.

* [APIV2 Repo](https://bitbucket.org/agtechlabs/api-server/)

### How do I get set up? ###

* git clone https://USERNAME@bitbucket.org/agtechlabs/api-server.git
* Install pip and virtualenv
* virtualenv ENV_NAME
* pip install -r requirements.txt

### Postges ###
* createdb apiserverdb;
* psql
* \c apiserverdb
* CREATE EXTENSION postgis;
* CREATE EXTENSION adminpack;
* ALTER USER username SUPERUSER;
* Grant all privileges on database apiserverdb to USERNAME;
* \q