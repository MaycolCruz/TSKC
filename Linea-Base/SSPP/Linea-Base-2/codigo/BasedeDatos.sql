
CREATE DATABASE SSPP 
use SSPP
use master
drop DATABASE  SSPP
Create table prision(
Cod_prision numeric primary key,
Nombre varchar(20) not null,
Direccion varchar(50) not null,
Capacidad int
);
Create table Celda(
Cod_celda numeric primary key,
Numero int not null,
Capacidad varchar(50) not null,
Cod_prision numeric,
FOREIGN KEY (Cod_celda) REFERENCES prision(Cod_prision)
);
Create table Recluso(
Cod_recluso numeric primary key,
Nombre varchar(20) not null,
Apellido varchar(20) not null,
Fecha_nacimiento datetime,
Cod_crimen numeric,
Cod_curso numeric,
Cod_conducta numeric,
Cod_celda numeric,
FOREIGN KEY (Cod_celda) REFERENCES Celda(Cod_celda)
);
Create table Crimen(
Cod_crimen numeric primary key,
Nombre varchar(20) not null,
Descripcion varchar(50) not null,
);
Create table Curso(
Cod_curso numeric primary key,
Nombre varchar(20) not null,
Descripcion varchar(50) not null,
);
Create table Conducta(
Cod_conducta numeric primary key,
Nombre varchar(20) not null,
Descripcion varchar(50) not null,
);
CREATE TABLE Sentencia (
  Cod_sentencia numeric primary key,
  Cod_recluso numeric ,
  Cod_crimen numeric,
  FOREIGN KEY (Cod_recluso) REFERENCES Recluso(Cod_recluso),
  FOREIGN KEY (Cod_crimen) REFERENCES Crimen(Cod_crimen),
);

CREATE TABLE Calificacion_cond (
  Cod_calificacion_cond numeric primary key,
  Cod_recluso numeric,
  Cod_conducta numeric,
  FOREIGN KEY (Cod_recluso) REFERENCES Recluso(Cod_recluso),
  FOREIGN KEY (Cod_conducta) REFERENCES Conducta(Cod_conducta),
);
CREATE TABLE Matricula (
  Cod_matricula numeric primary key,
  Cod_recluso  numeric,
  Cod_curso numeric,
  FOREIGN KEY (Cod_recluso) REFERENCES Recluso(Cod_recluso),
  FOREIGN KEY (Cod_curso) REFERENCES Curso(Cod_curso),
);