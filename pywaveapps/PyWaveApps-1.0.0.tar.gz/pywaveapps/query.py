from gql import gql


class Query:
    def __init__(self, wave_connection) -> None:
        """
        The Query object should only be initialized from the WaveApps.__init__(...) method.
        :param wave_connection: WaveApps object
        """
        self.wave = wave_connection

    def custom(self, query_str: str, **kwargs) -> dict:
        """Run a custom query based on a query string; pass names query parameters in the query_str as kwargs.

        :param query_str: a WaveApps-compatible query-string, such as: 'query { ... }'
        :type query_str: str
        :return: the result of the query
        :rtype: dict
        """
        query = gql(query_str)
        result: dict = self.wave.client.execute(query, variable_values=kwargs)
        return result

    def user(self) -> dict:
        # Provide a GraphQL query
        query = gql(
            """
            query {
                user {
                    id
                    firstName
                    lastName
                    defaultEmail
                    createdAt
                    modifiedAt
                }  
            }
        """
        )
        return self.wave.client.execute(query)

    def businesses(self, page: int = 1, page_size: int = 10, list_only=True) -> list | dict:
        """Query a list of businesses. If you are unsure if you have retrieved all items, set list_only=False for additional output.

        :param page: the page to return, defaults to 1
        :type page: int, optional
        :param page_size: the size of each page, defaults to 10
        :type page_size: int, optional
        :param list_only: return only the list of businesses from the entire output, defaults to True
        :type list_only: bool, optional
        :return: either the list of businesses or the entire dict result, depending on 'list_only'
        :rtype: list | dict
        """
        query = gql(f"""
            query {{
                businesses(page: {page}, pageSize: {page_size}) {{
                    pageInfo {{
                    currentPage
                    totalPages
                    totalCount
                    }}
                    edges {{
                    node {{
                        id
                        name
                        isClassicAccounting
                        isClassicInvoicing
                        isPersonal
                    }}
                    }}
                }}
                }}
            """
                    )
        result: dict = self.wave.client.execute(query)
        if list_only:
            filtered = result['businesses']['edges']
            return filtered
        else:
            return result

    def customers(self, business_id: str, page: int = 1, page_size: int = 20, list_only: bool = True, return_all: bool = True) -> list | dict:
        """Query a list of customers for a business. If you are unsure if you have retrieved all items, set list_only=False for additional output.

        :param business_id: the ID of the business to retrieve invoices for (use `WaveApps.query.businesses` to obtain it)
        :param page: the page to return, defaults to 1
        :param page_size: the size of each page, defaults to 20
        :param list_only: return only the list of businesses from the entire output, defaults to True
        :param return_all: query all pages based on 'page_size' (starting at 'page'), or return only the specified 'page'
        :return: either the list of customers or the entire dict result, depending on 'list_only'
        """
        params = {
            "businessId": f"{business_id}",
            "page": page,
            "pageSize": page_size
        }

        query = gql(f"""query($businessId: ID!, $page: Int!, $pageSize: Int!) {{
          business(id: $businessId) {{
            id
            customers(page: $page, pageSize: $pageSize) {{
              pageInfo {{
                currentPage
                totalPages
                totalCount
              }}
              edges {{
                node {{
                  id
                  name
                  email
                }}
              }}
            }}
          }}
        }}""")
        result: dict = self.wave.client.execute(query, variable_values=params)

        if return_all:
            page_info: dict = result['business']['customers']['pageInfo']  # {'currentPage': int, 'totalPages': int, 'totalCount': int}
            current_page = page_info['currentPage']
            total_pages = page_info['totalPages']
            while current_page < total_pages:
                params['page'] += 1
                additional_results = self.wave.client.execute(query, variable_values=params)
                result['business']['customers']['edges'] += additional_results['business']['customers']['edges']
                current_page = additional_results['business']['customers']['pageInfo']['currentPage']

        if list_only:
            filtered = result['business']['customers']['edges']
            return filtered
        else:
            return result

    def invoices_by_customer(self, business_id: str, customer_id: str, page: int = 1, page_size: int = 40, list_only: bool = True, return_all: bool = True) -> list | dict:
        """Query a list of invoices from a business for a specific customer. If you are unsure if you have retrieved all items, set list_only=False for additional output.

        :param business_id: the ID of the business to retrieve invoices for (use `WaveApps.query.businesses` to obtain it)
        :param customer_id: the ID of the customer to retrieve invoices for (use `WaveApps.query.customers` to obtain it)
        :param page: the page to return, defaults to 1
        :param page_size: the size of each page, defaults to 20
        :param list_only: return only the list of businesses from the entire output, defaults to True
        :param return_all: query all pages based on 'page_size' (starting at 'page'), or return only the specified 'page'
        :return: either the list of businesses or the entire dict result, depending on 'list_only'
        """

        params = {
            "businessId": f"{business_id}",
            "page": page,
            "pageSize": page_size,
            "customerId": f"{customer_id}"
        }
        query = gql("""query($businessId: ID!, $page: Int!, $pageSize: Int!, $customerId: ID!) {
          business(id: $businessId) {
            id
            isClassicInvoicing
            invoices(page: $page, pageSize: $pageSize, customerId: $customerId) {
              pageInfo {
                currentPage
                totalPages
                totalCount
              }
              edges {
                node {
                  id
                  createdAt
                  modifiedAt
                  pdfUrl
                  viewUrl
                  status
                  title
                  subhead
                  invoiceNumber
                  invoiceDate
                  poNumber
                  customer {
                    id
                    name
                    # Can add additional customer fields here
                  }
                  currency {
                    code
                  }
                  dueDate
                  amountDue {
                    value
                    currency {
                      symbol
                    }
                  }
                  amountPaid {
                    value
                    currency {
                      symbol
                    }
                  }
                  taxTotal {
                    value
                    currency {
                      symbol
                    }
                  }
                  total {
                    value
                    currency {
                      symbol
                    }
                  }
                  exchangeRate
                  footer
                  memo
                  disableCreditCardPayments
                  disableBankPayments
                  itemTitle
                  unitTitle
                  priceTitle
                  amountTitle
                  hideName
                  hideDescription
                  hideUnit
                  hidePrice
                  hideAmount
                  items {
                    product {
                      id
                      name
                      # Can add additional product fields here
                    }
                    description
                    quantity
                    price
                    subtotal {
                      value
                      currency {
                        symbol
                      }
                    }
                    total {
                      value
                      currency {
                        symbol
                      }
                    }
                    account {
                      id
                      name
                      subtype {
                        name
                        value
                      }
                      # Can add additional account fields here
                    }
                    taxes {
                      amount {
                        value
                      }
                      salesTax {
                        id
                        name
                        # Can add additional sales tax fields here
                      }
                    }
                  }
                  lastSentAt
                  lastSentVia
                  lastViewedAt
                }
              }
            }
          }
        }""")
        result: dict = self.wave.client.execute(query, variable_values=params)

        if return_all:
            page_info: dict = result['business']['invoices']['pageInfo']  # {'currentPage': int, 'totalPages': int, 'totalCount': int}
            current_page = page_info['currentPage']
            total_pages = page_info['totalPages']
            while current_page < total_pages:
                params['page'] += 1
                additional_results = self.wave.client.execute(query, variable_values=params)
                result['business']['invoices']['edges'] += additional_results['business']['invoices']['edges']
                current_page = additional_results['business']['invoices']['pageInfo']['currentPage']

        if list_only:
            filtered = result['business']['invoices']['edges']
            return filtered
        else:
            return result

    def invoices(self, business_id: str, page: int = 1, page_size: int = 20, list_only=True, return_all: bool = True) -> list | dict:
        """Query a list of invoices from a business. If you are unsure if you have retrieved all items, set list_only=False for additional output.

        :param business_id: the ID of the business to retrieve invoices for (use `WaveApps.query.businesses` to obtain it)
        :type business_id: str
        :param page: the page to return, defaults to 1
        :type page: int, optional
        :param page_size: the size of each page, defaults to 20
        :type page_size: int, optional
        :param list_only: return only the list of businesses from the entire output, defaults to True
        :type list_only: bool, optional
        :param return_all: query all pages based on 'page_size' (starting at 'page'), or return only the specified 'page'
        :return: either the list of businesses or the entire dict result, depending on 'list_only'
        :rtype: list | dict
        """

        params = {
            "businessId": f"{business_id}",
            "page": page,
            "pageSize": page_size
        }
        query = gql(f"""
        query($businessId: ID!, $page: Int!, $pageSize: Int!) {{
            business(id: $businessId) {{
                id
                isClassicInvoicing
                invoices(page: $page, pageSize: $pageSize) {{
                    pageInfo {{
                        currentPage
                        totalPages
                        totalCount
                    }}
                    edges {{
                        node {{
                        id
                        createdAt
                        modifiedAt
                        pdfUrl
                        viewUrl
                        status
                        title
                        subhead
                        invoiceNumber
                        invoiceDate
                        poNumber
                        customer {{
                            id
                            name
                            # Can add additional customer fields here
                        }}
                        currency {{
                            code
                        }}
                        dueDate
                        amountDue {{
                            value
                            currency {{
                            symbol
                            }}
                        }}
                        amountPaid {{
                            value
                            currency {{
                            symbol
                            }}
                        }}
                        taxTotal {{
                            value
                            currency {{
                            symbol
                            }}
                        }}
                        total {{
                            value
                            currency {{
                            symbol
                            }}
                        }}
                        exchangeRate
                        footer
                        memo
                        disableCreditCardPayments
                        disableBankPayments
                        itemTitle
                        unitTitle
                        priceTitle
                        amountTitle
                        hideName
                        hideDescription
                        hideUnit
                        hidePrice
                        hideAmount
                        items {{
                            product {{
                            id
                            name
                            # Can add additional product fields here
                            }}
                            description
                            quantity
                            price
                            subtotal {{
                            value
                            currency {{
                                symbol
                            }}
                            }}
                            total {{
                            value
                            currency {{
                                symbol
                            }}
                            }}
                            account {{
                            id
                            name
                            subtype {{
                                name
                                value
                            }}
                            # Can add additional account fields here
                            }}
                            taxes {{
                            amount {{
                                value
                            }}
                            salesTax {{
                                id
                                name
                                # Can add additional sales tax fields here
                            }}
                            }}
                        }}
                        lastSentAt
                        lastSentVia
                        lastViewedAt
                        }}
                    }}
                }}
            }}
            }}
        """)
        result: dict = self.wave.client.execute(query, variable_values=params)

        if return_all:
            page_info: dict = result['business']['invoices']['pageInfo']  # {'currentPage': int, 'totalPages': int, 'totalCount': int}
            current_page = page_info['currentPage']
            total_pages = page_info['totalPages']
            while current_page < total_pages:
                params['page'] += 1
                additional_results = self.wave.client.execute(query, variable_values=params)
                result['business']['invoices']['edges'] += additional_results['business']['invoices']['edges']
                current_page = additional_results['business']['invoices']['pageInfo']['currentPage']

        if list_only:
            filtered = result['business']['invoices']['edges']
            return filtered
        else:
            return result
