# autoLogger
script for adding nginx logs to a mysql/mariadb database

- rename the config file to `autoLogger.conf` and fill it with the correct information
- make sure the database is correct and run `ddl.sql` in it to make the database
- run the program every so often using cron for example `*/2 * * * * python3 /home/eden/autoLogger/autoLogger.py /home/eden/autoLogger/`
- the old log files will be removed so save disk space
- log lines that couldn't be parsed are appended to `couldntparse.log`
