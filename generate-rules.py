# Description: TODO

import errno
import os
import json
import datetime
import requests

# where to cache downloaded files
cache_path = "./iran_domains"

# cache age in days
cache_lifetime = -100

iran_hosted_domains_link = "https://github.com/SamadiPour/iran-hosted-domains/releases/latest/download/domains.txt"
iran_hosted_domains_file_path = cache_path + "/domains.txt"

iran_ads_domains_link = "https://raw.githubusercontent.com/MasterKia/PersianBlocker/main/PersianBlockerHosts.txt"
iran_ads_domains_file_path = cache_path + "/PersianBlockerHosts.txt"

datetime_format = '%Y/%m/%d - %H:%M:%S'

v2rayN_template_file_path = './v2rayN-rules-template.json'

v2rayN_output_file_path = './v2rayN_rules.json'

def log(msg):
    time = datetime.datetime.now()
    print('[' + time.strftime(datetime_format) + '] ' + str(msg))


# returns raw content of a file
def load_from_file(file_full_path):
    f = open(file_full_path, 'r', encoding="utf-8")
    content = f.read()
    f.close()
    return content


# save to file
def save_to_file(file_full_path, content, mode='w'):
    if not os.path.exists(os.path.dirname(file_full_path)):
        try:
            os.makedirs(os.path.dirname(file_full_path))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    with open(file_full_path, mode, encoding="utf-8") as f:
        f.write(content)


# download and save list of domains, if `from_local_cache` is true, `the_path` must be local path
def get_domains(the_path, from_local_cache):
    if from_local_cache:
        if not os.path.exists(the_path):
            return ""
        raw = load_from_file(the_path)
        log('got domain list from local path: ' + the_path)
    else:
        log('downloading domain list from web: ' + the_path)
        try:
            raw = requests.get(the_path, timeout=5000).content.decode('utf-8')
        except (requests.exceptions.RequestException, ValueError) as e:
            log('Error: ' + str(e))
            log('fetching domains failed')
            raw = ""
    # todo from this function -> save_to_file(local_path, raw)
    return raw


def download_domains_to_cache():
    error_message = ''
    iran_hosted_domains_raw = get_domains(iran_hosted_domains_link, False)
    iran_ads_domains_raw = get_domains(iran_ads_domains_link, False)
    if len(iran_hosted_domains_raw) > 5000:
        save_to_file(iran_hosted_domains_file_path, iran_hosted_domains_raw)
    else:
        error_message = 'Error downloading from ' + iran_hosted_domains_link + '\n'
    if len(iran_ads_domains_raw) > 5000:
        save_to_file(iran_ads_domains_file_path, iran_ads_domains_raw)
    else:
        error_message = 'Error downloading from ' + iran_ads_domains_link + '\n'
    return error_message


def get_block_domain_list():
    domains_list = []
    for line in get_domains(iran_ads_domains_file_path, True).splitlines():
        if line.startswith("#") or line.startswith("[") or len(line) < 2:
            continue
        domains_list.append(line)
    return domains_list


def get_iran_domain_list():
    domains_list = []
    for line in get_domains(iran_hosted_domains_file_path, True).splitlines():
        if line.endswith('.ir'):
            continue
        domains_list.append(line)
    return domains_list


def get_cache_age(cache_last_update_file_path):
    try:
        cache_last_update = load_from_file(cache_last_update_file_path)
        cache_last_update = datetime.datetime.strptime(
            cache_last_update, datetime_format).strftime(datetime_format)
    except (ValueError, FileNotFoundError):
        cache_last_update = (datetime.datetime.now(
        ) - datetime.timedelta(days=100, seconds=15)).strftime(datetime_format)

    return datetime.datetime.now(
    ) - datetime.datetime.strptime(cache_last_update, datetime_format)


def set_cache_age(cache_last_update_file_path):
    save_to_file(cache_last_update_file_path,
                 datetime.datetime.now().strftime(datetime_format))


def update_iran_domains():
    cache_last_update_file_path = os.path.join(
        cache_path, "cache_last_update.txt")
    cache_age = get_cache_age(cache_last_update_file_path)
    # if cache_age is expired or one of lists are not exists, then download lists
    if cache_age.days > cache_lifetime or not os.path.exists(iran_ads_domains_file_path) or not os.path.exists(
            iran_hosted_domains_file_path):
        save_error_messages = download_domains_to_cache()
        if len(save_error_messages) > 0:
            log(save_error_messages)
        else:
            log('domains list downloaded and cached successfully')
            set_cache_age(cache_last_update_file_path)
    else:
        log('domains list is up to date (updated less than ' +
            str(cache_lifetime) + ' days ago !)')


# Program entry
if __name__ == '__main__':
    update_iran_domains()
    block_domain_list = get_block_domain_list()
    iran_domain_list = get_iran_domain_list()
    with open(v2rayN_template_file_path, 'r', encoding="utf-8") as v2rayN_template_file:
        v2rayN_rules = json.load(v2rayN_template_file)
        for rule in v2rayN_rules:
            if rule['id'] == 'ads-block':
                rule['domain'] = block_domain_list
            if rule['id'] == 'iran-sites':
                rule['domain'] = iran_domain_list
    with open(v2rayN_output_file_path, 'w', encoding="utf-8") as f:
        json.dump(v2rayN_rules, f)
    log("v2rayN rules file saved to: " + v2rayN_output_file_path)
