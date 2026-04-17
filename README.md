# 🧪 Laboratory Journal — COVID-19 Data Analysis

---

| Field | Details |
|---|---|
| **Student Name** | Jayvee Shah |
| **PRN** | 25070123058 |
| **Division** | A3 — ENTC |
| **Subject** | Data Analysis Practicals |
| **Experiment Title** | Exploratory Data Analysis & Geospatial Visualization of COVID-19 Global & India-Specific Data |
| **Dataset Range** | January 2020 — May 29, 2021 |
| **Journal Entry No.** | 01 |

---

## 1. Aim

To perform an end-to-end exploratory data analysis on the global COVID-19 dataset, extract meaningful epidemiological insights, compute derived metrics such as active caseloads, and produce interactive geospatial choropleth maps for both worldwide and India-specific case distributions across all states and union territories.

---

## 2. Objectives

- Load, inspect, and clean a large-scale real-world epidemiological dataset of over 306,000 records.
- Perform type normalization and handle missing or malformed entries across numerical and temporal columns.
- Engineer a derived feature — Active Cases — from existing confirmed, recovered, and death tallies.
- Isolate the most recent snapshot of data as a surrogate for "current" global and national conditions.
- Aggregate case statistics at the country and state levels for comparative analysis.
- Visualize global and Indian state-level confirmed case distributions using interactive choropleth mapping with appropriate GeoJSON boundary data.

---

## 3. Theory

### 3.1 The COVID-19 Pandemic — Background

COVID-19 (Coronavirus Disease 2019) is an infectious respiratory illness caused by the SARS-CoV-2 (Severe Acute Respiratory Syndrome Coronavirus 2) pathogen. First identified in Wuhan, Hubei Province, China in late December 2019, it was declared a Public Health Emergency of International Concern (PHEIC) by the World Health Organization (WHO) on January 30, 2020, and subsequently classified as a global pandemic on March 11, 2020.

SARS-CoV-2 is a single-stranded positive-sense RNA betacoronavirus. It primarily spreads through respiratory droplets and aerosols released when an infected individual breathes, speaks, coughs, or sneezes. The virus enters human cells by binding its spike (S) protein to the ACE2 (Angiotensin-Converting Enzyme 2) receptor, which is expressed widely in the lungs, heart, kidneys, and intestines — explaining the multi-organ nature of severe COVID-19 disease.

The pandemic resulted in one of the largest and fastest-generated epidemiological datasets in recorded history. Institutions such as Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE), the WHO, and individual national health ministries published daily case counts, enabling unprecedented real-time tracking of a global outbreak.

---

### 3.2 Epidemiological Metrics

Epidemiology is the study of how diseases distribute across populations and what factors control their presence or absence. The dataset used in this experiment captures four core surveillance metrics.

#### 3.2.1 Confirmed Cases

A **confirmed case** is an individual who has tested positive for SARS-CoV-2 infection using a laboratory-validated diagnostic method. The primary methods employed globally include:

- **RT-PCR (Reverse Transcription Polymerase Chain Reaction):** Detects viral RNA from a nasopharyngeal or throat swab. Considered the gold standard due to high sensitivity and specificity.
- **Rapid Antigen Tests (RATs):** Detect viral proteins (antigens) in secretions. Faster but less sensitive than PCR, leading to potential undercounting.
- **Antibody / Serological Tests:** Detect immune response (IgM/IgG antibodies) rather than the virus itself; used for seroprevalence studies, not active case surveillance.

In the dataset, `Confirmed` is a **cumulative** count — it strictly increases over time and never decreases. It represents the total number of confirmed infections from the beginning of the outbreak up to the `ObservationDate`.

> ⚠️ **Undercounting Bias:** True infection counts are significantly higher than confirmed counts due to asymptomatic cases, limited testing capacity (particularly in low-income countries), and testing policy differences across nations. Confirmed case data should be interpreted as a lower bound on true infection prevalence.

#### 3.2.2 Deaths

The `Deaths` column records the **cumulative number of fatalities** where COVID-19 was identified as the primary or a contributing cause of death. The case fatality rate (CFR) is derived from this metric:

