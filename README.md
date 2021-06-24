# autoLogger, dockerized

Automatically add nginx logs to a MySQL/MariaDB database.

## nginx setup

Add a log file to your nginx config, remember the path

`access_log /home/eden/edaweb/access.log;`

## Docker setup

- Rename `db_example.env` to `db.env` and populate it with the credentials
for a MySQL or MariaDB server.
- Edit `docker-compose.yml` and add the paths to the nginx logs as volumes. They need 
to be in `/app/logfiles` and have the name of the service as their filename (examples are present).
- `sudo docker-compose build && sudo docker-compose up -d`