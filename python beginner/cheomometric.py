# ==============================
# 1. IMPORT LIBRARIES
# ==============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, KFold, cross_val_predict
from sklearn.cross_decomposition import PLSRegression
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, r2_score

# ==============================
# 2. LOAD DATA
# ==============================
df = pd.read_excel("chemometric values 3.xlsx")

# Clean data
df['dextromethorphan µg/mL'] = pd.to_numeric(df['dextromethorphan µg/mL'], errors='coerce')
df['bupropion µg/mL'] = df['bupropion µg/mL'].astype(str).str.replace(':','')
df['bupropion µg/mL'] = pd.to_numeric(df['bupropion µg/mL'], errors='coerce')

df = df.dropna()

# Features (UV absorbance)
X = df.iloc[:,3:].values

# Targets
y = df[['dextromethorphan µg/mL','bupropion µg/mL']].values

# ==============================
# 3. TRAIN TEST SPLIT
# ==============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==============================
# 4. DEFINE MODELS
# ==============================

# PLS
pls = PLSRegression(n_components=5)

# PCR
pca = PCA(n_components=5)
lr = LinearRegression()

# Ridge
ridge = Ridge(alpha=1.0)

# ANN (MLP)
mlp = MLPRegressor(hidden_layer_sizes=(50,50), max_iter=5000, random_state=42)

# ==============================
# 5. TRAIN MODELS
# ==============================
pls.fit(X_train, y_train)

X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)
lr.fit(X_train_pca, y_train)

ridge.fit(X_train, y_train)
mlp.fit(X_train, y_train)

# ==============================
# 6. PREDICTIONS
# ==============================
y_pls_cal = pls.predict(X_train)
y_pls_pred = pls.predict(X_test)

y_pcr_pred = lr.predict(X_test_pca)
y_ridge_pred = ridge.predict(X_test)
y_mlp_pred = mlp.predict(X_test)

# ==============================
# 7. ERROR METRICS
# ==============================
def rmse(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

# Cross-validation
cv = KFold(n_splits=5, shuffle=True, random_state=42)
y_pls_cv = cross_val_predict(pls, X_train, y_train, cv=cv)

RMSEC = rmse(y_train, y_pls_cal)
RMSECV = rmse(y_train, y_pls_cv)
RMSEP = rmse(y_test, y_pls_pred)

print("RMSEC:", RMSEC)
print("RMSECV:", RMSECV)
print("RMSEP:", RMSEP)

# ==============================
# 8. RESIDUAL PLOT
# ==============================
residuals = y_test - y_pls_pred

plt.figure()
plt.scatter(y_pls_pred[:,0], residuals[:,0])
plt.axhline(0, linestyle='--')
plt.xlabel("Predicted")
plt.ylabel("Residuals")
plt.title("Residual Plot (PLS - Dextromethorphan)")
plt.show()

# ==============================
# 9. CORRELATION HEATMAP
# ==============================
corr_matrix = np.corrcoef(X.T)

plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, cmap="viridis")
plt.title("Correlation Heatmap (UV Spectra)")
plt.show()

# ==============================
# 10. MEAN & RSD
# ==============================
mean_vals = np.mean(y, axis=0)
std_vals = np.std(y, axis=0)
rsd_vals = (std_vals / mean_vals) * 100

table = pd.DataFrame({
    "Compound": ["Dextromethorphan", "Bupropion"],
    "Mean": mean_vals,
    "RSD (%)": rsd_vals
})

print(table)

# ==============================
# 11. MODEL COMPARISON TABLE
# ==============================
results = pd.DataFrame({
    "Model": ["PLS", "PCR", "Ridge", "ANN"],
    "RMSE": [
        rmse(y_test, y_pls_pred),
        rmse(y_test, y_pcr_pred),
        rmse(y_test, y_ridge_pred),
        rmse(y_test, y_mlp_pred)
    ],
    "R2": [
        r2_score(y_test, y_pls_pred),
        r2_score(y_test, y_pcr_pred),
        r2_score(y_test, y_ridge_pred),
        r2_score(y_test, y_mlp_pred)
    ]
})

print(results)