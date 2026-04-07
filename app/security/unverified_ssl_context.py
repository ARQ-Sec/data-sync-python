import ssl

def build_context():
    return ssl._create_unverified_context()
