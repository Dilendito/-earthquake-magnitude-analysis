# Earthquake Magnitude Analysis

## Project Overview

This project explores global earthquake events recorded by the [USGS Earthquake Hazards Program](https://earthquake.usgs.gov/) between 2023 and 2024. We aim to understand which seismic and geographic features best predict the magnitude of an earthquake.

---

## Dataset Questions

### What does your dataset explore?
This dataset explores characteristics of earthquake events worldwide, including their depth, location, seismic measurement quality, and classification. We examine which geophysical properties are most associated with higher or lower earthquake magnitudes.

### What is your dependent variable?
**`mag`** — the magnitude of the earthquake on the Richter-equivalent scale.
- **Type:** Quantitative (continuous)

### What are your independent variables?

| Variable | Type | Description |
|---|---|---|
| `depth` | Quantitative | Depth of the earthquake hypocenter in kilometers |
| `latitude` | Quantitative | Geographic latitude of the epicenter |
| `longitude` | Quantitative | Geographic longitude of the epicenter |
| `nst` | Quantitative | Number of seismic stations used to determine the location |
| `gap` | Quantitative | Largest azimuthal gap between adjacent stations (degrees) |
| `dmin` | Quantitative | Horizontal distance from the epicenter to the nearest station (degrees) |
| `rms` | Quantitative | Root-mean-square travel time residual (seconds) |
| `month` | Quantitative | Month the earthquake occurred (1–12) |
| `year` | Quantitative | Year the earthquake occurred (2023 or 2024) |
| `magType` | Categorical | Algorithm used to calculate magnitude (e.g., ml, mb, mw, md) |
| `type` | Categorical | Event type (earthquake, quarry blast, explosion, etc.) |
| `status` | Categorical | Review status (reviewed, automatic) |
| `region` | Categorical | Broad geographic region extracted from the place description |

**Total independent variables: 13** ✅

### Is the dependent variable categorical or quantitative?
Quantitative — `mag` is a continuous numeric value representing earthquake magnitude.

### Are the independent variables quantitative or categorical?
A mix of both:
- **Quantitative (9):** depth, latitude, longitude, nst, gap, dmin, rms, month, year
- **Categorical (4):** magType, type, status, region

### How many independent variables?
**13 independent variables** ✅ (more than the required 5)

### How large is your dataset?
- **Rows:** 20,000 (all earthquakes magnitude ≥ 1.5 globally, 2023–2024)
- **Columns:** 16
- Well above the 1,000-row minimum ✅

---

## Repository Structure

```
├── data/
│   └── earthquakes.csv           # Output CSV from data_ingestion.py
├── notebooks/
│   └── eda.ipynb                 # Exploratory data analysis notebook
├── results/                      # Generated charts and HTML report
├── data_ingestion.py             # Script to pull data from USGS API → CSV
├── requirements.txt              # Python dependencies
└── README.md
```

---

## How to Run

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Pull the data**
```bash
python data_ingestion.py
```
This will create `data/earthquakes.csv` automatically.

**3. Run your EDA**

Open your personal notebook in `notebooks/` and run all cells.

---

## Data Source

- **API:** [USGS Earthquake Hazards Program](https://earthquake.usgs.gov/fdsnws/event/1/)
- **Endpoint used:** `/fdsnws/event/1/query`
- **No API key required**
- **Date range:** January 2023 – December 2024
- **Filter:** Minimum magnitude 1.5

---

## Team Members

| Name | EDA Notebook |
|---|---|
| Lendi | `notebooks/lendi_eda.ipynb` |
| [Name 2] | `notebooks/name2_eda.ipynb` |
| [Name 3] | `notebooks/name3_eda.ipynb` |
