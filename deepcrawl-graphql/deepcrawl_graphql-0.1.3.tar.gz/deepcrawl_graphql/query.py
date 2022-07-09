"""
Query
=====
"""

from deepcrawl_graphql.api import DeepCrawlConnection


class Query:
    """Query class"""

    def __init__(self, conn: DeepCrawlConnection) -> None:
        self.ds = conn.ds
        self.query = self.ds.Query

    def page_fields(self):
        """Returns a tule of PageInfo fields."""
        return (
            self.ds.PageInfo.startCursor,
            self.ds.PageInfo.endCursor,
            self.ds.PageInfo.hasNextPage,
            self.ds.PageInfo.hasPreviousPage,
        )
