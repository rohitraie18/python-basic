# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer

# Load the breast cancer dataset (binary classification)
data = load_breast_cancer()
X = data['data']
y = data['target']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display the dataset description
print(data['DESCR'])


# Plot the ROC curves
plt.figure(figsize=(8, 6))

# ROC curve for before cross-validation
plt.plot(fpr_before_cv, tpr_before_cv, color='blue', label=f'Before Cross-Validation (AUC = {auc_before_cv:.4f})')

# ROC curve for after cross-validation
plt.plot(fpr_after_cv, tpr_after_cv, color='green', label=f'After Cross-Validation (AUC = {auc_after_cv:.4f})')

# Diagonal line representing random classifier
plt.plot([0, 1], [0, 1], color='gray', linestyle='--')

# Plot settings
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve Comparison: Before vs After Cross-Validation')
plt.legend(loc="lower right")
plt.grid(True)  # Ensuring the grid is visible

# Show the plot
plt.show()
