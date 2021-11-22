from tensorflow.keras import models, layers

def initialize_model():
    ### Model architecture
    model = models.Sequential()
    model.add(layers.Dense(5, activation='relu', input_dim=2))
    model.add(layers.Dense(1, activation='sigmoid'))
    ### Model optimization : Optimizer, loss and metric
    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    return model
