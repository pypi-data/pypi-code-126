import os

import pytest
import traceback
from docparser.doc_parser_factory import DocParserFactory

config = {
    "id": "AN_MSC_",
    "parse": {
        "id": "MSC",
        "name": "MSC config",
        "kv": {
            "VESSEL": {
                "position_pattern": [
                    "VESSEL NAME"
                ],
                "value_pattern": [
                    "(?P<Vessel>.{2,})"
                ],
                "repeat_count": 1,
                "find_mode": "v",
                "separator_mode": "regex",
                "is_split_cell": 1,
                "split_pattern": [
                    "(?P<s0>^|)(?P<now>VESSEL\\s*NAME)\\s*(?P<s2>VOYAGE\\s*No\\.)\\s*(?P<s3>Estimated\\s*Arrival\\s*Date)"
                ],
                "action": [
                    {
                        "keyword": "VesselName",
                        "key": "Vessel"
                    }
                ]
            },
            "VOYAGE": {
                "position_pattern": [
                    "\\s*VOYAGE"
                ],
                "value_pattern": [
                    "(?P<VOYAGE>.{2,})"
                ],
                "repeat_count": 1,
                "find_mode": "v",
                "separator_mode": "regex",
                "is_split_cell": 0,
                "split_pattern": [
                    ""
                ],
                "action": [
                    {
                        "keyword": "VoyageNo",
                        "key": "VOYAGE"
                    }
                ]
            },
            "ETA": {
                "position_pattern": [
                    "\\s*Estimated\\s*Arrival\\s*Date"
                ],
                "value_pattern": [
                    "(?P<eta>.{2,})"
                ],
                "repeat_count": 1,
                "find_mode": "v",
                "separator_mode": "regex",
                "is_split_cell": 0,
                "split_pattern": [
                    ""
                ],
                "action": [
                    {
                        "keyword": "EstimatedArrivalDate",
                        "key": "eta"
                    }
                ]
            },
            "BILL": {
                "position_pattern": [
                    "^FLAG\\s*REGISTRY"
                ],
                "value_pattern": [
                    "(?P<BILL>[a-z]{4,}\\d{6,})"
                ],
                "repeat_count": 1,
                "find_mode": "h",
                "separator_mode": "regex",
                "is_split_cell": 0,
                "split_pattern": [
                    ""
                ],
                "action": [
                    {
                        "keyword": "BillOfLadingsId",
                        "key": "BILL"
                    }
                ]
            },
            "DestinationPortName": {
                "position_pattern": [
                    "^PORT\\s*OF\\s*DISCHARGE"
                ],

                "value_pattern": [
                    "(?P<DestinationPortName>.*)"
                ],
                "read_orgin": {"val": "PORT\\s*OF\\s*LOADING", "key": "DestinationPortName"},
                "repeat_count": 1,
                "find_mode": "v",
                "separator_mode": "regex",
                "is_split_cell": 0,
                "split_pattern": [""],
                "action": [
                    {
                        "keyword": "DestinationPortName",
                        "key": "DestinationPortName"
                    }
                ]
            },
            "DeliveryPlaceName": {
                "position_pattern": [
                    "^PORT\\s*OF\\s*DISCHARGE"
                ],

                "value_pattern": [
                    "(?P<DeliveryPlaceName>.*)"
                ],
                "read_orgin": {"val": "PORT\\s*OF\\s*DISCHARGE", "key": "DeliveryPlaceName"},
                "repeat_count": 1,
                "find_mode": "v",
                "separator_mode": "regex",
                "is_split_cell": 0,
                "split_pattern": [""],
                "action": [
                    {
                        "keyword": "DeliveryPlaceName",
                        "key": "DeliveryPlaceName"
                    }
                ]
            },
        },
        "table": {
            "containers": {
                "position_pattern": [
                    "(^CONTAINER\\s*NUMBER)|([a-zA-Z]{4,}\\d{7,}-\\d{2}[a-zA-Z]{2})"
                ],
                "separator": "\\n",

                "find_mode": "h",
                "separator_mode": "regex",
                "column": [
                    "ContainerNo",
                    "ContainerSize"
                ],
                "behaviors": [
                    {
                        "over_action": "row",
                        "loop": 1,
                        "value_pattern": [
                            '(?P<col_1>[a-zA-Z]{4,}\\d{7,})-(?P<col_2>\\d{2}[a-zA-Z]{2})'
                        ],
                        "action": []
                    }
                ]
            }
        },
        "data_type_format": {
            "VoyageNo": {
                "data_type": "str",
                "filter": "r([/\\s])"
            },
            "EstimatedArrivalDate": {
                "data_type": "time",
                "format": "%m/%d/%Y",
                "filter": ""
            },
            "BillOfLadingsId": {
                "data_type": "str",
                "filter": "(\\s)"
            }
        },
        "address_repair": {
            "db": {
                "pub": {
                    "user": "co",
                    "pwd": "Co&23@2332$22",
                    "server": "db.uat.com:1433",
                    "database": "CO_PUB"
                }
            },
            "repairs": [
                {
                    "key": "DeliveryPlaceName",
                    "db_key": "pub",
                    "sql": "SELECT  [FullName],[LocalName],[name],[code],[Id] from Places WHERE IsDeleted = 0 and IsOcean = 1 and IsValid = 1 and ([FullName] like '%${value}%' or charindex([FullName],'${value}')> 0) ;",
                    "column": [
                        0,
                        1,
                        2,
                        3
                    ],
                    "value": 4,
                    "mapping": "DeliveryPlaceId",
                    "old_val_handle": "empty"
                },
                {
                    "key": "DestinationPortName",
                    "db_key": "pub",
                    "sql": "SELECT  [FullName],[LocalName],[name],[code],[Id] from Places WHERE IsDeleted = 0 and IsOcean = 1 and IsValid = 1 and ([FullName] like '%${value}%' or charindex([FullName],'${value}')> 0) ;",
                    "column": [
                        0,
                        1,
                        2,
                        3
                    ],
                    "value": 4,
                    "mapping": "DestinationPortId",
                    "old_val_handle": "empty"
                }
            ]
        }
    }
}

