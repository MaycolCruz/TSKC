CREATE DATABASE SSPP 
use SSPP
use master
drop DATABASE  SSPP
Create table prision(
Cod_prision numeric primary key,
Nombre varchar(20) not null,
Direccion varchar(150) not null,
Capacidad int
);
Create table Celda(
Cod_celda numeric primary key,
Numero int not null,
Capacidad varchar(150) not null,
Cod_prision numeric,
FOREIGN KEY (Cod_celda) REFERENCES prision(Cod_prision)
);
Create table Recluso(
Cod_recluso numeric primary key,
Nombre varchar(20) not null,
Apellido varchar(20) not null,
Fecha_nacimiento date,
Cod_crimen numeric,
Cod_curso numeric,
Cod_conducta numeric,
Cod_celda numeric,
FOREIGN KEY (Cod_celda) REFERENCES Celda(Cod_celda)
);
Create table Crimen(
Cod_crimen numeric primary key,
Nombre varchar(20) not null,
Descripcion varchar(150) not null,
);
ALTER TABLE Crimen
ALTER COLUMN Descripcion  varchar(150);
Create table Curso(
Cod_curso numeric primary key,
Nombre varchar(20) not null,
)
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
SELECT * FROM Recluso
SELECT * FROM Matricula
SELECT * FROM Curso
SELECT * FROM prision
SELECT * FROM Celda
SELECT * FROM Conducta
SELECT * FROM recluso
iNSERT INTO prision VALUES (1,'Santa Monica','Chorrillos cuadra 5',160) 
iNSERT INTO Celda VALUES (1,322,5,1) 
-- Inserta nuevos registros en la tabla Recluso
INSERT INTO Recluso VALUES (1,'Jose','Romero','01/12/1999',1,1,1,1)
INSERT INTO Recluso VALUES (2,'Marco','Benites','01/12/2000',1,1,1,1)
INSERT INTO Recluso VALUES (3,'Juan','xas','01/12/2000',2,1,1,1)
select * from Matricula
-- Inserta registros en la tabla Matricula para asignar cursos a los reclusos
INSERT INTO Matricula VALUES (1,1,1)
INSERT INTO Matricula VALUES (2,2,2)
INSERT INTO Matricula VALUES (3,3,3)
iNSERT INTO curso VALUES (1,'Mecanica')
iNSERT INTO curso VALUES (2,'Soldadura')
iNSERT INTO curso VALUES (3,'Jardineria')
iNSERT INTO curso VALUES (4,'Informatica')
iNSERT INTO curso VALUES (5,'Arte y manualidades')

iNSERT INTO Conducta VALUES (1,'Buena conducta','Cumple con las reglas y normas de la prision')
iNSERT INTO Conducta VALUES (2,'Conducta regular','Algunas infracciones menores')
iNSERT INTO Conducta VALUES (3,'Mala conducta','Infracciones graves')
iNSERT INTO Calificacion_cond VALUES (1,1,1)
iNSERT INTO Calificacion_cond VALUES (2,2,2)
iNSERT INTO Calificacion_cond VALUES (3,3,1)
iNSERT INTO Crimen VALUES (1,'Robo','Tomar ilegalmente la propiedad de otra persona sin su consentimiento, mediante el uso de fuerza.')
iNSERT INTO Crimen VALUES (2,'Agresion','Causar daño fiisico o amenazar con hacerlo a otra persona intencionalmente.')
iNSERT INTO Crimen VALUES (3,'Homicidio','Matar a otra persona de manera intencional (homicidio intencional) o sin intencion de causar la muerte (homicidio involuntario).')
iNSERT INTO Crimen VALUES (4,'Trafico de drogas','La produccion, distribucion, venta o transporte ilegal de sustancias controladas, como drogas ilegales.')
iNSERT INTO Crimen VALUES (5,'Fraude','Actividades engañosas realizadas para obtener beneficios financieros o personales de manera deshonesta, como estafas o falsificacion de documentos.')


CREATE FUNCTION ObtenerDatosRecluso()
RETURNS TABLE
AS
RETURN
(
    SELECT Recluso.Nombre, Recluso.Apellido, Recluso.Fecha_nacimiento, Crimen.Nombre AS CrimenNombre, Prision.Nombre AS PrisionNombre, Celda.Numero AS CeldaNumero, Curso.Nombre AS CursoNombre, Conducta.Nombre AS ConductaNombre
    FROM Recluso
    JOIN Celda ON Recluso.Cod_celda = Celda.Cod_celda
    JOIN Prision ON Celda.Cod_prision = Prision.Cod_prision
    JOIN Matricula ON Recluso.Cod_recluso = Matricula.Cod_recluso
    JOIN Curso ON Matricula.Cod_curso = Curso.Cod_curso
    JOIN Calificacion_cond ON Calificacion_cond.Cod_recluso = Recluso.Cod_recluso
    JOIN Conducta ON Conducta.Cod_conducta = Calificacion_cond.Cod_conducta
    JOIN Crimen ON Recluso.Cod_crimen = Crimen.Cod_crimen
);
select * from ObtenerDatosRecluso()

