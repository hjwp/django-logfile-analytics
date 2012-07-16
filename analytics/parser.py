import csv
from datetime import datetime
from analytics.models import Hit

def quote_fixing_iterator(filename):
    with open(filename) as f:
        for row in f.readlines():
            yield row.replace('[', '"').replace(']', '"')


def parse_logfile(filename):
    row_parser = csv.reader(quote_fixing_iterator(filename), delimiter=" ")
    for row in row_parser:
        print row
        source_ip, _, __, timestamp_str, method_url_protocol, status_code, response_size, referer_url, user_agent = row
        try:
            response_size = int(response_size)
        except ValueError:
            response_size = 0
        method, url, _ = method_url_protocol.split()
        timestamp = datetime.strptime(timestamp_str[:-6], '%d/%b/%Y:%H:%M:%S')
        Hit(
                source_ip=source_ip,
                timestamp=timestamp,
                method=method,
                url=url,
                referer_url=referer_url,
                status_code=status_code,
                response_size=response_size,
                user_agent=user_agent
        ).save()
