#1
import sklearn
from sklearn.datasets import load_iris
from sklearn.metrics._plot import confusion_matrix
from sklearn.preprocessing import StandardScaler


iris = load_iris()

X =iris.data

print ("Forma setului de date:", X.shape)

print ("\nDenumirele atributelor:")
print(iris.feature_names) # <---

print("\nClasele:")
print(iris.target_names) #

#2
from sklearn.model_selection import train_test_split

y = iris.target

X_train, X_test, y_train, y_test =train_test_split(X ,y, test_size = 0.2 , random_state = 42)
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)
print(X)
print(y)

#3
import sklearn.preprocessing
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(X_train[5])

print(X_train_scaled[5])

#4
import sklearn.neighbors
knn = sklearn.neighbors.KNeighborsClassifier(n_neighbors=3)
knn.fit (X_train_scaled, y_train)
acuratete = knn.score (X_test_scaled, y_test)
print (acuratete)

#5















#6
from sklearn.metrics import confusion_matrix, classification_report

y_pred = knn.predict(X_test_scaled)
matrice = confusion_matrix(y_test, y_pred)
print(matrice)
report = classification_report(y_test, y_pred, target_names=iris.target_names)
print(report)


#7















