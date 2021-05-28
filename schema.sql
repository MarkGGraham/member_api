create table users (
    id serial primary key,
    name text not null,
    password text not null,
    expert boolean not null,
    admin boolean not null

);

create table questions (
    id serial primary key,
    question text not null,
    answer text,
    asked_by_id serial not null,
    expert_id serial not null
);