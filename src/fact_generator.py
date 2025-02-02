import requests
from config import API_URL  # Import the API URL from the config file

def fetch_fact():
    """
    Fetches a random fact from the API.

    Returns:
        str: The fact as a string if successful, or an error message.
    """
    try: 
        response = requests.get(API_URL)
        #print(API_URL)
        #print(response.status_code)

        if response.status_code == 200:
            data = response.json()
            write_to("facts.txt", data)
            return data.get("text", "No fact available.")
        else:
            return f"Error: Received status code {response.status_code}"
    except requests.RequestException as e:
        return f"Error: Unable to fetch fact. Details: {e}"

def fetch_multiple_facts(numb):
  """
    Fetches multiple random facts from the API.

    Args:
        n (int): The number of random facts to fetch.

    Returns:
        list: A list of facts as strings if successful, or an error message.
    """
  facts = []
  for i in range(numb):
     facts.append(fetch_fact())
  return facts


def write_to(filename, data):
   with open(filename, "a+") as file:
      file.write(str(data) + "\n")
      file.close()

     
      
if __name__ == '__main__':
  print("Welcome to the Fact API \nHere is a fun fact for you: ")
  print(fetch_fact())
  print("Want more? Run the program again or generate multiple facts at once!")
