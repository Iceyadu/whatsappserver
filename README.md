```markdown
# WhatsApp API Server - Django Project Structure

## Project Directory Contents

The `whatsappapi` project directory includes the following key components:

- `chat` Directory**: Contains the main application logic.
- `db.sqlite3`: The SQLite database file used by the project.
- `README.md`: An existing README file, which might require updates or replacement.
- `manage.py`: A Django script for performing various administrative tasks.
- `whatsappapi` Directory**: Likely includes settings and configuration for the project.

## Overview of the WhatsApp API Server

This Django project is designed to emulate the functionalities of WhatsApp, enabling features such as creating chat rooms, managing chatrooms, sending messages, and handling attachments.

## Getting Started with the Project

### Prerequisites

You will need to have the following installed:

- Python 3.x
- Django
- Django REST Framework
- Channels and Channels Redis
- Daphne
- Redis
- RabbitMQ

### Installation Steps

1. Setting Up the Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. **Installing Required Packages**:
   ```bash
   pip install django
   pip install djangorestframework
   pip install channels channels_redis
   pip install daphne
   ```

3. **Installing and Configuring Redis and RabbitMQ**:
   - Install Redis locally.
   - Configure RabbitMQ:
     ```bash
     sudo rabbitmqctl add_user myuser mypassword
     sudo rabbitmqctl add_vhost myvhost
     sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"
     ```

### Running the Project

1. **Database Migration**:
   ```bash
   python manage.py migrate
   ```

2. **Creating a Superuser (Optional)**:
   ```bash
   python manage.py createsuperuser
   Username: yadu
   Email: yadu.guluma@gmail.com
   Password: 123456
   ```

3. **Starting the Server**:
   ```bash
   python manage.py runserver
   ```
  
  3. **Starting Daphne**:
  Daphne is an HTTP, HTTP2, and WebSocket protocol server for ASGI and ASGI-HTTP,  developed as part of the Django Channels project. It serves as an interface server for ASGI applications, allowing them to communicate over the network. We can use any unused ports here. 
   ```bash
   daphne whatsappapi.asgi:application -p 9004
   ```

## API Endpoints

- **Create Chatroom**: POST `/api/chatroom/create`
- **List Chatrooms**: GET `/api/chatrooms`
- **Enter Chatroom**: POST `/api/chatroom/enter/`
	   -   room_id: 
       -   	user_id:
- **Leave Chatroom**: POST `/api/chatroom/leave/`
		-   room_id: 
       -   	user_id: 
- **List Messages**: GET `/api/messages/`


## Infrastructure and Architecture

- Backend powered by Python and Django.
- API development with Django REST Framework.
- Real-time chat features using Channels and Channels Redis.
- RabbitMQ as the message broker service.
- SQLite database with a structured RDB schema.
- Project follows `controller-service-entity-repository` structure:
  - `controller`: Manages requests and responses.
  - `service`: Implements business logic.
  - `repository`: Handles database queries.
  - `entity`: Models the database.

## WebSocket Usage

- WebSocket is utilized for the chat feature.
- Users in a chatroom are connected via WebSocket for real-time interaction.

## Development Notes

- Due to time constraints, not all features and tasks could be fully tested or included. The focus was on showcasing key components and required skills.
