-- Active: 1755784433023@@127.0.0.1@3306@pruebas
--curso profesional de base de datos en Codigo Facilito

--Modelo Relacional
--es un conjunto de tablas que almacenan entidades(poseen atributos que son representadas mediante columnas)

--declarar variables
USE pruebas;
SET @nombre = "Luciano";
SET @curso = "Base de datos", @gestor = "Mysql";
SELECT @nombre;
SELECT @nombre, @curso, @gestor;

--crear base de datos
CREATE DATABASE pruebas;

SHOW DATABASES;

DROP DATABASE libreria;