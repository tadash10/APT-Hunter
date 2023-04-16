import subprocess

def block_traffic(ip_address):
    """
    Blocks all traffic from a given IP address using iptables.
    """
    subprocess.check_call(['iptables', '-A', 'INPUT', '-s', ip_address, '-j', 'DROP'])
    print(f"All traffic from {ip_address} has been blocked.")
    
    #To add the block_traffic function to the main repository script through CLI in Bash, you can follow these steps:

    #Open your terminal and navigate to the directory where your main repository script is located.

    #Open the script in your preferred text editor.

    #Add the block_traffic function to the script.

    #Save and close the script.

    #Open your terminal and navigate to the directory where your main repository script is located.

    #Run the following command to make the script executable: chmod +x main_script.py.

    #Run the script using the following command: ./main_script.py.

    #The block_traffic function will now be available in the main repository script for you to use. You can call the function from within the script or from the command line by passing in the appropriate arguments.
     
