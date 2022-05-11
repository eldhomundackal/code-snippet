def ssh_key_t0_string(file_path):
    with open(file_path, 'r') as f:
        key = f.readlines()
        value = '\n'.join([line.strip() for line in key])
        return repr(value)

