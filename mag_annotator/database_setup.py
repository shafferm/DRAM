from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# TODO: Do all processing of descriptions here

Base = declarative_base()

KEGG_DESCRIPTION_TABLE_NAME = 'kegg_description'


class KeggDescription(Base):
    __tablename__ = KEGG_DESCRIPTION_TABLE_NAME

    id = Column(String(20), primary_key=True, nullable=False)

    description = Column(String(100000))

    @property
    def serialize(self):
        return {
            'kegg_id': self.id,
            'kegg_description': self.description,
        }


UNIREF_DESCRIPTION_TABLE_NAME = 'uniref_description'


class UniRefDescription(Base):
    __tablename__ = UNIREF_DESCRIPTION_TABLE_NAME

    id = Column(String(20), primary_key=True, nullable=False)

    description = Column(String(1000))

    @property
    def serialize(self):
        return {
            'kegg_id': self.id,
            'kegg_description': self.description,
        }


PFAM_DESCRIPTION_TABLE_NAME = 'pfam_description'


class PfamDescription(Base):
    __tablename__ = PFAM_DESCRIPTION_TABLE_NAME

    id = Column(String(12), primary_key=True, nullable=False)

    description = Column(String(1000))

    @property
    def serialize(self):
        return {
            'pfam_id': self.id,
            'pfam_description': self.description,
        }


DBCAN_DESCRIPTION_TABLE_NAME = 'dbcan_description'


class DbcanDescription(Base):
    __tablename__ = DBCAN_DESCRIPTION_TABLE_NAME

    id = Column(String(30), primary_key=True, nullable=False)

    description = Column(String(1000))

    @property
    def serialize(self):
        return {
            'dbcan_id': self.id,
            'dbcan_description': self.description,
        }


VIRAL_DESCRIPTION_TABLE_NAME = 'viral_description'


class ViralDescription(Base):
    __tablename__ = VIRAL_DESCRIPTION_TABLE_NAME

    id = Column(String(14), primary_key=True, nullable=False)

    description = Column(String(1000))

    @property
    def serialize(self):
        return {
            'viral_id': self.id,
            'viral_description': self.description,
        }


PEPTIDASE_DESCRIPTION_TABLE_NAME = 'peptidase_description'


class PeptidaseDescription(Base):
    __tablename__ = PEPTIDASE_DESCRIPTION_TABLE_NAME

    id = Column(String(10), primary_key=True, nullable=False)

    description = Column(String(1000))

    @property
    def serialize(self):
        return {
            'peptidase_id': self.id,
            'peptidase_description': self.description,
        }


def create_description_db(db_loc):
    engine = create_engine('sqlite:///%s' % db_loc)
    Base.metadata.create_all(engine)


TABLE_NAME_TO_CLASS_DICT = {KEGG_DESCRIPTION_TABLE_NAME: KeggDescription,
                            UNIREF_DESCRIPTION_TABLE_NAME: UniRefDescription,
                            PFAM_DESCRIPTION_TABLE_NAME: PfamDescription,
                            DBCAN_DESCRIPTION_TABLE_NAME: DbcanDescription,
                            VIRAL_DESCRIPTION_TABLE_NAME: ViralDescription,
                            PEPTIDASE_DESCRIPTION_TABLE_NAME: PeptidaseDescription}
