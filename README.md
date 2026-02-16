# 📌 Tabla de Contenido

- Descripción del Proyecto

- Alcance de Pruebas

- Stack Tecnológico

- Arquitectura del Framework

- Estructura del Proyecto

- Instalación

- Ejecución de Pruebas

- Casos de Prueba Automatizados

- Buenas Prácticas Implementadas

- Sección para Recruiters

- Autor

---

# 📖 Descripción del Proyecto

Urban Routes es una plataforma de movilidad que permite a los usuarios:

- Configurar una dirección de origen y destino

- Seleccionar tipos de transporte

- Calcular costos y tiempos estimados

- Solicitar servicios adicionales durante el viaje

Este proyecto automatiza los flujos críticos del usuario para validar el correcto funcionamiento del sistema bajo diferentes escenarios.

---

# 🎯 Alcance de Pruebas

Tipos de pruebas implementadas:

✅ Pruebas End-to-End (E2E)

✅ Pruebas funcionales

✅ Pruebas de usabilidad

✅ Validaciones de UI

✅ Flujos críticos del negocio

---

# 🛠️ Stack Tecnológico

| Tecnología              | Uso                         |
| ----------------------- | --------------------------- |
| Python                  | Lenguaje principal          |
| Selenium WebDriver      | Automatización de navegador |
| Pytest                  | Framework de testing        |
| Page Object Model (POM) | Arquitectura de pruebas     |
| Git                     | Control de versiones        |

---

# 🏗️ Arquitectura del Framework

El proyecto sigue el patrón Page Object Model (POM) para mejorar la mantenibilidad y reutilización del código.

Separación de responsabilidades:

- test/ → Casos de prueba

- model/ → Objetos de página

- data/ → Datos de prueba

- utils/ → Funciones auxiliares

- config/ → Configuración del entorno

```
src/
├── config/
├── data/
├── model/
├── test/
└── utils/
```

---

# ⚙️ Instalación

### Clonar repositorio

```bash
git clone https://github.com/usuario/Urban-Routes.git
```

### Crear entorno virtual (opcional pero recomendado)

```bash
1.python -m venv venv
2.venv\Scripts\activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Ejecución de Pruebas

```bash
pytest .\src\test\TestUrbanRoutes.py
```

---

# 🧪 Casos de Prueba Automatizados

Flujo principal automatizado:

- Configurar la dirección

- Seleccionar la tarifa Comfort

- Rellenar el número de teléfono

- Agregar una tarjeta de crédito

- Escribir un mensaje para el conductor

- Solicitar manta y pañuelos

- Pedir 2 helados

- Validar aparición del modal de búsqueda de taxi

- Esperar información del conductor

Estos escenarios validan el comportamiento completo del usuario desde la configuración del viaje hasta la asignación del conductor.

---

# ✅ Buenas Prácticas Implementadas

- Page Object Model (POM)

- Separación de datos de prueba

- Selectores estables

- Tests independientes

- Reutilización de métodos

- Manejo de esperas explícitas

- Código limpio y mantenible

- Validaciones claras con asserts

- Estructura escalable para crecimiento futuro

- Automatización orientada a flujos de negocio

---

# 🎯 Sección para Recruiters

Este proyecto demuestra experiencia práctica en:

✔ Automatización con Selenium y Python

✔ Diseño de frameworks de testing desde cero

✔ Implementación de Page Object Model

✔ Identificación de flujos críticos de negocio

✔ Buenas prácticas de QA Automation

✔ Testing end-to-end en aplicaciones web reales

✔ Organización de código profesional

✔ Pensamiento analítico orientado a calidad

---

# 👨‍💻 Autor

Axel Arteaga

QA Engineer | Automation Tester | Software Quality

LinkedIn: www.linkedin.com/in/axel-arteaga