# wanhai
config1 = {
    "id": "AN_WANHAI_",
    "parse": {
        "id": "WANHAI",
        "name": "WANHAI config",
        "kv": {
            "ETA": {
                "position_pattern": [
                    "[\\w\\W]*Est\\.\\s*Arrival\\s*Date\\s*:\\s*"
                ],
                "value_pattern": [
                    "[\\w\\W]*Est\\.\\s*Arrival\\s*Date\\s*:\\s*(?P<ETA>[a-zA-Z]*\\s*\\d{1,2}\\s*\\d{2,4})"
                ],
                "repeat_count": 1,
                "find_mode": "default",
                "separator_mode": "regex",
                "is_split_cell": 0,
                "split_pattern": [],
                "action": [
                    {
                        "keyword": "EstimatedArrivalDate",
                        "key": "ETA"
                    }
                ]
            },
            "BILL": {
                "position_pattern": [
                    "[\\w\\W]*B/L\\s*No\\s*:",
                    "B/L\\s*No\\s*:\\s*"
                ],
                "value_pattern": [
                    "[\\w\\W]*B/L\\s*No\\s*:\\s*(?P<bill>[a-zA-Z]{4}[a-zA-Z0-9]{5}\\d{4,})",
                    "B/L\\s*No\\s*:\\s*(?P<bill>[a-zA-Z0-9]{5}\\d{4,})"
                ],
                "repeat_count": 1,
                "find_mode": "default",
                "separator_mode": "regex",
                "is_split_cell": 0,
                "split_pattern": [],
                "action": [
                    {
                        "keyword": "BillOfLadingsId",
                        "key": "bill"
                    }
                ]
            },
            "BILL2": {
                "position_pattern": [
                    "B/L\\s*No\\s*:\\s*"
                ],
                "value_pattern": [
                    "(?P<bill>[a-zA-Z0-9]{5}\\d{4,})"
                ],
                "repeat_count": 1,
                "find_mode": "h",
                "separator_mode": "regex",
                "is_split_cell": 0,
                "split_pattern": [],
                "action": [
                    {
                        "keyword": "BillOfLadingsId",
                        "key": "bill"
                    }
                ]
            },
            "VOYAGE": {
                "position_pattern": [
                    "[\\w\\W]*?Voyage\\s*No\\s*:\\s*"
                ],
                "value_pattern": [
                    "(?P<VOYAGE>.*)"
                ],
                "repeat_count": 1,
                "find_mode": "h",
                "separator_mode": "regex",
                "is_split_cell": 0,
                "split_pattern": [
                    ""
                ],
                "action": [
                    {
                        "keyword": "VoyageNo",
                        "key": "VOYAGE"
                    }
                ]
            },
            "Vessel": {
                "position_pattern": [
                    "[\\w\\W]*?Ocean\\s*Vessel\\s*:\\s*"
                ],
                "value_pattern": [
                    "(?P<Vessel>.*)"
                ],
                "repeat_count": 1,
                "find_mode": "h",
                "separator_mode": "regex",
                "is_split_cell": 0,
                "split_pattern": [
                    ""
                ],
                "action": [
                    {
                        "keyword": "VesselName",
                        "key": "Vessel"
                    }
                ]
            },
            "DestinationPortName": {
                "position_pattern": [
                    "Place\\s*of\\s*receipt\\s*:\\s*"
                ],

                "value_pattern": [
                    "(?P<DestinationPortName>[^\\n]*?)(\\n|$)"
                ],
                "repeat_count": 1,
                "find_mode": "h",
                "separator_mode": "regex",
                "is_split_cell": 0,
                "split_pattern": [""],
                "action": [
                    {
                        "keyword": "DestinationPortName",
                        "key": "DestinationPortName"
                    }
                ]
            },
            "DeliveryPlaceName": {
                "position_pattern": [
                    "[\\w\\W]*?Place\\s*of\\s*delivery\\s*:\\s*"
                ],

                "value_pattern": [
                    ".*?\\n{1}(?P<DeliveryPlaceName>.*)$"
                ],
                "repeat_count": 1,
                "find_mode": "h",
                "separator_mode": "regex",
                "is_split_cell": 0,
                "split_pattern": [""],
                "action": [
                    {
                        "keyword": "DeliveryPlaceName",
                        "key": "DeliveryPlaceName"
                    }
                ]
            },
        },
        "table": {
            "containers": {
                "position_pattern": [
                    "[\\w\\W]*?([a-zA-Z]{4}\\d{7})\\s*\\d+[a-zA-Z]+\\d+\\s*[a-zA-Z]+\\d{6,}"
                ],
                "separator": "\\n",
                "find_mode": "h",
                "separator_mode": "regex",
                "column": [
                    "ContainerNo"
                ],
                "behaviors": [
                    {
                        "over_action": "row",
                        "loop": 1,
                        "value_pattern": [
                            '(?P<col_1>[a-zA-Z]{4}\\d{7})'
                        ],
                        "action": []
                    }
                ]
            }
        },
        "data_type_format": {
            "EstimatedArrivalDate": {
                "data_type": "time",
                "format": "%b  %d  %Y",
                "filter": ""
            },
        },
        "address_repair": {
            "db": {
                "pub": {
                    "user": "co",
                    "pwd": "Co&23@2332$22",
                    "server": "db.uat.com:1433",
                    "database": "CO_PUB"
                }
            },
            "repairs": [
                {
                    "key": "DeliveryPlaceName",
                    "db_key": "pub",
                    "sql": "SELECT  [FullName],[LocalName],[name],[code],[Id] from Places WHERE IsDeleted = 0 and IsOcean = 1 and IsValid = 1 and ([FullName] like '%${value}%' or charindex([FullName],'${value}')> 0) ;",
                    "column": [
                        0,
                        1,
                        2,
                        3
                    ],
                    "value": 4,
                    "mapping": "DeliveryPlaceId",
                    "old_val_handle": "empty"
                },
                {
                    "key": "DestinationPortName",
                    "db_key": "pub",
                    "sql": "SELECT  [FullName],[LocalName],[name],[code],[Id] from Places WHERE IsDeleted = 0 and IsOcean = 1 and IsValid = 1 and ([FullName] like '%${value}%' or charindex([FullName],'${value}')> 0) ;",
                    "column": [
                        0,
                        1,
                        2,
                        3
                    ],
                    "value": 4,
                    "mapping": "DestinationPortId",
                    "old_val_handle": "empty"
                }
            ]
        }
    }
}


