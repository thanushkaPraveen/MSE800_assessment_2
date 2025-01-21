import configparser

config = configparser. ConfigParser()

# Add the structure t o the file we will create
config.add_section('mysql')
config.set ('mysql', 'host', 'localhost')
config.set ('mysql', 'user', 'root')
config.set ('mysql', 'password', '')
config.set ('mysql', 'database', 'mydatabase')

# Write the new structure to a file using a relative path
with open("configfile.ini", 'w') as configfile:
    config.write(configfile)


