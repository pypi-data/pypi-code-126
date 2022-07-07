from dataclasses import dataclass
from typing import Optional, List

class SchemaRequired(Exception):
    pass

@dataclass
class Table:
    '''
    You may establish a database and schema at the connection level
    but we want to know the table name for later
    '''
    table: str
    schema: Optional[str] = None
    database: Optional[str] = None

    def __post_init__(self) -> None:
        if self.database and not self.schema:
            raise SchemaRequired('Database name provided but schema missing')

    @property
    def fullname(self) -> str:
        '''
        As long as this raises when a database is provided but a schema isn't
        then it doesn't need to be any more complicated than this
        '''
        name = self.table
        
        if self.schema:
            name = f'{self.schema}.{name}'

        if self.database:
            name = f'{self.database}.{name}'

        return name

@dataclass
class ExternalStage:
    stage: str
    schema: Optional[str] = None
    database: Optional[str] = None

    def __post_init__(self) -> None:
        if self.database and not self.schema:
            raise SchemaRequired('Database name provided but schema missing')

    @property
    def fullname(self) -> str:
        '''
        As long as this raises when a database is provided but a schema isn't
        then it doesn't need to be any more complicated than this
        '''

        name = self.stage

        if self.schema:
            name = f'{self.schema}.{name}'

        if self.database:
            name = f'{self.database}.{name}'

        return name

@dataclass
class CopyCommands:
    stage: ExternalStage
    table: Table
    filenames: List[str]
    force: bool

    def get_sql_statements(self) -> List[str]:
        force_statement = ''
        if self.force:
            force_statement = f'force = {str(self.force).lower()}'
        return [
            f'copy into {self.table.fullname} from @{self.stage.fullname}/{x} {force_statement} ;' 
            for x in self.filenames
        ]
