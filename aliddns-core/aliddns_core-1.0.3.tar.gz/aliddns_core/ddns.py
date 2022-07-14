"""Library to handle aliyun ddns."""
import logging
import hmac
import base64

from datetime import datetime
from requests import get
from hashlib import sha1
from random import randint
from json import JSONDecoder
from urllib.parse import quote
from urllib.parse import urlencode
from urllib.error import HTTPError

logger = logging.getLogger(__name__)


class AliddnsCore:
    """Representation of a aliyun ddns core."""
    def __init__(self, access_id, access_key, domain, sub_domain):
        self._Aliyun_API_URL = "https://alidns.aliyuncs.com/?"
        self._access_id = access_id
        self._access_key = access_key
        self._domain = domain
        self._sub_domain = sub_domain
        self._update_time = ""
        self._Aliyun_API_Type = "A"
        self._Aliyun_API_V6_Type = "AAAA"
        self._record = None
        self._record_v6 = None
        self._last_record = "0.0.0.0"
        self._last_record_v6 = "0.0.0.0"
        self._rc_record_id = -1
        self._rc_record_v6_id = -1

    @property
    def update_time(self):
        """Return the update time of ddns."""
        return self._update_time

    @property
    def domain(self):
        """Return the domain of ddns."""
        return self._domain

    @property
    def sub_domain(self):
        """Return the sub_domain of ddns."""
        return self._sub_domain

    @property
    def record(self):
        """Return the record of ddns."""
        return self._record

    @property
    def last_record(self):
        """Return the last record of ddns."""
        return self._last_record

    @property
    def record_v6(self):
        """Return the ipv6 record of ddns."""
        return self._record_v6

    @property
    def last_record_v6(self):
        """Return the last ipv6 record of ddns."""
        return self._last_record_v6

    def AliyunSignature(self,parameters):
        sortedParameters = sorted(parameters.items(), key=lambda parameters: parameters[0])
        canonicalizedQueryString = ''
        for (k, v) in sortedParameters:
            canonicalizedQueryString += '&' + self.CharacterEncode(k) + '=' + self.CharacterEncode(v)
        stringToSign = 'GET&%2F&' + self.CharacterEncode(canonicalizedQueryString[1:])
        h = hmac.new((self._access_key + "&").encode('ASCII'), stringToSign.encode('ASCII'), sha1)
        signature = base64.encodebytes(h.digest()).strip()
        return signature

    def CharacterEncode(self,encodeStr):
        encodeStr = str(encodeStr)
        res = quote(encodeStr.encode('utf-8'), '')
        res = res.replace('+', '%20')
        res = res.replace('*', '%2A')
        res = res.replace('%7E', '~')
        return res

    def AliyunAPIPOST(self,Aliyun_API_Action):
        Aliyun_API_SD = {
            'Format': 'json',
            'Version': '2015-01-09',
            'AccessKeyId': self._access_id,
            'SignatureMethod': 'HMAC-SHA1',
            'Timestamp': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
            'SignatureVersion': '1.0',	
            'SignatureNonce': randint(0, 99999999999999),
            'Action': Aliyun_API_Action
        }
        return Aliyun_API_SD

    def check_record_id(self,sub_domain,domain):
        Aliyun_API_Post = self.AliyunAPIPOST('DescribeDomainRecords')
        Aliyun_API_Post['DomainName'] = domain
        Aliyun_API_Post['Signature'] = self.AliyunSignature(Aliyun_API_Post)
        Aliyun_API_Post = urlencode(Aliyun_API_Post)
        Aliyun_API_Request = get(self._Aliyun_API_URL + Aliyun_API_Post)

        domainRecords = ''
        try:
            domainRecords = Aliyun_API_Request.text
        except HTTPError as e:
            return -1
        try:
            result = JSONDecoder().decode(domainRecords)
            if not result:
                return -1
            result = result['DomainRecords']['Record']
            index = 0
            for record_info in result:
                if record_info['RR'] == sub_domain:
                    if record_info['Type'] == self._Aliyun_API_Type:
                        self._rc_record_id = int(result[index]['RecordId'])
                    if record_info['Type'] == self._Aliyun_API_V6_Type:
                        self._rc_record_v6_id = int(result[index]['RecordId'])

                index += 1
            return 0
        except Exception as e:
            return -1

    
    def old_ip(self,Aliyun_API_RecordID):
        Aliyun_API_Post = self.AliyunAPIPOST('DescribeDomainRecordInfo')
        Aliyun_API_Post['RecordId'] = Aliyun_API_RecordID
        Aliyun_API_Post['Signature'] = self.AliyunSignature(Aliyun_API_Post)
        Aliyun_API_Post = urlencode(Aliyun_API_Post)
        Aliyun_API_Request = get(self._Aliyun_API_URL + Aliyun_API_Post)
        result = JSONDecoder().decode(Aliyun_API_Request.text)
        return result.get('Value','no record')

    def add_dns(self,domainIP, Aliyun_API_Type):
        Aliyun_API_Post = self.AliyunAPIPOST('AddDomainRecord')
        Aliyun_API_Post['DomainName'] = self.domain
        Aliyun_API_Post['RR'] = self._sub_domain
        Aliyun_API_Post['Type'] = Aliyun_API_Type
        Aliyun_API_Post['Value'] = domainIP
        Aliyun_API_Post['Signature'] = self.AliyunSignature(Aliyun_API_Post)
        Aliyun_API_Post = urlencode(Aliyun_API_Post)
        get(self._Aliyun_API_URL + Aliyun_API_Post)

    def delete_dns(self,Aliyun_API_RecordID):
        Aliyun_API_Post = self.AliyunAPIPOST('DeleteDomainRecord')
        Aliyun_API_Post['RecordId'] = Aliyun_API_RecordID
        Aliyun_API_Post['Signature'] = self.AliyunSignature(Aliyun_API_Post)
        Aliyun_API_Post = urlencode(Aliyun_API_Post)
        get(self._Aliyun_API_URL + Aliyun_API_Post)

    def update_dns(self,Aliyun_API_RecordID, Aliyun_API_Value, Aliyun_API_Type):
        Aliyun_API_Post = self.AliyunAPIPOST('UpdateDomainRecord')
        Aliyun_API_Post['RecordId'] = Aliyun_API_RecordID
        Aliyun_API_Post['RR'] = self._sub_domain
        Aliyun_API_Post['Type'] = Aliyun_API_Type
        Aliyun_API_Post['Value'] = Aliyun_API_Value
        Aliyun_API_Post['Signature'] = self.AliyunSignature(Aliyun_API_Post)
        Aliyun_API_Post = urlencode(Aliyun_API_Post)
        get(self._Aliyun_API_URL + Aliyun_API_Post)

    def set_dns(self,Aliyun_API_RecordID, Aliyun_API_Enabled):
        Aliyun_API_Post = self.AliyunAPIPOST('SetDomainRecordStatus')
        Aliyun_API_Post['RecordId'] = Aliyun_API_RecordID
        Aliyun_API_Post['Status'] = "Enable" if Aliyun_API_Enabled else "Disable"
        Aliyun_API_Post['Signature'] = self.AliyunSignature(Aliyun_API_Post)
        Aliyun_API_Post = urlencode(Aliyun_API_Post)
        get(self._Aliyun_API_URL + Aliyun_API_Post)

    def need_check_record_id(self, update_ip_v6):
        if self._rc_record_id < 0 :
            return True
        if update_ip_v6 and self._rc_record_v6_id < 0:
            return True
        return False

    def update_dns_record(self, rc_value, rc_record_id, api_type, record_ip_v6=False):
        if rc_record_id < 0:
            self.add_dns(rc_value, api_type)
        else:         
            rc_value_old = self.old_ip(rc_record_id)
            if rc_value != rc_value_old:
                if record_ip_v6 :
                    self._last_record_v6 = rc_value_old
                else :
                    self._last_record = rc_value_old
                self.update_dns(rc_record_id, rc_value, api_type)

        if record_ip_v6 :
            self._record_v6 = rc_value
        else:      
            self._record = rc_value

        self._update_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def update_ddns(self, ddns_record, ddns_record_v6=None):

        if self.need_check_record_id(ddns_record_v6):
            if self.check_record_id(self._sub_domain, self._domain) < 0:
                self._state = "network error"
                return False

        self.update_dns_record(ddns_record, self._rc_record_id, self._Aliyun_API_Type)
        if ddns_record_v6:
            self.update_dns_record(ddns_record_v6, self._rc_record_v6_id, 
                self._Aliyun_API_V6_Type, True)

        return True
