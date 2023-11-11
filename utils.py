import os


def make_directory(directory, log_dir_name) -> str:
    log_dir_path = os.path.join(directory, log_dir_name)
    if os.path.exists(log_dir_path) is False:
        os.makedirs(log_dir_path)
    return log_dir_path
