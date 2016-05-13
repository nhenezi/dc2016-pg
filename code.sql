-- Initial user and database setup
-- CREATE ROLE dc2016 LOGIN PASSWORD `dc2016`;
-- CREATE DATABASE dc2016 OWNER dc2016;
-- CREATE TYPE sex AS ENUM ('Male', 'Female');


CREATE TABLE person (
  id serial NOT NULL,
  first_name character varying NOT NULL,
  last_name character varying NOT NULL,
  sex sex NOT NULL,
  referal character varying NOT NULL,
  last_location point NOT NULL,
  last_activity timestamp,

  CONSTRAINT person_pk PRIMARY KEY (id)
);

CREATE TABLE thread (
  id serial NOT NULL,
  author_id serial NOT NULL,
  sticky boolean NOT NULL,
  created timestamp NOT NULL,

  CONSTRAINT thread_pk PRIMARY KEY (id)
);

CREATE TABLE post (
  id serial NOT NULL,
  person_id serial NOT NULL,
  thread_id serial NOT NULL,
  sponsored boolean NOT NULL,
  created timestamp NOT NULL,

  CONSTRAINT post_pk PRIMARY KEY (id)
);

CREATE TABLE tag (
  post_id serial NOT NULL,
  tag_id serial NOT NULL,
  created timestamp NOT NULL,

  CONSTRAINT tag_pk PRIMARY KEY (post_id, tag_id)
);

CREATE TABLE tag_type (
  id serial NOT NULL,
  CONSTRAINT tag_type_pk PRIMARY KEY (id)
);

--EXPLAIN (buffers, ANALYZE, COSTS true, TIMING true, verbose) select u.first_name, post.created from post, person as u where u.id=post.person_id ORDER BY post.created LIMIT 10000;
