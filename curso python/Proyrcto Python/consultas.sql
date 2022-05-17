 #nos da el id del usuario
select id_usuario, mail, contraseña from usuarios where mail="@mail.com" and contraseña="Estroberti2"
 
 #nos da el dni del usuarios
select dni from informacion where id_usuario in (select id_usuario from usuarios where mail="Mail@mail.com" and contraseña="Estroberti2")

#nos da el numero del cliente
select num_cliennte from clientes where dni in (select dni from informacion where id_usuario in (select id_usuario from usuarios where mail="Mail@mail.com" and contraseña="Estroberti2"))

#nos da el numero del empleado
select num_empleado from personal where dni in (select dni from informacion where id_usuario in (select id_usuario from usuarios where mail="Mail@mail.com" and contraseña="Estroberti2"))

select num_cliennte from clientes where dni in (select dni from informacion where id_usuario=2);

select num_cliennte from clientes where dni=12345679

insert into sucursal (id_sucursal, nom_sucursal) values (7, "Papaya");
select * from sucursal

insert into usuarios (id_sucursal, mail, contraseña) values (7, "Mail@mail.com", "Estroberti2");
insert into usuarios (id_sucursal, mail, contraseña) values (7, "Mail2@mail.com", "1234");
select * from usuarios

insert into informacion (id_usuario, dni, nombre, apellido, direccion) values (1, 12345678, "Renzo", "Martinez", "A. Romero 1800");
insert into informacion (id_usuario, dni, nombre, apellido, direccion) values (2, 12345679, "Ramon", "Martin", "A. Romero 1880");
select * from informacion

insert into personal (dni, puesto) values (12345678, "capitan")
update personal set dni= 12345678 where dni= 12345679
select * from personal

insert into clientes (dni, saldo) values (12345679, 75);
select * from clientes

select usuarios.mail, usuarios.contraseña, informacion.dni, informacion.nombre, informacion.apellido  from usuarios inner join informacion on usuarios.id_usuario = informacion.id_usuario
// la condicion de union es la igualdad