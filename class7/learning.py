from sklearn import linear_model
#see: http://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
X = [[1, 1, 1],
     [2, 2, 2],
     [1.5, 1.5, 1.5],
     [-5, -5, -5],
     [0, 0, -2],
     [-1, 0, 0]]
Y = [1, 1, 1, 0, 0, 0]

lr = linear_model.LogisticRegression()
lr.fit(X,Y)

lr.predict([3,3,3])
lr.predict([0,0,3])
lr.predict([0,0,0])

lr.predict_proba([3,3,3])
lr.predict_proba([0,0,3])
lr.predict_proba([0,0,0])

lr.coef_
lr.intercept_


from sklearn import tree
#see: http://scikit-learn.org/stable/modules/tree.html
dt = tree.DecisionTreeClassifier()
dt.fit(X,Y)

dt.predict([3,3,3])
dt.predict([0,0,3])
dt.predict([0,0,0])

dt.predict_proba([3,3,3])
dt.predict_proba([0,0,3])
dt.predict_proba([0,0,0])
 

from sklearn.datasets import load_iris
#see: http://scikit-learn.org/stable/datasets/index.html
iris = load_iris()

X = iris.data

Y = iris.target


lr.fit(X,Y)

dt.fit(X,Y)
















from sklearn import cross_validation
#see: http://scikit-learn.org/dev/modules/cross_validation.html
lr_scores = cross_validation.cross_val_score(lr, X, Y, cv=10)
dt_scores = cross_validation.cross_val_score(dt, X, Y, cv=10)


print "Iris (toy problem):"
print "lr accuracy: %0.2f (+/- %0.2f)" % (lr_scores.mean(), lr_scores.std() / 2)
print "dt accuracy: %0.2f (+/- %0.2f)" % (dt_scores.mean(), dt_scores.std() / 2)


from sklearn.datasets import load_boston
import numpy
boston = load_boston()
X = boston.data
Y = [ 1 if x > numpy.median(boston.target) else 0 for x in boston.target ]

lr.fit(X,Y)

dt.fit(X,Y)


from sklearn import cross_validation
#see: http://scikit-learn.org/dev/modules/cross_validation.html
lr_scores = cross_validation.cross_val_score(lr, X, Y, cv=10)
dt_scores = cross_validation.cross_val_score(dt, X, Y, cv=10)

print "Boston Housing:"
print "lr accuracy: %0.2f (+/- %0.2f)" % (lr_scores.mean(), lr_scores.std() / 2)
print "dt accuracy: %0.2f (+/- %0.2f)" % (dt_scores.mean(), dt_scores.std() / 2)
