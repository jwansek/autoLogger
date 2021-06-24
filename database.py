import pymysql
import os

class Database:
    def __enter__(self):
        self.__connection = pymysql.connect(
            host = os.environ["MYSQL_HOST"],
            port = int(os.environ["MYSQL_PORT"]),
            user = os.environ["MYSQL_USER"],
            passwd = os.environ["MYSQL_PASSWORD"],
        )

        with self.__connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS %s" % os.environ["MYSQL_DATABASE"])
            cursor.execute("USE %s" % os.environ["MYSQL_DATABASE"])
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS `access_log` (
                `access_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
                `remote_addr` varchar(15) NOT NULL,
                `remote_user` text DEFAULT NULL,
                `utc_time` datetime NOT NULL,
                `time_offset` int(11) NOT NULL,
                `request` text NOT NULL,
                `status` int(10) unsigned NOT NULL,
                `bytes_sent` int(10) unsigned NOT NULL,
                `referrer` text DEFAULT NULL,
                `http_agent` text DEFAULT NULL,
                `service` varchar(20) NOT NULL,
                PRIMARY KEY (`access_id`)
            );""")
            self.__connection.commit()

        return self

    def append_log(self, service, remote_addr, remote_user, utc_time, time_offset, request, status, bytes_sent, referrer, http_agent):
        with self.__connection.cursor() as cursor:
            cursor.execute("""
            INSERT INTO access_log (`service`, `remote_addr`, `remote_user`, `utc_time`, `time_offset`, `request`, `status`, `bytes_sent`, `referrer`, `http_agent`)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """, (service, remote_addr, remote_user, utc_time, time_offset, request, status, bytes_sent, referrer, http_agent))

    def __exit__(self, type, value, traceback):
        self.__connection.commit()
        self.__connection.close()




if __name__ == "__main__":
    with Database() as db:
        print(db)
