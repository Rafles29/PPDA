import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras.optimizers import Adam
from sklearn.preprocessing import MinMaxScaler

def predict_lstm(X, Y, steps=5):

    scaler_x = MinMaxScaler()
    scaler_y = MinMaxScaler()

    X_sc = scaler_x.fit_transform(X)
    y_sc = scaler_y.fit_transform(Y.values.reshape(-1, 1))

    features = X.shape[1]
    X_shaped = np.reshape(X_sc, newshape=(-1, steps, features))
    y_shaped = np.reshape(y_sc, newshape=(-1, steps, 1))
    assert X_shaped.shape[0] == y_shaped.shape[0]

    model = Sequential()
    model.add(LSTM(15, return_sequences=True))
    model.add(Dense(units=10, activation="relu"))
    model.add(Dense(units=1, activation="linear"))
    adam = Adam(lr=0.01)
    model.compile(optimizer=adam, loss="mse")

    model.fit(X_shaped, y_shaped, epochs=20, use_multiprocessing=True, batch_size=8, verbose=0)
    y_pred = model.predict(X_shaped)

    return scaler_y.inverse_transform(y_pred.reshape(-1, 1))