> **Case Fatality Rate (CFR) = (Deaths / Confirmed) × 100%**

CFR varies substantially across countries due to differences in demographics (older populations carry higher risk), healthcare system capacity, testing rates (more testing lowers apparent CFR), and comorbidity prevalence. Like confirmed cases, the death count is also subject to undercounting; excess mortality analyses comparing deaths in 2020–2021 to historical baselines reveal significantly more deaths than were officially attributed to COVID-19 in several countries.

#### 3.2.3 Recovered Cases

The `Recovered` column reflects the **cumulative number of individuals** who were previously confirmed positive and have since been discharged from isolation or medical care, based on government-defined recovery criteria (which varied by country — some required two consecutive negative PCR tests, others used time-based criteria).

> ⚠️ **Data Quality Note:** Recovery data is one of the least consistently reported metrics globally. Many countries discontinued public reporting of recoveries mid-pandemic, leading to gaps, zeroes, and abrupt jumps in this column. Figures should be treated with caution.

#### 3.2.4 Active Cases — Derived Feature

**Active cases** are not directly observed — they are computed as a derived feature using the accounting identity:

> **Active = Confirmed − Recovered − Deaths**

This metric estimates the number of individuals who are currently infected: they have been confirmed positive, have not yet recovered, and have not died. It is the most operationally relevant metric for assessing real-time pressure on healthcare infrastructure — hospital beds, ICU capacity, oxygen supply, and medical personnel.

When active cases rise steeply, health systems face acute strain. When they fall, it typically signals that a wave has peaked and is receding. Because it depends on both recovery and death reporting quality, active case figures inherit all the data quality limitations of their component metrics.

---

### 3.3 Epidemiological Curves and Pandemic Waves

An **epidemic curve** (epi curve) plots the number of new cases (incidence) over time. Its shape encodes critical information about outbreak dynamics:

- **Point-source outbreak:** A sharp spike followed by rapid decline, indicating a single common exposure event.
- **Propagated epidemic:** A gradual rise with a plateau, followed by decline — characteristic of person-to-person transmission.
- **Multiple peaks (waves):** Successive waves arise from new variants, waning immunity, relaxation of public health measures, or seasonal effects.

COVID-19 exhibited a pronounced multi-wave pattern globally. India, specifically, experienced at least two devastating waves within the period covered by this dataset:

- **Wave 1 (Sep–Oct 2020):** India reached its first peak of approximately 97,000 new daily cases in mid-September 2020, before gradually declining through early 2021.
- **Wave 2 (Apr–May 2021):** Driven primarily by the Delta (B.1.617.2) variant, India recorded over 400,000 new daily cases at its peak in early May 2021 — the most severe wave in the country's COVID-19 history, with Maharashtra at the epicentre.

The dataset endpoint (May 29, 2021) captures India near the tail of this devastating second wave, explaining the extremely high cumulative case counts observed for Maharashtra and other major states.

---

### 3.4 Exploratory Data Analysis (EDA)

**Exploratory Data Analysis** is a philosophy of analysis — advocated by statistician John W. Tukey in his 1977 book *Exploratory Data Analysis* — that prioritizes discovering patterns, anomalies, and structure in data before applying formal statistical or machine learning models. EDA techniques include:

- **Structural inspection:** Checking data types, memory usage, row/column counts, and null distributions using `.info()`, `.describe()`, and `.shape`.
- **Missing value analysis:** Quantifying and strategically handling nulls — through imputation, forward/backward fill, or removal — depending on the column's role in analysis.
- **Type normalization:** Ensuring columns are stored in their correct computational types (e.g., dates as `datetime64`, integers as `int64`) to enable arithmetic and temporal operations.
- **Aggregation and groupby operations:** Summarizing data by categorical dimensions (country, state, date) to expose distributional patterns.
- **Visual exploration:** Using histograms, line plots, box plots, and heatmaps to understand distributions, trends, outliers, and correlations.

EDA is not a fixed procedure — it is an iterative, hypothesis-generating process. The analyst cycles between inspection, hypothesis, transformation, and re-inspection until the data is well-understood.

---

