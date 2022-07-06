
from __future__ import annotations
from typing import TYPE_CHECKING, Iterable, Mapping, Optional, Sequence, Iterator, overload, Union, Any
if TYPE_CHECKING:
    from ...client_ASYNC import Client

from ...models.submission_ASYNC import Submission
from .listing.mixins.time_ASYNC import Time
from .listing.mixins.sort_ASYNC import Sort
from .listing.submission_listing_async_paginator import SubmissionListingAsyncPaginator
from .listing.listing_async_paginator import ListingAsyncPaginator
from ...model_loaders.submission_ASYNC import load_submission

class SearchSubmissionsListingAsyncPaginator(
    Time[Submission],
    Sort[Submission],
    SubmissionListingAsyncPaginator,
):
    def __init__(self,
        client: Client,
        uri: str,
        *,
        params: Optional[Mapping[str, str]] = None,
        sort: str = 'relevance',
        time: str = 'all',
    ):
        super().__init__(client, uri, params=params)
        self.sort: str = sort
        self.time: str = time


class SubmissionDuplicates(Sequence[Submission]):
    def __init__(self, dups: Sequence[Submission], origin: Submission) -> None:
        self.origin: Submission = origin
        self.dups: Sequence[Submission] = dups

    def __len__(self) -> int:
        return len(self.dups)

    def __contains__(self, item: object) -> bool:
        return item in self.dups

    def __iter__(self) -> Iterator[Submission]:
        return iter(self.dups)

    @overload
    def __getitem__(self, index: int) -> Submission: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[Submission]: ...
    def __getitem__(self, index: Union[int, slice]) -> Union[Submission, Sequence[Submission]]:
        return self.dups[index]

class SubmissionDuplicatesAsyncPaginator(ListingAsyncPaginator[Submission]):
    def __init__(self,
        client: Client,
        uri: str,
        *,
        sort: str = 'num_comments',
        crossposts_only: bool = False,
    ):
        super().__init__(client, uri)
        self.sort: str = sort
        self.crossposts_only: bool = crossposts_only

    def _generate_params(self) -> Iterable[tuple[str, str]]:
        yield from super()._generate_params()
        if self.crossposts_only:
            yield ('crossposts_only', '1')
        if self.sort:
            ('sort', self.sort)

    async def _fetch_data(self) -> Any:
        params = dict(self._generate_params())
        root = await self.client.request('GET', self.uri, params=params)
        data = root[1]['data']
        children = data['children']

        dist: int = x if (x := data['dist']) else len(children)
        self.after_count += (1 if self.direction else -1) * dist
        self.before_count: int = self.after_count - dist + 1

        suggested_forward_cursor = data['after'] or ''
        suggested_backward_cursor = data['before'] or ''
        if children:
            self.after: str = suggested_forward_cursor if suggested_forward_cursor else self.cursor_extractor(children[-1])
            self.before: str = suggested_backward_cursor if suggested_backward_cursor else self.cursor_extractor(children[0])
        self.has_after: bool = bool(suggested_forward_cursor)
        self.has_before: bool = bool(suggested_backward_cursor)

        return root

    async def fetch(self) -> SubmissionDuplicates:
        root = await self._fetch_data()
        origin = load_submission(root[0]['data']['children'][0]['data'], self.client)
        data = root[1]['data']
        return SubmissionDuplicates([load_submission(d['data'], self.client) for d in data['children']], origin)
