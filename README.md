# Pokémon API Python

A Python project that retrieves Pokémon information using the [PokéAPI](https://pokeapi.co/).

## About

This program allows users to search for a Pokémon by name and retrieve information from an external REST API.

## Features

- Search Pokémon by name.
- Display Pokémon ID, height, and weight.
- List the Pokémon's types.
- Validate user input.
- Handle invalid Pokémon names and HTTP request errors.
- Set a request timeout to avoid waiting indefinitely.

## Technologies

- Python 3
- Requests
- REST APIs
- JSON

## Requirements

Python 3 and the `requests` library are required.

Install the dependency with:

```bash
python3 -m pip install requests
```

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/pokemon-api-python.git
   ```

2. Navigate to the project directory:

   ```bash
   cd pokemon-api-python
   ```

3. Install the dependencies:

   ```bash
   python3 -m pip install requests
   ```

4. Run the program:

   ```bash
   python3 main.py
   ```

5. Enter a Pokémon name when prompted.

## Example

```text
Enter the name of the Pokémon: pikachu
Name: pikachu
ID: 25
Height: 4
Weight: 60
Types:
- electric
```

## API Reference

This project uses the [PokéAPI Pokémon endpoint](https://pokeapi.co/docs/v2#pokemon).

## Learning Goals

This project was created to practice:

- Making HTTP requests with Python.
- Working with REST APIs and JSON responses.
- Handling exceptions and HTTP errors.
- Validating user input.

## Author

Created as part of my Python learning journey.
