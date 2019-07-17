from dqn.model import Model
from keras.models import Sequential, Model
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Activation, BatchNormalization, GlobalAveragePooling2D, merge
from keras.optimizers import Adam
from keras import backend as K
import numpy as np


class DuelingNet(Model):
    
    def build_model(self):
        model = Sequential()
        conv_1 = Conv2D(filters=32, kernel_size=(8,8), padding='same', activation='relu', 
                        strides=2, input_shape=self.state_size)

        conv_2 = Conv2D(filters=64, kernel_size=(4,4), padding='same', activation='relu',
                        strides=2)(conv_1)

        conv_3 = Conv2D(filters=64, kernel_size=(3,3), padding='same', activation='relu',
                        strides=2)(conv_2)

        flatten = Flatten()(conv_3)

        # Dueling Layer 1
        fc1 = Dense(512, activation='relu')(flatten)
        advantage = Dense(self.action_size)(fc1)
        # Dueling Layer 2
        fc2 = Dense(512, activation='relu')(flatten)
        value = Dense(self.action_size)(fc2)

        # Merge both layers
        policy = merge([advantage, value], mode=lambda x: x[0]-K.mean(x[0])+x[1], output_shape=(self.action_size,))
        model = Model(input=[input_layer], output=[policy])

        # compile the model
        model.compile(optimizer=Adam(lr=self.learning_rate), loss='mse')

        return model