import tensorflow_hub as hub
# import tensorflow as tf


def initialize():
    # @param ["https://tfhub.dev/google/universal-sentence-encoder/4", "https://tfhub.dev/google/universal-sentence-encoder-large/5"]
    module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
    global embed
    embed = hub.load(module_url)


def embed(text):
    embedded_text = embed([text])
    return embedded_text
