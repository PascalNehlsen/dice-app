# Dice Web App

A minimal Flask web application that displays a dice as an SVG, with customizable dice color via an environment variable.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Quickstart](#quickstart)
- [Usage](#usage)
    - [Run with Docker](#run-with-docker)
    - [Deployment](#deployment)

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

### Deployment

This GitHub Actions workflow automates the process of building, pushing, and deploying a Dockerized application whenever changes are pushed to the `main` branch.

#### Workflow Overview
- Trigger: The workflow is triggered on pushes to the main branch.
- Environment Variables: Utilizes environment variables for registry and image configuration.

#### Jobs
Build:

**Steps:**
- Set Up Docker Buildx: Prepares the environment for building multi-platform Docker images.
- Log into GHCR: Authenticates with the GitHub Container Registry using a Personal Access Token.
- Extract Metadata: Gathers Docker image metadata for tagging.
- Create .env File: Generates a .env file from an example and appends the current commit SHA.
- Build and Push Docker Image: Builds the Docker image and pushes it to GHCR with multiple tags.
- Upload Artifacts: Stores the .env and docker-compose.yml files for use in the deployment job.

Deploy:
**Steps:**
- Checkout Code: Retrieves the latest code from the repository.
- Download Artifacts: Fetches the deployment files from the build job.
- Copy Files via SCP: Transfers the .env and docker-compose.yml files to the remote server.
- Run Docker Commands via SSH: Connects to the remote server to update the Docker containers using docker-compose.
