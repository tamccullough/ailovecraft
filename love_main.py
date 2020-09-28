# canpl statistics
# Todd McCullough 2020
import tensorflow as tf
from tensorflow import keras
import numpy as np
import os
import time

lovecraft_predict = tf.keras.models.load_model('model/lovecraft_predict.h5')

path_to_file = 'lovecraft.txt'# Read, then decode for py2 compat.
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
vocab = sorted(set(text))

vocab_size = len(vocab) # Length of the vocabulary in chars
embedding_dim = 256 # The embedding dimension
rnn_units = 1024 # Number of RNN units

# Creating a mapping from unique characters to indices
char2idx = {u:i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)

text_as_int = np.array([char2idx[c] for c in text])

def generate_text(start_string,temp):
    # Evaluation step (generating text using the learned model)

    # Number of characters to generate
    num_generate = 1000

    # Converting our start string to numbers (vectorizing)
    input_eval = [char2idx[s] for s in start_string]
    input_eval = tf.expand_dims(input_eval, 0)

    # Empty string to store our results
    text_generated = []

    # Low temperatures results in more predictable text.
    # Higher temperatures results in more surprising text.
    # Experiment to find the best setting.
    temperature = temp

    # Here batch size == 1
    lovecraft_predict.reset_states()
    for i in range(num_generate):
        predictions = lovecraft_predict(input_eval)
        # remove the batch dimension
        predictions = tf.squeeze(predictions, 0)

        # using a categorical distribution to predict the character returned by the model
        predictions = predictions / temperature
        predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()

        # We pass the predicted character as the next input to the model
        # along with the previous hidden state
        input_eval = tf.expand_dims([predicted_id], 0)

        text_generated.append(idx2char[predicted_id])
        send_text = ''.join(text_generated)
        #send_text = send_text.split('\n')[0]

    #return (start_string + ''.join(text_generated))
    return send_text#(start_string + ''.join(text_generated))
