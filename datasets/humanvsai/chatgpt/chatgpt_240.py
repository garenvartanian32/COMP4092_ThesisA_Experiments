import subprocess

def delete_principal(principal):
    try:
        subprocess.run(['kadmin', '-p', 'admin/admin', '-w', 'password', '-q', f'delete_principal -force {principal}'])
    except subprocess.CalledProcessError:
        print(f"Failed to delete principal '{principal}'")
