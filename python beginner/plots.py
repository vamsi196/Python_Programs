import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

# 1. Load and Clean Data
file_path = "chemometric values 3(1).xlsx"

try:
    df = pd.read_excel(file_path)
    print("✅ Excel file loaded successfully.")
except Exception as e:
    print(f"❌ Error: {e}")
    exit()

# Data Cleaning
df['dextromethorphan µg/mL'] = pd.to_numeric(df['dextromethorphan µg/mL'], errors='coerce')
df['bupropion µg/mL'] = df['bupropion µg/mL'].astype(str).str.replace(':', '')
df['bupropion µg/mL'] = pd.to_numeric(df['bupropion µg/mL'], errors='coerce')
df = df.dropna(subset=['dextromethorphan µg/mL', 'bupropion µg/mL', '230nm'])

X = df.iloc[:, 3:]  
y = df[['dextromethorphan µg/mL', 'bupropion µg/mL']]
wavelengths = X.columns

# 2. Train Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pls = PLSRegression(n_components=5)
pls.fit(X_train, y_train)
y_pred = pls.predict(X_test)

# 3. Plotting
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
plt.subplots_adjust(hspace=0.4)

# UV Spectra
for i in range(len(X)):
    axes[0, 0].plot(wavelengths, X.iloc[i, :], alpha=0.3)
axes[0, 0].set_title("UV Absorption Spectra")

# Loadings
coeffs = pls.coef_.T if pls.coef_.shape[0] == 2 else pls.coef_
axes[0, 1].plot(wavelengths, coeffs[:, 0], label='Dextromethorphan')
axes[0, 1].plot(wavelengths, coeffs[:, 1], label='Bupropion')
axes[0, 1].set_title("Wavelength Importance")
axes[0, 1].legend()

# Prediction Plots
for i, name in enumerate(['Dextromethorphan', 'Bupropion']):
    ax = axes[1, i]
    ax.scatter(y_test.iloc[:, i], y_pred[:, i])
    ax.plot([y_test.iloc[:,i].min(), y_test.iloc[:,i].max()], 
            [y_test.iloc[:,i].min(), y_test.iloc[:,i].max()], 'r--')
    ax.set_title(f"{name}: Actual vs Predicted")

plt.show()
