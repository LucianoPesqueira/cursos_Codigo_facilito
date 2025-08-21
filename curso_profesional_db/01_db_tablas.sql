USE pruebas;

--CREAR TABLAS
/*Tipos de entidades: autores
Nombre : autores
Genero
Fecha de nacimiento
Pais de origen

columna y el tipo de dato
*/
CREATE TABLE autores (
    autor_id INT,
    nombre VARCHAR(25),
    apellido VARCHAR(25),
    genero CHAR(1), -- M o F,
    fecha_nacimiento DATE,
    pais_origen VARCHAR(40)
);

--Listar y eliminar tablas
SHOW TABLES;
DROP TABLE autores;

SHOW COLUMNS FROM autores;
DESC autores; --es igual a show columns from

--Crear tablas a partir de otras
CREATE TABLE usuarios LIKE autores; --crear una tabla a partir de otra
DESC usuarios;

--Insertar registros
INSERT INTO autores (autor_id, nombre, apellido, genero, fecha_nacimiento, pais_origen)
VALUES(1, 'Test autor', 'Test autor', 'M', '2025-08-21', 'Argentina');
SELECT * FROM autores;
INSERT INTO autores (autor_id, nombre)
VALUES(2, 'Test autor');

--Ejercicios 4 inserciones con diferentes cantidades de columnas:
INSERT INTO autores (autor_id, nombre, genero, fecha_nacimiento, pais_origen)
VALUES(1, 'Test autor', 'M', '2025-08-21', 'Argentina');
INSERT INTO autores (autor_id)
VALUES(3);
INSERT INTO autores (fecha_nacimiento, pais_origen)
VALUES('2025-08-21', 'Argentina');
INSERT INTO autores ()
VALUES();
