import subprocess

def quarantine_container(container_id):
    """
    Quarantines a suspicious Docker container by stopping it and removing its network access.
    """
    # Stop the container
    subprocess.check_call(['docker', 'stop', container_id])

    # Remove the container's network access
    subprocess.check_call(['docker', 'network', 'disconnect', '-f', 'bridge', container_id])

    print(f"Container {container_id} has been quarantined.")
    
    
