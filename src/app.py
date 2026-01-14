import os
from pathlib import Path
from flask import Flask
from flask_admin import Admin
from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate
from sqlalchemy.event import listens_for
from dotenv import load_dotenv
from .admin import (
    MyAdminIndexView,
    ImageAdmin,
    LeadAdmin,
    ProjectAdmin,
    SiteSettingsAdmin,
)
from .clients import NextRevalidateClient
from .controllers import lead_bp, project_bp, site_settings_bp, static_bp, uploads_bp
from .models import db_conn, Image, Lead, Project, SiteSettings, User
from .schemas import ma
from .services import LeadService, ProjectService, SiteSettingsService, UserService
from .repos import LeadRepo, ProjectRepo, SiteSettingsRepo, UserRepo

load_dotenv()

app = Flask(__name__)

# Environment settings
app.config["CSRF_SECRET"] = os.getenv("CSRF_SECRET")
app.config["DEBUG"] = bool(int(os.getenv("DEBUG")))
app.config["ADMIN_USERNAME"] = os.getenv("ADMIN_USERNAME")
app.config["ADMIN_PASSWORD"] = os.getenv("ADMIN_PASSWORD")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{Path(__file__).parent / 'mvc.db' }"
app.config["UPLOAD_FOLDER"] = Path(__file__).parent / "static" / "uploads"
app.config["FLASK_ADMIN_SWATCH"] = "solar"
app.config["FRONTEND_URL"] = os.getenv("FRONTEND_URL", "http://localhost:3000")

# CORS settings
RESOURCES = {
    r"/api/*": {
        "origins": ["http://smth.xyz", "https://smth.xyz"],
        "allow_headers": ["Content-Type", "Authorization"],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    },
}
if app.config["DEBUG"]:
    RESOURCES[r"/api/*"]["origins"] = ["*"]
CORS(app, resources=RESOURCES, supports_credentials=True)

# Application settings
app.static_folder = "static"
app.secret_key = app.config["CSRF_SECRET"]
app.register_blueprint(lead_bp, url_prefix="/api/leads")
app.register_blueprint(project_bp, url_prefix="/api/projects")
app.register_blueprint(site_settings_bp, url_prefix="/api/settings")
app.register_blueprint(static_bp, url_prefix="/api/static")
app.register_blueprint(uploads_bp, url_prefix="/api/uploads")

# Flask-SQLAlchemy initialization
db_conn.init_app(app)

# Flask-Migrate initialization
Migrate(app, db_conn)

# Flask-Marshmallow initialization
ma.init_app(app)

# Flask-Login initialization
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db_conn.session.get(User, int(user_id))


# Application context
with app.app_context():
    db_conn.create_all()
    next_client = NextRevalidateClient(app.config["FRONTEND_URL"])
    (lead_repo, project_repo, site_settings_repo, user_repo) = (
        LeadRepo(),
        ProjectRepo(),
        SiteSettingsRepo(),
        UserRepo(),
    )
    lead_service = LeadService(lead_repo)
    project_service = ProjectService(project_repo)
    site_settings_service = SiteSettingsService(site_settings_repo)
    user_service = UserService(user_repo)
    app.next_client = next_client
    app.lead_service = lead_service
    app.project_service = project_service
    app.site_settings_service = site_settings_service
    app.user_service = user_service
    admin_username = app.config["ADMIN_USERNAME"]
    admin_password = app.config["ADMIN_PASSWORD"]
    user_service.save_admin(
        admin_username=admin_username, admin_password=admin_password
    )

# Flask-Admin initialization
admin = Admin(
    app,
    name="Kvutsat Eitanim Admin",
    index_view=MyAdminIndexView(),
    base_template="_master.html",
    template_mode="bootstrap4",
)
admin.add_view(ImageAdmin(Image, db_conn.session))
admin.add_view(LeadAdmin(Lead, db_conn.session))
admin.add_view(ProjectAdmin(Project, db_conn.session))
admin.add_view(SiteSettingsAdmin(SiteSettings, db_conn.session))


# SQLAlchemy event listeners
@listens_for(Image, "after_delete")
def del_resource(mapper, connection, target):
    if target.filename:
        path = Path(app.config["UPLOAD_FOLDER"]) / target.filename
        if path.exists():
            path.unlink()


if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])
