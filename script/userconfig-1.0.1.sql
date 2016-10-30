CREATE DATABASE amangadb;
CREATE DATABASE amangadb_backup1;
CREATE DATABASE amangadb_backup2;
CREATE USER 'admin'@'%' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON 'amangadb'.* TO admin@'%' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON 'amangadb_backup1'.* TO admin@'%' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON 'amangadb_backup2'.* TO admin@'%' IDENTIFIED BY '';
