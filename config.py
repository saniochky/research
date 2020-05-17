API_KEY = "cxCB9MUriHyczSza-CBe"

INDEX_DICT = {
    1: "CPI",
    2: "IC_FRM_CORR_GRAFT2",
    3: "IC_FRM_OBS_OBST4",
    4: "IC_FRM_CORR_CORR4",
    5: "IC_FRM_CORR_CORR2",
    6: "IC_FRM_CORR_CORR11",
    7: "IC_FRM_CORR_CRIME9",
    8: "IC_FRM_CORR_CORR3"
}

QUANDL = {
    2: 'Bribery index (% of gift or informal payment requests during public transactions)',
    3: 'Percent of firms choosing corruption as their biggest obstacle',
    4: 'Percent of firms expected to give gifts to public officials "to get things done"',
    5: 'Percent of firms expected to give gifts to secure government contract',
    6: 'Percent of firms identifying corruption as a major constraint',
    7: 'Percent of firms identifying the courts system as a major constraint',
    8: 'Value of gift expected to secure a government contract (% of contract value)'
}

ISO = {
    'afghanistan': 'AFG',
    'åland islands': 'ALA',
    'albania': 'ALB',
    'algeria': 'DZA',
    'american samoa': 'ASM',
    'andorra': 'AND',
    'angola': 'AGO',
    'anguilla': 'AIA',
    'antarctica': 'ATA',
    'antigua and barbuda': 'ATG',
    'argentina': 'ARG',
    'armenia': 'ARM',
    'aruba': 'ABW',
    'australia': 'AUS',
    'austria': 'AUT',
    'azerbaijan': 'AZE',
    'bahamas': 'BHS',
    'bahrain': 'BHR',
    'bangladesh': 'BGD',
    'barbados': 'BRB',
    'belarus': 'BLR',
    'belgium': 'BEL',
    'belize': 'BLZ',
    'benin': 'BEN',
    'bermuda': 'BMU',
    'bhutan': 'BTN',
    'bolivia': 'BOL',
    'bonaire, sint eustatius and saba': 'BES',
    'bosnia and herzegovina': 'BIH',
    'botswana': 'BWA',
    'bouvet island': 'BVT',
    'brazil': 'BRA',
    'british indian ocean territory': 'IOT',
    'brunei darussalam': 'BRN',
    'bulgaria': 'BGR',
    'burkina faso': 'BFA',
    'burundi': 'BDI',
    'cape verde': 'CPV',
    'cambodia': 'KHM',
    'cameroon': 'CMR',
    'canada': 'CAN',
    'cayman islands': 'CYM',
    'central african republic': 'CAF',
    'chad': 'TCD',
    'chile': 'CHL',
    'china': 'CHN',
    'christmas island': 'CXR',
    'cocos (keeling) islands': 'CCK',
    'colombia': 'COL', 'comoros': 'COM',
    'congo, republic of': 'COG',
    'congo, democratic republic of': 'COD',
    'cook islands': 'COK',
    'costa rica': 'CRI',
    "côte d'ivoire": 'CIV',
    'croatia': 'HRV',
    'cuba': 'CUB',
    'curaçao': 'CUW',
    'cyprus': 'CYP',
    'czech republic': 'CZE',
    'denmark': 'DNK',
    'djibouti': 'DJI',
    'dominica': 'DMA',
    'dominican republic': 'DOM',
    'ecuador': 'ECU',
    'egypt': 'EGY',
    'el salvador': 'SLV',
    'equatorial guinea': 'GNQ',
    'eritrea': 'ERI',
    'estonia': 'EST',
    'eswatini': 'SWZ',
    'ethiopia': 'ETH',
    'falkland islands (malvinas)': 'FLK',
    'faroe islands': 'FRO',
    'fiji': 'FJI',
    'finland': 'FIN',
    'france': 'FRA',
    'french guiana': 'GUF',
    'french polynesia': 'PYF',
    'french southern territories': 'ATF',
    'gabon': 'GAB',
    'gambia': 'GMB',
    'georgia': 'GEO',
    'germany': 'DEU',
    'ghana': 'GHA',
    'gibraltar': 'GIB',
    'greece': 'GRC',
    'greenland': 'GRL',
    'grenada': 'GRD',
    'guadeloupe': 'GLP',
    'guam': 'GUM',
    'guatemala': 'GTM',
    'guernsey': 'GGY',
    'guinea': 'GIN',
    'guinea-bissau': 'GNB',
    'guyana': 'GUY',
    'haiti': 'HTI',
    'heard island and mcdonald islands': 'HMD',
    'holy see': 'VAT',
    'honduras': 'HND',
    'hong kong': 'HKG',
    'hungary': 'HUN',
    'iceland': 'ISL',
    'india': 'IND',
    'indonesia': 'IDN',
    'iran': 'IRN',
    'iraq': 'IRQ',
    'ireland': 'IRL',
    'isle of man': 'IMN',
    'israel': 'ISR',
    'italy': 'ITA',
    'jamaica': 'JAM',
    'japan': 'JPN',
    'jersey': 'JEY',
    'jordan': 'JOR',
    'kazakhstan': 'KAZ',
    'kenya': 'KEN',
    'kiribati': 'KIR',
    "korea (democratic people's republic of)": 'PRK',
    'korea, republic of': 'KOR',
    'kuwait': 'KWT',
    'kyrgyzstan': 'KGZ',
    "laos": 'LAO',
    'latvia': 'LVA',
    'lebanon': 'LBN',
    'lesotho': 'LSO',
    'liberia': 'LBR',
    'libya': 'LBY',
    'liechtenstein': 'LIE',
    'lithuania': 'LTU',
    'luxembourg': 'LUX',
    'macao': 'MAC',
    'madagascar': 'MDG',
    'malawi': 'MWI',
    'malaysia': 'MYS',
    'maldives': 'MDV',
    'mali': 'MLI',
    'malta': 'MLT',
    'marshall islands': 'MHL',
    'martinique': 'MTQ',
    'mauritania': 'MRT',
    'mauritius': 'MUS',
    'mayotte': 'MYT',
    'mexico': 'MEX',
    'micronesia (federated states of)': 'FSM',
    'moldova': 'MDA',
    'monaco': 'MCO',
    'mongolia': 'MNG',
    'montenegro': 'MNE',
    'montserrat': 'MSR',
    'morocco': 'MAR',
    'mozambique': 'MOZ',
    'myanmar': 'MMR',
    'namibia': 'NAM',
    'nauru': 'NRU',
    'nepal': 'NPL',
    'netherlands': 'NLD',
    'new caledonia': 'NCL',
    'new zealand': 'NZL',
    'nicaragua': 'NIC',
    'niger': 'NER',
    'nigeria': 'NGA',
    'niue': 'NIU',
    'norfolk island': 'NFK',
    'macedonia fyr': 'MKD',
    'northern mariana islands': 'MNP',
    'norway': 'NOR', 'oman': 'OMN',
    'pakistan': 'PAK', 'palau': 'PLW',
    'palestine, state of': 'PSE',
    'panama': 'PAN',
    'papua new guinea': 'PNG',
    'paraguay': 'PRY',
    'peru': 'PER',
    'philippines': 'PHL',
    'pitcairn': 'PCN',
    'poland': 'POL',
    'portugal': 'PRT',
    'puerto rico': 'PRI',
    'qatar': 'QAT',
    'réunion': 'REU',
    'romania': 'ROU',
    'russia': 'RUS',
    'rwanda': 'RWA',
    'saint barthélemy': 'BLM',
    'saint helena, ascension and tristan da cunha': 'SHN',
    'saint kitts and nevis': 'KNA',
    'saint lucia': 'LCA',
    'saint martin (french part)': 'MAF',
    'saint pierre and miquelon': 'SPM',
    'saint vincent and the grenadines': 'VCT',
    'samoa': 'WSM',
    'san marino': 'SMR',
    'sao tome and principe': 'STP',
    'saudi arabia': 'SAU',
    'senegal': 'SEN',
    'serbia': 'SRB',
    'seychelles': 'SYC',
    'sierra leone': 'SLE',
    'singapore': 'SGP',
    'sint maarten (dutch part)': 'SXM',
    'slovakia': 'SVK',
    'slovenia': 'SVN',
    'solomon islands': 'SLB',
    'somalia': 'SOM',
    'south africa': 'ZAF',
    'south georgia and the south sandwich islands': 'SGS',
    'south sudan': 'SSD',
    'spain': 'ESP',
    'sri lanka': 'LKA',
    'sudan': 'SDN',
    'suriname': 'SUR',
    'svalbard and jan mayen': 'SJM',
    'sweden': 'SWE',
    'switzerland': 'CHE',
    'syria': 'SYR',
    'taiwan, province of china': 'TWN',
    'tajikistan': 'TJK',
    'tanzania': 'TZA',
    'thailand': 'THA',
    'timor-leste': 'TLS',
    'togo': 'TGO',
    'tokelau': 'TKL',
    'tonga': 'TON',
    'trinidad and tobago': 'TTO',
    'tunisia': 'TUN',
    'turkey': 'TUR',
    'turkmenistan': 'TKM',
    'turks and caicos islands': 'TCA',
    'tuvalu': 'TUV',
    'uganda': 'UGA',
    'ukraine': 'UKR',
    'united arab emirates': 'ARE',
    'united kingdom of great britain and northern ireland': 'GBR',
    'united states of america': 'USA',
    'united states minor outlying islands': 'UMI',
    'uruguay': 'URY',
    'uzbekistan': 'UZB',
    'vanuatu': 'VUT',
    'venezuela': 'VEN',
    'vietnam': 'VNM',
    'virgin islands (british)': 'VGB',
    'virgin islands (u.s.)': 'VIR',
    'wallis and futuna': 'WLF',
    'western sahara': 'ESH',
    'yemen': 'YEM',
    'zambia': 'ZMB',
    'zimbabwe': 'ZWE'
}

