# 🐼 Python Pandas Series

A hands-on Python project for learning and practicing **Pandas Series** from basic to advanced concepts.

This repository contains practical examples, exercises, datasets, indexing operations, and important Pandas methods that are useful for **Data Analysis, Data Science, Machine Learning, and Python interviews**.

---

## 🚀 About Pandas

**Pandas** is a powerful Python library used for:

- Data manipulation
- Data analysis
- Data cleaning
- Data preprocessing
- Working with CSV and tabular data
- Handling missing values
- Sorting and filtering data
- Statistical analysis

The main Pandas data structures are:

- **Series** – One-dimensional labeled data
- **DataFrame** – Two-dimensional tabular data

This repository mainly focuses on **Pandas Series**.

---

## 📚 Topics Covered

### 1. Pandas Series Basics

- Creating a Series
- Series from lists
- Series from NumPy arrays
- Series from dictionaries
- Custom indexes
- Index and values
- Data types
- Series attributes
- `head()`
- `tail()`
- `size`
- `shape`
- `dtype`

### 2. Series Indexing

- Positive indexing
- Negative indexing
- Slicing
- Fancy indexing
- `iloc`
- Label-based indexing
- Selecting multiple values

Example:

```python
import pandas as pd

data = pd.Series([10, 20, 30, 40, 50])

print(data[0])
print(data[1:4])
print(data.iloc[2])
```

---

## 🔍 Important Pandas Methods

Some of the important methods practiced in this repository include:

```text
head()
tail()
info()
describe()
sort_values()
sort_index()
value_counts()
unique()
nunique()
isnull()
notnull()
dropna()
fillna()
astype()
```

---

## 📊 Working With Datasets

The repository also contains datasets for practicing Pandas operations.

Examples of datasets include:

- Subscribers data
- Virat Kohli IPL data
- Bollywood data
- Other CSV datasets

These datasets are used to practice:

- Reading CSV files
- Selecting columns
- Filtering rows
- Sorting data
- Finding unique values
- Counting values
- Statistical operations
- Data cleaning

---

## 📂 Repository Contents

The repository includes:

- `Series.py` – Pandas Series practice
- `Data.py` – Data-related Pandas operations
- `indexing.py` – Series indexing and selection
- `ImportantMethods` – Important Pandas methods
- `Datasets` – Practice datasets
- `screenSlots` – Supporting practice/material

---

## 🛠️ Technologies Used

- Python 🐍
- Pandas 🐼
- NumPy
- VS Code
- CSV datasets

---

## 💻 Installation

Make sure Python is installed.

Check Python:

```bash
python3 --version
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install Pandas:

```bash
python3 -m pip install pandas
```

Install NumPy:

```bash
python3 -m pip install numpy
```

---

## ▶️ How to Run

Clone the repository:

```bash
git clone git@github.com:PrathmeshSurwase6250/Python_Pandas_Series.git
```

Move into the project:

```bash
cd Python_Pandas_Series
```

Run a Python file:

```bash
python3 Series.py
```

For indexing practice:

```bash
python3 indexing.py
```

---

## 🧠 Learning Objectives

Through this repository, I am practicing:

- Python data analysis
- Pandas Series
- Data indexing
- Data selection
- Data filtering
- Sorting
- Data cleaning
- CSV file handling
- Statistical operations
- Real-world datasets

---

## 📈 Learning Progress

```text
Python Basics
      ↓
NumPy
      ↓
Pandas Series
      ↓
Pandas DataFrame
      ↓
Data Cleaning
      ↓
Data Analysis
      ↓
Data Visualization
      ↓
Machine Learning
```

---

## 🎯 Future Learning

The next topics planned for Pandas and Data Analysis include:

- Pandas DataFrame
- DataFrame indexing
- Selecting rows and columns
- Filtering data
- Missing data handling
- `groupby()`
- `merge()`
- `join()`
- `concat()`
- Pivot tables
- Data cleaning
- Data visualization
- Matplotlib
- Seaborn
- Exploratory Data Analysis (EDA)

---

## 📌 Purpose

This repository is created as part of my **Python and Data Science learning journey**.

The main goal is to build strong practical knowledge of Pandas by solving problems and working with real datasets.

---

## 👨‍💻 Author

**Prathmesh Surwase**

Computer Engineering Student

GitHub: [PrathmeshSurwase6250](https://github.com/PrathmeshSurwase6250)

---

## ⭐ If You Find This Repository Useful

Feel free to **star ⭐ the repository** and use the examples for your own Pandas practice.

Happy Coding! 🐍🐼
