create schema mywatchlist;

create table mywatchlist.movies(
movie_id int(10) not null primary key,
movie_name varchar(50) not null,
movie_director varchar(30) not null,
movie_release_date date,
movie_genre varchar(30));

describe mywatchlist.movies;

drop table mywatchlist.movies;

create table mywatchlist.movies(
movie_id integer not null primary key,
movie_name varchar(50) not null,
movie_director varchar(30) not null,
movie_release_date date,
movie_genre varchar(30));

describe mywatchlist.movies;

insert into mywatchlist.movies values
(1, "DUNE", "Denis Villeneuve", "2021-09-03", "science fiction"),
(2, "Harry Potter and the Goblet of Fire", "Mike Newell", "2005-11-18", "fantasy");

select * from mywatchlist.movies;

create table mywatchlist.series(
series_id integer not null primary key,
series_name varchar(50) not null,
series_director varchar(30) not null,
series_release_date date,
series_genre varchar(30));

describe mywatchlist.series;

insert into mywatchlist.series values
(1, "Stranger Things", "The Duffer Brothers", "2016-07-15", "Sci -fi Horror"),
(2, "Obi-Wan Kenobi","Deborah Chow", "2022-05-27", "Action Adventure");

select * from mywatchlist.series;

alter table mywatchlist.series 
change series_director series_creator varchar(30);

select * from mywatchlist.series;












