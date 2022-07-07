#  =============================================================================
#  GNU Lesser General Public License (LGPL)
#
#  Copyright (c) 2022 Qujamlee from www.aztquant.com
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#  =============================================================================

# 尚未连接服务
class UnconnectedError(Exception):
    pass


# 服务器连接失败
class ConnectedFailed(ConnectionError):
    pass


# 服务器连接中断
class ConnectedBroken(ConnectionError):
    pass


# 尚未登录
class NotLoginedError(Exception):
    pass


# 非交易时间
class NonTradingTimeError(Exception):
    pass


# 时间格式错误
class DatetimeTypeError(TypeError):
    pass


# 列表格式错误
class ListTypeError(TypeError):
    pass


# 字典格式错误
class DictTypeError(TypeError):
    pass


# 参数错误
class ArgsError(Exception):
    pass


# 错误的行情数据
class MarketDataError(Exception):
    pass


# 订阅失败
class SubscribeError(Exception):
    pass


# 退订失败
class UnsubscribeError(Exception):
    pass