### 3.5 Data Preprocessing Concepts

#### 3.5.1 Type Casting and Normalization

Raw data loaded from CSV files is often stored in suboptimal types. Text columns containing numbers arrive as `object` (string) dtype; date columns arrive as plain strings; integer quantities may be stored as floats due to the presence of NaN values (since NumPy's integer dtypes historically could not represent missing values natively).

Type normalization serves multiple purposes:
- Enables arithmetic operations on numeric columns.
- Enables date-based filtering, sorting, and resampling on temporal columns.
- Reduces memory consumption (int64 is more memory-efficient than float64 for whole numbers).
- Prevents silent type coercion errors in downstream operations.

#### 3.5.2 Handling Missing Values

The `Province/State` column in this dataset has 78,103 missing values (306,429 − 228,326), representing country-level records where no sub-national breakdown was reported. Missing value strategies include:

- **Dropping:** Remove rows with nulls — appropriate when missing data is sparse and rows are otherwise redundant.
- **Imputation with a constant:** Fill with a placeholder string (e.g., `"Unknown"`) to preserve the row while flagging the absence of information.
- **Mode imputation:** Fill with the most frequently occurring value — appropriate for low-cardinality categorical variables when missing-at-random is a reasonable assumption.
- **Forward/backward fill:** Propagate the previous or next valid observation — appropriate for time series with occasional gaps.

#### 3.5.3 Feature Engineering

Feature engineering is the process of creating new informative variables from existing ones. In this experiment, `Active` is an **additive composite feature** derived from three source columns. Feature engineering is one of the most impactful steps in any data science pipeline — well-engineered features often improve analytical insights and model performance more than algorithmic complexity alone.

---

### 3.6 Data Aggregation with GroupBy

The `groupby` operation in Pandas implements the **Split-Apply-Combine** paradigm:

1. **Split:** Divide the DataFrame into groups based on a key column (e.g., `Country/Region`).
2. **Apply:** Perform an aggregation function within each group (e.g., `.sum()`, `.mean()`, `.max()`).
3. **Combine:** Reassemble the per-group results into a new DataFrame.

In this experiment, grouping by `Country/Region` and summing is critical because several countries — the US, Canada, Australia, and China — report data at the province/state level, creating multiple rows per country in the raw dataset. Without aggregation, a choropleth would receive duplicated or partial values per country, producing a misleading map.

---

### 3.7 Geospatial Visualization and Choropleth Maps

#### 3.7.1 What Is a Choropleth Map?

A **choropleth map** (from Greek *choros* = place/region, *plethos* = multitude) is a thematic map in which geographic areas are shaded or colored in proportion to a statistical variable. First formally described by French statistician Baron Pierre Charles Dupin in 1826, choropleths are among the most widely used techniques in spatial data visualization.

Key design considerations for choropleths:

- **Color scale selection:** Sequential scales (light-to-dark single hue) are appropriate for data ranging from zero upward — such as case counts. Diverging scales (two hues from a midpoint) suit data with a meaningful center. Qualitative scales suit categorical data.
- **Classification method:** How the data range is divided into color bins — equal intervals, quantiles, natural breaks (Jenks), or logarithmic — dramatically affects the map's visual impression and can mislead if chosen carelessly.
- **Normalization:** Raw counts favor large-population regions. Mapping cases per million population reveals true burden more fairly. This analysis uses raw counts, which biases toward densely populated countries like India and the US.
- **MAUP (Modifiable Areal Unit Problem):** The choice of geographic unit (country vs. state vs. district) fundamentally changes visible patterns. Country-level mapping hides vast internal disparities; state-level mapping reveals them.

#### 3.7.2 GeoJSON Format

**GeoJSON** is an open geospatial data interchange format based on JSON (RFC 7946). It encodes geographic features — points, lines, and polygons — along with their non-spatial properties in a single, human-readable document.

A GeoJSON file for Indian states contains a `FeatureCollection` of `Feature` objects, each with:

- A `geometry` field: a `Polygon` or `MultiPolygon` defining the state's exact boundary as arrays of longitude/latitude coordinate pairs.
- A `properties` field: a dictionary of attribute data — including a state name key (in this file, `NAME_1`).

For Plotly Express to correctly join a DataFrame's rows to the geographic polygons, the `locations` column in the DataFrame must match the GeoJSON's `featureidkey` property exactly — including capitalization and spelling. Any mismatch results in that state silently going uncolored on the map.

#### 3.7.3 Coordinate Reference Systems

All geographic coordinates in GeoJSON use the **WGS 84** (World Geodetic System 1984) datum — the same system used by GPS. Coordinates are expressed as decimal degrees of longitude and latitude. When Plotly renders a choropleth using GeoJSON, it reprojects these coordinates into a chosen **map projection**.

The **Mercator projection** (used in this experiment) maps the spherical Earth onto a flat plane. It preserves local angles (conformal) but significantly distorts area, making regions near the poles appear disproportionately large. For India, which spans roughly 8°N to 37°N latitude, Mercator distortion is moderate and acceptable for visual comparison purposes.

---

### 3.8 Plotly Express and Interactive Visualization

**Plotly** is an open-source graphing library that produces interactive, web-based visualizations using WebGL and D3.js under the hood. **Plotly Express** is its high-level API, enabling complex chart types — including choropleths — to be produced with a single function call.

Key parameters used in `px.choropleth()`:

| Parameter | Role |
|---|---|
| `locations` | Column containing the geographic identifier (country or state name) |
| `locationmode` | How to interpret `locations` — `"country names"` for world-level maps |
| `color` | Column whose values drive the color encoding |
| `color_continuous_scale` | Color ramp (e.g., `"Reds"`, `"Viridis"`, `"Blues"`) |
| `range_color` | Manually clamps the scale endpoints to prevent outliers from compressing variation |
| `geojson` | Python dictionary of the loaded GeoJSON FeatureCollection |
| `featureidkey` | Dot-notation path to the GeoJSON join key (e.g., `"properties.NAME_1"`) |
| `fitbounds` | Auto-zooms the map to the extent of available features when set to `"locations"` |

The resulting charts are interactive: users can hover to see exact values, pan, zoom, and export the visualization as a static PNG.

---

### 3.9 Pandas DataFrame Architecture

A **DataFrame** is Pandas' primary two-dimensional, heterogeneous tabular data structure — conceptually similar to a relational database table, but optimized for numerical computing via integration with NumPy's ndarray.

Key architectural properties relevant to this experiment:

- **Column dtypes:** Each column maintains a single dtype. Mixed-type columns are stored as `object` (Python object references), which is memory-inefficient and prevents vectorized numeric operations.
- **Copy vs. View semantics:** When a DataFrame is sliced (e.g., `india = data[data["Country/Region"] == "India"]`), the result may be a **view** (a window into the original data) or a **copy** (an independent object), depending on the operation. Pandas emits the `SettingWithCopyWarning` when it detects ambiguous assignment on a potential view — the safe practice is to use `.loc[]` for all targeted assignments, or call `.copy()` explicitly when a true independent copy is needed.
- **Memory layout:** Pandas stores columns as contiguous arrays (columnar storage). Column-wise operations (summing all values in a column) are therefore far faster than row-wise operations.
- **Index:** Every DataFrame has a row index (default: integer `RangeIndex`). Temporal DataFrames can use `DatetimeIndex` for powerful time-based slicing and resampling.

---

### 3.10 Temporal Filtering in Panel Data

The raw dataset is a **panel dataset** (longitudinal or time-series cross-sectional data): it records the same set of entities (countries/states) at multiple points in time. This structure enables trend analysis but creates a challenge for point-in-time comparisons — summing all rows per country without temporal filtering would produce nonsensical totals (adding January cases to December cases when both are already cumulative).

Filtering to a single date extracts a **cross-sectional snapshot** — a single slice through the panel at the most recent available date. This snapshot represents the final, cumulative tally for each country and state, making them directly comparable across geographies for choropleth mapping.

---

## 4. Tools & Technologies

| Tool / Library | Purpose |
|---|---|
| Python 3.x | Core programming language |
| Pandas | Data ingestion, transformation, and aggregation |
| NumPy | Numerical operations and array handling |
| Matplotlib | Static plotting framework |
| Seaborn | Statistical visualization |
| Plotly Express | Interactive choropleth and geographic mapping |
| Requests | HTTP client for GeoJSON file retrieval |
| JSON (stdlib) | Parsing and loading GeoJSON boundary data |
| Google Colab | Cloud execution environment |
| GeoJSON (GitHub CDN) | Indian state boundary polygons |

---

## 5. Dataset Description

**Source File:** `covid_19_data.csv`
**Total Records:** 306,429 entries
**Observation Window:** January 2020 — May 29, 2021
**Geographic Coverage:** 195 countries and regions, including sub-national data for India (38 states/UTs)

### Column Schema (Post-Cleaning)

| Column | Dtype | Description |
|---|---|---|
| ObservationDate | datetime64[ns] | Date of data recording |
| Province/State | object | Sub-national region (nullable — 78,103 missing) |
| Country/Region | object | Country or region name |
| Confirmed | int64 | Cumulative confirmed cases |
| Deaths | int64 | Cumulative deaths |
| Recovered | int64 | Cumulative recoveries |
| Active *(engineered)* | int64 | Confirmed − Recovered − Deaths |

**Dropped Columns:** `SNo` (redundant integer row index), `Last Update` (irregular timestamps, not required for analysis)

---

## 6. Methodology

### Phase I — Data Ingestion & Inspection

The raw CSV file was loaded using a fault-tolerant parser configuration (`on_bad_lines='skip'`) to handle malformed rows without halting execution. An initial structural inspection confirmed 306,429 rows, 8 raw columns, three object-typed columns, three float64 columns, and approximately 14 MB memory footprint.

### Phase II — Preprocessing & Type Normalization

Administrative columns (`SNo`, `Last Update`) were dropped. The `ObservationDate` field was cast from raw string to `datetime64[ns]` using `pd.to_datetime()` with `errors='coerce'` to safely handle unparseable date strings. The three numeric case columns were filled with zero and cast from `float64` to `int64`, eliminating unnecessary decimal precision and enabling integer arithmetic.

### Phase III — Feature Engineering

A new `Active` column was computed row-wise as `Confirmed − Recovered − Deaths`. This derived metric serves as a proxy for the instantaneous infection burden and is essential for understanding whether a region was still in active transmission on any given observation date.

### Phase IV — Temporal Filtering (Latest Snapshot)

The maximum `ObservationDate` — May 29, 2021 — was identified programmatically. All 765 records matching this date were extracted as a cross-sectional snapshot representing the cumulative pandemic status of every country and state at the end of the data window.

### Phase V — Country-Level Aggregation

Records in the latest snapshot were grouped by `Country/Region` and summed across all four numeric columns. This collapsed multiple sub-national rows (US states, Canadian provinces, Chinese provinces) into single country-level totals, producing a clean 195-row summary suitable for world choropleth mapping.

### Phase VI — Global Choropleth Map

An interactive choropleth was generated using `px.choropleth()` with `locationmode="country names"` and a red-gradient color scale anchored between 0 and 10,000,000. The ceiling was chosen to prevent the US from monopolizing the top of the scale and compressing all other countries into indistinguishable low-intensity shades.

### Phase VII — India Isolation & State-Level Analysis

All records with `Country/Region == "India"` were extracted. The latest date for India was identified, records were grouped by `Province/State`, and a 38-row state-level summary was produced. Maharashtra was confirmed as the most severely affected state with 5,713,215 cumulative confirmed cases.

### Phase VIII — India State Choropleth with GeoJSON

A GeoJSON boundary file for Indian states was downloaded programmatically from GitHub using the `requests` library. After loading and parsing, the `featureidkey` was identified as `"properties.NAME_1"`. An interactive state-level choropleth was rendered using this GeoJSON with `fitbounds="locations"` to auto-zoom to India's geographic extent.

---

## 7. Observations

| Metric | Value |
|---|---|
| Total dataset records | 306,429 |
| Columns before cleaning | 8 |
| Columns after cleaning | 6 (+ 1 engineered) |
| Missing `Province/State` values | 78,103 |
| Latest observation date | May 29, 2021 |
| Countries / regions in latest snapshot | 195 |
| Records on latest date | 765 |
| Indian states / UTs with data | 38 |
| Highest confirmed state | Maharashtra — 5,713,215 |
| GeoJSON feature key used | `properties.NAME_1` |

---

## 8. Results & Analysis

The global choropleth map revealed a stark geographic concentration of COVID-19 burden. Countries in North America (US), South Asia (India), and South America (Brazil) carried disproportionately large caseloads relative to their geographic area. Sub-Saharan Africa and much of Central Asia showed relatively low confirmed case counts — a reflection of both genuinely lower spread and severely limited testing infrastructure, which suppresses confirmed case detection.

The India-specific analysis confirmed Maharashtra's overwhelming dominance. With 5.71M cases as of May 29, 2021 — more than double the second-ranked state — it stood as the epicentre of India's catastrophic second wave, driven by the Delta variant and extreme urban density in Mumbai and Pune. Karnataka, Kerala, Uttar Pradesh, Tamil Nadu, and Delhi also appeared as the most severely affected states in the top-20 ranking.

The Active Cases metric proved analytically valuable in distinguishing regions still mid-wave from those in recovery. Countries with high confirmed counts but low active cases (e.g., Mainland China, with aggressive containment) presented very differently from countries with rapidly rising active cases at the snapshot date — demonstrating the diagnostic power of the derived feature.

---

## 9. Conclusions

- Large-scale epidemiological datasets require systematic preprocessing pipelines — type normalization, null handling, and feature engineering — before any spatiotemporal analysis is possible.
- Temporal filtering to a single cross-sectional snapshot is the correct technique for converting cumulative panel data into comparable point-in-time figures suitable for geographic mapping.
- Standard country-name geocoding is sufficient for world-level maps, but sub-national analysis in India requires explicit GeoJSON boundary files with correctly matched feature property keys.
- Maharashtra was the worst-affected Indian state as of May 29, 2021, with 5.7M confirmed cases, reflecting the devastating impact of the Delta-driven second wave on western India.
- Interactive Plotly choropleths significantly enhance exploratory spatial analysis through hover-based inspection, dynamic zoom, and immediate visual comparison across 195 geographic units.
- Confirmed case data systematically undercounts true infections; all findings should be interpreted as lower bounds on true prevalence, with cross-country comparability limited by heterogeneous testing policies and reporting standards.

---

## 10. Precautions

**`on_bad_lines='skip'` in CSV loading** — While this prevents pipeline failure on malformed rows, skipped rows are silently discarded. In production, all skipped rows should be logged and inspected before conclusions are drawn from the cleaned dataset.

**`SettingWithCopyWarning` on India subset** — Mutations on a DataFrame slice may or may not propagate to the original, depending on whether Pandas internally created a copy or a view. The correct pattern is `.loc[row_indexer, col_indexer] = value` for all targeted assignments, or calling `.copy()` explicitly when creating an independent sub-DataFrame.

**GeoJSON property key case-sensitivity** — `featureidkey="properties.NAME_1"` must match the GeoJSON file exactly. A mismatch causes all polygons to go uncolored without raising any error — the failure is entirely silent.

**`fillna("mode")` logical error** — The notebook fills null `Province/State` values with the Python string literal `"mode"` rather than the computed mode value. The correct call is `india['Province/State'].mode()[0]`, which extracts the actual most-frequently-occurring state name.

**Normalization omitted** — All choropleth maps visualize raw confirmed case counts rather than cases per million population. This biases the visual representation toward large-population countries and states. A population-normalized map would provide a fairer comparison of true burden.

**Recovery data reliability** — The `Recovered` column — and by extension the derived `Active` column — is one of the least reliably reported metrics in international COVID-19 surveillance. Many countries dropped recovery reporting mid-pandemic. Active case figures should be treated as approximate indicators of burden rather than precise epidemiological counts.

---

*This journal entry is a record of practical work performed as part of the Data Analysis curriculum. All observations, results, and conclusions are based on the dataset provided for the experiment.*
