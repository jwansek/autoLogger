CREATE TABLE access_log ( 
    access_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    remote_addr VARCHAR(15) NOT NULL, 
    remote_user TEXT NULL, 
    `utc_time` DATETIME NOT NULL, 
    time_offset INT NOT NULL, 
    request TEXT NOT NULL, 
    status UNSIGNED INT NOT NULL, 
    bytes_sent UNSIGNED INT NOT NULL, 
    referrer TEXT NOT NULL, 
    http_agent TEXT NOT NULL, 
    service VARCHAR(20) NOT NULL )
;