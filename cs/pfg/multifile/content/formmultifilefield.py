"""Definition of the FormMultiFileField content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.PloneFormGen.content.fields import FGFileField
# -*- Message Factory Imported Here -*-

from cs.pfg.multifile.interfaces import IFormMultiFileField
from cs.pfg.multifile.config import PROJECTNAME
from .widgets import UploadWidget
from Products.CMFCore.permissions import View

FormMultiFileFieldSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

FormMultiFileFieldSchema['title'].storage = atapi.AnnotationStorage()
FormMultiFileFieldSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(FormMultiFileFieldSchema, moveDiscussion=False)


class FormMultiFileField(FGFileField):
    """Mutiple File upload field"""
    implements(IFormMultiFileField)

    meta_type = "FormMultiFileField"
    content_icon = 'FileField.gif'
    typeDescription= 'A file field'

    # -*- Your ATSchema to Python Property Bridges Here ... -*-


    def __init__(self, oid, **kwargs):
        """ initialize class """

        FGFileField.__init__(self, oid, **kwargs)

        # set a preconfigured field as an instance attribute
        self.fgField = atapi.FileField(
            'fg_file_field',
            searchable=0,
            required=0,
            write_permission=View,
            accessor='nullAccessor',
            maxsize=0,
            validators=('isMaxSize',),
            widget=UploadWidget(
                mediaupload=[],
                typeupload=None,
            ),
            )

atapi.registerType(FormMultiFileField, PROJECTNAME)
