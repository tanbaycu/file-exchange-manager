import requests

def upload_file(file_path):
    url = "https://store1.gofile.io/uploadFile"  
    files = {'file': open(file_path, 'rb')}
    
    try:
        response = requests.post(url, files=files)
        response.raise_for_status()
        response_json = response.json()
        if response_json.get("status") == "ok":
            print("Upload successful!")
            print("Download link:", response_json.get("data", {}).get("downloadPage"))
        else:
            print("Failed to upload file.")
            print("Error:", response_json.get("message"))
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except ValueError as e:
        print(f"Error decoding JSON response: {e}")


upload_file("path của bạn")

