#!/usr/bin/env python
# -*- coding:utf-8 -*-

def is_similar_by_degree_of_similarity(standard_text, text):
    degree_of_similarity = difflib.SequenceMatcher(None, standard_text, text).quick_ratio()
    if degree_of_similarity < 0.85:
        return True
    return False

def check_200_or_404(url):
    # 200 -> True    404 -> False
    parse_result = urlparse(url)
    url_404 = "%s://%s/this_is_404_page_%s"%(parse_result.scheme, parse_result.netloc, random8string())
    try:
        standard_text = Requester(url_404).html
    except RequesterOpenError as e:
        try:
            standard_text = Requester(url_404).html
        except:
            return True
    try:
        text = Requester(url).html
    except RequesterOpenError as e:
        try:
            text = Requester(url).html
        except:
            return True
    return is_similar_by_degree_of_similarity(standard_text, text)

globals()['check_200_or_404'] = check_200_or_404
globals()['is_similar_by_degree_of_similarity'] = is_similar_by_degree_of_similarity