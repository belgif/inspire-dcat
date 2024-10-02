import requests
import io
import owslib.csw as owscsw
import owslib.fes as owsfes

from lxml import etree

from params.params import get_param


class GeoNetworkError(Exception):

    pass


def check_response(r):
    if r.status_code >= 400:
        raise GeoNetworkError("The geonetwork server returned the http code: {}\n\n"
                              "The error content is:\n".format(r.status_code) + r.content)


def add_xml_declaration(xml):
    if xml[:5] != '<?xml':
        return '<?xml version="1.0" encoding="UTF-8"?>\n' + xml
    return xml


class GeoNetwork(object):

    def __init__(self, url, username=None, password=None):
        self.url = url
        self.session = requests.Session()

        r = self.session.get(self.url + get_param("gn_signin_path"))
        check_response(r)
        self.session.post(self.url + get_param("gn_get_info_me"))

        self.csrftoken = self.session.cookies['XSRF-TOKEN']
        self.jsessionid = self.session.cookies['JSESSIONID']

        if username:
            post_data = {
                "username": username,
                "password": password,
                '_csrf': self.csrftoken
            }
            r = self.session.post(self.url + get_param("gn_signin_post_path"), data=post_data)
            check_response(r)

    def _prepare_request(self, operation, url, accept='xml', files=None, data=None, json=None):
        print (url, "VERIF URL")
        headers_data = {
            'X-XSRF-TOKEN': self.csrftoken,
            'Accept': 'application/json, text/javascript, */*; q=0.01' if accept != 'xml'
            else 'text/html,application/xhtml+xml,application/xml;q=0.9'
        }
        req = requests.Request(operation, url, headers=headers_data, files=files, data=data, json=json)
        prepped = self.session.prepare_request(req)
        prepped.headers['Cookie'] += ";JSESSIONID={};XSRF-TOKEN={}".format(self.jsessionid, self.csrftoken)
        return prepped

    def upload_record(self, xml_content): #function that uses the GeoNetwork API
        xml_content = add_xml_declaration(xml_content)
        print (xml_content)
        post_data = {
            'metadataType': 'METADATA',
            'uuidProcessing': 'NOTHING',
            'transformWith': '_none_',
            'group': get_param("gn_group_id"),
            'category': ''
        }
        files_data = {'file': ('dummy.xml', io.StringIO(xml_content), 'text/xml')}
        print ('VERIF URL', self.url, ' ',get_param("gn_api_records_path"))
        prepped = self._prepare_request('POST', self.url + get_param("gn_api_records_path"),
                                        accept='json', files=files_data, data=post_data)
        r = self.session.send(prepped)
        print ("RESPONSE CODE ",r.status_code)

        print (r.text)
        # check_response(r)
        
       

    def get_record(self, id):
        """
        fetches the metadata where the fileIdentifier is equal to id
        """
        url = self.url + get_param('gn_unpublished_record_xml_path').format(id=id)
        prepped = self._prepare_request('GET', url, accept='xml')
        r = self.session.send(prepped)
        check_response(r)
        return etree.fromstring(r.content)

    def record_exists(self, id):
        url = self.url + get_param('gn_unpublished_record_path').format(id=id)
        return not self._is_404(url)

    def delete_record(self, id):
        url = self.url + get_param('gn_unpublished_record_path').format(id=id)
        prepped = self._prepare_request('DELETE', url, accept='json')
        r = self.session.send(prepped)
        check_response(r)

    def _is_404(self, url):
        r = self.session.get(url)
        return r.status_code == 404

    def delete_attachment(self, id, filename):
        url = self.url + get_param("gn_api_attachment_path").format(id=id, filename=filename)
        if not self._is_404(url):
            prepped = self._prepare_request('DELETE', url, accept='json')
            r = self.session.send(prepped)
            check_response(r)
            return True
        return False

    def add_attachment(self, id, filename):
        # it seems to work with 'text/xml' all the time but maybe we should try to infer the type from the file...
        files_data = {'file': (filename, open(filename, 'rb'), 'text/xml')}
        prepped = self._prepare_request('POST', self.url + get_param("gn_api_attachments_path").format(id=id),
                                        accept='json', files=files_data)
        r = self.session.send(prepped)
        check_response(r)

    def update_attachment(self, id, filename):
        self.delete_attachment(id, filename)
        self.add_attachment(id, filename)

    def unpublish_record(self, id):
        json_data = {
            "clear": "false",
            "privileges": [{
                "group": "1",
                "operations": {"view": "false", "download": "false", "dynamic": "false"}
            }]
        }
        prepped = self._prepare_request('PUT', self.url + get_param("gn_api_record_sharing_path").format(id=id),
                                        accept='json', json=json_data)
        r = self.session.send(prepped)
        check_response(r)

    def publish_record(self, id):
        json_data = {
            "clear": "false",
            "privileges": [{
                "group": "1",
                "operations": {"view": "true", "download": "true", "dynamic": "true"}
            }]
        }
        prepped = self._prepare_request('PUT', self.url + get_param("gn_api_record_sharing_path").format(id=id),
                                        accept='json', json=json_data)
        r = self.session.send(prepped)
        check_response(r)


class CSW(object):

    def __init__(self, url, username=None, password=None, skip_caps=False):
        self.url = url
        self.csw = owscsw.CatalogueServiceWeb(self.url, username=username, password=password, skip_caps=skip_caps)
        self.username = username
        self.password = password

    def list_records(self, keywords=[], typerecord=[]):
        #par defaut les types et les keywords a selectionner sont vides --> toutes les fiches sont selectionnees
        constrains = []
        if len(typerecord) > 0:
            for type in typerecord:
                constrains.append(owsfes.PropertyIsEqualTo('dc:type', type))
        if len(keywords) > 0:
            for keyword in keywords:
                constrains.append(owsfes.PropertyIsEqualTo('dc:subject', keyword))
        self.csw.getrecords2(constraints=constrains, maxrecords=100000)
        identifiers = []
        for rec in self.csw.records:
            identifiers.append(self.csw.records[rec].identifier)
        return identifiers

    def update_record(self, id, xml_content):
        xml_content = add_xml_declaration(xml_content)
        self.csw.transaction(ttype='update', typename='gmd:MD_Metadata', record=xml_content, identifier=id)

    def get_record(self, id):
        """
        fetches the metadata where the fileIdentifier is equal to id
        """
        url = self.url + get_param("csw_get_record_by_id") + "&id=" + id
        if self.username is None:
            r = requests.get(url)
        else:
            r = requests.get(url, auth=(self.username, self.password))
        check_response(r)
        tree = etree.fromstring(r.content)
        # CSW results encapsulate the xml in one tag
        return tree[0]


