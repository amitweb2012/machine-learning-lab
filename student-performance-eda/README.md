# 📊 Student Performance EDA

> Explore how study habits and attendance relate to student marks through data cleaning, visualizations, and descriptive analysis.

![Python](https://img.shields.io/badge/Python-EDA-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Data-pandas-150458?logo=pandas&logoColor=white)
![Charts](https://img.shields.io/badge/Charts-Matplotlib%20%7C%20Seaborn-4C8CBF)

---

## 🧭 Contents

- [Project overview](#-project-overview)
- [Quick start](#-quick-start)
- [Analysis workflow](#-analysis-workflow)
- [Performance bands](#-performance-bands)
- [Output](#-output)
- [Interpretation note](#-interpretation-note)

## 🔎 Project overview

This project analyzes a small student dataset containing study hours, attendance, gender, and marks in math, science, and English.

| File | Purpose |
| --- | --- |
| [`student_performance.py`](student_performance.py) | Runs the EDA workflow |
| [`data/student_performance.csv`](data/student_performance.csv) | Input dataset |
| [`requirements.txt`](requirements.txt) | Python dependencies |

## 🚀 Quick start

### 1. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it:

```bash
# macOS / Linux
source .venv/bin/activate
```

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Run the analysis

Run this from the project directory:

```bash
python student_performance.py
```

The script opens charts in plot windows. Close each window to continue.

## 🧪 Analysis workflow

The script:

1. Previews the data and reports data types, descriptive statistics, missing values, and duplicates.
2. Cleans duplicate and missing rows and validates feature ranges:
   - Study hours: **0–24**
   - Attendance and subject marks: **0–100**
3. Replaces out-of-range values with the mean of valid values; subject-mark replacements are rounded to whole numbers.
4. Calculates five-number summaries and IQR-based outlier counts.
5. Plots feature distributions and gender counts.
6. Creates `average_marks` and compares it with study hours, attendance, and gender.
7. Prints and plots correlations among study habits and subject marks.
8. Prints a short descriptive findings summary.

The identifier `student_id` is not used as a measured numeric feature.

## 🏅 Performance bands

The `performance` category is derived from each student's average across math, science, and English:

| Average marks | Category |
| ---: | :--- |
| `< 70` | Needs Improvement |
| `70–<80` | Average |
| `80–<90` | Good |
| `≥ 90` | Excellent |

These are project-defined cutoffs, not universal grading standards. `average_marks` may be fractional; individual subject marks remain whole numbers.

## 📁 Output

After a successful run, the cleaned dataset is written to:

```text
data/processed/student_performance_eda_cleaned.csv
```

The output includes the input columns plus `average_marks` and `performance`. The processed directory is created automatically if needed.

## ⚠️ Interpretation note

The sample contains only **10 students**. Use charts and correlations as exploratory descriptions; they do not establish that study hours or attendance cause higher marks.
