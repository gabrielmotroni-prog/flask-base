-- esquema.sql
-- Toda definição de banco deverá ser feita nesse arquivo


drop table if exists presenca;
create table presenca (
  id integer primary key autoincrement,
  email string not null,
  presenca string not null,
  resposta string not null,
  comentario string not null
);