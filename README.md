# Community Events App Documentation

## Table of Contents

1. [Introduction](#introduction)
2. [Project Overview](#project-overview)
3. [System Architecture](#system-architecture)
   - [Client-Side Architecture](#client-side-architecture)
   - [Server-Side Architecture](#server-side-architecture)
4. [Technology Stack](#technology-stack)
5. [Installation and Setup](#installation-and-setup)
6. [Usage Guide](#usage-guide)
   - [Event Creation](#event-creation)
   - [Event RSVP](#event-rsvp)
   - [Event Review](#event-review)
7. [Code Structure](#code-structure)
   - [Directory Structure](#directory-structure)
   - [Key Files](#key-files)
8. [Database Schema](#database-schema)
9. [API Reference](#api-reference)
10. [Testing](#testing)
11. [Deployment](#deployment)
12. [Maintenance and Support](#maintenance-and-support)
13. [Contributors](#contributors)
14. [Appendix](#appendix)
   - [Troubleshooting](#troubleshooting)
   - [FAQs](#faqs)

---

## Introduction

Welcome to the Community Events App documentation! This document provides an overview of the project, its architecture, technology stack, installation instructions, usage guide, and other relevant information.

## Project Overview

The Community Events App is designed to facilitate the organization and management of local community events. It allows users to create events, RSVP to events, and provide reviews for events they attend.

## System Architecture

### Client-Side Architecture

The client-side architecture of the app is built using HTML, CSS, and JavaScript. It utilizes the Bootstrap framework for responsive design and user interface components.

### Server-Side Architecture

The server-side of the app is powered by Django, a high-level Python web framework. It follows a Model-View-Template (MVT) architecture, where models define the data structure, views handle the business logic, and templates render the user interface.

![image](https://github.com/SaiKrishnaIyer/Hackathon-3/assets/113880966/9a7ad9a6-232f-4721-9392-f2e27dfa723b)
![image](https://github.com/SaiKrishnaIyer/Hackathon-3/assets/113880966/4f0a88a5-b938-496a-bb20-f9c24d3cda65)


## Technology Stack

- Frontend: HTML, CSS, JavaScript, Bootstrap
- Backend: Python, Django
- Database: SQLite (for development), PostgreSQL (for production)
- Version Control: Git, GitHub
- Deployment: Heroku

## Installation and Setup

Follow the instructions in the README.md file of the project repository to install and set up the Community Events App on your local machine.

## Usage Guide

### Event Creation

1. Log in to the app.
2. Navigate to the "Create Event" page.
3. Fill in the event details and submit the form.

### Event RSVP

1. View the list of upcoming events.
2. Click on an event to view its details.
3. Fill in the RSVP form with your name and submit.

### Event Review

1. Attend an event.
2. Navigate to the event's detail page.
3. Fill in the review form with your rating and comments.

## Code Structure

### Directory Structure

- `events/`: Django app directory
  - `templates/`: HTML templates for rendering pages
  - `static/`: Static files like CSS, JavaScript, and images
  - `admin.py`: Django admin configuration
  - `models.py`: Django models defining the database schema
  - `views.py`: Django views handling request processing

### Key Files

- `manage.py`: Django project management script
- `settings.py`: Django project settings file
- `urls.py`: URL configuration for routing requests
- `views.py`: Business logic for handling user requests


## Database Schema

The database schema includes tables for events, users, reviews, and RSVPs. Refer to the database documentation for detailed schema information.

![image](https://github.com/SaiKrishnaIyer/Hackathon-3/assets/113880966/ac011467-c04e-44f4-bb44-5c07bb05bd2d)
![image](https://github.com/SaiKrishnaIyer/Hackathon-3/assets/113880966/0645d8fe-93e0-4564-8e15-736d964f3eff)
![image](https://github.com/SaiKrishnaIyer/Hackathon-3/assets/113880966/6febe67e-cc41-4ee6-b958-b14017a4b0e2)

## API Reference

The app provides RESTful APIs for creating, retrieving, updating, and deleting events. Refer to the API documentation for endpoints and usage.

## Testing

Unit tests and integration tests are implemented using Django's testing framework. Run tests using the `python manage.py test` command.

## Deployment

The app is deployed on Heroku for production. Follow the deployment guide in the README.md file for deploying to Heroku.

## Maintenance and Support

For maintenance and support inquiries, contact the project maintainers or refer to the project's GitHub repository for updates and bug fixes.

## Contributors

Acknowledge and list the contributors who have contributed to the project's development.

## Appendix

### Troubleshooting

Include troubleshooting tips and common issues encountered during installation or usage.

### FAQs

Provide answers to frequently asked questions related to the app.