class TestExcelDocumentParser:

    # def test_excel_file_parse(self):
    #     """
    #     单文件测试
    #     :return:
    #     """
    #     factory = DocParserFactory.create("excel2",
    #                                       r"C:\Users\APing\Desktop\temp\wanhai\wdmft505-an-usphx01-us01000135-0706-000075-115c505107-a.xlsx",
    #                                       config['parse'])
    #     result, errors = factory.parse()
    #
    #     print(result, errors)

    def test_excel_file_parse_more(self):
        dir_path = r'C:\Users\APing\Desktop\temp\msc'
        files = os.listdir(dir_path)
        succ_list = []
        for f in files:
            if f.endswith('.xlsx') and '~$' not in f:
                try:
                    factory = DocParserFactory.create("excel2", os.path.join(dir_path, f), config['parse'])
                    result, errors = factory.parse()
                    if (len(result) > 0 and len([v for k,v in result[0].items() if v=='']) > 0) or len(result) == 0 or len(result[0]) == 0:
                        print(f'{f}:{result}')
                    elif len(result) > 0:
                        succ_list.append(result[0])
                except Exception as e:
                    print(f'{f}:{e}{traceback.format_exc()}')
                    return
        print("===================================================")
        for item in succ_list:
            print(f'{f}:{item}')


if __name__ == '__main__':
    pytest.main("-q --html=report.html")
