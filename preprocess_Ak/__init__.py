from preprocess_Ak import utils

__version__ = '0.0.1'


def get_wordcounts(x):
    return utils._get_wordcounts(x)


def get_charcounts(x):
    return utils._get_charcounts(x)


def get_avg_word_length(x):
    return utils._get_avg_word_length(x)


def get_stopwords_counts(x):
    return utils._get_stopwords_counts(x)


def get_hashtag_count(x):
    return utils._get_hashtag_count(x)


def get_mention_count(x):
    return utils._get_mention_count(x)


def get_digit_counts(x):
    return utils._get_digit_counts(x)


def get_upper_counts(x):
    return utils._get_upper_counts(x)


def get_contraction_to_expansion(x):
    return utils._get_contraction_to_expansion(x)


def get_emails(x):
    return utils._get_emails(x)


def remove_emails(x):
    return utils._remove_emails(x)


def get_urls(x):
    return utils._get_urls(x)


def remove_urls(x):
    return utils._remove_urls(x)


def remove_rt(x):
    return utils._remove_rt(x)


def remove_special_chars(x):
    return utils._remove_special_chars(x)


def remove_html_tags(x):
    return utils._remove_html_tags(x)


def remove_accented_chars(x):
    return utils._remove_accented_chars(x)


def remove_stopword(x):
    return utils._remove_stopword(x)


def make_base(x):
    return utils._make_base(x)


def remove_common_words(x, n=20):
    return utils._remove_common_words(x)


def remove_rarewords(x, n=20):
    return utils._remove_rarewords(x)


def spelling_correction(x):
    return utils._spelling_correction(x)

