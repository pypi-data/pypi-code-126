from fxiaoke.api import FxiaokeApi
from fxiaoke.api import Request


class baseObj(object):
    SysObjs = [
        "LeadsObj",  # 线索
        "AccountObj",  # 客户
        "ContactObj",  # 联系人
        "ProductObj",  # 产品
        "RefundObj",  # 退款
        "SaleActionObj",  # 销售活动
        "OpportunityObj",  # 商机
        "InvoiceApplicationObj",  # 开票申请
        "SalesOrderObj",  # 销售订单
        "ReturnedGoodsInvoiceObj",  # 退货单
        "VisitingObj",
        "ContractObj",  # 合同对象
        "LeadsPoolObj",
        "HighSeasObj",
        "MarketingEventObj",  # 市场活动
        "AccountAttObj",
        "AccountCostObj",
        "ReturnedGoodsInvoiceProductObj",  # 退货单关联的产品
        "SalesOrderProductObj",  # 订单产品
        "AccountAddObj",
        "AccountFinInfoObj",  # 财务信息
        "AccountAddrObj",  # 客户地址
        "ActiveRecordObj",  # 销售记录
        "ApprovalInstanceObj",  # 审批流实例
        "ApprovalTaskObj",  # 审批流任务
        "AvailableAccountObj",  # 可售客户
        "AvailablePriceBookObj",  # 可售价目表
        "AvailableProductObj",  # 可售产品表
        "AvailableRangeObj",  # 可售范围
        "BatchObj",  # 批次
        "BatchStockObj",  # 批次库存
        "BOMObj",  # 产品选配明细
        "CasesDeviceObj",  # 工单设备
        "CasesObj",  # 工单
        "CheckinsObj",  # 高级外勤对象
        "CreditFileObj",  # 信用
        "CustomerAccountObj",  # 客户账户
        "DeliveryNoteObj",  # 发货单
        "DeliveryNoteProductObj",  # 发货单产品
        "DepartmentObj",  # 部门
        "DeviceObj",  # 设备
        "DevicePartObj",  # 设备配件规格关系
        "ExchangeReturnNoteObj",  # 退换货单
        "ExchangeReturnNoteProductObj",  # 退换货单产品
        "FeedReplyObj",  # 工作圈回复
        "FundReturnBackObj",  # 退款单
        "GoalValueObj",  # 目标值
        "GoodsReceivedNoteObj",  # 入库单
        "GoodsReceivedNoteProductObj",  # 入库单产品
        "InvoiceApplicationLinesObj",  # 开票申请明细
        "LeadsTransferLogObj",  # 线索转换日志
        "MemberGradeObj",  # 会员等级
        "MemberGrowthValueDetailObj",  # 会员成长值明细
        "MemberIntegralDetailObj",  # 会员积分明细
        "MemberObj",  # 会员
        "NewOpportunityContactsObj",  # 商机联系人
        "NewOpportunityLinesObj",  # 商机2.0明细
        "NewOpportunityObj",  # 商机2.0
        "OrderPaymentObj",  # 回款明细
        "OutboundDeliveryNoteObj",  # 出库单
        "OutboundDeliveryNoteProductObj",  # 出库单产品
        "PartnerObj",  # 合作伙伴
        "PaymentObj",  # 回款
        "PaymentPlanObj",  # 回款计划
        "PersonnelObj",  # 人员
        "PrepayDetailObj",  # 预存款
        "PriceBookObj",  # 价目表
        "PriceBookProductObj",  # 价目表明细
        "ProductGroupObj",  # 产品分组
        "PromotionObj",  # 促销
        "PromotionProductObj",  # 促销产品
        "PromotionRuleObj",  # 促销规则
        "PurchaseOrderObj",  # 采购订单
        "PurchaseOrderProductObj",  # 采购订单产品
        "QuoteLinesObj",  # 报价单明细
        "QuoteObj",  # 报价单
        "RebateIncomeDetailObj",  # 返利
        "RebateOutcomeDetailObj",  # 返利支出
        "ReceiveMaterialBillObj",  # 领料单
        "ReceiveMaterialBillProductObj",  # 领料单产品
        "RefundMaterialBillObj",  # 退料单
        "RefundMaterialBillProductObj",  # 退料单产品
        "RequisitionNoteObj",  # 调拨单
        "RequisitionNoteProductObj",  # 调拨单产品
        "SaleEventObj",  # 销售记录(已下线)
        "SerialNumberObj",  # 序列号
        "ServiceRecordObj",  # 通话记录
        "SpecificationObj",  # 规格表
        "SpecificationValueObj",  # 规格值表
        "SPUObj",  # 商品对象
        "StockCheckNoteObj",  # 盘点单
        "StockCheckNoteProductObj",  # 盘点单产品
        "StockDetailsObj",  # 出入库明细
        "StockObj",  # 库存
        "SubProductCatalogObj",  # 子产品分组
        "SubProductObj",  # 子产品明细
        "SupplierObj",  # 供应商
        "TelesalesRecordObj",  # 电销记录
        "UnitInfoObj",  # 产品单位
        "WarehouseObj",  # 仓库
        "WechatFanObj",  # 微信粉丝
    ]
    CustomType = 'custom'
    dataObjectApiName = ''

    node_id = None
    endpoint = None

    def __init__(self, api=None, dataObjectApiName=None):
        self._api = api or FxiaokeApi.get_default_api()
        self.dataObjectApiName = dataObjectApiName

    @classmethod
    def get_endpoint(cls):
        return cls.endpoint

    @classmethod
    def get_id_assured(cls):
        return cls.node_id

    def get_api(self):
        """
        Returns the api associated with the object.
        """
        return self._api

    @classmethod
    def is_sysobj(cls, dataObjectApiName):
        if dataObjectApiName in cls.SysObjs:
            return True

        if dataObjectApiName.startswith('object_') and \
                dataObjectApiName.endswith('__c'):
            return False

        if dataObjectApiName.endswith('Obj'):
            return True

        return False

    def describe(
        self,
        dataObjectApiName: str = None,
    ):
        dataObjectApiName = dataObjectApiName or self.dataObjectApiName
        params = {
            "includeDetail": True,
            "apiName": dataObjectApiName,
        }
        request = Request(
            'object',
            method='POST',
            endpoint=self.endpoint or 'describe',
            api=self._api,
        )
        request.add_params(params)
        return request.execute()

    def query(
        self,
        dataObjectApiName: str = None,
        filters: list = None,
        orders: list = None,
        fieldProjection: list = None,
        offset: int = 0,
        limit: int = 100,
    ):
        dataObjectApiName = dataObjectApiName or self.dataObjectApiName
        api_type = None if self.is_sysobj(dataObjectApiName) else self.CustomType
        params = {
            'data': {
                'dataObjectApiName': dataObjectApiName or self.dataObjectApiName,
                'search_query_info': {
                    'limit': limit,
                    'offset': offset,
                    'filters': filters or [],
                    'orders': orders or [],
                    'fieldProjection': fieldProjection or []
                }
            }
        }

        request = Request(
            self.node_id or 'data',
            method='POST',
            endpoint=self.endpoint or 'query',
            api=self._api,
            api_type=api_type,
        )
        # request.add_fields(fieldProjection)
        request.add_params(params)

        return request.execute()

    def create(
        self,
        object_data: dict = None,
        details: dict = None,
        dataObjectApiName: str = None,
    ):
        dataObjectApiName = dataObjectApiName or self.dataObjectApiName
        api_type = None if self.is_sysobj(dataObjectApiName) else self.CustomType

        details = details or {}
        if dataObjectApiName or self.dataObjectApiName:
            object_data['dataObjectApiName'] = dataObjectApiName or self.dataObjectApiName
        params = {
            'data': {
                'object_data': object_data,
                'details': details,
            }
        }

        request = Request(
            self.node_id or 'data',
            method='POST',
            endpoint=self.endpoint or 'create',
            api=self._api,
            api_type=api_type,
        )
        # request.add_fields(fieldProjection)
        request.add_params(params)

        return request.execute()

    def get(
        self,
        objectDataId: str,
        dataObjectApiName: str = None,
    ):
        dataObjectApiName = dataObjectApiName or self.dataObjectApiName
        api_type = None if self.is_sysobj(dataObjectApiName) else self.CustomType

        params = {
            'data': {
                'dataObjectApiName': dataObjectApiName or self.dataObjectApiName,
                'objectDataId': objectDataId,
            }
        }

        request = Request(
            self.node_id or 'data',
            method='POST',
            endpoint=self.endpoint or 'get',
            api=self._api,
            api_type=api_type,
        )
        request.add_params(params)

        return request.execute()
