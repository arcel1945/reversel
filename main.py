import subprocess
import json

ip_input = input("Enter the IP address: ")

curl_command = f'curl https://api.reverseipdomain.com/?ip={ip_input}'

response = subprocess.run(curl_command, shell=True, capture_output=True, text=True)

if response.returncode == 0:
    try:
        data = json.loads(response.stdout)
        
        if 'result' in data:
            file_name = f"{ip_input}.txt"
            
            with open(file_name, 'w') as file:
                for domain in data['result']:
                    print(domain)
                    file.write(domain + '\n')
            
            print(f"Output has been written to {file_name}")
        else:
            print("No 'result' key found in the response.")
    except json.JSONDecodeError:
        print("Failed to decode JSON response.")
else:
    print(f"Error occurred: {response.stderr}")
