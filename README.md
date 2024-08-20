
 # Python Endpoint with Flask

Simple endpoint using Flask that connects to an API and fetches information according to certain filters specified by the user.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install and test this project locally, follow these steps:

1. Clone the repository and open the folder:
	```
	git clone https://github.com/Saquial-g/Python_Endpoint.git
	cd Python_Endpoint
	```
2. Setup a new python environment and install the following packages:
	```
	pip install flask
	pip install requests
	```
	
## Usage

To start the endpoint for development, run the following command:
	```
	flask --app main run
	```
By default the endpoint will run on the address http://127.0.0.1:5000. It's important to consider that this is for development only, and shouldn't be deployed as a public server.

## Routes

This endpoint connects with the Rick & Morty API, so it has the following routes:

- (GET) {{base_url}}/character
- (POST) {{base_url}}/character
- (GET) {{base_url}}/location
- (POST) {{base_url}}/location
- (GET) {{base_url}}/episode
- (POST) {{base_url}}/episode

Both GET and POST endpoints use the same filters according to their category. These are the filters available:

- character: name, status, species, type, gender.
- location: name, type, dimension.
- episode: name, episode.

## Contributing

This was made as a technical test, but feel free to contribute as you wish:

1. Fork the repository.

2. Create a new branch for your feature or bugfix: 
	
	git checkout -b feature-name

3. Make your changes and commit them: 

	git commit -m "Description of your changes"

4. Push your changes to your fork: 

	git push origin feature-name

5. Open a pull request on the main repository.

## License

This project is licensed under the MIT License.

