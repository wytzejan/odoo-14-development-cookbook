def migrate(cr, version):
    cr.execute('ALTER TABLE library_book RENAME COLUMN date_release TO date_release_char')