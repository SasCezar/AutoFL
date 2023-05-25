# Generated from PythonLexer.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


if "." in __name__:
    from .PythonLexerBase import PythonLexerBase
else:
    from PythonLexerBase import PythonLexerBase

def serializedATN():
    return [
        4,0,100,854,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,
        78,7,78,2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,2,84,7,
        84,2,85,7,85,2,86,7,86,2,87,7,87,2,88,7,88,2,89,7,89,2,90,7,90,2,
        91,7,91,2,92,7,92,2,93,7,93,2,94,7,94,2,95,7,95,2,96,7,96,2,97,7,
        97,2,98,7,98,2,99,7,99,2,100,7,100,2,101,7,101,2,102,7,102,2,103,
        7,103,2,104,7,104,2,105,7,105,2,106,7,106,2,107,7,107,2,108,7,108,
        2,109,7,109,2,110,7,110,2,111,7,111,1,0,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,
        1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,
        12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,
        15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,
        19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,
        22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,25,1,25,1,
        25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,
        27,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,
        29,1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,
        31,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,1,
        34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,
        36,1,36,1,36,1,37,1,37,1,38,1,38,1,38,1,38,1,39,1,39,1,40,1,40,1,
        41,1,41,1,42,1,42,1,43,1,43,1,44,1,44,1,44,1,45,1,45,1,46,1,46,1,
        47,1,47,1,48,1,48,1,49,1,49,1,49,1,50,1,50,1,50,1,51,1,51,1,52,1,
        52,1,53,1,53,1,54,1,54,1,55,1,55,1,55,1,56,1,56,1,57,1,57,1,58,1,
        58,1,59,1,59,1,59,1,60,1,60,1,60,1,61,1,61,1,61,1,62,1,62,1,62,1,
        63,1,63,1,63,1,64,1,64,1,65,1,65,1,65,1,66,1,66,1,66,1,67,1,67,1,
        67,1,68,1,68,1,68,1,69,1,69,1,69,1,70,1,70,1,70,1,71,1,71,1,71,1,
        72,1,72,1,72,1,73,1,73,1,73,1,74,1,74,1,74,1,75,1,75,1,75,1,75,1,
        76,1,76,1,76,1,76,1,77,1,77,1,77,1,77,1,78,1,78,1,78,1,78,1,79,1,
        79,1,79,3,79,543,8,79,1,79,1,79,3,79,547,8,79,3,79,549,8,79,1,79,
        1,79,3,79,553,8,79,1,79,1,79,3,79,557,8,79,1,79,1,79,3,79,561,8,
        79,1,79,1,79,3,79,565,8,79,3,79,567,8,79,1,80,1,80,5,80,571,8,80,
        10,80,12,80,574,9,80,1,80,4,80,577,8,80,11,80,12,80,578,3,80,581,
        8,80,1,81,1,81,1,81,4,81,586,8,81,11,81,12,81,587,1,82,1,82,1,82,
        4,82,593,8,82,11,82,12,82,594,1,83,1,83,1,83,4,83,600,8,83,11,83,
        12,83,601,1,84,1,84,4,84,606,8,84,11,84,12,84,607,3,84,610,8,84,
        1,84,1,84,1,85,1,85,1,86,1,86,1,86,1,87,1,87,1,87,1,88,1,88,1,88,
        1,89,1,89,1,89,1,90,1,90,1,90,1,91,1,91,1,91,1,92,1,92,5,92,636,
        8,92,10,92,12,92,639,9,92,1,93,1,93,5,93,643,8,93,10,93,12,93,646,
        9,93,1,93,1,93,1,93,1,93,1,94,1,94,1,94,1,94,1,94,1,95,4,95,658,
        8,95,11,95,12,95,659,1,95,1,95,1,95,1,95,1,96,1,96,5,96,668,8,96,
        10,96,12,96,671,9,96,1,96,1,96,1,97,1,97,1,97,1,97,3,97,679,8,97,
        1,97,5,97,682,8,97,10,97,12,97,685,9,97,1,97,1,97,1,97,1,97,1,97,
        3,97,692,8,97,1,97,5,97,695,8,97,10,97,12,97,698,9,97,1,97,3,97,
        701,8,97,1,98,1,98,1,98,1,98,1,98,5,98,708,8,98,10,98,12,98,711,
        9,98,1,98,1,98,1,98,1,98,1,98,1,98,1,98,1,98,5,98,721,8,98,10,98,
        12,98,724,9,98,1,98,1,98,1,98,3,98,729,8,98,1,99,1,99,1,99,1,99,
        3,99,735,8,99,3,99,737,8,99,1,100,3,100,740,8,100,1,100,1,100,1,
        101,4,101,745,8,101,11,101,12,101,746,1,101,3,101,750,8,101,1,101,
        1,101,3,101,754,8,101,1,101,4,101,757,8,101,11,101,12,101,758,1,
        101,3,101,762,8,101,1,102,5,102,765,8,102,10,102,12,102,768,9,102,
        1,102,1,102,4,102,772,8,102,11,102,12,102,773,1,102,4,102,777,8,
        102,11,102,12,102,778,1,102,3,102,782,8,102,1,103,1,103,1,103,5,
        103,787,8,103,10,103,12,103,790,9,103,1,103,1,103,1,103,1,103,5,
        103,796,8,103,10,103,12,103,799,9,103,1,103,3,103,802,8,103,1,104,
        1,104,1,104,1,104,1,104,5,104,809,8,104,10,104,12,104,812,9,104,
        1,104,1,104,1,104,1,104,1,104,1,104,1,104,1,104,5,104,822,8,104,
        10,104,12,104,825,9,104,1,104,1,104,1,104,3,104,830,8,104,1,105,
        1,105,3,105,834,8,105,1,106,3,106,837,8,106,1,107,3,107,840,8,107,
        1,108,3,108,843,8,108,1,109,1,109,1,109,1,110,1,110,3,110,850,8,
        110,1,111,3,111,853,8,111,4,709,722,810,823,0,112,1,4,3,5,5,6,7,
        7,9,8,11,9,13,10,15,11,17,12,19,13,21,14,23,15,25,16,27,17,29,18,
        31,19,33,20,35,21,37,22,39,23,41,24,43,25,45,26,47,27,49,28,51,29,
        53,30,55,31,57,32,59,33,61,34,63,35,65,36,67,37,69,38,71,39,73,40,
        75,41,77,42,79,43,81,44,83,45,85,46,87,47,89,48,91,49,93,50,95,51,
        97,52,99,53,101,54,103,55,105,56,107,57,109,58,111,59,113,60,115,
        61,117,62,119,63,121,64,123,65,125,66,127,67,129,68,131,69,133,70,
        135,71,137,72,139,73,141,74,143,75,145,76,147,77,149,78,151,79,153,
        80,155,81,157,82,159,83,161,84,163,85,165,86,167,87,169,88,171,89,
        173,90,175,91,177,92,179,93,181,94,183,95,185,96,187,97,189,98,191,
        99,193,100,195,0,197,0,199,0,201,0,203,0,205,0,207,0,209,0,211,0,
        213,0,215,0,217,0,219,0,221,0,223,0,1,0,25,2,0,85,85,117,117,2,0,
        70,70,102,102,2,0,82,82,114,114,2,0,66,66,98,98,1,0,49,57,1,0,48,
        57,2,0,79,79,111,111,1,0,48,55,2,0,88,88,120,120,3,0,48,57,65,70,
        97,102,1,0,48,49,2,0,74,74,106,106,2,0,9,9,32,32,2,0,10,10,12,13,
        4,0,10,10,13,13,39,39,92,92,4,0,10,10,13,13,34,34,92,92,1,0,92,92,
        2,0,69,69,101,101,2,0,43,43,45,45,5,0,0,9,11,12,14,38,40,91,93,127,
        5,0,0,9,11,12,14,33,35,91,93,127,2,0,0,91,93,127,1,0,0,127,148,0,
        48,57,768,879,1155,1158,1425,1465,1467,1469,1471,1471,1473,1474,
        1476,1477,1479,1479,1552,1557,1611,1630,1632,1641,1648,1648,1750,
        1756,1759,1764,1767,1768,1770,1773,1776,1785,1809,1809,1840,1866,
        1958,1968,2305,2307,2364,2364,2366,2381,2385,2388,2402,2403,2406,
        2415,2433,2435,2492,2492,2494,2500,2503,2504,2507,2509,2519,2519,
        2530,2531,2534,2543,2561,2563,2620,2620,2622,2626,2631,2632,2635,
        2637,2662,2673,2689,2691,2748,2748,2750,2757,2759,2761,2763,2765,
        2786,2787,2790,2799,2817,2819,2876,2876,2878,2883,2887,2888,2891,
        2893,2902,2903,2918,2927,2946,2946,3006,3010,3014,3016,3018,3021,
        3031,3031,3046,3055,3073,3075,3134,3140,3142,3144,3146,3149,3157,
        3158,3174,3183,3202,3203,3260,3260,3262,3268,3270,3272,3274,3277,
        3285,3286,3302,3311,3330,3331,3390,3395,3398,3400,3402,3405,3415,
        3415,3430,3439,3458,3459,3530,3530,3535,3540,3542,3542,3544,3551,
        3570,3571,3633,3633,3636,3642,3655,3662,3664,3673,3761,3761,3764,
        3769,3771,3772,3784,3789,3792,3801,3864,3865,3872,3881,3893,3893,
        3895,3895,3897,3897,3902,3903,3953,3972,3974,3975,3984,3991,3993,
        4028,4038,4038,4140,4146,4150,4153,4160,4169,4182,4185,4959,4959,
        4969,4977,5906,5908,5938,5940,5970,5971,6002,6003,6070,6099,6109,
        6109,6112,6121,6155,6157,6160,6169,6313,6313,6432,6443,6448,6459,
        6470,6479,6576,6592,6600,6601,6608,6617,6679,6683,7616,7619,8255,
        8256,8276,8276,8400,8412,8417,8417,8421,8427,12330,12335,12441,12442,
        43010,43010,43014,43014,43019,43019,43043,43047,64286,64286,65024,
        65039,65056,65059,65075,65076,65101,65103,65296,65305,65343,65343,
        295,0,65,90,95,95,97,122,170,170,181,181,186,186,192,214,216,246,
        248,577,592,705,710,721,736,740,750,750,890,890,902,902,904,906,
        908,908,910,929,931,974,976,1013,1015,1153,1162,1230,1232,1273,1280,
        1295,1329,1366,1369,1369,1377,1415,1488,1514,1520,1522,1569,1594,
        1600,1610,1646,1647,1649,1747,1749,1749,1765,1766,1774,1775,1786,
        1788,1791,1791,1808,1808,1810,1839,1869,1901,1920,1957,1969,1969,
        2308,2361,2365,2365,2384,2384,2392,2401,2429,2429,2437,2444,2447,
        2448,2451,2472,2474,2480,2482,2482,2486,2489,2493,2493,2510,2510,
        2524,2525,2527,2529,2544,2545,2565,2570,2575,2576,2579,2600,2602,
        2608,2610,2611,2613,2614,2616,2617,2649,2652,2654,2654,2674,2676,
        2693,2701,2703,2705,2707,2728,2730,2736,2738,2739,2741,2745,2749,
        2749,2768,2768,2784,2785,2821,2828,2831,2832,2835,2856,2858,2864,
        2866,2867,2869,2873,2877,2877,2908,2909,2911,2913,2929,2929,2947,
        2947,2949,2954,2958,2960,2962,2965,2969,2970,2972,2972,2974,2975,
        2979,2980,2984,2986,2990,3001,3077,3084,3086,3088,3090,3112,3114,
        3123,3125,3129,3168,3169,3205,3212,3214,3216,3218,3240,3242,3251,
        3253,3257,3261,3261,3294,3294,3296,3297,3333,3340,3342,3344,3346,
        3368,3370,3385,3424,3425,3461,3478,3482,3505,3507,3515,3517,3517,
        3520,3526,3585,3632,3634,3635,3648,3654,3713,3714,3716,3716,3719,
        3720,3722,3722,3725,3725,3732,3735,3737,3743,3745,3747,3749,3749,
        3751,3751,3754,3755,3757,3760,3762,3763,3773,3773,3776,3780,3782,
        3782,3804,3805,3840,3840,3904,3911,3913,3946,3976,3979,4096,4129,
        4131,4135,4137,4138,4176,4181,4256,4293,4304,4346,4348,4348,4352,
        4441,4447,4514,4520,4601,4608,4680,4682,4685,4688,4694,4696,4696,
        4698,4701,4704,4744,4746,4749,4752,4784,4786,4789,4792,4798,4800,
        4800,4802,4805,4808,4822,4824,4880,4882,4885,4888,4954,4992,5007,
        5024,5108,5121,5740,5743,5750,5761,5786,5792,5866,5870,5872,5888,
        5900,5902,5905,5920,5937,5952,5969,5984,5996,5998,6000,6016,6067,
        6103,6103,6108,6108,6176,6263,6272,6312,6400,6428,6480,6509,6512,
        6516,6528,6569,6593,6599,6656,6678,7424,7615,7680,7835,7840,7929,
        7936,7957,7960,7965,7968,8005,8008,8013,8016,8023,8025,8025,8027,
        8027,8029,8029,8031,8061,8064,8116,8118,8124,8126,8126,8130,8132,
        8134,8140,8144,8147,8150,8155,8160,8172,8178,8180,8182,8188,8305,
        8305,8319,8319,8336,8340,8450,8450,8455,8455,8458,8467,8469,8469,
        8472,8477,8484,8484,8486,8486,8488,8488,8490,8497,8499,8505,8508,
        8511,8517,8521,8544,8579,11264,11310,11312,11358,11392,11492,11520,
        11557,11568,11621,11631,11631,11648,11670,11680,11686,11688,11694,
        11696,11702,11704,11710,11712,11718,11720,11726,11728,11734,11736,
        11742,12293,12295,12321,12329,12337,12341,12344,12348,12353,12438,
        12443,12447,12449,12538,12540,12543,12549,12588,12593,12686,12704,
        12727,12784,12799,13312,19893,19968,40891,40960,42124,43008,43009,
        43011,43013,43015,43018,43020,43042,44032,55203,63744,64045,64048,
        64106,64112,64217,64256,64262,64275,64279,64285,64285,64287,64296,
        64298,64310,64312,64316,64318,64318,64320,64321,64323,64324,64326,
        64433,64467,64829,64848,64911,64914,64967,65008,65019,65136,65140,
        65142,65276,65313,65338,65345,65370,65382,65470,65474,65479,65482,
        65487,65490,65495,65498,65500,892,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,
        0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,
        0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,
        0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,
        0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,
        0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,
        0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,
        0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,
        0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,
        0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,
        0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,
        1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,
        0,115,1,0,0,0,0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,0,123,1,
        0,0,0,0,125,1,0,0,0,0,127,1,0,0,0,0,129,1,0,0,0,0,131,1,0,0,0,0,
        133,1,0,0,0,0,135,1,0,0,0,0,137,1,0,0,0,0,139,1,0,0,0,0,141,1,0,
        0,0,0,143,1,0,0,0,0,145,1,0,0,0,0,147,1,0,0,0,0,149,1,0,0,0,0,151,
        1,0,0,0,0,153,1,0,0,0,0,155,1,0,0,0,0,157,1,0,0,0,0,159,1,0,0,0,
        0,161,1,0,0,0,0,163,1,0,0,0,0,165,1,0,0,0,0,167,1,0,0,0,0,169,1,
        0,0,0,0,171,1,0,0,0,0,173,1,0,0,0,0,175,1,0,0,0,0,177,1,0,0,0,0,
        179,1,0,0,0,0,181,1,0,0,0,0,183,1,0,0,0,0,185,1,0,0,0,0,187,1,0,
        0,0,0,189,1,0,0,0,0,191,1,0,0,0,0,193,1,0,0,0,1,225,1,0,0,0,3,229,
        1,0,0,0,5,236,1,0,0,0,7,242,1,0,0,0,9,247,1,0,0,0,11,254,1,0,0,0,
        13,263,1,0,0,0,15,266,1,0,0,0,17,273,1,0,0,0,19,280,1,0,0,0,21,283,
        1,0,0,0,23,288,1,0,0,0,25,293,1,0,0,0,27,299,1,0,0,0,29,303,1,0,
        0,0,31,306,1,0,0,0,33,310,1,0,0,0,35,315,1,0,0,0,37,323,1,0,0,0,
        39,328,1,0,0,0,41,335,1,0,0,0,43,342,1,0,0,0,45,345,1,0,0,0,47,349,
        1,0,0,0,49,353,1,0,0,0,51,356,1,0,0,0,53,362,1,0,0,0,55,368,1,0,
        0,0,57,372,1,0,0,0,59,377,1,0,0,0,61,386,1,0,0,0,63,392,1,0,0,0,
        65,398,1,0,0,0,67,404,1,0,0,0,69,410,1,0,0,0,71,415,1,0,0,0,73,420,
        1,0,0,0,75,426,1,0,0,0,77,428,1,0,0,0,79,432,1,0,0,0,81,434,1,0,
        0,0,83,436,1,0,0,0,85,438,1,0,0,0,87,440,1,0,0,0,89,442,1,0,0,0,
        91,445,1,0,0,0,93,447,1,0,0,0,95,449,1,0,0,0,97,451,1,0,0,0,99,453,
        1,0,0,0,101,456,1,0,0,0,103,459,1,0,0,0,105,461,1,0,0,0,107,463,
        1,0,0,0,109,465,1,0,0,0,111,467,1,0,0,0,113,470,1,0,0,0,115,472,
        1,0,0,0,117,474,1,0,0,0,119,476,1,0,0,0,121,479,1,0,0,0,123,482,
        1,0,0,0,125,485,1,0,0,0,127,488,1,0,0,0,129,491,1,0,0,0,131,493,
        1,0,0,0,133,496,1,0,0,0,135,499,1,0,0,0,137,502,1,0,0,0,139,505,
        1,0,0,0,141,508,1,0,0,0,143,511,1,0,0,0,145,514,1,0,0,0,147,517,
        1,0,0,0,149,520,1,0,0,0,151,523,1,0,0,0,153,527,1,0,0,0,155,531,
        1,0,0,0,157,535,1,0,0,0,159,566,1,0,0,0,161,580,1,0,0,0,163,582,
        1,0,0,0,165,589,1,0,0,0,167,596,1,0,0,0,169,609,1,0,0,0,171,613,
        1,0,0,0,173,615,1,0,0,0,175,618,1,0,0,0,177,621,1,0,0,0,179,624,
        1,0,0,0,181,627,1,0,0,0,183,630,1,0,0,0,185,633,1,0,0,0,187,640,
        1,0,0,0,189,651,1,0,0,0,191,657,1,0,0,0,193,665,1,0,0,0,195,700,
        1,0,0,0,197,728,1,0,0,0,199,736,1,0,0,0,201,739,1,0,0,0,203,761,
        1,0,0,0,205,781,1,0,0,0,207,801,1,0,0,0,209,829,1,0,0,0,211,833,
        1,0,0,0,213,836,1,0,0,0,215,839,1,0,0,0,217,842,1,0,0,0,219,844,
        1,0,0,0,221,849,1,0,0,0,223,852,1,0,0,0,225,226,5,100,0,0,226,227,
        5,101,0,0,227,228,5,102,0,0,228,2,1,0,0,0,229,230,5,114,0,0,230,
        231,5,101,0,0,231,232,5,116,0,0,232,233,5,117,0,0,233,234,5,114,
        0,0,234,235,5,110,0,0,235,4,1,0,0,0,236,237,5,114,0,0,237,238,5,
        97,0,0,238,239,5,105,0,0,239,240,5,115,0,0,240,241,5,101,0,0,241,
        6,1,0,0,0,242,243,5,102,0,0,243,244,5,114,0,0,244,245,5,111,0,0,
        245,246,5,109,0,0,246,8,1,0,0,0,247,248,5,105,0,0,248,249,5,109,
        0,0,249,250,5,112,0,0,250,251,5,111,0,0,251,252,5,114,0,0,252,253,
        5,116,0,0,253,10,1,0,0,0,254,255,5,110,0,0,255,256,5,111,0,0,256,
        257,5,110,0,0,257,258,5,108,0,0,258,259,5,111,0,0,259,260,5,99,0,
        0,260,261,5,97,0,0,261,262,5,108,0,0,262,12,1,0,0,0,263,264,5,97,
        0,0,264,265,5,115,0,0,265,14,1,0,0,0,266,267,5,103,0,0,267,268,5,
        108,0,0,268,269,5,111,0,0,269,270,5,98,0,0,270,271,5,97,0,0,271,
        272,5,108,0,0,272,16,1,0,0,0,273,274,5,97,0,0,274,275,5,115,0,0,
        275,276,5,115,0,0,276,277,5,101,0,0,277,278,5,114,0,0,278,279,5,
        116,0,0,279,18,1,0,0,0,280,281,5,105,0,0,281,282,5,102,0,0,282,20,
        1,0,0,0,283,284,5,101,0,0,284,285,5,108,0,0,285,286,5,105,0,0,286,
        287,5,102,0,0,287,22,1,0,0,0,288,289,5,101,0,0,289,290,5,108,0,0,
        290,291,5,115,0,0,291,292,5,101,0,0,292,24,1,0,0,0,293,294,5,119,
        0,0,294,295,5,104,0,0,295,296,5,105,0,0,296,297,5,108,0,0,297,298,
        5,101,0,0,298,26,1,0,0,0,299,300,5,102,0,0,300,301,5,111,0,0,301,
        302,5,114,0,0,302,28,1,0,0,0,303,304,5,105,0,0,304,305,5,110,0,0,
        305,30,1,0,0,0,306,307,5,116,0,0,307,308,5,114,0,0,308,309,5,121,
        0,0,309,32,1,0,0,0,310,311,5,78,0,0,311,312,5,111,0,0,312,313,5,
        110,0,0,313,314,5,101,0,0,314,34,1,0,0,0,315,316,5,102,0,0,316,317,
        5,105,0,0,317,318,5,110,0,0,318,319,5,97,0,0,319,320,5,108,0,0,320,
        321,5,108,0,0,321,322,5,121,0,0,322,36,1,0,0,0,323,324,5,119,0,0,
        324,325,5,105,0,0,325,326,5,116,0,0,326,327,5,104,0,0,327,38,1,0,
        0,0,328,329,5,101,0,0,329,330,5,120,0,0,330,331,5,99,0,0,331,332,
        5,101,0,0,332,333,5,112,0,0,333,334,5,116,0,0,334,40,1,0,0,0,335,
        336,5,108,0,0,336,337,5,97,0,0,337,338,5,109,0,0,338,339,5,98,0,
        0,339,340,5,100,0,0,340,341,5,97,0,0,341,42,1,0,0,0,342,343,5,111,
        0,0,343,344,5,114,0,0,344,44,1,0,0,0,345,346,5,97,0,0,346,347,5,
        110,0,0,347,348,5,100,0,0,348,46,1,0,0,0,349,350,5,110,0,0,350,351,
        5,111,0,0,351,352,5,116,0,0,352,48,1,0,0,0,353,354,5,105,0,0,354,
        355,5,115,0,0,355,50,1,0,0,0,356,357,5,99,0,0,357,358,5,108,0,0,
        358,359,5,97,0,0,359,360,5,115,0,0,360,361,5,115,0,0,361,52,1,0,
        0,0,362,363,5,121,0,0,363,364,5,105,0,0,364,365,5,101,0,0,365,366,
        5,108,0,0,366,367,5,100,0,0,367,54,1,0,0,0,368,369,5,100,0,0,369,
        370,5,101,0,0,370,371,5,108,0,0,371,56,1,0,0,0,372,373,5,112,0,0,
        373,374,5,97,0,0,374,375,5,115,0,0,375,376,5,115,0,0,376,58,1,0,
        0,0,377,378,5,99,0,0,378,379,5,111,0,0,379,380,5,110,0,0,380,381,
        5,116,0,0,381,382,5,105,0,0,382,383,5,110,0,0,383,384,5,117,0,0,
        384,385,5,101,0,0,385,60,1,0,0,0,386,387,5,98,0,0,387,388,5,114,
        0,0,388,389,5,101,0,0,389,390,5,97,0,0,390,391,5,107,0,0,391,62,
        1,0,0,0,392,393,5,97,0,0,393,394,5,115,0,0,394,395,5,121,0,0,395,
        396,5,110,0,0,396,397,5,99,0,0,397,64,1,0,0,0,398,399,5,97,0,0,399,
        400,5,119,0,0,400,401,5,97,0,0,401,402,5,105,0,0,402,403,5,116,0,
        0,403,66,1,0,0,0,404,405,5,112,0,0,405,406,5,114,0,0,406,407,5,105,
        0,0,407,408,5,110,0,0,408,409,5,116,0,0,409,68,1,0,0,0,410,411,5,
        101,0,0,411,412,5,120,0,0,412,413,5,101,0,0,413,414,5,99,0,0,414,
        70,1,0,0,0,415,416,5,84,0,0,416,417,5,114,0,0,417,418,5,117,0,0,
        418,419,5,101,0,0,419,72,1,0,0,0,420,421,5,70,0,0,421,422,5,97,0,
        0,422,423,5,108,0,0,423,424,5,115,0,0,424,425,5,101,0,0,425,74,1,
        0,0,0,426,427,5,46,0,0,427,76,1,0,0,0,428,429,5,46,0,0,429,430,5,
        46,0,0,430,431,5,46,0,0,431,78,1,0,0,0,432,433,5,96,0,0,433,80,1,
        0,0,0,434,435,5,42,0,0,435,82,1,0,0,0,436,437,5,44,0,0,437,84,1,
        0,0,0,438,439,5,58,0,0,439,86,1,0,0,0,440,441,5,59,0,0,441,88,1,
        0,0,0,442,443,5,42,0,0,443,444,5,42,0,0,444,90,1,0,0,0,445,446,5,
        61,0,0,446,92,1,0,0,0,447,448,5,124,0,0,448,94,1,0,0,0,449,450,5,
        94,0,0,450,96,1,0,0,0,451,452,5,38,0,0,452,98,1,0,0,0,453,454,5,
        60,0,0,454,455,5,60,0,0,455,100,1,0,0,0,456,457,5,62,0,0,457,458,
        5,62,0,0,458,102,1,0,0,0,459,460,5,43,0,0,460,104,1,0,0,0,461,462,
        5,45,0,0,462,106,1,0,0,0,463,464,5,47,0,0,464,108,1,0,0,0,465,466,
        5,37,0,0,466,110,1,0,0,0,467,468,5,47,0,0,468,469,5,47,0,0,469,112,
        1,0,0,0,470,471,5,126,0,0,471,114,1,0,0,0,472,473,5,60,0,0,473,116,
        1,0,0,0,474,475,5,62,0,0,475,118,1,0,0,0,476,477,5,61,0,0,477,478,
        5,61,0,0,478,120,1,0,0,0,479,480,5,62,0,0,480,481,5,61,0,0,481,122,
        1,0,0,0,482,483,5,60,0,0,483,484,5,61,0,0,484,124,1,0,0,0,485,486,
        5,60,0,0,486,487,5,62,0,0,487,126,1,0,0,0,488,489,5,33,0,0,489,490,
        5,61,0,0,490,128,1,0,0,0,491,492,5,64,0,0,492,130,1,0,0,0,493,494,
        5,45,0,0,494,495,5,62,0,0,495,132,1,0,0,0,496,497,5,43,0,0,497,498,
        5,61,0,0,498,134,1,0,0,0,499,500,5,45,0,0,500,501,5,61,0,0,501,136,
        1,0,0,0,502,503,5,42,0,0,503,504,5,61,0,0,504,138,1,0,0,0,505,506,
        5,64,0,0,506,507,5,61,0,0,507,140,1,0,0,0,508,509,5,47,0,0,509,510,
        5,61,0,0,510,142,1,0,0,0,511,512,5,37,0,0,512,513,5,61,0,0,513,144,
        1,0,0,0,514,515,5,38,0,0,515,516,5,61,0,0,516,146,1,0,0,0,517,518,
        5,124,0,0,518,519,5,61,0,0,519,148,1,0,0,0,520,521,5,94,0,0,521,
        522,5,61,0,0,522,150,1,0,0,0,523,524,5,60,0,0,524,525,5,60,0,0,525,
        526,5,61,0,0,526,152,1,0,0,0,527,528,5,62,0,0,528,529,5,62,0,0,529,
        530,5,61,0,0,530,154,1,0,0,0,531,532,5,42,0,0,532,533,5,42,0,0,533,
        534,5,61,0,0,534,156,1,0,0,0,535,536,5,47,0,0,536,537,5,47,0,0,537,
        538,5,61,0,0,538,158,1,0,0,0,539,549,7,0,0,0,540,542,7,1,0,0,541,
        543,7,2,0,0,542,541,1,0,0,0,542,543,1,0,0,0,543,549,1,0,0,0,544,
        546,7,2,0,0,545,547,7,1,0,0,546,545,1,0,0,0,546,547,1,0,0,0,547,
        549,1,0,0,0,548,539,1,0,0,0,548,540,1,0,0,0,548,544,1,0,0,0,548,
        549,1,0,0,0,549,552,1,0,0,0,550,553,3,195,97,0,551,553,3,197,98,
        0,552,550,1,0,0,0,552,551,1,0,0,0,553,567,1,0,0,0,554,556,7,3,0,
        0,555,557,7,2,0,0,556,555,1,0,0,0,556,557,1,0,0,0,557,561,1,0,0,
        0,558,559,7,2,0,0,559,561,7,3,0,0,560,554,1,0,0,0,560,558,1,0,0,
        0,561,564,1,0,0,0,562,565,3,207,103,0,563,565,3,209,104,0,564,562,
        1,0,0,0,564,563,1,0,0,0,565,567,1,0,0,0,566,548,1,0,0,0,566,560,
        1,0,0,0,567,160,1,0,0,0,568,572,7,4,0,0,569,571,7,5,0,0,570,569,
        1,0,0,0,571,574,1,0,0,0,572,570,1,0,0,0,572,573,1,0,0,0,573,581,
        1,0,0,0,574,572,1,0,0,0,575,577,5,48,0,0,576,575,1,0,0,0,577,578,
        1,0,0,0,578,576,1,0,0,0,578,579,1,0,0,0,579,581,1,0,0,0,580,568,
        1,0,0,0,580,576,1,0,0,0,581,162,1,0,0,0,582,583,5,48,0,0,583,585,
        7,6,0,0,584,586,7,7,0,0,585,584,1,0,0,0,586,587,1,0,0,0,587,585,
        1,0,0,0,587,588,1,0,0,0,588,164,1,0,0,0,589,590,5,48,0,0,590,592,
        7,8,0,0,591,593,7,9,0,0,592,591,1,0,0,0,593,594,1,0,0,0,594,592,
        1,0,0,0,594,595,1,0,0,0,595,166,1,0,0,0,596,597,5,48,0,0,597,599,
        7,3,0,0,598,600,7,10,0,0,599,598,1,0,0,0,600,601,1,0,0,0,601,599,
        1,0,0,0,601,602,1,0,0,0,602,168,1,0,0,0,603,610,3,203,101,0,604,
        606,7,5,0,0,605,604,1,0,0,0,606,607,1,0,0,0,607,605,1,0,0,0,607,
        608,1,0,0,0,608,610,1,0,0,0,609,603,1,0,0,0,609,605,1,0,0,0,610,
        611,1,0,0,0,611,612,7,11,0,0,612,170,1,0,0,0,613,614,3,203,101,0,
        614,172,1,0,0,0,615,616,5,40,0,0,616,617,6,86,0,0,617,174,1,0,0,
        0,618,619,5,41,0,0,619,620,6,87,1,0,620,176,1,0,0,0,621,622,5,123,
        0,0,622,623,6,88,2,0,623,178,1,0,0,0,624,625,5,125,0,0,625,626,6,
        89,3,0,626,180,1,0,0,0,627,628,5,91,0,0,628,629,6,90,4,0,629,182,
        1,0,0,0,630,631,5,93,0,0,631,632,6,91,5,0,632,184,1,0,0,0,633,637,
        3,223,111,0,634,636,3,221,110,0,635,634,1,0,0,0,636,639,1,0,0,0,
        637,635,1,0,0,0,637,638,1,0,0,0,638,186,1,0,0,0,639,637,1,0,0,0,
        640,644,5,92,0,0,641,643,7,12,0,0,642,641,1,0,0,0,643,646,1,0,0,
        0,644,642,1,0,0,0,644,645,1,0,0,0,645,647,1,0,0,0,646,644,1,0,0,
        0,647,648,3,201,100,0,648,649,1,0,0,0,649,650,6,93,6,0,650,188,1,
        0,0,0,651,652,3,201,100,0,652,653,6,94,7,0,653,654,1,0,0,0,654,655,
        6,94,6,0,655,190,1,0,0,0,656,658,7,12,0,0,657,656,1,0,0,0,658,659,
        1,0,0,0,659,657,1,0,0,0,659,660,1,0,0,0,660,661,1,0,0,0,661,662,
        6,95,8,0,662,663,1,0,0,0,663,664,6,95,6,0,664,192,1,0,0,0,665,669,
        5,35,0,0,666,668,8,13,0,0,667,666,1,0,0,0,668,671,1,0,0,0,669,667,
        1,0,0,0,669,670,1,0,0,0,670,672,1,0,0,0,671,669,1,0,0,0,672,673,
        6,96,6,0,673,194,1,0,0,0,674,683,5,39,0,0,675,678,5,92,0,0,676,679,
        3,201,100,0,677,679,9,0,0,0,678,676,1,0,0,0,678,677,1,0,0,0,679,
        682,1,0,0,0,680,682,8,14,0,0,681,675,1,0,0,0,681,680,1,0,0,0,682,
        685,1,0,0,0,683,681,1,0,0,0,683,684,1,0,0,0,684,686,1,0,0,0,685,
        683,1,0,0,0,686,701,5,39,0,0,687,696,5,34,0,0,688,691,5,92,0,0,689,
        692,3,201,100,0,690,692,9,0,0,0,691,689,1,0,0,0,691,690,1,0,0,0,
        692,695,1,0,0,0,693,695,8,15,0,0,694,688,1,0,0,0,694,693,1,0,0,0,
        695,698,1,0,0,0,696,694,1,0,0,0,696,697,1,0,0,0,697,699,1,0,0,0,
        698,696,1,0,0,0,699,701,5,34,0,0,700,674,1,0,0,0,700,687,1,0,0,0,
        701,196,1,0,0,0,702,703,5,39,0,0,703,704,5,39,0,0,704,705,5,39,0,
        0,705,709,1,0,0,0,706,708,3,199,99,0,707,706,1,0,0,0,708,711,1,0,
        0,0,709,710,1,0,0,0,709,707,1,0,0,0,710,712,1,0,0,0,711,709,1,0,
        0,0,712,713,5,39,0,0,713,714,5,39,0,0,714,729,5,39,0,0,715,716,5,
        34,0,0,716,717,5,34,0,0,717,718,5,34,0,0,718,722,1,0,0,0,719,721,
        3,199,99,0,720,719,1,0,0,0,721,724,1,0,0,0,722,723,1,0,0,0,722,720,
        1,0,0,0,723,725,1,0,0,0,724,722,1,0,0,0,725,726,5,34,0,0,726,727,
        5,34,0,0,727,729,5,34,0,0,728,702,1,0,0,0,728,715,1,0,0,0,729,198,
        1,0,0,0,730,737,8,16,0,0,731,734,5,92,0,0,732,735,3,201,100,0,733,
        735,9,0,0,0,734,732,1,0,0,0,734,733,1,0,0,0,735,737,1,0,0,0,736,
        730,1,0,0,0,736,731,1,0,0,0,737,200,1,0,0,0,738,740,5,13,0,0,739,
        738,1,0,0,0,739,740,1,0,0,0,740,741,1,0,0,0,741,742,5,10,0,0,742,
        202,1,0,0,0,743,745,7,5,0,0,744,743,1,0,0,0,745,746,1,0,0,0,746,
        744,1,0,0,0,746,747,1,0,0,0,747,750,1,0,0,0,748,750,3,205,102,0,
        749,744,1,0,0,0,749,748,1,0,0,0,750,751,1,0,0,0,751,753,7,17,0,0,
        752,754,7,18,0,0,753,752,1,0,0,0,753,754,1,0,0,0,754,756,1,0,0,0,
        755,757,7,5,0,0,756,755,1,0,0,0,757,758,1,0,0,0,758,756,1,0,0,0,
        758,759,1,0,0,0,759,762,1,0,0,0,760,762,3,205,102,0,761,749,1,0,
        0,0,761,760,1,0,0,0,762,204,1,0,0,0,763,765,7,5,0,0,764,763,1,0,
        0,0,765,768,1,0,0,0,766,764,1,0,0,0,766,767,1,0,0,0,767,769,1,0,
        0,0,768,766,1,0,0,0,769,771,5,46,0,0,770,772,7,5,0,0,771,770,1,0,
        0,0,772,773,1,0,0,0,773,771,1,0,0,0,773,774,1,0,0,0,774,782,1,0,
        0,0,775,777,7,5,0,0,776,775,1,0,0,0,777,778,1,0,0,0,778,776,1,0,
        0,0,778,779,1,0,0,0,779,780,1,0,0,0,780,782,5,46,0,0,781,766,1,0,
        0,0,781,776,1,0,0,0,782,206,1,0,0,0,783,788,5,39,0,0,784,787,3,213,
        106,0,785,787,3,219,109,0,786,784,1,0,0,0,786,785,1,0,0,0,787,790,
        1,0,0,0,788,786,1,0,0,0,788,789,1,0,0,0,789,791,1,0,0,0,790,788,
        1,0,0,0,791,802,5,39,0,0,792,797,5,34,0,0,793,796,3,215,107,0,794,
        796,3,219,109,0,795,793,1,0,0,0,795,794,1,0,0,0,796,799,1,0,0,0,
        797,795,1,0,0,0,797,798,1,0,0,0,798,800,1,0,0,0,799,797,1,0,0,0,
        800,802,5,34,0,0,801,783,1,0,0,0,801,792,1,0,0,0,802,208,1,0,0,0,
        803,804,5,39,0,0,804,805,5,39,0,0,805,806,5,39,0,0,806,810,1,0,0,
        0,807,809,3,211,105,0,808,807,1,0,0,0,809,812,1,0,0,0,810,811,1,
        0,0,0,810,808,1,0,0,0,811,813,1,0,0,0,812,810,1,0,0,0,813,814,5,
        39,0,0,814,815,5,39,0,0,815,830,5,39,0,0,816,817,5,34,0,0,817,818,
        5,34,0,0,818,819,5,34,0,0,819,823,1,0,0,0,820,822,3,211,105,0,821,
        820,1,0,0,0,822,825,1,0,0,0,823,824,1,0,0,0,823,821,1,0,0,0,824,
        826,1,0,0,0,825,823,1,0,0,0,826,827,5,34,0,0,827,828,5,34,0,0,828,
        830,5,34,0,0,829,803,1,0,0,0,829,816,1,0,0,0,830,210,1,0,0,0,831,
        834,3,217,108,0,832,834,3,219,109,0,833,831,1,0,0,0,833,832,1,0,
        0,0,834,212,1,0,0,0,835,837,7,19,0,0,836,835,1,0,0,0,837,214,1,0,
        0,0,838,840,7,20,0,0,839,838,1,0,0,0,840,216,1,0,0,0,841,843,7,21,
        0,0,842,841,1,0,0,0,843,218,1,0,0,0,844,845,5,92,0,0,845,846,7,22,
        0,0,846,220,1,0,0,0,847,850,3,223,111,0,848,850,7,23,0,0,849,847,
        1,0,0,0,849,848,1,0,0,0,850,222,1,0,0,0,851,853,7,24,0,0,852,851,
        1,0,0,0,853,224,1,0,0,0,57,0,542,546,548,552,556,560,564,566,572,
        578,580,587,594,601,607,609,637,644,659,669,678,681,683,691,694,
        696,700,709,722,728,734,736,739,746,749,753,758,761,766,773,778,
        781,786,788,795,797,801,810,823,829,833,836,839,842,849,852,9,1,
        86,0,1,87,1,1,88,2,1,89,3,1,90,4,1,91,5,0,1,0,1,94,6,1,95,7
    ]

