import re

from config import HTTP_HEADER


__item__ = "Yunsuo Web Application Firewall (Yunsuo)"


def detect(content, **kwargs):
    headers = kwargs.get("headers", None)
    content = str(content)
    detection_schema = (
        re.compile(r"<img.class=.yunsuologo.", re.I),
        re.compile(r"yunsuo.session", re.I)
    )
    for detection in detection_schema:
        if detection.search(content) is not None:
            return True
        for header in headers.keys():
            if detection.search(headers[header]) is not None:
                return True