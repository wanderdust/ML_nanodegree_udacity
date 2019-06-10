from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Activation, BatchNormalization, GlobalAveragePooling2D
from keras.optimizers import Adam

class Model:
  def __init__(self, state_size, action_size, learning_rate):
    self.state_size = state_size # size tuple
    self.action_size = action_size
    self.learning_rate = learning_rate

    self.model = self.build_model()

  def build_model(self):
    model = Sequential()
    model.add(Conv2D(filters=32, kernel_size=(8,8), padding='same', activation='relu', 
                      strides=4, input_shape=self.state_size))
    #model.add(MaxPooling2D(pool_size=2))

    model.add(Conv2D(filters=64, kernel_size=(4,4), padding='same', activation='relu',
                      strides=4))
    #model.add(MaxPooling2D(pool_size=2))

    model.add(Conv2D(filters=64, kernel_size=(3,3), padding='same', activation='relu',
                      strides=4,))
    #model.add(MaxPooling2D(pool_size=2))

    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.4))
    model.add(Dense(self.action_size, activation='softmax'))

    # compile the model
    model.compile(optimizer=Adam(lr=self.learning_rate), loss='mse')

    return model