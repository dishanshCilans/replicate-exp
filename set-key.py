import configparser

# Create a configuration object.
config = configparser.ConfigParser()

# Add the API key to the configuration object.
config['API'] = {'OPENAI_API_KEY_CILANS' : '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'}

# Save the configuration object to a file.
with open('config.ini', 'x') as configfile:
    config.write(configfile)