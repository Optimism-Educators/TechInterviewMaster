# Data Science Project Template

## Project Structure
```
data-science-project-template/
├── .gitignore
├── README.md
├── LICENSE
├── requirements.txt
├── /data
│   ├── raw/                # Original data
│   ├── processed/          # Cleaned data
│   └── external/           # Third-party data
├── /notebooks
│   ├── 01_EDA.ipynb
│   ├── 02_FeatureEngineering.ipynb
│   └── 03_Modeling.ipynb
├── /src
│   ├── data_loader.py
│   ├── preprocess.py
│   ├── train_model.py
│   └── evaluate.py
├── /models
│   └── model.pkl
├── /tests
│   └── test_preprocess.py
```

## Key Files
- **README.md**: Overview of the project.
- **requirements.txt**: Python dependencies.
- **notebooks/**: Jupyter notebooks for analysis.
- **src/**: Scripts for data processing and modeling.
- **data/**: Contains raw, processed, and external data.
- **models/**: Stores trained models.
- **tests/**: Contains test scripts.

## Usage
1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Use the notebooks for exploratory data analysis and modeling.
4. Run scripts in the `src/` folder for data processing and training.

---

### Example Workflow
1. Place raw data in the `data/raw/` folder.
2. Use `notebooks/01_EDA.ipynb` for exploratory data analysis.
3. Preprocess data using `src/preprocess.py`.
4. Train models using `src/train_model.py`.
5. Evaluate models using `src/evaluate.py`.
6. Save trained models in the `models/` folder.