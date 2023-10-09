import os
import configparser

# Create a configuration object.
config = configparser.ConfigParser()

# Load the configuration object from a file.
config.read('config.ini')

# Get the API key from the configuration object.
api_key = config['API']['replicate_api_key']

os.environ["REPLICATE_API_TOKEN"] = api_key

import replicate
output = replicate.run(
    "daanelson/minigpt-4:b96a2f33cc8e4b0aa23eacfce731b9c41a7d9466d9ed4e167375587b54db9423",
    input={"image": open("data\earring.jpg", "rb"),
           "prompt": "the image is about jewellery, the description needed for the image must be in the format of "}
)
print(output)

