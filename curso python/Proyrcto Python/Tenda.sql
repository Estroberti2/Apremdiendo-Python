#create database Tienda;
USE Tienda;

CREATE TABLE if not exists Sucursal
(
id_sucursal int primary key not null,
nom_sucursal varchar(20) not null
);

create table if not exists Articulos
(
id_sucursal int,
id_articulos int primary key not null auto_increment unique,
foreign key (id_sucursal) references Sucursal(id_sucursal)
);

create table if not exists Caracteristicas
(
id_articulos int,
nom_articulo varchar(20)not null,
categoria varchar(20) not null,
stock int not null,
precio float not null,
foreign key (id_articulos) references Articulos(id_articulos)
);

create table if not exists Ventas
(
id_sucursal int,
id_articulos int,
fecha_compra date not null,
hora_compra time not null,
foreign key (id_articulos) references Articulos(id_articulos),
foreign key (id_sucursal) references Sucursal(id_sucursal)
);

create table if not exists Usuarios
(
id_sucursal int,
id_usuario int not null auto_increment primary key,
mail varchar(30) not null unique,
contraseña varchar(30) not null unique,
foreign key (id_sucursal) references Sucursal(id_sucursal)
);

create table if not exists Informacion
(
id_usuario int,
dni int primary key not null unique,
nombre varchar(20) not null,
apellido varchar(20) not null,
direccion varchar(40) not null,
foreign key (id_usuario) references Usuarios(id_usuario)
);

create table if not exists Personal
(
dni int,
num_empleado int not null auto_increment primary key,
puesto varchar(20) not null,
foreign key (dni) references Informacion(dni)
);

create table if not exists Clientes
(
dni int,
num_cliente int not null unique auto_increment primary key,
saldo float not null,
foreign key (dni) references Informacion(dni)
);

create table if not exists Carrito
(
num_cliente int,
num_carrito int not null primary key auto_increment,
id_articulos int,
precio float not null,
foreign key (id_articulos) references Articulos(id_articulos),
foreign key (num_cliente) references Clientes(num_cliente)
);

#drop database Tienda