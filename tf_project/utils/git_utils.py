import os
import subprocess


def get_current_commit_id():
    sha_bytes = subprocess.check_output(["git", "rev-parse", "HEAD"]).strip()
    sha_str = str(sha_bytes, 'utf-8')

    return sha_str


def save_current_commit_id(save_dir):
    commit_id = get_current_commit_id()

    id_log_path = os.path.join(save_dir, "git_commit_id.txt")

    text_file = open(id_log_path, "w")
    text_file.write(commit_id)
    text_file.close()
