from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.svm import SVR
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, MinMaxScaler
def predict_svr(X, Y):

    X_train, X_test, Y_train, Y_test =\
        train_test_split(X, Y, test_size=0.05, shuffle=False, random_state=0x17250972)

    params = {
        "svr__kernel": ["rbf"],
        "svr__gamma": ["scale"],
        "svr__C": [0.3, 0.4, 0.5, 0.7, 0.95, 1.0, 1.05, 1.1, 1.2],
        "svr__epsilon": [0.01, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.9]
    }
    clf = GridSearchCV(make_pipeline(StandardScaler(with_mean=False), SVR()), params)
    clf.fit(X_train, Y_train)
    print("Best parameter (CV score=%0.3f):" % clf.best_score_)
    print(clf.best_params_)
    print(clf.score(X_test, Y_test))

    return clf.predict(X)