"""Auto-generated file, do not edit by hand. IL metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_IL = PhoneMetadata(id='IL', country_code=972, international_prefix='0(?:0|1[2-9])',
    general_desc=PhoneNumberDesc(national_number_pattern='[17]\\d{6,9}|[2-589]\\d{3}(?:\\d{3,6})?|6\\d{3}', possible_number_pattern='\\d{4,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='[2-489]\\d{7}', possible_number_pattern='\\d{7,8}', example_number='21234567'),
    mobile=PhoneNumberDesc(national_number_pattern='5(?:[02347-9]\\d{2}|5(?:2[23]|3[34]|4[45]|5[5689]|6[67]|7[78]|8[89])|6[2-9]\\d)\\d{5}', possible_number_pattern='\\d{9}', example_number='501234567'),
    toll_free=PhoneNumberDesc(national_number_pattern='1(?:80[019]\\d{3}|255)\\d{3}', possible_number_pattern='\\d{7,10}', example_number='1800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern='1(?:212|(?:9(?:0[01]|19)|200)\\d{2})\\d{4}', possible_number_pattern='\\d{8,10}', example_number='1919123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern='1700\\d{6}', possible_number_pattern='\\d{10}', example_number='1700123456'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='7(?:2[23]\\d|3[237]\\d|47\\d|6(?:5\\d|8[08])|7\\d{2}|8(?:33|55|77|81))\\d{5}', possible_number_pattern='\\d{9}', example_number='771234567'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='[2-689]\\d{3}|1599\\d{6}', possible_number_pattern='\\d{4}(?:\\d{6})?', example_number='1599123456'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='1700\\d{6}|[2-689]\\d{3}', possible_number_pattern='\\d{4,10}', example_number='1700123456'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='([2-489])(\\d{3})(\\d{4})', format=u'\\1-\\2-\\3', leading_digits_pattern=['[2-489]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([57]\\d)(\\d{3})(\\d{4})', format=u'\\1-\\2-\\3', leading_digits_pattern=['[57]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(1)([7-9]\\d{2})(\\d{3})(\\d{3})', format=u'\\1-\\2-\\3-\\4', leading_digits_pattern=['1[7-9]'], national_prefix_formatting_rule=u'\\1'),
        NumberFormat(pattern='(1255)(\\d{3})', format=u'\\1-\\2', leading_digits_pattern=['125'], national_prefix_formatting_rule=u'\\1'),
        NumberFormat(pattern='(1200)(\\d{3})(\\d{3})', format=u'\\1-\\2-\\3', leading_digits_pattern=['120'], national_prefix_formatting_rule=u'\\1'),
        NumberFormat(pattern='(1212)(\\d{2})(\\d{2})', format=u'\\1-\\2-\\3', leading_digits_pattern=['121'], national_prefix_formatting_rule=u'\\1'),
        NumberFormat(pattern='(1599)(\\d{6})', format=u'\\1-\\2', leading_digits_pattern=['15'], national_prefix_formatting_rule=u'\\1'),
        NumberFormat(pattern='(\\d{4})', format=u'*\\1', leading_digits_pattern=['[2-689]'], national_prefix_formatting_rule=u'\\1')])
