from typeguard import typechecked

from genesisapi.datatypes import JSON, Language
from genesisapi.table import TableResult


class DataService:
    service_name: str = 'data'

    def __init__(self, client):
        self.client = client

    @typechecked
    def chart2result(
            self,
            name,
            area,
            chart_type,
            draw_points,
            zoom,
            focus,
            tops,
            format,
            page_length: int = None,
            language: Language = None
    ) -> JSON:
        url = self.client.get_url(
            DataService.service_name,
            'chart2result',
            name=name,
            area=area,
            chartType=chart_type,
            drawPoints=draw_points,
            zoom=zoom,
            focus=focus,
            tops=tops,
            format=format,
            language=language,
            pagelength=page_length)

        return self.client.get_json_result(url)

    @typechecked
    def chart2table(
            self,
            name,
            area,
            chartType,
            drawPoints,
            zoom,
            focus,
            tops,
            startyear,
            endyear,
            timeslices,
            regionalvariable,
            regionalkey,
            classifyingvariable1,
            classifyingkey1,
            classifyingvariable2,
            classifyingkey2,
            classifyingvariable3,
            classifyingkey3,
            format,
            stand,
            language: Language = None
    ) -> JSON:
        pass

    @typechecked
    def chart2timeseries(
            self,
            name,
            area,
            chartType,
            drawPoints,
            zoom,
            focus,
            tops,
            contents,
            startyear,
            endyear,
            timeslices,
            regionalvariable,
            regionalkey,
            classifyingvariable1,
            classifyingkey1,
            classifyingvariable2,
            classifyingkey2,
            classifyingvariable3,
            classifyingkey3,
            format,
            stand,
            language: Language = None
    ) -> JSON:
        pass

    @typechecked
    def cube(
            self,
            name,
            area,
            values,
            metadata,
            additionals,
            startyear,
            endyear,
            timeslices,
            regionalvariable,
            regionalkey,
            classifyingvariable1,
            classifyingkey1,
            classifyingvariable2,
            classifyingkey2,
            classifyingvariable3,
            classifyingkey3,
            stand,
            language: Language = None
    ) -> JSON:
        pass

    @typechecked
    def cubefile(
            self,
            name,
            area,
            values,
            metadata,
            additionals,
            startyear,
            endyear,
            timeslices,
            regionalvariable,
            regionalkey,
            classifyingvariable1,
            classifyingkey1,
            classifyingvariable2,
            classifyingkey2,
            classifyingvariable3,
            classifyingkey3,
            format,
            stand,
            language: Language = None
    ) -> JSON:
        pass

    @typechecked
    def map2result(
            self,
            name,
            area='all',
            mapType='0',
            classes='5',
            classification='0',
            zoom='2',
            format='png',
            page_length=None,
            language=None
    ) -> JSON:
        url = self.client.get_url(
            DataService.service_name,
            'map2result',
            name=name,
            area=area,
            mapType=mapType,
            classes=classes,
            classification=classification,
            zoom=zoom,
            format=format,
            language=language,
            pagelength=page_length)

        json = self.client.get_json_result(url)
        return json

    @typechecked
    def map2table(
            self,
            name,
            area,
            mapType,
            classes,
            classification,
            zoom,
            startyear,
            endyear,
            timeslices,
            regionalvariable,
            regionalkey,
            classifyingvariable1,
            classifyingkey1,
            classifyingvariable2,
            classifyingkey2,
            classifyingvariable3,
            classifyingkey3,
            format,
            stand,
            language: Language = None
    ) -> JSON:
        pass

    @typechecked
    def map2timeseries(
            self,
            name,
            area,
            mapType,
            classes,
            classification,
            zoom,
            contents,
            startyear,
            endyear,
            timeslices,
            regionalvariable,
            regionalkey,
            classifyingvariable1,
            classifyingkey1,
            classifyingvariable2,
            classifyingkey2,
            classifyingvariable3,
            classifyingkey3,
            format,
            stand,
            language: Language = None
    ) -> JSON:
        pass

    @typechecked
    def result(
            self,
            name,
            area,
            compress,
            language: Language = None
    ) -> JSON:
        pass

    def resultfile(
            self,
            name,
            area,
            compress,
            format,
            language: Language = None
    ) -> JSON:
        pass

    @typechecked
    def table(
            self,
            name,
            area=None,
            compress=False,
            transpose=False,
            start_year='',
            end_year='',
            time_slices='',
            regional_variable='',
            regional_key='',
            classifying_variable1='',
            classifying_key1='',
            classifying_variable2='',
            classifying_key2='',
            classifying_variable3='',
            classifying_key3='',
            job=False,
            stand='',
            page_length=None,
            language: Language = None
    ) -> TableResult:
        url = self.client.get_url(
            DataService.service_name,
            'table',
            name=name,
            area=area,
            compress=compress,
            transpose=transpose,
            startyear=start_year,
            endyear=end_year,
            timeslices=time_slices,
            regionalvariable=regional_variable,
            regionalkey=regional_key,
            classifyingvariable1=classifying_variable1,
            classifyingkey1=classifying_key1,
            classifyingvariable2=classifying_variable2,
            classifyingkey2=classifying_key2,
            classifyingvariable3=classifying_variable3,
            classifyingkey3=classifying_key3,
            job=job,
            stand=stand,
            anguage=language,
            pagelength=page_length)

        json = self.client.get_json_result(url)
        return TableResult(self.client, json)

    @typechecked
    def tablefile(
            self,
            name,
            area,
            compress,
            transpose,
            startyear,
            endyear,
            timeslices,
            regionalvariable,
            regionalkey,
            classifyingvariable1,
            classifyingkey1,
            classifyingvariable2,
            classifyingkey2,
            classifyingvariable3,
            classifyingkey3,
            format,
            job,
            stand,
            language: Language = None
    ) -> JSON:
        pass

    @typechecked
    def timeseries(
            self,
            name,
            area,
            compress,
            transpose,
            contents,
            startyear,
            endyear,
            timeslices,
            regionalvariable,
            regionalkey,
            regionalcode,
            classifyingvariable1,
            classifyingkey1,
            classifyingkeycode1,
            classifyingvariable2,
            classifyingkey2,
            classifyingkeycode2,
            classifyingvariable3,
            classifyingkey3,
            classifyingkeycode3,
            job,
            stand,
            language: Language = None
    ) -> JSON:
        pass

    @typechecked
    def timeseriesfile(
            self,
            name,
            area,
            compress,
            transpose,
            contents,
            startyear,
            endyear,
            timeslices,
            regionalvariable,
            regionalkey,
            regionalcode,
            classifyingvariable1,
            classifyingkey1,
            classifyingkeycode1,
            classifyingvariable2,
            classifyingkey2,
            classifyingkeycode2,
            classifyingvariable3,
            classifyingkey3,
            classifyingkeycode3,
            format,
            job,
            stand,
            language: Language = None
    ) -> JSON:
        pass
