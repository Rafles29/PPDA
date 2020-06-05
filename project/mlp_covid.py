from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


def predict_mlp(X, Y):

    # define wider model
    X_values = X.values
    Y_values = Y.values
    # define wider model
    def wider_model():
        # create model
        model = Sequential()
        model.add(Dense(20, input_dim=3, kernel_initializer='normal', activation='relu'))
        model.add(Dense(1, kernel_initializer='normal'))
        # Compile model
        model.compile(loss='mean_squared_error', optimizer='adam')
        return model
    # evaluate model with standardized dataset
    estimators = []
    estimators.append(('standardize', StandardScaler()))
    estimators.append(('mlp', KerasRegressor(build_fn=wider_model, epochs=100, batch_size=5, verbose=0)))
    pipeline = Pipeline(estimators)
    kfold = KFold(n_splits=10)
    results = cross_val_score(pipeline, X, Y, cv=kfold)
    print("Wider: %.2f (%.2f) MSE" % (results.mean(), results.std()))
    pipeline.fit(X_values, Y_values)
    return pipeline.predict(X_values)