DEVELOPING_COUNTRIES = [
    'afghanistan',
    'albania',
    'algeria',
    'samoa',
    'angola',
    'argentina',
    'armenia',
    'azerbaijan',
    'bahrain',
    'bangladesh',
    'barbados',
    'belarus',
    'belize',
    'benin',
    'bhutan',
    'bolivia',
    'bosnia and herzegovina',
    'botswana',
    'brazil',
    'bulgaria',
    'burkina faso',
    'burundi',
    'cambodia',
    'cameroon',
    'cape verde',
    'central african republic',
    'chad',
    'chile',
    'china',
    'colombia',
    'comoros',
    'congo, democratic republic of',
    'congo, republic of',
    'costa rica',
    'croatia',
    'cuba',
    'czech republic',
    'djibouti',
    'dominica',
    'dominican republic',
    'ecuador',
    'egypt',
    'el salvador',
    'eritrea',
    'estonia',
    'ethiopia',
    'fiji',
    'gabon',
    'gambia',
    'georgia',
    'ghana',
    'grenada',
    'guatemala',
    'guinea',
    'guinea-bissau',
    'guyana', 'haiti',
    'honduras',
    'hungary',
    'india',
    'indonesia',
    'iran',
    'iraq',
    'jamaica',
    'jordan',
    'kazakhstan',
    'kenya',
    'kiribati',
    'korea, republic of',
    'kyrgyzstan',
    'laos',
    'latvia',
    'lebanon',
    'lesotho',
    'liberia',
    'libya',
    'lithuania',
    'macedonia fyr',
    'madagascar',
    'malawi',
    'malaysia',
    'maldives',
    'mali',
    'malta',
    'mauritania',
    'mauritius',
    'mexico',
    'moldova',
    'mongolia',
    'morocco',
    'mozambique',
    'myanmar',
    'namibia',
    'nepal',
    'netherlands',
    'nicaragua',
    'niger',
    'nigeria',
    'oman',
    'pakistan',
    'panama',
    'papua new guinea',
    'paraguay',
    'peru',
    'philippines',
    'poland',
    'puerto rico',
    'romania',
    'russia',
    'rwanda',
    'samoa',
    'sao tome and principe',
    'saudi arabia',
    'senegal',
    'seychelles',
    'sierra leone',
    'slovakia',
    'slovenia',
    'solomon islands',
    'somalia',
    'south africa',
    'sri lanka',
    'saint lucia',
    'saint vincent and the grenadines',
    'sudan',
    'suriname',
    'syria',
    'tajikistan',
    'tanzania',
    'thailand',
    'togo',
    'tonga',
    'trinidad and tobago',
    'tunisia',
    'turkey',
    'turkmenistan',
    'uganda',
    'ukraine',
    'uruguay',
    'uzbekistan',
    'vanuatu',
    'venezuela',
    'vietnam',
    'yemen',
    'zambia',
    'zimbabwe'
]