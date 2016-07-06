from Products.Archetypes.Widget import TypesWidget
from Products.Archetypes.Registry import registerWidget


class UploadWidget(TypesWidget):
    """ Quick Upload Widget via drag&drop.
    Custom properties:
      mediaupload -- Allowed file extensions e.g.: '*.gif; *.tif; *.jpg',
                     empty for all.
                     Default: '*.txt; *.csv; *.tsv; *.tab'
    """
    _properties = TypesWidget._properties.copy()
    _properties.update({
        'macro': "upload_widget",
        'helper_js': (
            '++resource++cs.pfg.multifile.jqueryfiler/js/jquery.filer.min.js',
        ),
        'helper_css': (
            '++resource++cs.pfg.multifile.jqueryfiler/css/jquery.filer.css',
            '++resource++cs.pfg.multifile.jqueryfiler/css/jquery.filer-dragdropbox-theme.css',

        )
    })


registerWidget(
    UploadWidget,
    title='Multiple File Upload',
    description=("Allows you to drag&drop files directly "
                 "from your computer's Desktop")
)
