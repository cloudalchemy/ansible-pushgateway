import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_directories(host):
    dirs = [
        "/var/lib/pushgateway"
    ]
    for dir in dirs:
        d = host.file(dir)
        assert not d.exists


def test_files(host):
    files = [
        "/var/lib/pushgateway/persistence"
    ]
    for file in files:
        f = host.file(file)
        assert not f.exists


def test_socket(host):
    sockets = [
        "tcp://127.0.0.1:9091"
    ]
    for socket in sockets:
        s = host.socket(socket)
        assert s.is_listening
