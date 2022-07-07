from wbxSearch.filterArgs import FilterArgs


class MinerArgs:
    def __init__(self, str_args, miner):
        self.miner = miner
        self.str_args = str_args

        """elasticsearch"""
        self.context_subject = None
        self.query = None
        self.irrelevant_score_percent = None
        self.filter = None
        self.max_product = None
        self.boost_query = None
        self.boost_query_percent = None
        self.sorting_group_number = None
        self.search_model = None
        self.adult_filter_show_threshold = None
        self.enrich_response = None
        self.sort_version = None
        self.keep_adult = None

        self.limit = None
        self.arr_urls = []
        self.limit = None
        self.country = None
        self.timeout_between_requests = None
        self.one_by_one_join = None
        # @sort
        self.apply_self_ranker_sales = None
        self.apply_self_ranker_views = None
        self.self_ranker_views_weight = None
        self.self_ranker_sales_weight = None



        self.arr_str_args = self.str_args.split("--")

        self._flag_boost_query = "boost-query"
        self._flag_adult_filter_show_threshold = "adult-filter-show-threshold"
        self._flag_max_product = "max-product"
        self._flag_boost_query_percent = "boost-query-percent"
        self._flag_sorting_group_number = "sorting-group-number"
        self._flag_search_model = "search-model"
        self._flag_enrich_response = "enrich-response"
        self._flag_sort_version = "sort-version"
        self._flag_keep_adult = "keep-adult"

        self._flag_one_by_one_join = "--one-by-one-join"
        self._flag_limit = "limit"
        self._flag_country = "country"
        # @sort
        self._flag_apply_self_ranker_sales = "apply-self-ranker-sales"
        self._flag_apply_self_ranker_views = "apply-self-ranker-views"
        self._flag_self_ranker_views_weight = "self-ranker-views-weight"
        self._flag_self_ranker_sales_weight = "self-ranker-sales-weight"

        self._flag_context_subject = "context-subject"
        self._flag_query = "query"
        self._flag_irrelevant_score_percent = "irrelevant-score-percent"
        self._flag_filter = "filter"
        self._flag_timeout_between_requests = "timeoutBetweenRequests"

        self.parse_args()
        self.filter_object = FilterArgs(self.filter)

    def parse_args(self):
        if self._check_str_args():

            self.search_url()
            # if self.arr_urls:
            #     self._set_apply_self_ranker_sales()
            #     self._set_apply_self_ranker_views()
            if self._check_apply_self_ranker_sales():
                self._set_apply_self_ranker_sales()
            if self._check_apply_self_ranker_views():
                self._set_apply_self_ranker_views()
            if self._check_self_ranker_views_weight():
                self._set_self_ranker_views_weight()
            if self._check_self_ranker_sales_weight():
                self._set_self_ranker_sales_weight()

            if self._check_one_by_one_join():
                self._set_one_by_one_join()
            if self._check_query():
                self._set_query()
            if self._check_limit():
                self._set_limit()
            if self._check_context_subject():
                self._set_context_subject()
            if self._check_filter():
                self._set_filter()
            if self._check_irrelevant_score_percent():
                self._set_irrelevant_score_percent()
            if self._check_limit():
                self._set_limit()
            if self._check_country():
                self._set_country()
            if self._check_timeout_between_requests():
                self._set_timeout_between_requests()
            if self._check_max_product():
                self._set_max_product()
            if self._check_boost_query():
                self._set_boost_query()
            if self._check_boost_query_percent():
                self._set_boost_query_percent()
            if self._check_sorting_group_number():
                self._set_sorting_group_number()
            if self._check_search_model():
                self._set_search_model()
            if self._check_adult_filter_show_threshold():
                self._set_adult_filter_show_threshold()
            if self._check_enrich_response():
                self._set_enrich_response()
            if self._check_sort_version():
                self._set_sort_version()
            if self._check_keep_adult():
                self._set_keep_adult()

    def _check_str_args(self) -> bool:
        return True if self.str_args else False

    def _get_arg(self, key, separator="=") -> str:
        """в этой функции достаем аргумент по флагу"""
        result = ""
        for arg in self.arr_str_args:
            if arg.startswith(key):
                arr_key = arg.split(separator)
                result = arr_key[1].replace('"', "")
                break
        return result

    def _check_query(self) -> bool:
        return self._flag_query in self.str_args

    def _set_query(self):
        self.query = self._get_arg(self._flag_query)

    def _check_apply_self_ranker_sales(self) -> bool:
        return self._flag_apply_self_ranker_sales in self.str_args

    def _set_apply_self_ranker_sales(self):
        self.apply_self_ranker_sales = self._get_arg(self._flag_apply_self_ranker_sales)

    def _check_apply_self_ranker_views(self) -> bool:
        return self._flag_apply_self_ranker_views in self.str_args

    def _set_apply_self_ranker_views(self):
        self.apply_self_ranker_views = self._get_arg(self._flag_apply_self_ranker_views)

    def _check_self_ranker_views_weight(self) -> bool:
        return self._flag_self_ranker_views_weight in self.str_args

    def _set_self_ranker_views_weight(self):
        self.self_ranker_views_weight = self._get_arg(self._flag_self_ranker_views_weight)

    def _check_self_ranker_sales_weight(self) -> bool:
        return self._flag_self_ranker_sales_weight in self.str_args

    def _set_self_ranker_sales_weight(self):
        self.self_ranker_sales_weight = self._get_arg(self._flag_self_ranker_sales_weight)

    def _check_one_by_one_join(self) -> bool:
        return self._flag_query in self.str_args

    def _set_one_by_one_join(self):
        self.one_by_one_join = self._flag_one_by_one_join

    def _check_boost_query(self) -> bool:
        return self._flag_boost_query in self.str_args

    def _set_boost_query(self):
        self.boost_query = self._get_arg(self._flag_boost_query)

    def _check_sort_version(self) -> bool:
        return self._flag_sort_version in self.str_args

    def _set_sort_version(self):
        self.sort_version = self._get_arg(self._flag_sort_version)

    def _check_keep_adult(self) -> bool:
        return self._flag_keep_adult in self.str_args

    def _set_keep_adult(self):
        self.keep_adult = self._get_arg(self._flag_keep_adult)

    def _check_adult_filter_show_threshold(self) -> bool:
        return self._flag_adult_filter_show_threshold in self.str_args

    def _set_adult_filter_show_threshold(self):
        self.adult_filter_show_threshold = self._get_arg(self._flag_adult_filter_show_threshold)

    def _check_search_model(self) -> bool:
        return self._flag_search_model in self.str_args

    def _set_search_model(self):
        self.search_model = self._get_arg(self._flag_search_model)

    def _check_enrich_response(self) -> bool:
        return self._flag_enrich_response in self.str_args

    def _set_enrich_response(self):
        self.enrich_response = self._get_arg(self._flag_enrich_response)

    def _check_sorting_group_number(self) -> bool:
        return self._flag_sorting_group_number in self.str_args

    def _set_sorting_group_number(self):
        self.sorting_group_number = self._get_arg(self._flag_sorting_group_number)

    def _check_boost_query_percent(self) -> bool:
        return self._flag_boost_query_percent in self.str_args

    def _set_boost_query_percent(self):
        self.boost_query_percent = self._get_arg(self._flag_boost_query_percent)

    def _check_limit(self) -> bool:
        return self._flag_limit in self.str_args

    def _set_limit(self):
        self.limit = self._get_arg(self._flag_limit)

    def _check_context_subject(self) -> bool:
        return self._flag_context_subject in self.str_args

    def _set_context_subject(self):
        self.context_subject = self._get_arg(self._flag_context_subject)

    def _check_filter(self) -> bool:
        return self._flag_filter in self.str_args

    def _set_filter(self):
        self.filter = self._get_arg(self._flag_filter)

    def _check_irrelevant_score_percent(self) -> bool:
        return self._flag_irrelevant_score_percent in self.str_args

    def _set_irrelevant_score_percent(self):
        self.irrelevant_score_percent = self._get_arg(self._flag_irrelevant_score_percent)

    def _check_limit(self) -> bool:
        return self._flag_limit in self.str_args

    def _set_limit(self):
        self.limit = self._get_arg(self._flag_limit)

    def _check_max_product(self) -> bool:
        return self._flag_max_product in self.str_args

    def _set_max_product(self):
        try:
            self.max_product = self._get_arg(self._flag_max_product)
        except IndexError:
            self.max_product = self._get_arg(self._flag_max_product, separator=" ")

    def _check_country(self) -> bool:
        return self._flag_country in self.str_args

    def _set_country(self):
        self.country = self._get_arg(self._flag_country, separator=" ")

    def _check_timeout_between_requests(self) -> bool:
        return self._flag_timeout_between_requests in self.str_args

    def _set_timeout_between_requests(self):
        self.timeout_between_requests = self._get_arg(self._flag_timeout_between_requests, separator=" ")

    def search_url(self):
        list_str_args = self.str_args.split(" ")
        for x in list_str_args:
            if x.startswith('"http'):
                self.arr_urls.append(x)

    def construct_url_record(self):
        str_urls = " ".join(self.arr_urls)
        sort = f"{str_urls} @sort: --{self._flag_apply_self_ranker_sales}={self.apply_self_ranker_sales} --{self._flag_apply_self_ranker_views}={self.apply_self_ranker_views}"
        return sort

    def construct_url_record_for_elasticsearch(self):
        list_result = []
        if self.apply_self_ranker_sales:
            list_result.append(f'--{self._flag_apply_self_ranker_sales}={self.del_space(self.apply_self_ranker_sales)}')
        if self.apply_self_ranker_views:
            list_result.append(f'--{self._flag_apply_self_ranker_views}={self.del_space(self.apply_self_ranker_views)}')
        if self.self_ranker_views_weight:
            list_result.append(f'--{self._flag_self_ranker_views_weight}={self.del_space(self.self_ranker_views_weight)}')
        if self.self_ranker_sales_weight:
            list_result.append(f'--{self._flag_self_ranker_sales_weight}={self.del_space(self.self_ranker_sales_weight)}')
        sort = f"@sort: {' '.join(list_result)}"
        return sort

    def create_result_elasticsearch(self):
        """Собираем результат для выдачи, новый str_args, функция для майнера elasticsearch"""
        list_result = []

        if self.context_subject:
            list_result.append(f'--{self._flag_context_subject}="{self.del_space(self.context_subject)}"')
        if self.max_product:
            list_result.append(f'--{self._flag_max_product}={self.del_space(self.max_product)}')
        if self.query:
            list_result.append(f'--{self._flag_query}="{self.del_sort(self.del_space(self.query))}"')
        if self.keep_adult:
            list_result.append(f'--{self._flag_keep_adult}={self.del_space(self.keep_adult)}')
        if self.boost_query:
            list_result.append(f'--{self._flag_boost_query}="{self.del_space(self.boost_query)}"')
        if self.boost_query_percent:
            list_result.append(f'--{self._flag_boost_query_percent}={self.del_space(self.boost_query_percent)}')
        if self.sorting_group_number:
            list_result.append(f'--{self._flag_sorting_group_number}={self.del_space(self.sorting_group_number)}')
        if self.search_model:
            list_result.append(f'--{self._flag_search_model}={self.del_space(self.search_model)}')
        if self.sort_version:
            list_result.append(f'--{self._flag_sort_version}={self.del_space(self.sort_version)}')
        if self.enrich_response:
            list_result.append(f'--{self._flag_enrich_response}={self.del_space(self.enrich_response)}')
        if self.adult_filter_show_threshold:
            list_result.append(f'--{self._flag_adult_filter_show_threshold}'
                               f'={self.del_space(self.adult_filter_show_threshold)}')
        if self.irrelevant_score_percent:
            list_result.append(
                f"--{self._flag_irrelevant_score_percent}={self.del_space(self.irrelevant_score_percent)}")
        if self.filter:
            list_result.append(f'--{self._flag_filter}="{self.filter_object.get_result_for_write()}"')
        if self.apply_self_ranker_views or self.apply_self_ranker_sales or self.self_ranker_sales_weight or \
                self.self_ranker_views_weight:
            list_result.append(self.construct_url_record_for_elasticsearch())
        return " ".join(list_result)

    def get_result_for_write(self):
        if self.miner == "elasticsearch":
            result = self.create_result_elasticsearch()
            return result
        result = self.str_args
        return result

    def del_space(self, arg):
        if arg[-1:] == " ":
            return arg[:-1]
        return arg

    def del_sort(self, arg):
        if arg[-7:] == " @sort:":
            return arg[:-7]
        return arg

    def __str__(self):
        return self.str_args
