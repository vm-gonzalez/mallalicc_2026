from flask import Flask, render_template
import json
import os

app = Flask(__name__)

malla_data = {
    "Semestre 1": [
        {"nombre": "IIC1103 - Introducción a la Programación", "tipo": "pc"},
        {"nombre": "IIC1001 - Algoritmos y Sist. Computacionales", "tipo": "pc"},
        {"nombre": "MAT1107 - Introducción al Cálculo", "tipo": "pc"},
        {"nombre": "MAT1207 - Intro. al Álgebra y Geometría", "tipo": "pc"},
        {"nombre": "FIL2001 - Filosofía: ¿Para Qué?", "tipo": "fg"}
    ],
    "Semestre 2": [
        {"nombre": "IIC1253 - Matemáticas Discretas", "tipo": "pc"},
        {"nombre": "IIC2233 - Programación Avanzada", "tipo": "pc"},
        {"nombre": "IIC2343 - Arquitectura de Computadores", "tipo": "pc"},
        {"nombre": "MAT1610 - Cálculo I", "tipo": "pc"},
        {"nombre": "Electivo Formación Teológica", "tipo": "fg"}
    ],
    "Semestre 3": [
        {"nombre": "IIC2133 - Estructuras de Datos y Algoritmos", "tipo": "pc"},
        {"nombre": "IIC2413 - Bases de Datos", "tipo": "pc"},
        {"nombre": "MAT1620 - Cálculo II", "tipo": "pc"},
        {"nombre": "MAT1203 - Álgebra Lineal", "tipo": "pc"},
        {"nombre": "Electivo Formación General", "tipo": "fg"}
    ],
    "Semestre 4": [
        {"nombre": "EYP1025 - Modelos Probabilísticos", "tipo": "pc"},
        {"nombre": "IIC2143 - Ingeniería de Software", "tipo": "pc"},
        {"nombre": "IIC2224 - Autómatas y Compiladores", "tipo": "mj"},
        {"nombre": "IIC2333 - Sistemas Operativos y Redes", "tipo": "mj"},
        {"nombre": "Electivo Formación General", "tipo": "fg"}
    ],
    "Semestre 5": [
        {"nombre": "IIC2560 - Fundamentos de Leng. de Programación", "tipo": "mj"},
        {"nombre": "IIC2214 - Teoría de la computación", "tipo": "mj"},
        {"nombre": "IIC2513 - Tecnologías y Aplicaciones Web", "tipo": "mj"},
        {"nombre": "Optativo de Ciencias", "tipo": "pc"},
        {"nombre": "Electivo Formación General", "tipo": "fg"}
    ],
    "Semestre 6": [
        {"nombre": "IIC2613 - Inteligencia Artificial", "tipo": "mj"},
        {"nombre": "IIC2283 - Diseño y Análisis de Algoritmos", "tipo": "mj"},
        {"nombre": "IIC2531 - Seguridad Computacional", "tipo": "mj"},
        {"nombre": "ETI1001 - Ética para Cs. de la Computación", "tipo": "pc"},
        {"nombre": "Electivo Formación General", "tipo": "fg"}
    ],
    "Semestre 7": [
        {"nombre": "IIC2523 - Sistemas Distribuidos", "tipo": "mj"},
        {"nombre": "IIC2182 - Interfaces y Experiencia de Usuario", "tipo": "mj"},
        {"nombre": "Optativos de Profundización o Minor", "tipo": "mn"},
        {"nombre": "Optativos de Profundización o Minors", "tipo": "mn"},
        {"nombre": "Electivo Formación General", "tipo": "fg"}
    ],
    "Semestre 8": [
        {"nombre": "IIC2164 - Proyecto de Innovación y Computación", "tipo": "pc"},
        {"nombre": "Optativos de Profundización o Minor", "tipo": "mn"},
        {"nombre": "Optativos de Profundización o Minor", "tipo": "mn"},
        {"nombre": "Optativos de Profundización o Minor", "tipo": "mn"},
        {"nombre": "Electivo Formación General", "tipo": "fg"}
    ]
}

# Cargar el archivo de prerrequisitos si existe
prerrequisitos_path = 'prerrequisitos.json'
mapa_prerrequisitos = {}
if os.path.exists(prerrequisitos_path):
    with open(prerrequisitos_path, 'r', encoding='utf-8') as f:
        mapa_prerrequisitos = json.load(f)

# Extraer sigla de cada ramo
for semestre, cursos in malla_data.items():
    for curso in cursos:
        partes = curso["nombre"].split(" - ")
        if len(partes) > 1:
            curso["sigla"] = partes[0].strip()
        else:
            curso["sigla"] = ""

@app.route('/')
def index():
    return render_template('index.html', malla=malla_data, prerrequisitos=mapa_prerrequisitos)

if __name__ == '__main__':
    app.run(debug=True)