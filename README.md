# 🚁 AgroDron v2.2 "Flora+" — Agentic Vision for Precision Farming

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-5.0-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Devpost](https://img.shields.io/badge/Devpost-Hackathon-003B5C)

Sistema de visión computacional y agente autónomo multicapa para el diagnóstico de cultivos, identificación taxonómica de precisión, detección de estrés hídrico y evaluación de la presión de malezas.

---

## 📺 Demostración en Vídeo
* **Vídeo de presentación en Devpost:** [Añade aquí tu enlace de YouTube / Vimeo / Devpost]

---

## 📌 Descripción General

**AgroDron v2.2 "Flora+"** evoluciona la telemetría agrícola tradicional convirtiendo la captura aéreofotográfica en **decisiones autónomas en tiempo real**. El sistema procesa imágenes RGB y multiespectrales para identificar cultivos clave (incluyendo leguminosas tutoradas como *Phaseolus vulgaris*), detectar malezas invasoras e indicadoras de anoxia hídrica, y calcular el **Índice de Presión de Competencia (IPC)**.

---

## 🏗️ Arquitectura del Sistema (Pipeline Multicapa)

El agente opera en 4 capas secuenciales de procesamiento:

1. **Capa 1 - Percepción HSV & Segmentación:** Aislamiento de cobertura vegetal viva mediante espacio de color HSV y filtrado de ruido en el terreno.
2. **Capa 2 - Clasificación Taxonómica:** Segmentación morfológica de follaje y estructuras (hojas trifoliadas, gramíneas, cladodios, guías rastreras, presencia de estacas/tutores).
3. **Capa 3 - Evaluación Fitosanitaria & Competencia:** Cálculo del IPC y detección de anomalías (anoxia por encharcamiento, clorosis, daño foliar por plagas).
4. **Capa 4 - Generación de Prescripción Autónoma:** Emisión de mapas de acción, registros georreferenciados (CSV) y cargas útiles de integración (JSON).

---

## 🧮 Formulación Matemática

### Índice de Presión de Competencia (IPC)
$$\text{IPC} = \left( \frac{\text{Área de Cobertura de Maleza}}{\text{Área Vegetada Total}} \right) \times 100$$

* **IPC < 20%:** Estado Normal / Monitoreo estándar.
* **IPC 20% - 50%:** Alerta de Competencia / Deshierbe manual o localizado.
* **IPC > 50%:** Intervención Crítica / Control mecánico o térmico urgente.

---

## 🌿 Catálogo Taxonómico e Identificación de Flora

| Especie / Taxón | Categoría | Marcadores Visuales Clave | Nivel de Confianza |
| :--- | :--- | :--- | :--- |
| **_Phaseolus vulgaris_** (Frijol de guía) | Cultivo Agrícola | Hojas compuestas **trifoliadas** (tres folíolos ovado-acorazonados), guías volubles, presencia de **tutores/estacas de madera**. | 98% |
| **_Zea mays_ / _Sorghum_** (Maíz / Sorgo) | Cultivo Agrícola | Gramíneas de hoja ancha, láminas lanceoladas con nervadura paralela, etapas vegetativas tempranas (V2-V4). | 95% |
| **_Opuntia ficus-indica_** (Nopal) | Cultivo Agrícola | Cladodios carnosos aplanados (pencas) con aréolas y brotes vegetativos apicales. | 98% |
| **_Ipomoea spp._** (Camote / Campanilla) | Cultivo / Rastrera | Guías rastreras sobre el suelo con hojas simples cordadas (forma de corazón) y nervación palmatinervia. | 92% |
| **_Saccharum officinarum_** (Caña de Azúcar) | Cultivo / Forraje | Cañas erguidas de alto porte, láminas foliares elongadas con nervadura central prominente. | 94% |
| **_Adenium obesum_** (Rosa del Desierto) | Planta de Jardín | Cáudex basal engrosado suculento, hojas espatuladas, cultivada en macetas/contenedores. | 98% |
| **_Bidens pilosa_** (Aceitilla / Mozote) | Maleza Competitiva | Hojas compuestas serradas, capítulos florales pequeños con lígulas blancas y disco central amarillo. | 95% |
| **_Commelina spp._** (Tripa de pollo) | Maleza Indicadora | Tallos suculentos decumbentes, hojas ovadas; **indicadora de exceso de humedad / encharcamiento**. | 93% |

---

## 🔬 Diagnóstico Fitosanitario y Estrés Fisiológico

* **Asfixia Radicular (Anoxia Hídrica):** Detectada por presencia de lámina de agua libre ($2 - 5\text{ cm}$) y clorosis incipiente en hojas basales de maíz/sorgo.
* **Herbivoría / Plagas:** Identificación de muescas y bordes deshilachados en cogollos por *Spodoptera frugiperda* (Gusano cogollero).
* **Riesgo Fúngico Radicular:** Monitoreo preventivo contra *Pythium spp.*, *Phytophthora spp.* y *Colletotrichum lindemuthianum* (Antracnosis) en entornos de alta humedad.

---

## 📂 Estructura del Repositorio

```text
agrodron-flora-plus/
├── data/
│   ├── dataset_agrodron_flora.csv
│   └── diagnostic_export.json
├── docs/
│   └── manual_entrenamiento.md
├── src/
│   ├── __init__.py
│   └── classifier.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
