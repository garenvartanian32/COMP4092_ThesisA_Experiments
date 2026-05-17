import coremltools
from keras.models import Model
from keras.layers import Dense, Activation

# Assuming you have a Keras model
input_names = ['input_1']
output_names = ['softmax_output']

# Create a Keras model
input_layer = Input(shape=(3,))
output_layer = Dense(5)(input_layer)
output_layer = Activation('softmax')(output_layer)
model = Model(inputs=input_layer, outputs=output_layer)

# Convert the model
coreml_model = coremltools.converters.keras.convert(model, input_names=input_names, output_names=output_names)

# Save the CoreML model
coreml_model.save('keras_model.mlmodel')