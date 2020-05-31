# WUFOO API (POST)
<p align="center">
	<a href="https://forthebadge.com" alt="MADE WITH: PYTHON">
		<img src="https://forthebadge.com/images/badges/made-with-python.svg" />
	</a>
</p>
<p align="center">
	<a href="https://badgen.net" alt="Powered by: Python 3.8.2">
		<img src="https://badgen.net/badge/Powered%20by/Python%203.8.2/3570A0" />
	</a>
	<a href="https://opensource.org/licenses/MIT" alt="License: MIT">
		<img src="https://img.shields.io/badge/License-MIT-green.svg" />
	</a>
</p>
<p align="center">
  <strong>This project is written in Python and leverages the Wufoo API's POST method to add the entries in an existing Form.</strong>
</p>

## Usage

1. Clone the Repository
2. Change the name of config file 'config.example.py' to 'config.py' in the config directory.
3. Change the name of the 'description_entries.example.csv' to 'description_entries.csv' in the storage directory.
4. Make sure you have a Wufoo form created with the following fields.

![Wufoo_form](https://user-images.githubusercontent.com/29580265/68093597-53a53a00-fe65-11e9-8a2c-a3eeab5dc607.jpg)

5. Update the 'config.py' file with the file_name (i.e. storage/description_entries.csv in my case), Add your Wufoo subdomain in the BASE_URL, Add your API-KEY as the USERNAME, Any random PASSWORD, and FORM_HASH.
6. Make sure to make a GET request to know the id's defined for the Form fields.
```python
import requests

response = requests.get(self.__base_url + '/forms/' + self.__form_hash +'/fields.json', params={'q':'system=true'}, auth = self.__auth_values)
print(json.dumps(response.json(), indent = 4, sort_keys = True))
```
Which is in my case are "Field6,Field106,Field108,Field111,Field114,Field115,Field117,Field119" as written in the "description_entries.example.csv" 

7. To run the code write the following after navigating to the Wufoo_api directory:
```bash
python Request_controller.py
```

## License
[MIT](https://choosealicense.com/licenses/mit/)