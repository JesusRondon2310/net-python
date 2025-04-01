from os import getenv
from paramiko import SSHClient, AutoAddPolicy
from dotenv import load_dotenv

load_dotenv()


def init():
    host = getenv("SSH_HOST")
    port = getenv("SSH_PORT")
    user = getenv("SSH_USER")
    passwd = getenv("SSH_PASSWORD")
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(host, port, user, passwd)
    return client


def command(channel: SSHClient, cmd: str) -> tuple:
    _, stdout, stderr = channel.exec_command(cmd)
    output = stdout.read().decode()
    errors = stderr.read().decode()
    if errors != "":
        return (True, errors)
    return (False, output)


def exit_ssh(channel: SSHClient) -> None:
    channel.close()
