-- schema file for pqs flask app
create schema if not exists hits;
create table if not exists hits.hits (id integer primary key) sal_buckets=4;
create sequence if not exists hits.hit_sequence start 1 increment by 1 cache 10;
