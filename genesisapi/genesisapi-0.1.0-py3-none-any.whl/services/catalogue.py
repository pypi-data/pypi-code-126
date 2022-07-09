from typeguard import typechecked

from genesisapi.datatypes import JSON, Language, Criterion


class CatalogueService:

    service_name: str = 'catalogue'

    def __init__(self, client):
        self.client = client

    @typechecked
    def cubes(
            self,
            selection=None,
            area=None,
            page_length: int = None,
            language: Language = None
    ) -> JSON:
        url = self.client.get_url(
            CatalogueService.service_name,
            'cubes',
            selection=selection,
            area=area,
            language=language,
            pagelength=page_length)

        return self.client.get_json_result(url)

    @typechecked
    def cubes2statistic(
            self,
            name,
            selection=None,
            area=None,
            page_length: int = None,
            language: Language = None
    ) -> JSON:
        url = self.client.get_url(
            CatalogueService.service_name,
            'cubes2statistic',
            name=name,
            selection=selection,
            area=area,
            language=language,
            pagelength=page_length)

        return self.client.get_json_result(url)

    @typechecked
    def cubes2variable(
            self,
            name,
            selection=None,
            area=None,
            page_length: int = None,
            language: Language = None
    ) -> JSON:
        url = self.client.get_url(
            CatalogueService.service_name,
            'cubes2variable',
            name=name,
            selection=selection,
            area=area,
            language=language,
            pagelength=page_length)

        return self.client.get_json_result(url)

    @typechecked
    def jobs(
            self,
            selection=None,
            search_criterion=Criterion.CODE,
            sort_criterion=Criterion.CODE,
            object_type=None,
            page_length: int = None,
            language: Language = None
    ) -> JSON:
        url = self.client.get_url(
            CatalogueService.service_name,
            'jobs',
            selection=selection,
            searchcriterion=str(search_criterion),
            sortcriterion=str(sort_criterion),
            type=object_type,
            language=language,
            pagelength=page_length)

        return self.client.get_json_result(url)

    @typechecked
    def modified_data(
            self,
            selection,
            object_type,
            date,
            page_length: int = None,
            language: Language = None
    ) -> JSON:
        url = self.client.get_url(
            CatalogueService.service_name,
            'modified_data',
            selection=selection,
            type=object_type,
            date=date,
            language=language,
            pagelength=page_length)

        return self.client.get_json_result(url)

    @typechecked
    def quality_signs(
            self,
            language=None
    ) -> JSON:
        url = self.client.get_url(
            CatalogueService.service_name,
            'quality_signs',
            language=language)

        return self.client.get_json_result(url)

    @typechecked
    def results(
            self,
            selection=None,
            area=None,
            page_length: int = None,
            language: Language = None
    ) -> JSON:
        url = self.client.get_url(
            CatalogueService.service_name,
            'results',
            selection=selection,
            area=area,
            language=language,
            pagelength=page_length)

        return self.client.get_json_result(url)

    @typechecked
    def statistics(
            self,
            selection,
            search_criterion=None,
            sort_criterion=None,
            page_length: int = None,
            language: Language = None
    ) -> JSON:
        url = self.client.get_url(
            CatalogueService.service_name,
            'statistics',
            selection=selection,
            searchcriterion=search_criterion,
            sortcriterion=sort_criterion,
            language=language,
            pagelength=page_length)

        return self.client.get_json_result(url)

    @typechecked
    def statistics2variable(
            self,
            selection,
            area,
            search_criterion,
            sort_criterion,
            page_length: int = None,
            language: Language = None
    ) -> JSON:
        url = self.client.get_url(
            CatalogueService.service_name,
            'statistics2variable',
            selection=selection,
            area=area,
            searchcriterion=search_criterion,
            sortcriterion=sort_criterion,
            language=language,
            pagelength=page_length)

        return self.client.get_json_result(url)

    @typechecked
    def tables(
            self,
            selection=None,
            area=None,
            search_criterion=None,
            sort_criterion=None,
            page_length: int = None,
            language: Language = None
    ) -> JSON:
        url = self.client.get_url(
            CatalogueService.service_name,
            'tables',
            selection=selection,
            area=area,
            searchcriterion=search_criterion,
            sortcriterion=sort_criterion,
            language=language,
            pagelength=page_length)

        return self.client.get_json_result(url)

    @typechecked
    def tables2statistics(
            self,
            name,
            selection=None,
            area=None,
            search_criterion=None,
            sort_criterion=None,
            page_length: int = None,
            language: Language = None
    ) -> JSON:
        url = self.client.get_url(
            CatalogueService.service_name,
            'tables2statistics',
            name=name,
            selection=selection,
            area=area,
            searchcriterion=search_criterion,
            sortcriterion=sort_criterion,
            language=language,
            pagelength=page_length)

        return self.client.get_json_result(url)

    @typechecked
    def tables2variables(
            self,
            name,
            selection,
            area,
            page_length: int = None,
            language: Language = None
    ) -> JSON:
        url = self.client.get_url(
            CatalogueService.service_name,
            'tables2statistics',
            name=name,
            selection=selection,
            area=area,
            language=language,
            pagelength=page_length)

        return self.client.get_json_result(url)

    @typechecked
    def tables2variable(
            self,
            name,
            selection=None,
            area=None,
            page_length: int = None,
            language: Language = None
    ) -> JSON:
        url = self.client.get_url(
            CatalogueService.service_name,
            'tables2variable',
            name=name,
            selection=selection,
            area=area,
            language=language,
            pagelength=page_length)

        return self.client.get_json_result(url)

    @typechecked
    def terms(
            self,
            selection,
            page_length: int = None,
            language: Language = None
    ) -> JSON:
        url = self.client.get_url(
            CatalogueService.service_name,
            'terms',
            selection=selection,
            language=language,
            pagelength=page_length)

        return self.client.get_json_result(url)

    @typechecked
    def timeseries(
            self,
            selection=None,
            area=None,
            page_length: int = None,
            language: Language = None
    ) -> JSON:
        url = self.client.get_url(
            CatalogueService.service_name,
            'timeseries',
            selection=selection,
            area=area,
            language=language,
            pagelength=page_length)

        return self.client.get_json_result(url)

    @typechecked
    def timeseries2statistic(
            self,
            name,
            selection=None,
            area=None,
            page_length: int = None,
            language: Language = None
    ) -> JSON:
        url = self.client.get_url(
            CatalogueService.service_name,
            'timeseries2statistic',
            name=name,
            selection=selection,
            area=area,
            language=language,
            pagelength=page_length)

        return self.client.get_json_result(url)

    @typechecked
    def timeseries2variable(
            self,
            name,
            selection=None,
            area=None,
            page_length: int = None,
            language: Language = None
    ) -> JSON:
        url = self.client.get_url(
            CatalogueService.service_name,
            'timeseries2variable',
            name=name,
            selection=selection,
            area=area,
            language=language,
            pagelength=page_length)

        return self.client.get_json_result(url)

    @typechecked
    def values(
            self,
            selection,
            area=None,
            search_criterion=None,
            sort_criterion=None,
            page_length: int = None,
            language: Language = None

    ) -> JSON:
        url = self.client.get_url(
            CatalogueService.service_name,
            'values',
            selection=selection,
            area=area,
            searchcriterion=search_criterion,
            sortcriterion=sort_criterion,
            language=language,
            pagelength=page_length)

        return self.client.get_json_result(url)

    @typechecked
    def values2variable(
            self,
            name,
            selection=None,
            area=None,
            search_criterion=Criterion.CODE,
            sort_criterion=Criterion.CODE,
            page_length=None,
            language=None
    ) -> JSON:
        url = self.client.get_url(
            CatalogueService.service_name,
            'values2variable',
            name=name,
            selection=selection,
            area=area,
            searchcriterion=search_criterion,
            sortcriterion=sort_criterion,
            language=language,
            pagelength=page_length)

        return self.client.get_json_result(url)

    @typechecked
    def variables(
            self,
            selection=None,
            area=None,
            search_criterion=None,
            sort_criterion=None,
            object_type=None,
            page_length: int = None,
            language: Language = None
    ) -> JSON:
        url = self.client.get_url(
            CatalogueService.service_name,
            'variables',
            selection=selection,
            area=area,
            searchcriterion=search_criterion,
            sortcriterion=sort_criterion,
            type=object_type,
            language=language,
            pagelength=page_length)

        return self.client.get_json_result(url)

    @typechecked
    def variables2statistic(
            self,
            name,
            selection=None,
            area=None,
            search_criterion=None,
            sort_criterion=None,
            object_type=None,
            page_length: int = None,
            language: Language = None
    ) -> JSON:
        url = self.client.get_url(
            CatalogueService.service_name,
            'variables2statistic',
            name=name,
            selection=selection,
            area=area,
            searchcriterion=search_criterion,
            sortcriterion=sort_criterion,
            type=object_type,
            language=language,
            pagelength=page_length)

        return self.client.get_json_result(url)
