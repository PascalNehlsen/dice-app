# Dice Web App

A minimal Flask web application that displays a dice as an SVG, with customizable dice color via an environment variable.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Quickstart](#quickstart)
- [Usage](#usage)
    - [Run with Docker](#run-with-docker)

## Features

- Renders a random dice using SVG in the browser.
- Specific Variables can be customized by variables in the example.env

## Requirements

- Python 3.10.5

## Quickstart

1. **Install dependencies:**
   ```bash
    git clone https://github.com/PascalNehlsen/dice-app.git
    cd dice-app
   ```

1. **Create and activate a virtual environment:**
   ```bash
    python -m venv venv
    source venv/bin/activate
    # or
    venv\Scripts\activate
   ```

1. **Install the requirements:**
   ```bash
    pip install -r requirements.txt
   ```

1. **Start the Flask app:**
   ```bash
    flask --app dice run
   ```

1. **Open in your browser:**
   ```bash
    http://localhost:5000/
   ```

## Usage

1. **You can customize the app by changing the variable in [example.env](./example.env). For example:**
   ```bash
    OWNER="MR. X"
    BG_COLOR="#0c7077"
    DICE_COLOR="#eb856b"
   ```

1. **If you want to use your variables:**
   ```bash
    cp example.env .env
   ```

1. **Start the Flask app:**
   ```bash
    flask --app dice run
   ```

### Run with Docker

1. **You can also run the app using Docker with the [Dockerfile](./Dockerfile):**
   ```bash
    docker build -t dice-app .
    docker run -p 5000:5000 dice-app
   ```

1. **Open in your browser:**
   ```bash
    http://localhost:5000/
   ```
