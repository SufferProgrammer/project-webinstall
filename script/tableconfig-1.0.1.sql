CREATE SCHEMA amangaproject;

CREATE TABLE amangaproject.`user` ( 
	u_id                 int  NOT NULL  AUTO_INCREMENT,
	username             varchar(40)  NOT NULL  ,
	password             varchar(50)  NOT NULL  ,
	email                varchar(50)  NOT NULL  ,
	prof_img             varchar(150)    ,
	prof_bg              varchar(150)    ,
	user_level           int  NOT NULL  ,
	user_status          int  NOT NULL  ,
	join_date            date    ,
	CONSTRAINT pk_user PRIMARY KEY ( u_id )
 );

ALTER TABLE amangaproject.`user` MODIFY prof_img varchar(150)     COMMENT 'this is the path to image profile';

ALTER TABLE amangaproject.`user` MODIFY prof_bg varchar(150)     COMMENT 'this is for parallax background that selected by user';

CREATE TABLE amangaproject.content ( 
	cont_id              int  NOT NULL  AUTO_INCREMENT,
	cont_name            varchar(150)  NOT NULL  ,
	cont_desc            varchar(150)    ,
	cont_img             varchar(150)    ,
	content_path         varchar(150)  NOT NULL  ,
	cont_type            int  NOT NULL  ,
	content_uploader     int  NOT NULL  ,
	content_dateadded    date  NOT NULL  ,
	CONSTRAINT pk_content PRIMARY KEY ( cont_id )
 ) engine=InnoDB;

CREATE INDEX idx_content ON amangaproject.content ( content_uploader );

ALTER TABLE amangaproject.content MODIFY cont_img varchar(150)     COMMENT 'this is path to content preview image';

ALTER TABLE amangaproject.content MODIFY content_path varchar(150)  NOT NULL   COMMENT 'this is path to content';

ALTER TABLE amangaproject.content MODIFY cont_type int  NOT NULL   COMMENT 'this is content type, it''s described by number.
1 is manga
2 is anime
3 is news';

ALTER TABLE amangaproject.content ADD CONSTRAINT fk_content_user FOREIGN KEY ( content_uploader ) REFERENCES amangaproject.`user`( u_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;

