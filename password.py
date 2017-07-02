from hashlib import sha256

def get_hex_password(service, password):
	return sha256(service + password).hexdigest()

print get_hex_password('gmail', 'otisw@rd')
hash_val = get_hex_password('wells fargo', 'er1nw@rd')

SECRET_KEY = 'b@tM@n'

def make_password(password, service):
    salt = get_hex_password(SECRET_KEY, service)[:20]
    hsh = get_hex_password(salt, password)
    return ''.join((salt, hsh))
print make_password(hash_val, 'slack')

ALPHABET = ('abcdefghijklmnopqrstuvwxyz'
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            '0123456789!@#$%^&*()-_')

def password(password, service, length=10):
    raw_hexdigest = make_password(password, service)

    # Convert the hexdigest into decimal
    num = int(raw_hexdigest, 16)

    # What base will we convert `num` into?
    num_chars = len(ALPHABET)

    # Build up the new password one "digit" at a time,
    # up to a certain length
    chars = []
    while len(chars) < length:
        num, idx = divmod(num, num_chars)
        chars.append(ALPHABET[idx])

    return ''.join(chars)
    # print password
    # print service

print password('popsicle', 'BofA')

def set_password(self, raw_password):
    import random
    algo = 'sha1'
    salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
    hsh = get_hexdigest(algo, salt, raw_password)
    self.password = '%s$%s$%s' % (algo, salt, hsh)


def check_password(raw_password, enc_password):
    """
    Returns a boolean of whether the raw_password was correct. Handles
    encryption formats behind the scenes.
    """
    algo, salt, hsh = enc_password.split('$')
    return hsh == get_hexdigest(algo, salt, raw_password)



