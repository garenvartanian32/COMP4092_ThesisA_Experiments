import tensorflow as tf

def slicenet_middle(inputs_encoded, targets, target_space_emb, mask, hparams):
    # Define your model architecture here
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])

    # Compile the model
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    # Train the model
    model.fit(inputs_encoded, targets, epochs=5)

    # Return the model
    return model