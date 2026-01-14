from .base import ma
from ..models import Project, Image


class ImageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Image


class ProjectSchema(ma.SQLAlchemyAutoSchema):
    images = ma.Nested(ImageSchema, many=True)

    class Meta:
        model = Project
        include_relationships = True
        load_instance = True
        include_fk = True
