# Flask MVC Template

This template shows minimal Flask (and its extensions) configuration to create simple backend API with admin panel.

## MVC Architecture

This project follows the Model-View-Controller (MVC) architectural pattern with clear separation of concerns:

### Models
- Located in `/src/models/`
- Define data structures and database schema
- Built with SQLAlchemy ORM
- Base model provides the SQLAlchemy connection (`db_conn`)

### Views
- Admin views in `/src/admin/`
- HTML templates in `/src/templates/`
- API responses formatted using Marshmallow schemas in `/src/schemas/`

### Controllers
- Located in `/src/controllers/`
- Handle HTTP requests and route to appropriate services
- Only interact with the service layer, never directly with models or repos
- Implemented as Flask blueprints

### Additional Layers

#### Repositories
- Located in `/src/repos/`
- Handle database operations
- Utilize the Flask-SQLAlchemy session which is scoped to the current request context
- No need to explicitly inject DB sessions due to this design

#### Services
- Located in `/src/services/`
- Contain business logic
- Receive repository instances as dependencies
- Services are accessible via Flask app context (`app.service_name`)
- Handle transaction management with the `@transactional` decorator

This architecture leverages Flask's request context system, where the SQLAlchemy session is automatically managed within each request lifecycle. As noted in `models/base.py`, this eliminates the need to manually inject DB sessions into repositories, making the code cleaner and less prone to session management errors.

## Start Locally

1. Create *.env* file (see: [.env.example](.env.example))
2. Install API dependencies: ```pip install -r requirements.txt```
3. Start API: ```python run_api.py```

## Deploy

1. Create *.env* file (see: [.env.example](.env.example))
2. Create virtual environment
3. Install dependencies: ```pip install -r requirements.txt```
4. Create service file (see: [api.service](service_file\api.service))
5. Configure *systemd* service:
    - ```sudo systemctl daemon-reload```
    - ```sudo systemctl enable api.service```
    - ```sudo systemctl start api.service```
6. Configure *nginx*

## Restart

Restart API: ```sudo systemctl restart api.service```

## Logs

View journalctl logs: ```sudo journalctl -u api.service -n 50```

## Backup

Dump DB: ```scp root@your-server:/srv/flask-mvc-template/src/mvc.db ~/local_backup/mvc.db```

## Migrations

1. Activate venv: ```source .venv/bin/activate```
2. Create migration from *src*: ```flask db migrate -m "Describe your migration"```
3. Run migration from *src*: ```flask db upgrade```