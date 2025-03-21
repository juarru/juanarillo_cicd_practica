# PRÁCTICA CICLO DE VIDA DE UN DESARROLLO - CICD - JUAN ARILLO

Práctica de Juan Arillo para el módulo de **Ciclo de vida de un desarrollo - CICD**.

Repositorio de la aplicación *Flask* que usa base de datos *Redis*.

Configuraciones para Pipelines *CircleCI* y *Github Actions*.

## TABLA DE CONTENIDOS

- [Descripción](#descripción)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Configuración y ejecución local](#configuración-y-ejecución-local)

## Descripción

Este repositorio contiene una aplicación *Flask* que cuenta el número de veces que se recarga la página, y se persiste en una base de datos *Redis*.

Viene preparado para automatizar y preparar un contendor de desarrollo en Docker a través de *Visual Studio Code*.

También crea *Actions* de Github y pipelines de *CircleCI* para la construcción de imágenes de la aplicación de manera automatizada, así como la subida de la misma al repositorio *Docker Hub*.  

A su vez genera las releases, los changelogs y los artefactos en cada mergeo a la rama main del proyecto.

## Estructura del Proyecto

├── .circleci/                      -> Configuración de CircleCI  
│   ├── config.yml                  -> Configuración de la pipeline en CircleCI  
│  
├── .devcontainer/                  -> Configuración del entorno de desarrollo en VS Code  
│   ├── devcontainer.json           -> Configuración del DevContainer  
│  
├── .github/workflows/               -> Workflows de GitHub Actions  
│   ├── delete_branch.yml            -> Workflow para eliminar ramas después de merge a dev  
│   ├── pr_checks.yml                -> Workflow para ejecutar pruebas en PRs  
│  
├── .vscode/                         -> Configuración de VS Code  
│   ├── settings.json                -> Configuración del entorno en VS Code  
│   ├── tasks.json                   -> Tareas automatizadas para el desarrollo  
│  
├── app/                             -> Carpeta principal de la aplicación  
│   ├── app.py                       -> Archivo principal de la aplicación Flask  
│   ├── requirements.txt             -> Dependencias del proyecto  
│   ├── pytest.ini                   -> Configuración para pytest  
│   ├── test_app.py                  -> Pruebas unitarias de la aplicación  
│  
├── Dockerfile                       -> Definición de la imagen Docker  
├── docker-compose.yml               -> Configuración de servicios con Docker Compose  
├── sonar-project.properties         -> Configuración para SonarQube  
├── README.md                        -> Documentación del proyecto  

## Requisitos

- [*Docker*](https://www.docker.com/)
- [*Git*](https://git-scm.com/)

## Configuración y ejecución local

- Clonar el Repositorio

```bash
git clone https://github.com/juarru/juanarillo_cicd_practica.git
cd juanarillo_cicd_practica
```

- Levantar los servicios

```bash
docker-composer up -build
```

- La aplicación Flask se iniciará en `http://localhost:5001` .
