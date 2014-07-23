from sqlalchemy import Table, Column, Integer, String, MetaData

meta = MetaData()

user = Table(
    'users', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String()),
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    user.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    user.drop()
