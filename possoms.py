import pandas as pd
df = pd.read_csv("possum.csv")
df.sample(5, random_state=44)
df = df.dropna()
X = df.drop(["case", "site", "Pop", "sex"], axis=1)
y = df["sex"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=44)

from sklearn.ensemble import RandomForestClassifier
rf_model = RandomForestClassifier(n_estimators=50, max_features="sqrt", random_state=44)
rf_model.fit(X_train, y_train)
predictions = rf_model.predict(X_test)

importances = rf_model.feature_importances_
columns = X.columns
i=0
while i < len(columns):
    print(f"The importance of feature '{columns[i]}' is {round(importances[i] * 100,2)}%.")
    i+=1
new_possum = [[7.0,83.2,54.3,81,37,70,46.3,14.7,25,32]]
print(rf_model.predict(new_possum))