import configparser

# Create a configuration object.
config = configparser.ConfigParser()

# Load the configuration object from a file.
config.read('config.ini')

# Get the API key from the configuration object.
api_key = config['API']['OPENAI_API_KEY_CILANS']

print(api_key)