class PythonLexer(PythonLexerBase):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INDENT = 1
    DEDENT = 2
    LINE_BREAK = 3
    DEF = 4
    RETURN = 5
    RAISE = 6
    FROM = 7
    IMPORT = 8
    NONLOCAL = 9
    AS = 10
    GLOBAL = 11
    ASSERT = 12
    IF = 13
    ELIF = 14
    ELSE = 15
    WHILE = 16
    FOR = 17
    IN = 18
    TRY = 19
    NONE = 20
    FINALLY = 21
    WITH = 22
    EXCEPT = 23
    LAMBDA = 24
    OR = 25
    AND = 26
    NOT = 27
    IS = 28
    CLASS = 29
    YIELD = 30
    DEL = 31
    PASS = 32
    CONTINUE = 33
    BREAK = 34
    ASYNC = 35
    AWAIT = 36
    PRINT = 37
    EXEC = 38
    TRUE = 39
    FALSE = 40
    DOT = 41
    ELLIPSIS = 42
    REVERSE_QUOTE = 43
    STAR = 44
    COMMA = 45
    COLON = 46
    SEMI_COLON = 47
    POWER = 48
    ASSIGN = 49
    OR_OP = 50
    XOR = 51
    AND_OP = 52
    LEFT_SHIFT = 53
    RIGHT_SHIFT = 54
    ADD = 55
    MINUS = 56
    DIV = 57
    MOD = 58
    IDIV = 59
    NOT_OP = 60
    LESS_THAN = 61
    GREATER_THAN = 62
    EQUALS = 63
    GT_EQ = 64
    LT_EQ = 65
    NOT_EQ_1 = 66
    NOT_EQ_2 = 67
    AT = 68
    ARROW = 69
    ADD_ASSIGN = 70
    SUB_ASSIGN = 71
    MULT_ASSIGN = 72
    AT_ASSIGN = 73
    DIV_ASSIGN = 74
    MOD_ASSIGN = 75
    AND_ASSIGN = 76
    OR_ASSIGN = 77
    XOR_ASSIGN = 78
    LEFT_SHIFT_ASSIGN = 79
    RIGHT_SHIFT_ASSIGN = 80
    POWER_ASSIGN = 81
    IDIV_ASSIGN = 82
    STRING = 83
    DECIMAL_INTEGER = 84
    OCT_INTEGER = 85
    HEX_INTEGER = 86
    BIN_INTEGER = 87
    IMAG_NUMBER = 88
    FLOAT_NUMBER = 89
    OPEN_PAREN = 90
    CLOSE_PAREN = 91
    OPEN_BRACE = 92
    CLOSE_BRACE = 93
    OPEN_BRACKET = 94
    CLOSE_BRACKET = 95
    NAME = 96
    LINE_JOIN = 97
    NEWLINE = 98
    WS = 99
    COMMENT = 100

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'def'", "'return'", "'raise'", "'from'", "'import'", "'nonlocal'", 
            "'as'", "'global'", "'assert'", "'if'", "'elif'", "'else'", 
            "'while'", "'for'", "'in'", "'try'", "'None'", "'finally'", 
            "'with'", "'except'", "'lambda'", "'or'", "'and'", "'not'", 
            "'is'", "'class'", "'yield'", "'del'", "'pass'", "'continue'", 
            "'break'", "'async'", "'await'", "'print'", "'exec'", "'True'", 
            "'False'", "'.'", "'...'", "'`'", "'*'", "','", "':'", "';'", 
            "'**'", "'='", "'|'", "'^'", "'&'", "'<<'", "'>>'", "'+'", "'-'", 
            "'/'", "'%'", "'//'", "'~'", "'<'", "'>'", "'=='", "'>='", "'<='", 
            "'<>'", "'!='", "'@'", "'->'", "'+='", "'-='", "'*='", "'@='", 
            "'/='", "'%='", "'&='", "'|='", "'^='", "'<<='", "'>>='", "'**='", 
            "'//='", "'('", "')'", "'{'", "'}'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "LINE_BREAK", "DEF", "RETURN", "RAISE", 
            "FROM", "IMPORT", "NONLOCAL", "AS", "GLOBAL", "ASSERT", "IF", 
            "ELIF", "ELSE", "WHILE", "FOR", "IN", "TRY", "NONE", "FINALLY", 
            "WITH", "EXCEPT", "LAMBDA", "OR", "AND", "NOT", "IS", "CLASS", 
            "YIELD", "DEL", "PASS", "CONTINUE", "BREAK", "ASYNC", "AWAIT", 
            "PRINT", "EXEC", "TRUE", "FALSE", "DOT", "ELLIPSIS", "REVERSE_QUOTE", 
            "STAR", "COMMA", "COLON", "SEMI_COLON", "POWER", "ASSIGN", "OR_OP", 
            "XOR", "AND_OP", "LEFT_SHIFT", "RIGHT_SHIFT", "ADD", "MINUS", 
            "DIV", "MOD", "IDIV", "NOT_OP", "LESS_THAN", "GREATER_THAN", 
            "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ_1", "NOT_EQ_2", "AT", "ARROW", 
            "ADD_ASSIGN", "SUB_ASSIGN", "MULT_ASSIGN", "AT_ASSIGN", "DIV_ASSIGN", 
            "MOD_ASSIGN", "AND_ASSIGN", "OR_ASSIGN", "XOR_ASSIGN", "LEFT_SHIFT_ASSIGN", 
            "RIGHT_SHIFT_ASSIGN", "POWER_ASSIGN", "IDIV_ASSIGN", "STRING", 
            "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", 
            "IMAG_NUMBER", "FLOAT_NUMBER", "OPEN_PAREN", "CLOSE_PAREN", 
            "OPEN_BRACE", "CLOSE_BRACE", "OPEN_BRACKET", "CLOSE_BRACKET", 
            "NAME", "LINE_JOIN", "NEWLINE", "WS", "COMMENT" ]

    ruleNames = [ "DEF", "RETURN", "RAISE", "FROM", "IMPORT", "NONLOCAL", 
                  "AS", "GLOBAL", "ASSERT", "IF", "ELIF", "ELSE", "WHILE", 
                  "FOR", "IN", "TRY", "NONE", "FINALLY", "WITH", "EXCEPT", 
                  "LAMBDA", "OR", "AND", "NOT", "IS", "CLASS", "YIELD", 
                  "DEL", "PASS", "CONTINUE", "BREAK", "ASYNC", "AWAIT", 
                  "PRINT", "EXEC", "TRUE", "FALSE", "DOT", "ELLIPSIS", "REVERSE_QUOTE", 
                  "STAR", "COMMA", "COLON", "SEMI_COLON", "POWER", "ASSIGN", 
                  "OR_OP", "XOR", "AND_OP", "LEFT_SHIFT", "RIGHT_SHIFT", 
                  "ADD", "MINUS", "DIV", "MOD", "IDIV", "NOT_OP", "LESS_THAN", 
                  "GREATER_THAN", "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ_1", 
                  "NOT_EQ_2", "AT", "ARROW", "ADD_ASSIGN", "SUB_ASSIGN", 
                  "MULT_ASSIGN", "AT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                  "AND_ASSIGN", "OR_ASSIGN", "XOR_ASSIGN", "LEFT_SHIFT_ASSIGN", 
                  "RIGHT_SHIFT_ASSIGN", "POWER_ASSIGN", "IDIV_ASSIGN", "STRING", 
                  "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", 
                  "IMAG_NUMBER", "FLOAT_NUMBER", "OPEN_PAREN", "CLOSE_PAREN", 
                  "OPEN_BRACE", "CLOSE_BRACE", "OPEN_BRACKET", "CLOSE_BRACKET", 
                  "NAME", "LINE_JOIN", "NEWLINE", "WS", "COMMENT", "SHORT_STRING", 
                  "LONG_STRING", "LONG_STRING_ITEM", "RN", "EXPONENT_OR_POINT_FLOAT", 
                  "POINT_FLOAT", "SHORT_BYTES", "LONG_BYTES", "LONG_BYTES_ITEM", 
                  "SHORT_BYTES_CHAR_NO_SINGLE_QUOTE", "SHORT_BYTES_CHAR_NO_DOUBLE_QUOTE", 
                  "LONG_BYTES_CHAR", "BYTES_ESCAPE_SEQ", "ID_CONTINUE", 
                  "ID_START" ]

    grammarFileName = "PythonLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[86] = self.OPEN_PAREN_action 
            actions[87] = self.CLOSE_PAREN_action 
            actions[88] = self.OPEN_BRACE_action 
            actions[89] = self.CLOSE_BRACE_action 
            actions[90] = self.OPEN_BRACKET_action 
            actions[91] = self.CLOSE_BRACKET_action 
            actions[94] = self.NEWLINE_action 
            actions[95] = self.WS_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def OPEN_PAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.IncIndentLevel();
     

    def CLOSE_PAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.DecIndentLevel();
     

    def OPEN_BRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.IncIndentLevel();
     

    def CLOSE_BRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.DecIndentLevel();
     

    def OPEN_BRACKET_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.IncIndentLevel();
     

    def CLOSE_BRACKET_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            self.DecIndentLevel();
     

    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            self.HandleNewLine();
     

    def WS_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            self.HandleSpaces();
     


