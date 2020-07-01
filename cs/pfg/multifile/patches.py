# -*- coding: utf-8 -*-
from Products.PloneFormGen.content.formMailerAdapter import FormMailerAdapter
from zope.contenttype import guess_content_type

def our_get_attachments(self, fields, request):
    """Return all attachments uploaded in form.
    """

    from ZPublisher.HTTPRequest import FileUpload

    attachments = []

    for field in fields:

        if (field.isFileField() or field.Type() == "DataGrid Field") and (
            getattr(self, "showAll", True)
            or field.fgField.getName() in getattr(self, "showFields", ())
        ):
            if field.Type() == "DataGrid Field":
                # check if it contains any File columns
                for c in field.columnDefs:
                    if c["columnType"] == "File":
                        for row in request.form.get("%s" % field.__name__, None):
                            if row["orderindex_"] != "template_row_marker":
                                file = row[c["columnId"]]
                                if (
                                    file
                                    and isinstance(file, FileUpload)
                                    and file.filename != ""
                                ):
                                    file.seek(0)  # rewind
                                    data = file.read()
                                    filename = file.filename
                                    mimetype, enc = guess_content_type(
                                        filename, data, None
                                    )
                                    attachments.append(
                                        (filename, mimetype, enc, data)
                                    )
            elif field.Type() == 'FormMultiFileField':
                for file in request.form.get("%s" % field.__name__, []):

                    if (
                        file
                        and isinstance(file, FileUpload)
                        and file.filename != ""
                    ):
                        file.seek(0)  # rewind
                        data = file.read()
                        filename = file.filename
                        mimetype, enc = guess_content_type(
                            filename, data, None
                        )
                        attachments.append(
                            (filename, mimetype, enc, data)
                        )
            else:
                file = request.form.get("%s_file" % field.__name__, None)
                if file and isinstance(file, FileUpload) and file.filename != "":
                    file.seek(0)  # rewind
                    data = file.read()
                    filename = file.filename
                    mimetype, enc = guess_content_type(filename, data, None)
                    attachments.append((filename, mimetype, enc, data))
    return attachments

FormMailerAdapter.get_attachments = our_get_attachments


from logging import getLogger
log = getLogger(__name__)
log.info('Patching formMailerAdapter to allow MultiFileField values to be sent by email')
