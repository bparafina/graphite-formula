import pytest
import os
import yaml
from testinfra.backend import paramiko

SSH_CONFIG = '.ssh-config'
SSH_CONFIG_MAP = {
    'KITCHEN_HOSTNAME': 'Hostname',
    'KITCHEN_USERNAME': 'User',
    'KITCHEN_PORT': 'Port',
    'KITCHEN_SSH_KEY': 'IdentityFile',
}


@pytest.fixture
def TestinfraBackend(request, tmpdir):
    ssh_config = ['Host {0}'.format(os.environ['KITCHEN_INSTANCE'])]
    for key in SSH_CONFIG_MAP.keys():
        if key in os.environ:
            ssh_config.append('{0} {1}'.format(SSH_CONFIG_MAP[key],
                                               os.environ[key]))
    ssh_config_file = tmpdir.join(SSH_CONFIG)
    ssh_config_file.write('\n'.join(ssh_config))
    return paramiko.ParamikoBackend(os.environ['KITCHEN_INSTANCE'],
                                    ssh_config=str(ssh_config_file), sudo=True)


@pytest.fixture
def Pillar():
    def get_pillar(pillar):
        pillar_path = os.path.join(os.path.dirname(__file__), 'fixtures', pillar)
        with open(pillar_path) as yaml_file:
            pillar_yaml = yaml.safe_load(yaml_file)
        return pillar_yaml
    return get_pillar
