# Generated from D:/Bai tap/HL231/PPL/assignment3-initial/src/main/CSlang/parser/CSlang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,62,529,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,2,62,7,62,1,0,4,0,128,8,0,11,0,12,0,129,
        1,0,1,0,1,1,1,1,1,1,1,1,3,1,138,8,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,
        1,2,1,2,1,2,1,3,5,3,151,8,3,10,3,12,3,154,9,3,1,4,1,4,1,4,3,4,159,
        8,4,1,5,1,5,3,5,163,8,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,
        3,8,175,8,8,1,8,1,8,1,8,4,8,180,8,8,11,8,12,8,181,1,8,1,8,3,8,186,
        8,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,11,1,11,1,12,
        1,12,3,12,203,8,12,1,13,1,13,1,13,1,13,1,13,3,13,210,8,13,1,14,1,
        14,1,14,1,14,3,14,216,8,14,1,15,1,15,1,15,1,15,1,16,1,16,1,17,1,
        17,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,21,1,21,3,21,236,8,
        21,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,5,23,249,
        8,23,10,23,12,23,252,9,23,1,24,1,24,1,24,1,24,1,24,1,24,5,24,260,
        8,24,10,24,12,24,263,9,24,1,25,1,25,1,25,1,25,1,25,1,25,5,25,271,
        8,25,10,25,12,25,274,9,25,1,26,1,26,1,26,1,26,1,26,1,26,5,26,282,
        8,26,10,26,12,26,285,9,26,1,27,1,27,1,27,1,27,1,27,1,27,5,27,293,
        8,27,10,27,12,27,296,9,27,1,28,1,28,1,28,3,28,301,8,28,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,5,29,311,8,29,10,29,12,29,314,9,29,
        1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,323,8,30,5,30,325,8,30,10,
        30,12,30,328,9,30,1,31,1,31,1,31,3,31,333,8,31,1,31,1,31,3,31,337,
        8,31,1,31,3,31,340,8,31,1,32,1,32,3,32,344,8,32,1,33,1,33,1,33,1,
        33,1,33,3,33,351,8,33,1,34,1,34,1,34,1,34,1,35,3,35,358,8,35,1,35,
        1,35,5,35,362,8,35,10,35,12,35,365,9,35,1,36,1,36,1,36,5,36,370,
        8,36,10,36,12,36,373,9,36,1,37,1,37,1,37,1,37,1,38,1,38,1,38,1,38,
        1,38,1,39,1,39,1,39,1,39,1,40,1,40,1,40,3,40,391,8,40,1,40,1,40,
        1,41,1,41,1,41,1,41,1,41,1,42,1,42,1,42,3,42,403,8,42,1,42,1,42,
        1,42,1,43,1,43,1,43,1,43,1,44,1,44,1,44,5,44,415,8,44,10,44,12,44,
        418,9,44,1,45,1,45,1,45,5,45,423,8,45,10,45,12,45,426,9,45,1,46,
        1,46,1,46,3,46,431,8,46,1,46,1,46,1,47,1,47,1,47,3,47,438,8,47,1,
        47,1,47,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,
        48,3,48,454,8,48,1,49,1,49,1,49,1,49,1,50,1,50,1,50,1,50,1,51,1,
        51,1,51,1,52,1,52,3,52,469,8,52,1,52,1,52,1,52,1,52,3,52,475,8,52,
        1,53,1,53,1,54,1,54,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,56,
        1,56,1,56,1,57,1,57,1,57,1,58,1,58,3,58,497,8,58,1,58,1,58,1,59,
        1,59,3,59,503,8,59,1,59,1,59,1,60,1,60,1,60,1,60,1,61,5,61,512,8,
        61,10,61,12,61,515,9,61,1,62,1,62,1,62,1,62,1,62,1,62,1,62,1,62,
        1,62,1,62,3,62,527,8,62,1,62,0,7,46,48,50,52,54,58,60,63,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,
        52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,
        96,98,100,102,104,106,108,110,112,114,116,118,120,122,124,0,7,1,
        0,7,8,1,0,9,12,2,0,32,33,35,38,1,0,30,31,1,0,23,24,1,0,25,28,2,0,
        24,24,29,29,526,0,127,1,0,0,0,2,133,1,0,0,0,4,144,1,0,0,0,6,152,
        1,0,0,0,8,158,1,0,0,0,10,162,1,0,0,0,12,164,1,0,0,0,14,168,1,0,0,
        0,16,172,1,0,0,0,18,189,1,0,0,0,20,196,1,0,0,0,22,198,1,0,0,0,24,
        202,1,0,0,0,26,209,1,0,0,0,28,215,1,0,0,0,30,217,1,0,0,0,32,221,
        1,0,0,0,34,223,1,0,0,0,36,225,1,0,0,0,38,227,1,0,0,0,40,229,1,0,
        0,0,42,235,1,0,0,0,44,237,1,0,0,0,46,242,1,0,0,0,48,253,1,0,0,0,
        50,264,1,0,0,0,52,275,1,0,0,0,54,286,1,0,0,0,56,300,1,0,0,0,58,302,
        1,0,0,0,60,315,1,0,0,0,62,339,1,0,0,0,64,343,1,0,0,0,66,350,1,0,
        0,0,68,352,1,0,0,0,70,357,1,0,0,0,72,366,1,0,0,0,74,374,1,0,0,0,
        76,378,1,0,0,0,78,383,1,0,0,0,80,390,1,0,0,0,82,394,1,0,0,0,84,402,
        1,0,0,0,86,407,1,0,0,0,88,411,1,0,0,0,90,419,1,0,0,0,92,427,1,0,
        0,0,94,434,1,0,0,0,96,453,1,0,0,0,98,455,1,0,0,0,100,459,1,0,0,0,
        102,463,1,0,0,0,104,466,1,0,0,0,106,476,1,0,0,0,108,478,1,0,0,0,
        110,480,1,0,0,0,112,488,1,0,0,0,114,491,1,0,0,0,116,494,1,0,0,0,
        118,502,1,0,0,0,120,506,1,0,0,0,122,513,1,0,0,0,124,526,1,0,0,0,
        126,128,3,2,1,0,127,126,1,0,0,0,128,129,1,0,0,0,129,127,1,0,0,0,
        129,130,1,0,0,0,130,131,1,0,0,0,131,132,5,0,0,1,132,1,1,0,0,0,133,
        137,5,15,0,0,134,135,3,20,10,0,135,136,5,41,0,0,136,138,1,0,0,0,
        137,134,1,0,0,0,137,138,1,0,0,0,138,139,1,0,0,0,139,140,3,20,10,
        0,140,141,5,46,0,0,141,142,3,6,3,0,142,143,5,47,0,0,143,3,1,0,0,
        0,144,145,5,1,0,0,145,146,5,20,0,0,146,147,3,16,8,0,147,148,3,120,
        60,0,148,5,1,0,0,0,149,151,3,8,4,0,150,149,1,0,0,0,151,154,1,0,0,
        0,152,150,1,0,0,0,152,153,1,0,0,0,153,7,1,0,0,0,154,152,1,0,0,0,
        155,159,3,10,5,0,156,159,3,18,9,0,157,159,3,4,2,0,158,155,1,0,0,
        0,158,156,1,0,0,0,158,157,1,0,0,0,159,9,1,0,0,0,160,163,3,92,46,
        0,161,163,3,94,47,0,162,160,1,0,0,0,162,161,1,0,0,0,163,11,1,0,0,
        0,164,165,3,20,10,0,165,166,5,51,0,0,166,167,3,42,21,0,167,13,1,
        0,0,0,168,169,3,88,44,0,169,170,5,51,0,0,170,171,3,42,21,0,171,15,
        1,0,0,0,172,185,5,44,0,0,173,175,3,14,7,0,174,173,1,0,0,0,174,175,
        1,0,0,0,175,186,1,0,0,0,176,177,3,14,7,0,177,178,5,42,0,0,178,180,
        1,0,0,0,179,176,1,0,0,0,180,181,1,0,0,0,181,179,1,0,0,0,181,182,
        1,0,0,0,182,183,1,0,0,0,183,184,3,12,6,0,184,186,1,0,0,0,185,174,
        1,0,0,0,185,179,1,0,0,0,186,187,1,0,0,0,187,188,5,45,0,0,188,17,
        1,0,0,0,189,190,5,1,0,0,190,191,3,24,12,0,191,192,3,16,8,0,192,193,
        5,51,0,0,193,194,3,42,21,0,194,195,3,120,60,0,195,19,1,0,0,0,196,
        197,5,55,0,0,197,21,1,0,0,0,198,199,5,56,0,0,199,23,1,0,0,0,200,
        203,3,20,10,0,201,203,3,22,11,0,202,200,1,0,0,0,202,201,1,0,0,0,
        203,25,1,0,0,0,204,210,5,57,0,0,205,210,5,58,0,0,206,210,3,36,18,
        0,207,210,5,62,0,0,208,210,3,30,15,0,209,204,1,0,0,0,209,205,1,0,
        0,0,209,206,1,0,0,0,209,207,1,0,0,0,209,208,1,0,0,0,210,27,1,0,0,
        0,211,216,3,24,12,0,212,216,3,80,40,0,213,216,3,78,39,0,214,216,
        3,76,38,0,215,211,1,0,0,0,215,212,1,0,0,0,215,213,1,0,0,0,215,214,
        1,0,0,0,216,29,1,0,0,0,217,218,5,48,0,0,218,219,3,70,35,0,219,220,
        5,49,0,0,220,31,1,0,0,0,221,222,5,14,0,0,222,33,1,0,0,0,223,224,
        5,16,0,0,224,35,1,0,0,0,225,226,7,0,0,0,226,37,1,0,0,0,227,228,7,
        1,0,0,228,39,1,0,0,0,229,230,3,20,10,0,230,41,1,0,0,0,231,236,3,
        38,19,0,232,236,3,44,22,0,233,236,3,40,20,0,234,236,5,19,0,0,235,
        231,1,0,0,0,235,232,1,0,0,0,235,233,1,0,0,0,235,234,1,0,0,0,236,
        43,1,0,0,0,237,238,5,48,0,0,238,239,5,57,0,0,239,240,5,49,0,0,240,
        241,3,38,19,0,241,45,1,0,0,0,242,243,6,23,-1,0,243,244,3,48,24,0,
        244,250,1,0,0,0,245,246,10,2,0,0,246,247,5,40,0,0,247,249,3,46,23,
        3,248,245,1,0,0,0,249,252,1,0,0,0,250,248,1,0,0,0,250,251,1,0,0,
        0,251,47,1,0,0,0,252,250,1,0,0,0,253,254,6,24,-1,0,254,255,3,50,
        25,0,255,261,1,0,0,0,256,257,10,2,0,0,257,258,7,2,0,0,258,260,3,
        48,24,3,259,256,1,0,0,0,260,263,1,0,0,0,261,259,1,0,0,0,261,262,
        1,0,0,0,262,49,1,0,0,0,263,261,1,0,0,0,264,265,6,25,-1,0,265,266,
        3,52,26,0,266,272,1,0,0,0,267,268,10,2,0,0,268,269,7,3,0,0,269,271,
        3,52,26,0,270,267,1,0,0,0,271,274,1,0,0,0,272,270,1,0,0,0,272,273,
        1,0,0,0,273,51,1,0,0,0,274,272,1,0,0,0,275,276,6,26,-1,0,276,277,
        3,54,27,0,277,283,1,0,0,0,278,279,10,2,0,0,279,280,7,4,0,0,280,282,
        3,54,27,0,281,278,1,0,0,0,282,285,1,0,0,0,283,281,1,0,0,0,283,284,
        1,0,0,0,284,53,1,0,0,0,285,283,1,0,0,0,286,287,6,27,-1,0,287,288,
        3,56,28,0,288,294,1,0,0,0,289,290,10,2,0,0,290,291,7,5,0,0,291,293,
        3,56,28,0,292,289,1,0,0,0,293,296,1,0,0,0,294,292,1,0,0,0,294,295,
        1,0,0,0,295,55,1,0,0,0,296,294,1,0,0,0,297,298,7,6,0,0,298,301,3,
        56,28,0,299,301,3,58,29,0,300,297,1,0,0,0,300,299,1,0,0,0,301,57,
        1,0,0,0,302,303,6,29,-1,0,303,304,3,60,30,0,304,312,1,0,0,0,305,
        306,10,2,0,0,306,307,5,48,0,0,307,308,3,46,23,0,308,309,5,49,0,0,
        309,311,1,0,0,0,310,305,1,0,0,0,311,314,1,0,0,0,312,310,1,0,0,0,
        312,313,1,0,0,0,313,59,1,0,0,0,314,312,1,0,0,0,315,316,6,30,-1,0,
        316,317,3,62,31,0,317,326,1,0,0,0,318,319,10,2,0,0,319,320,5,43,
        0,0,320,322,3,20,10,0,321,323,3,74,37,0,322,321,1,0,0,0,322,323,
        1,0,0,0,323,325,1,0,0,0,324,318,1,0,0,0,325,328,1,0,0,0,326,324,
        1,0,0,0,326,327,1,0,0,0,327,61,1,0,0,0,328,326,1,0,0,0,329,330,3,
        64,32,0,330,331,5,43,0,0,331,333,1,0,0,0,332,329,1,0,0,0,332,333,
        1,0,0,0,333,334,1,0,0,0,334,336,3,22,11,0,335,337,3,74,37,0,336,
        335,1,0,0,0,336,337,1,0,0,0,337,340,1,0,0,0,338,340,3,64,32,0,339,
        332,1,0,0,0,339,338,1,0,0,0,340,63,1,0,0,0,341,344,3,86,43,0,342,
        344,3,66,33,0,343,341,1,0,0,0,343,342,1,0,0,0,344,65,1,0,0,0,345,
        351,3,24,12,0,346,351,3,32,16,0,347,351,3,34,17,0,348,351,3,26,13,
        0,349,351,3,68,34,0,350,345,1,0,0,0,350,346,1,0,0,0,350,347,1,0,
        0,0,350,348,1,0,0,0,350,349,1,0,0,0,351,67,1,0,0,0,352,353,5,44,
        0,0,353,354,3,46,23,0,354,355,5,45,0,0,355,69,1,0,0,0,356,358,3,
        46,23,0,357,356,1,0,0,0,357,358,1,0,0,0,358,363,1,0,0,0,359,360,
        5,42,0,0,360,362,3,46,23,0,361,359,1,0,0,0,362,365,1,0,0,0,363,361,
        1,0,0,0,363,364,1,0,0,0,364,71,1,0,0,0,365,363,1,0,0,0,366,371,3,
        46,23,0,367,368,5,42,0,0,368,370,3,46,23,0,369,367,1,0,0,0,370,373,
        1,0,0,0,371,369,1,0,0,0,371,372,1,0,0,0,372,73,1,0,0,0,373,371,1,
        0,0,0,374,375,5,44,0,0,375,376,3,70,35,0,376,377,5,45,0,0,377,75,
        1,0,0,0,378,379,3,58,29,0,379,380,5,48,0,0,380,381,3,46,23,0,381,
        382,5,49,0,0,382,77,1,0,0,0,383,384,3,58,29,0,384,385,5,43,0,0,385,
        386,3,20,10,0,386,79,1,0,0,0,387,388,3,58,29,0,388,389,5,43,0,0,
        389,391,1,0,0,0,390,387,1,0,0,0,390,391,1,0,0,0,391,392,1,0,0,0,
        392,393,3,22,11,0,393,81,1,0,0,0,394,395,3,58,29,0,395,396,5,43,
        0,0,396,397,3,20,10,0,397,398,3,74,37,0,398,83,1,0,0,0,399,400,3,
        58,29,0,400,401,5,43,0,0,401,403,1,0,0,0,402,399,1,0,0,0,402,403,
        1,0,0,0,403,404,1,0,0,0,404,405,3,22,11,0,405,406,3,74,37,0,406,
        85,1,0,0,0,407,408,5,22,0,0,408,409,3,20,10,0,409,410,3,74,37,0,
        410,87,1,0,0,0,411,416,3,20,10,0,412,413,5,42,0,0,413,415,3,20,10,
        0,414,412,1,0,0,0,415,418,1,0,0,0,416,414,1,0,0,0,416,417,1,0,0,
        0,417,89,1,0,0,0,418,416,1,0,0,0,419,424,3,24,12,0,420,421,5,42,
        0,0,421,423,3,24,12,0,422,420,1,0,0,0,423,426,1,0,0,0,424,422,1,
        0,0,0,424,425,1,0,0,0,425,91,1,0,0,0,426,424,1,0,0,0,427,430,5,17,
        0,0,428,431,3,98,49,0,429,431,3,96,48,0,430,428,1,0,0,0,430,429,
        1,0,0,0,431,432,1,0,0,0,432,433,5,50,0,0,433,93,1,0,0,0,434,437,
        5,18,0,0,435,438,3,98,49,0,436,438,3,96,48,0,437,435,1,0,0,0,437,
        436,1,0,0,0,438,439,1,0,0,0,439,440,5,50,0,0,440,95,1,0,0,0,441,
        442,3,24,12,0,442,443,5,51,0,0,443,444,3,42,21,0,444,445,5,34,0,
        0,445,446,3,46,23,0,446,454,1,0,0,0,447,448,3,24,12,0,448,449,5,
        42,0,0,449,450,3,96,48,0,450,451,5,42,0,0,451,452,3,46,23,0,452,
        454,1,0,0,0,453,441,1,0,0,0,453,447,1,0,0,0,454,97,1,0,0,0,455,456,
        3,90,45,0,456,457,5,51,0,0,457,458,3,42,21,0,458,99,1,0,0,0,459,
        460,3,28,14,0,460,461,5,39,0,0,461,462,3,46,23,0,462,101,1,0,0,0,
        463,464,3,100,50,0,464,465,5,50,0,0,465,103,1,0,0,0,466,468,5,4,
        0,0,467,469,3,106,53,0,468,467,1,0,0,0,468,469,1,0,0,0,469,470,1,
        0,0,0,470,471,3,46,23,0,471,474,3,120,60,0,472,473,5,5,0,0,473,475,
        3,108,54,0,474,472,1,0,0,0,474,475,1,0,0,0,475,105,1,0,0,0,476,477,
        3,120,60,0,477,107,1,0,0,0,478,479,3,120,60,0,479,109,1,0,0,0,480,
        481,5,6,0,0,481,482,3,100,50,0,482,483,5,50,0,0,483,484,3,46,23,
        0,484,485,5,50,0,0,485,486,3,100,50,0,486,487,3,120,60,0,487,111,
        1,0,0,0,488,489,5,2,0,0,489,490,5,50,0,0,490,113,1,0,0,0,491,492,
        5,3,0,0,492,493,5,50,0,0,493,115,1,0,0,0,494,496,5,13,0,0,495,497,
        3,46,23,0,496,495,1,0,0,0,496,497,1,0,0,0,497,498,1,0,0,0,498,499,
        5,50,0,0,499,117,1,0,0,0,500,503,3,84,42,0,501,503,3,82,41,0,502,
        500,1,0,0,0,502,501,1,0,0,0,503,504,1,0,0,0,504,505,5,50,0,0,505,
        119,1,0,0,0,506,507,5,46,0,0,507,508,3,122,61,0,508,509,5,47,0,0,
        509,121,1,0,0,0,510,512,3,124,62,0,511,510,1,0,0,0,512,515,1,0,0,
        0,513,511,1,0,0,0,513,514,1,0,0,0,514,123,1,0,0,0,515,513,1,0,0,
        0,516,527,3,92,46,0,517,527,3,94,47,0,518,527,3,102,51,0,519,527,
        3,104,52,0,520,527,3,110,55,0,521,527,3,112,56,0,522,527,3,114,57,
        0,523,527,3,116,58,0,524,527,3,118,59,0,525,527,3,120,60,0,526,516,
        1,0,0,0,526,517,1,0,0,0,526,518,1,0,0,0,526,519,1,0,0,0,526,520,
        1,0,0,0,526,521,1,0,0,0,526,522,1,0,0,0,526,523,1,0,0,0,526,524,
        1,0,0,0,526,525,1,0,0,0,527,125,1,0,0,0,42,129,137,152,158,162,174,
        181,185,202,209,215,235,250,261,272,283,294,300,312,322,326,332,
        336,339,343,350,357,363,371,390,402,416,424,430,437,453,468,474,
        496,502,513,526
    ]

class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'func'", "'break'", "'continue'", "'if'", 
                     "'else'", "'for'", "'true'", "'false'", "'bool'", "'int'", 
                     "'float'", "'string'", "'return'", "'null'", "'class'", 
                     "'self'", "'var'", "'const'", "'void'", "'constructor'", 
                     "'super'", "'new'", "'+'", "'-'", "'*'", "'/'", "'\\'", 
                     "'%'", "'!'", "'&&'", "'||'", "'!='", "'=='", "'='", 
                     "'<'", "'<='", "'>'", "'>='", "':='", "'^'", "'<-'", 
                     "','", "'.'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "BREAK", "CONTINUE", "IF", 
                      "ELSE", "FOR", "TRUE", "FALSE", "BOOLEAN", "INT", 
                      "FLOAT", "STRING", "RETURN", "NULL", "CLASS", "SELF", 
                      "VAR", "CONST", "VOID", "CONSTRUCTOR", "SUPER", "NEW", 
                      "ADD", "SUB", "MUL", "DIV", "DSLASH", "PERCENT", "NOT", 
                      "AND", "OR", "NOT_EQUALOP", "EQUALOP", "EQUAL", "LESS_THAN", 
                      "LESS_OR_EQUAL_THAN", "GREATER_THAN", "GREATER_OR_EQUAL_THAN", 
                      "ASSIGNMENT_OP", "STRING_CONCAT", "EXTEND", "CM", 
                      "DOT", "LB", "RB", "LP", "RP", "LS", "RS", "SEMI", 
                      "COLON", "WS", "COMMENT_BLOCK", "COMMENT_LINE", "ID", 
                      "STATIC_ID", "INTLIT", "FLOATLIT", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "STRINGLIT" ]

    RULE_program = 0
    RULE_classDecl = 1
    RULE_constructorDecl = 2
    RULE_classStmtsNullable = 3
    RULE_classStmt = 4
    RULE_attributeStmt = 5
    RULE_singleDeclParam = 6
    RULE_declParams = 7
    RULE_listDeclParams = 8
    RULE_methodDecl = 9
    RULE_idLit = 10
    RULE_staticId = 11
    RULE_mixedId = 12
    RULE_literal = 13
    RULE_variableLit = 14
    RULE_indexedArrayLit = 15
    RULE_nullLit = 16
    RULE_selfLit = 17
    RULE_booleanLit = 18
    RULE_primitiveType = 19
    RULE_classType = 20
    RULE_varType = 21
    RULE_arrayType = 22
    RULE_exp = 23
    RULE_exp1 = 24
    RULE_exp2 = 25
    RULE_exp3 = 26
    RULE_exp4 = 27
    RULE_exp5 = 28
    RULE_operand = 29
    RULE_operand1 = 30
    RULE_operand2 = 31
    RULE_operand3 = 32
    RULE_operand4 = 33
    RULE_operand5 = 34
    RULE_listExps = 35
    RULE_listExpsNotNull = 36
    RULE_listParams = 37
    RULE_indexOperator = 38
    RULE_memberAccess = 39
    RULE_staticMemberAccess = 40
    RULE_instanceMethodInvocation = 41
    RULE_staticMethodInvocation = 42
    RULE_objectCreation = 43
    RULE_listIds = 44
    RULE_listMixedIds = 45
    RULE_varDeclStmt = 46
    RULE_valDeclStmt = 47
    RULE_declareWithAssign = 48
    RULE_declareWithoutAssign = 49
    RULE_assignStmt = 50
    RULE_assignStmtSemi = 51
    RULE_ifStmt = 52
    RULE_preStmt = 53
    RULE_elseStmt = 54
    RULE_forStmt = 55
    RULE_breakStmt = 56
    RULE_continueStmt = 57
    RULE_returnStmt = 58
    RULE_methodInvocationStmt = 59
    RULE_blockStmt = 60
    RULE_stmts = 61
    RULE_stmt = 62

    ruleNames =  [ "program", "classDecl", "constructorDecl", "classStmtsNullable", 
                   "classStmt", "attributeStmt", "singleDeclParam", "declParams", 
                   "listDeclParams", "methodDecl", "idLit", "staticId", 
                   "mixedId", "literal", "variableLit", "indexedArrayLit", 
                   "nullLit", "selfLit", "booleanLit", "primitiveType", 
                   "classType", "varType", "arrayType", "exp", "exp1", "exp2", 
                   "exp3", "exp4", "exp5", "operand", "operand1", "operand2", 
                   "operand3", "operand4", "operand5", "listExps", "listExpsNotNull", 
                   "listParams", "indexOperator", "memberAccess", "staticMemberAccess", 
                   "instanceMethodInvocation", "staticMethodInvocation", 
                   "objectCreation", "listIds", "listMixedIds", "varDeclStmt", 
                   "valDeclStmt", "declareWithAssign", "declareWithoutAssign", 
                   "assignStmt", "assignStmtSemi", "ifStmt", "preStmt", 
                   "elseStmt", "forStmt", "breakStmt", "continueStmt", "returnStmt", 
                   "methodInvocationStmt", "blockStmt", "stmts", "stmt" ]

    EOF = Token.EOF
    T__0=1
    BREAK=2
    CONTINUE=3
    IF=4
    ELSE=5
    FOR=6
    TRUE=7
    FALSE=8
    BOOLEAN=9
    INT=10
    FLOAT=11
    STRING=12
    RETURN=13
    NULL=14
    CLASS=15
    SELF=16
    VAR=17
    CONST=18
    VOID=19
    CONSTRUCTOR=20
    SUPER=21
    NEW=22
    ADD=23
    SUB=24
    MUL=25
    DIV=26
    DSLASH=27
    PERCENT=28
    NOT=29
    AND=30
    OR=31
    NOT_EQUALOP=32
    EQUALOP=33
    EQUAL=34
    LESS_THAN=35
    LESS_OR_EQUAL_THAN=36
    GREATER_THAN=37
    GREATER_OR_EQUAL_THAN=38
    ASSIGNMENT_OP=39
    STRING_CONCAT=40
    EXTEND=41
    CM=42
    DOT=43
    LB=44
    RB=45
    LP=46
    RP=47
    LS=48
    RS=49
    SEMI=50
    COLON=51
    WS=52
    COMMENT_BLOCK=53
    COMMENT_LINE=54
    ID=55
    STATIC_ID=56
    INTLIT=57
    FLOATLIT=58
    ERROR_CHAR=59
    UNCLOSE_STRING=60
    ILLEGAL_ESCAPE=61
    STRINGLIT=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CSlangParser.EOF, 0)

        def classDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ClassDeclContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ClassDeclContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CSlangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 126
                self.classDecl()
                self.state = 129 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==15):
                    break

            self.state = 131
            self.match(CSlangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(CSlangParser.CLASS, 0)

        def idLit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.IdLitContext)
            else:
                return self.getTypedRuleContext(CSlangParser.IdLitContext,i)


        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def classStmtsNullable(self):
            return self.getTypedRuleContext(CSlangParser.ClassStmtsNullableContext,0)


        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def EXTEND(self):
            return self.getToken(CSlangParser.EXTEND, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_classDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDecl" ):
                listener.enterClassDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDecl" ):
                listener.exitClassDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDecl" ):
                return visitor.visitClassDecl(self)
            else:
                return visitor.visitChildren(self)




    def classDecl(self):

        localctx = CSlangParser.ClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(CSlangParser.CLASS)
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 134
                self.idLit()
                self.state = 135
                self.match(CSlangParser.EXTEND)


            self.state = 139
            self.idLit()
            self.state = 140
            self.match(CSlangParser.LP)
            self.state = 141
            self.classStmtsNullable()
            self.state = 142
            self.match(CSlangParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(CSlangParser.CONSTRUCTOR, 0)

        def listDeclParams(self):
            return self.getTypedRuleContext(CSlangParser.ListDeclParamsContext,0)


        def blockStmt(self):
            return self.getTypedRuleContext(CSlangParser.BlockStmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_constructorDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructorDecl" ):
                listener.enterConstructorDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructorDecl" ):
                listener.exitConstructorDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructorDecl" ):
                return visitor.visitConstructorDecl(self)
            else:
                return visitor.visitChildren(self)




    def constructorDecl(self):

        localctx = CSlangParser.ConstructorDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_constructorDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(CSlangParser.T__0)
            self.state = 145
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 146
            self.listDeclParams()
            self.state = 147
            self.blockStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassStmtsNullableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ClassStmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ClassStmtContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_classStmtsNullable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassStmtsNullable" ):
                listener.enterClassStmtsNullable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassStmtsNullable" ):
                listener.exitClassStmtsNullable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassStmtsNullable" ):
                return visitor.visitClassStmtsNullable(self)
            else:
                return visitor.visitChildren(self)




    def classStmtsNullable(self):

        localctx = CSlangParser.ClassStmtsNullableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_classStmtsNullable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 393218) != 0):
                self.state = 149
                self.classStmt()
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributeStmt(self):
            return self.getTypedRuleContext(CSlangParser.AttributeStmtContext,0)


        def methodDecl(self):
            return self.getTypedRuleContext(CSlangParser.MethodDeclContext,0)


        def constructorDecl(self):
            return self.getTypedRuleContext(CSlangParser.ConstructorDeclContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_classStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassStmt" ):
                listener.enterClassStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassStmt" ):
                listener.exitClassStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassStmt" ):
                return visitor.visitClassStmt(self)
            else:
                return visitor.visitChildren(self)




    def classStmt(self):

        localctx = CSlangParser.ClassStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_classStmt)
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.attributeStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.methodDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 157
                self.constructorDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDeclStmt(self):
            return self.getTypedRuleContext(CSlangParser.VarDeclStmtContext,0)


        def valDeclStmt(self):
            return self.getTypedRuleContext(CSlangParser.ValDeclStmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attributeStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributeStmt" ):
                listener.enterAttributeStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributeStmt" ):
                listener.exitAttributeStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributeStmt" ):
                return visitor.visitAttributeStmt(self)
            else:
                return visitor.visitChildren(self)




    def attributeStmt(self):

        localctx = CSlangParser.AttributeStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attributeStmt)
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.varDeclStmt()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.valDeclStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleDeclParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idLit(self):
            return self.getTypedRuleContext(CSlangParser.IdLitContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def varType(self):
            return self.getTypedRuleContext(CSlangParser.VarTypeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_singleDeclParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleDeclParam" ):
                listener.enterSingleDeclParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleDeclParam" ):
                listener.exitSingleDeclParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleDeclParam" ):
                return visitor.visitSingleDeclParam(self)
            else:
                return visitor.visitChildren(self)




    def singleDeclParam(self):

        localctx = CSlangParser.SingleDeclParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_singleDeclParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.idLit()
            self.state = 165
            self.match(CSlangParser.COLON)
            self.state = 166
            self.varType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listIds(self):
            return self.getTypedRuleContext(CSlangParser.ListIdsContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def varType(self):
            return self.getTypedRuleContext(CSlangParser.VarTypeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_declParams

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclParams" ):
                listener.enterDeclParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclParams" ):
                listener.exitDeclParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclParams" ):
                return visitor.visitDeclParams(self)
            else:
                return visitor.visitChildren(self)




    def declParams(self):

        localctx = CSlangParser.DeclParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_declParams)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.listIds()
            self.state = 169
            self.match(CSlangParser.COLON)
            self.state = 170
            self.varType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListDeclParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def singleDeclParam(self):
            return self.getTypedRuleContext(CSlangParser.SingleDeclParamContext,0)


        def declParams(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.DeclParamsContext)
            else:
                return self.getTypedRuleContext(CSlangParser.DeclParamsContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_listDeclParams

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListDeclParams" ):
                listener.enterListDeclParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListDeclParams" ):
                listener.exitListDeclParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListDeclParams" ):
                return visitor.visitListDeclParams(self)
            else:
                return visitor.visitChildren(self)




    def listDeclParams(self):

        localctx = CSlangParser.ListDeclParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_listDeclParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(CSlangParser.LB)
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==55:
                    self.state = 173
                    self.declParams()


                pass

            elif la_ == 2:
                self.state = 179 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 176
                        self.declParams()
                        self.state = 177
                        self.match(CSlangParser.CM)

                    else:
                        raise NoViableAltException(self)
                    self.state = 181 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                self.state = 183
                self.singleDeclParam()
                pass


            self.state = 187
            self.match(CSlangParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mixedId(self):
            return self.getTypedRuleContext(CSlangParser.MixedIdContext,0)


        def listDeclParams(self):
            return self.getTypedRuleContext(CSlangParser.ListDeclParamsContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def varType(self):
            return self.getTypedRuleContext(CSlangParser.VarTypeContext,0)


        def blockStmt(self):
            return self.getTypedRuleContext(CSlangParser.BlockStmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_methodDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDecl" ):
                listener.enterMethodDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDecl" ):
                listener.exitMethodDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDecl" ):
                return visitor.visitMethodDecl(self)
            else:
                return visitor.visitChildren(self)




    def methodDecl(self):

        localctx = CSlangParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_methodDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(CSlangParser.T__0)
            self.state = 190
            self.mixedId()
            self.state = 191
            self.listDeclParams()
            self.state = 192
            self.match(CSlangParser.COLON)
            self.state = 193
            self.varType()
            self.state = 194
            self.blockStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_idLit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdLit" ):
                listener.enterIdLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdLit" ):
                listener.exitIdLit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdLit" ):
                return visitor.visitIdLit(self)
            else:
                return visitor.visitChildren(self)




    def idLit(self):

        localctx = CSlangParser.IdLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_idLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(CSlangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaticIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC_ID(self):
            return self.getToken(CSlangParser.STATIC_ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_staticId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStaticId" ):
                listener.enterStaticId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStaticId" ):
                listener.exitStaticId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStaticId" ):
                return visitor.visitStaticId(self)
            else:
                return visitor.visitChildren(self)




    def staticId(self):

        localctx = CSlangParser.StaticIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_staticId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(CSlangParser.STATIC_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MixedIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idLit(self):
            return self.getTypedRuleContext(CSlangParser.IdLitContext,0)


        def staticId(self):
            return self.getTypedRuleContext(CSlangParser.StaticIdContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_mixedId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMixedId" ):
                listener.enterMixedId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMixedId" ):
                listener.exitMixedId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMixedId" ):
                return visitor.visitMixedId(self)
            else:
                return visitor.visitChildren(self)




    def mixedId(self):

        localctx = CSlangParser.MixedIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_mixedId)
        try:
            self.state = 202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [55]:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.idLit()
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.staticId()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(CSlangParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(CSlangParser.FLOATLIT, 0)

        def booleanLit(self):
            return self.getTypedRuleContext(CSlangParser.BooleanLitContext,0)


        def STRINGLIT(self):
            return self.getToken(CSlangParser.STRINGLIT, 0)

        def indexedArrayLit(self):
            return self.getTypedRuleContext(CSlangParser.IndexedArrayLitContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = CSlangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_literal)
        try:
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.match(CSlangParser.FLOATLIT)
                pass
            elif token in [7, 8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 206
                self.booleanLit()
                pass
            elif token in [62]:
                self.enterOuterAlt(localctx, 4)
                self.state = 207
                self.match(CSlangParser.STRINGLIT)
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 5)
                self.state = 208
                self.indexedArrayLit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mixedId(self):
            return self.getTypedRuleContext(CSlangParser.MixedIdContext,0)


        def staticMemberAccess(self):
            return self.getTypedRuleContext(CSlangParser.StaticMemberAccessContext,0)


        def memberAccess(self):
            return self.getTypedRuleContext(CSlangParser.MemberAccessContext,0)


        def indexOperator(self):
            return self.getTypedRuleContext(CSlangParser.IndexOperatorContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_variableLit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableLit" ):
                listener.enterVariableLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableLit" ):
                listener.exitVariableLit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableLit" ):
                return visitor.visitVariableLit(self)
            else:
                return visitor.visitChildren(self)




    def variableLit(self):

        localctx = CSlangParser.VariableLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_variableLit)
        try:
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.mixedId()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.staticMemberAccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 213
                self.memberAccess()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 214
                self.indexOperator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexedArrayLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(CSlangParser.LS, 0)

        def listExps(self):
            return self.getTypedRuleContext(CSlangParser.ListExpsContext,0)


        def RS(self):
            return self.getToken(CSlangParser.RS, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_indexedArrayLit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexedArrayLit" ):
                listener.enterIndexedArrayLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexedArrayLit" ):
                listener.exitIndexedArrayLit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexedArrayLit" ):
                return visitor.visitIndexedArrayLit(self)
            else:
                return visitor.visitChildren(self)




    def indexedArrayLit(self):

        localctx = CSlangParser.IndexedArrayLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_indexedArrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(CSlangParser.LS)
            self.state = 218
            self.listExps()
            self.state = 219
            self.match(CSlangParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NullLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NULL(self):
            return self.getToken(CSlangParser.NULL, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_nullLit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNullLit" ):
                listener.enterNullLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNullLit" ):
                listener.exitNullLit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullLit" ):
                return visitor.visitNullLit(self)
            else:
                return visitor.visitChildren(self)




    def nullLit(self):

        localctx = CSlangParser.NullLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_nullLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(CSlangParser.NULL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelfLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_selfLit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelfLit" ):
                listener.enterSelfLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelfLit" ):
                listener.exitSelfLit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelfLit" ):
                return visitor.visitSelfLit(self)
            else:
                return visitor.visitChildren(self)




    def selfLit(self):

        localctx = CSlangParser.SelfLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_selfLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(CSlangParser.SELF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(CSlangParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(CSlangParser.FALSE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_booleanLit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanLit" ):
                listener.enterBooleanLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanLit" ):
                listener.exitBooleanLit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanLit" ):
                return visitor.visitBooleanLit(self)
            else:
                return visitor.visitChildren(self)




    def booleanLit(self):

        localctx = CSlangParser.BooleanLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_booleanLit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CSlangParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(CSlangParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(CSlangParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_primitiveType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveType" ):
                listener.enterPrimitiveType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveType" ):
                listener.exitPrimitiveType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveType" ):
                return visitor.visitPrimitiveType(self)
            else:
                return visitor.visitChildren(self)




    def primitiveType(self):

        localctx = CSlangParser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idLit(self):
            return self.getTypedRuleContext(CSlangParser.IdLitContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_classType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassType" ):
                listener.enterClassType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassType" ):
                listener.exitClassType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassType" ):
                return visitor.visitClassType(self)
            else:
                return visitor.visitChildren(self)




    def classType(self):

        localctx = CSlangParser.ClassTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_classType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.idLit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitiveType(self):
            return self.getTypedRuleContext(CSlangParser.PrimitiveTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(CSlangParser.ArrayTypeContext,0)


        def classType(self):
            return self.getTypedRuleContext(CSlangParser.ClassTypeContext,0)


        def VOID(self):
            return self.getToken(CSlangParser.VOID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_varType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarType" ):
                listener.enterVarType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarType" ):
                listener.exitVarType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarType" ):
                return visitor.visitVarType(self)
            else:
                return visitor.visitChildren(self)




    def varType(self):

        localctx = CSlangParser.VarTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_varType)
        try:
            self.state = 235
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 11, 12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.primitiveType()
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.arrayType()
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 3)
                self.state = 233
                self.classType()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 234
                self.match(CSlangParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(CSlangParser.LS, 0)

        def INTLIT(self):
            return self.getToken(CSlangParser.INTLIT, 0)

        def RS(self):
            return self.getToken(CSlangParser.RS, 0)

        def primitiveType(self):
            return self.getTypedRuleContext(CSlangParser.PrimitiveTypeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_arrayType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayType" ):
                listener.enterArrayType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayType" ):
                listener.exitArrayType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = CSlangParser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(CSlangParser.LS)
            self.state = 238
            self.match(CSlangParser.INTLIT)
            self.state = 239
            self.match(CSlangParser.RS)
            self.state = 240
            self.primitiveType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self):
            return self.getTypedRuleContext(CSlangParser.Exp1Context,0)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExpContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExpContext,i)


        def STRING_CONCAT(self):
            return self.getToken(CSlangParser.STRING_CONCAT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.exp1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 250
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                    self.state = 245
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                    self.state = 246
                    self.match(CSlangParser.STRING_CONCAT)
                    self.state = 247
                    self.exp(3) 
                self.state = 252
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(CSlangParser.Exp2Context,0)


        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Exp1Context)
            else:
                return self.getTypedRuleContext(CSlangParser.Exp1Context,i)


        def EQUALOP(self):
            return self.getToken(CSlangParser.EQUALOP, 0)

        def NOT_EQUALOP(self):
            return self.getToken(CSlangParser.NOT_EQUALOP, 0)

        def GREATER_THAN(self):
            return self.getToken(CSlangParser.GREATER_THAN, 0)

        def LESS_THAN(self):
            return self.getToken(CSlangParser.LESS_THAN, 0)

        def GREATER_OR_EQUAL_THAN(self):
            return self.getToken(CSlangParser.GREATER_OR_EQUAL_THAN, 0)

        def LESS_OR_EQUAL_THAN(self):
            return self.getToken(CSlangParser.LESS_OR_EQUAL_THAN, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exp1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp1" ):
                listener.enterExp1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp1" ):
                listener.exitExp1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_exp1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 261
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 256
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 257
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 528280977408) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 258
                    self.exp1(3) 
                self.state = 263
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(CSlangParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(CSlangParser.Exp2Context,0)


        def OR(self):
            return self.getToken(CSlangParser.OR, 0)

        def AND(self):
            return self.getToken(CSlangParser.AND, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exp2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp2" ):
                listener.enterExp2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp2" ):
                listener.exitExp2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 272
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 267
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 268
                    _la = self._input.LA(1)
                    if not(_la==30 or _la==31):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 269
                    self.exp3(0) 
                self.state = 274
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(CSlangParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(CSlangParser.Exp3Context,0)


        def ADD(self):
            return self.getToken(CSlangParser.ADD, 0)

        def SUB(self):
            return self.getToken(CSlangParser.SUB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exp3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp3" ):
                listener.enterExp3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp3" ):
                listener.exitExp3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 283
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 278
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 279
                    _la = self._input.LA(1)
                    if not(_la==23 or _la==24):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 280
                    self.exp4(0) 
                self.state = 285
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(CSlangParser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(CSlangParser.Exp4Context,0)


        def DIV(self):
            return self.getToken(CSlangParser.DIV, 0)

        def MUL(self):
            return self.getToken(CSlangParser.MUL, 0)

        def PERCENT(self):
            return self.getToken(CSlangParser.PERCENT, 0)

        def DSLASH(self):
            return self.getToken(CSlangParser.DSLASH, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exp4

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp4" ):
                listener.enterExp4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp4" ):
                listener.exitExp4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 294
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 289
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 290
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 503316480) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 291
                    self.exp5() 
                self.state = 296
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(CSlangParser.Exp5Context,0)


        def NOT(self):
            return self.getToken(CSlangParser.NOT, 0)

        def SUB(self):
            return self.getToken(CSlangParser.SUB, 0)

        def operand(self):
            return self.getTypedRuleContext(CSlangParser.OperandContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exp5

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp5" ):
                listener.enterExp5(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp5" ):
                listener.exitExp5(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = CSlangParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_exp5)
        self._la = 0 # Token type
        try:
            self.state = 300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24, 29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                _la = self._input.LA(1)
                if not(_la==24 or _la==29):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 298
                self.exp5()
                pass
            elif token in [7, 8, 14, 16, 22, 44, 48, 55, 56, 57, 58, 62]:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.operand(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand1(self):
            return self.getTypedRuleContext(CSlangParser.Operand1Context,0)


        def operand(self):
            return self.getTypedRuleContext(CSlangParser.OperandContext,0)


        def LS(self):
            return self.getToken(CSlangParser.LS, 0)

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def RS(self):
            return self.getToken(CSlangParser.RS, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_operand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperand" ):
                listener.enterOperand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperand" ):
                listener.exitOperand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)



    def operand(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.OperandContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_operand, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.operand1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 312
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.OperandContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_operand)
                    self.state = 305
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 306
                    self.match(CSlangParser.LS)
                    self.state = 307
                    self.exp(0)
                    self.state = 308
                    self.match(CSlangParser.RS) 
                self.state = 314
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Operand1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand2(self):
            return self.getTypedRuleContext(CSlangParser.Operand2Context,0)


        def operand1(self):
            return self.getTypedRuleContext(CSlangParser.Operand1Context,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def idLit(self):
            return self.getTypedRuleContext(CSlangParser.IdLitContext,0)


        def listParams(self):
            return self.getTypedRuleContext(CSlangParser.ListParamsContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_operand1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperand1" ):
                listener.enterOperand1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperand1" ):
                listener.exitOperand1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand1" ):
                return visitor.visitOperand1(self)
            else:
                return visitor.visitChildren(self)



    def operand1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Operand1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_operand1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.operand2()
            self._ctx.stop = self._input.LT(-1)
            self.state = 326
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Operand1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_operand1)
                    self.state = 318
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 319
                    self.match(CSlangParser.DOT)
                    self.state = 320
                    self.idLit()
                    self.state = 322
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        self.state = 321
                        self.listParams()

             
                self.state = 328
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Operand2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def staticId(self):
            return self.getTypedRuleContext(CSlangParser.StaticIdContext,0)


        def operand3(self):
            return self.getTypedRuleContext(CSlangParser.Operand3Context,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def listParams(self):
            return self.getTypedRuleContext(CSlangParser.ListParamsContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_operand2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperand2" ):
                listener.enterOperand2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperand2" ):
                listener.exitOperand2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand2" ):
                return visitor.visitOperand2(self)
            else:
                return visitor.visitChildren(self)




    def operand2(self):

        localctx = CSlangParser.Operand2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_operand2)
        try:
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 329
                    self.operand3()
                    self.state = 330
                    self.match(CSlangParser.DOT)


                self.state = 334
                self.staticId()
                self.state = 336
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 335
                    self.listParams()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
                self.operand3()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operand3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def objectCreation(self):
            return self.getTypedRuleContext(CSlangParser.ObjectCreationContext,0)


        def operand4(self):
            return self.getTypedRuleContext(CSlangParser.Operand4Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_operand3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperand3" ):
                listener.enterOperand3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperand3" ):
                listener.exitOperand3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand3" ):
                return visitor.visitOperand3(self)
            else:
                return visitor.visitChildren(self)




    def operand3(self):

        localctx = CSlangParser.Operand3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_operand3)
        try:
            self.state = 343
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.objectCreation()
                pass
            elif token in [7, 8, 14, 16, 44, 48, 55, 56, 57, 58, 62]:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                self.operand4()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operand4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mixedId(self):
            return self.getTypedRuleContext(CSlangParser.MixedIdContext,0)


        def nullLit(self):
            return self.getTypedRuleContext(CSlangParser.NullLitContext,0)


        def selfLit(self):
            return self.getTypedRuleContext(CSlangParser.SelfLitContext,0)


        def literal(self):
            return self.getTypedRuleContext(CSlangParser.LiteralContext,0)


        def operand5(self):
            return self.getTypedRuleContext(CSlangParser.Operand5Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_operand4

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperand4" ):
                listener.enterOperand4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperand4" ):
                listener.exitOperand4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand4" ):
                return visitor.visitOperand4(self)
            else:
                return visitor.visitChildren(self)




    def operand4(self):

        localctx = CSlangParser.Operand4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_operand4)
        try:
            self.state = 350
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [55, 56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.mixedId()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.nullLit()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 347
                self.selfLit()
                pass
            elif token in [7, 8, 48, 57, 58, 62]:
                self.enterOuterAlt(localctx, 4)
                self.state = 348
                self.literal()
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 5)
                self.state = 349
                self.operand5()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operand5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_operand5

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperand5" ):
                listener.enterOperand5(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperand5" ):
                listener.exitOperand5(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand5" ):
                return visitor.visitOperand5(self)
            else:
                return visitor.visitChildren(self)




    def operand5(self):

        localctx = CSlangParser.Operand5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_operand5)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(CSlangParser.LB)
            self.state = 353
            self.exp(0)
            self.state = 354
            self.match(CSlangParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListExpsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExpContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExpContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_listExps

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListExps" ):
                listener.enterListExps(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListExps" ):
                listener.exitListExps(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListExps" ):
                return visitor.visitListExps(self)
            else:
                return visitor.visitChildren(self)




    def listExps(self):

        localctx = CSlangParser.ListExpsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_listExps)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5152417041432527232) != 0):
                self.state = 356
                self.exp(0)


            self.state = 363
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 359
                self.match(CSlangParser.CM)
                self.state = 360
                self.exp(0)
                self.state = 365
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListExpsNotNullContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExpContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExpContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_listExpsNotNull

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListExpsNotNull" ):
                listener.enterListExpsNotNull(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListExpsNotNull" ):
                listener.exitListExpsNotNull(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListExpsNotNull" ):
                return visitor.visitListExpsNotNull(self)
            else:
                return visitor.visitChildren(self)




    def listExpsNotNull(self):

        localctx = CSlangParser.ListExpsNotNullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_listExpsNotNull)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.exp(0)
            self.state = 371
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 367
                self.match(CSlangParser.CM)
                self.state = 368
                self.exp(0)
                self.state = 373
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def listExps(self):
            return self.getTypedRuleContext(CSlangParser.ListExpsContext,0)


        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_listParams

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListParams" ):
                listener.enterListParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListParams" ):
                listener.exitListParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListParams" ):
                return visitor.visitListParams(self)
            else:
                return visitor.visitChildren(self)




    def listParams(self):

        localctx = CSlangParser.ListParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_listParams)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(CSlangParser.LB)
            self.state = 375
            self.listExps()
            self.state = 376
            self.match(CSlangParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(CSlangParser.OperandContext,0)


        def LS(self):
            return self.getToken(CSlangParser.LS, 0)

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def RS(self):
            return self.getToken(CSlangParser.RS, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_indexOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexOperator" ):
                listener.enterIndexOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexOperator" ):
                listener.exitIndexOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexOperator" ):
                return visitor.visitIndexOperator(self)
            else:
                return visitor.visitChildren(self)




    def indexOperator(self):

        localctx = CSlangParser.IndexOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_indexOperator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.operand(0)
            self.state = 379
            self.match(CSlangParser.LS)
            self.state = 380
            self.exp(0)
            self.state = 381
            self.match(CSlangParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(CSlangParser.OperandContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def idLit(self):
            return self.getTypedRuleContext(CSlangParser.IdLitContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_memberAccess

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberAccess" ):
                listener.enterMemberAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberAccess" ):
                listener.exitMemberAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberAccess" ):
                return visitor.visitMemberAccess(self)
            else:
                return visitor.visitChildren(self)




    def memberAccess(self):

        localctx = CSlangParser.MemberAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_memberAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.operand(0)
            self.state = 384
            self.match(CSlangParser.DOT)
            self.state = 385
            self.idLit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaticMemberAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def staticId(self):
            return self.getTypedRuleContext(CSlangParser.StaticIdContext,0)


        def operand(self):
            return self.getTypedRuleContext(CSlangParser.OperandContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_staticMemberAccess

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStaticMemberAccess" ):
                listener.enterStaticMemberAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStaticMemberAccess" ):
                listener.exitStaticMemberAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStaticMemberAccess" ):
                return visitor.visitStaticMemberAccess(self)
            else:
                return visitor.visitChildren(self)




    def staticMemberAccess(self):

        localctx = CSlangParser.StaticMemberAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_staticMemberAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 387
                self.operand(0)
                self.state = 388
                self.match(CSlangParser.DOT)


            self.state = 392
            self.staticId()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstanceMethodInvocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(CSlangParser.OperandContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def idLit(self):
            return self.getTypedRuleContext(CSlangParser.IdLitContext,0)


        def listParams(self):
            return self.getTypedRuleContext(CSlangParser.ListParamsContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_instanceMethodInvocation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstanceMethodInvocation" ):
                listener.enterInstanceMethodInvocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstanceMethodInvocation" ):
                listener.exitInstanceMethodInvocation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstanceMethodInvocation" ):
                return visitor.visitInstanceMethodInvocation(self)
            else:
                return visitor.visitChildren(self)




    def instanceMethodInvocation(self):

        localctx = CSlangParser.InstanceMethodInvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_instanceMethodInvocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.operand(0)
            self.state = 395
            self.match(CSlangParser.DOT)
            self.state = 396
            self.idLit()
            self.state = 397
            self.listParams()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaticMethodInvocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def staticId(self):
            return self.getTypedRuleContext(CSlangParser.StaticIdContext,0)


        def listParams(self):
            return self.getTypedRuleContext(CSlangParser.ListParamsContext,0)


        def operand(self):
            return self.getTypedRuleContext(CSlangParser.OperandContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_staticMethodInvocation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStaticMethodInvocation" ):
                listener.enterStaticMethodInvocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStaticMethodInvocation" ):
                listener.exitStaticMethodInvocation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStaticMethodInvocation" ):
                return visitor.visitStaticMethodInvocation(self)
            else:
                return visitor.visitChildren(self)




    def staticMethodInvocation(self):

        localctx = CSlangParser.StaticMethodInvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_staticMethodInvocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 399
                self.operand(0)
                self.state = 400
                self.match(CSlangParser.DOT)


            self.state = 404
            self.staticId()
            self.state = 405
            self.listParams()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectCreationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(CSlangParser.NEW, 0)

        def idLit(self):
            return self.getTypedRuleContext(CSlangParser.IdLitContext,0)


        def listParams(self):
            return self.getTypedRuleContext(CSlangParser.ListParamsContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_objectCreation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjectCreation" ):
                listener.enterObjectCreation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjectCreation" ):
                listener.exitObjectCreation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjectCreation" ):
                return visitor.visitObjectCreation(self)
            else:
                return visitor.visitChildren(self)




    def objectCreation(self):

        localctx = CSlangParser.ObjectCreationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_objectCreation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.match(CSlangParser.NEW)
            self.state = 408
            self.idLit()
            self.state = 409
            self.listParams()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListIdsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idLit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.IdLitContext)
            else:
                return self.getTypedRuleContext(CSlangParser.IdLitContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_listIds

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListIds" ):
                listener.enterListIds(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListIds" ):
                listener.exitListIds(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListIds" ):
                return visitor.visitListIds(self)
            else:
                return visitor.visitChildren(self)




    def listIds(self):

        localctx = CSlangParser.ListIdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_listIds)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.idLit()
            self.state = 416
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 412
                self.match(CSlangParser.CM)
                self.state = 413
                self.idLit()
                self.state = 418
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListMixedIdsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mixedId(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.MixedIdContext)
            else:
                return self.getTypedRuleContext(CSlangParser.MixedIdContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_listMixedIds

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListMixedIds" ):
                listener.enterListMixedIds(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListMixedIds" ):
                listener.exitListMixedIds(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListMixedIds" ):
                return visitor.visitListMixedIds(self)
            else:
                return visitor.visitChildren(self)




    def listMixedIds(self):

        localctx = CSlangParser.ListMixedIdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_listMixedIds)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.mixedId()
            self.state = 424
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 420
                self.match(CSlangParser.CM)
                self.state = 421
                self.mixedId()
                self.state = 426
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def declareWithoutAssign(self):
            return self.getTypedRuleContext(CSlangParser.DeclareWithoutAssignContext,0)


        def declareWithAssign(self):
            return self.getTypedRuleContext(CSlangParser.DeclareWithAssignContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_varDeclStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclStmt" ):
                listener.enterVarDeclStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclStmt" ):
                listener.exitVarDeclStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclStmt" ):
                return visitor.visitVarDeclStmt(self)
            else:
                return visitor.visitChildren(self)




    def varDeclStmt(self):

        localctx = CSlangParser.VarDeclStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_varDeclStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.match(CSlangParser.VAR)
            self.state = 430
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 428
                self.declareWithoutAssign()
                pass

            elif la_ == 2:
                self.state = 429
                self.declareWithAssign()
                pass


            self.state = 432
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValDeclStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def declareWithoutAssign(self):
            return self.getTypedRuleContext(CSlangParser.DeclareWithoutAssignContext,0)


        def declareWithAssign(self):
            return self.getTypedRuleContext(CSlangParser.DeclareWithAssignContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_valDeclStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValDeclStmt" ):
                listener.enterValDeclStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValDeclStmt" ):
                listener.exitValDeclStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValDeclStmt" ):
                return visitor.visitValDeclStmt(self)
            else:
                return visitor.visitChildren(self)




    def valDeclStmt(self):

        localctx = CSlangParser.ValDeclStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_valDeclStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.match(CSlangParser.CONST)
            self.state = 437
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 435
                self.declareWithoutAssign()
                pass

            elif la_ == 2:
                self.state = 436
                self.declareWithAssign()
                pass


            self.state = 439
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclareWithAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mixedId(self):
            return self.getTypedRuleContext(CSlangParser.MixedIdContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def varType(self):
            return self.getTypedRuleContext(CSlangParser.VarTypeContext,0)


        def EQUAL(self):
            return self.getToken(CSlangParser.EQUAL, 0)

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def declareWithAssign(self):
            return self.getTypedRuleContext(CSlangParser.DeclareWithAssignContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_declareWithAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclareWithAssign" ):
                listener.enterDeclareWithAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclareWithAssign" ):
                listener.exitDeclareWithAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclareWithAssign" ):
                return visitor.visitDeclareWithAssign(self)
            else:
                return visitor.visitChildren(self)




    def declareWithAssign(self):

        localctx = CSlangParser.DeclareWithAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_declareWithAssign)
        try:
            self.state = 453
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.mixedId()
                self.state = 442
                self.match(CSlangParser.COLON)
                self.state = 443
                self.varType()
                self.state = 444
                self.match(CSlangParser.EQUAL)
                self.state = 445
                self.exp(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 447
                self.mixedId()
                self.state = 448
                self.match(CSlangParser.CM)
                self.state = 449
                self.declareWithAssign()
                self.state = 450
                self.match(CSlangParser.CM)
                self.state = 451
                self.exp(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclareWithoutAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listMixedIds(self):
            return self.getTypedRuleContext(CSlangParser.ListMixedIdsContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def varType(self):
            return self.getTypedRuleContext(CSlangParser.VarTypeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_declareWithoutAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclareWithoutAssign" ):
                listener.enterDeclareWithoutAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclareWithoutAssign" ):
                listener.exitDeclareWithoutAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclareWithoutAssign" ):
                return visitor.visitDeclareWithoutAssign(self)
            else:
                return visitor.visitChildren(self)




    def declareWithoutAssign(self):

        localctx = CSlangParser.DeclareWithoutAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_declareWithoutAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self.listMixedIds()
            self.state = 456
            self.match(CSlangParser.COLON)
            self.state = 457
            self.varType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableLit(self):
            return self.getTypedRuleContext(CSlangParser.VariableLitContext,0)


        def ASSIGNMENT_OP(self):
            return self.getToken(CSlangParser.ASSIGNMENT_OP, 0)

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_assignStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStmt" ):
                listener.enterAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStmt" ):
                listener.exitAssignStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignStmt(self):

        localctx = CSlangParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.variableLit()
            self.state = 460
            self.match(CSlangParser.ASSIGNMENT_OP)
            self.state = 461
            self.exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtSemiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignStmt(self):
            return self.getTypedRuleContext(CSlangParser.AssignStmtContext,0)


        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_assignStmtSemi

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStmtSemi" ):
                listener.enterAssignStmtSemi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStmtSemi" ):
                listener.exitAssignStmtSemi(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmtSemi" ):
                return visitor.visitAssignStmtSemi(self)
            else:
                return visitor.visitChildren(self)




    def assignStmtSemi(self):

        localctx = CSlangParser.AssignStmtSemiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_assignStmtSemi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            self.assignStmt()
            self.state = 464
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CSlangParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def blockStmt(self):
            return self.getTypedRuleContext(CSlangParser.BlockStmtContext,0)


        def preStmt(self):
            return self.getTypedRuleContext(CSlangParser.PreStmtContext,0)


        def ELSE(self):
            return self.getToken(CSlangParser.ELSE, 0)

        def elseStmt(self):
            return self.getTypedRuleContext(CSlangParser.ElseStmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = CSlangParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.match(CSlangParser.IF)
            self.state = 468
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 467
                self.preStmt()


            self.state = 470
            self.exp(0)
            self.state = 471
            self.blockStmt()
            self.state = 474
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 472
                self.match(CSlangParser.ELSE)
                self.state = 473
                self.elseStmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockStmt(self):
            return self.getTypedRuleContext(CSlangParser.BlockStmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_preStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreStmt" ):
                listener.enterPreStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreStmt" ):
                listener.exitPreStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreStmt" ):
                return visitor.visitPreStmt(self)
            else:
                return visitor.visitChildren(self)




    def preStmt(self):

        localctx = CSlangParser.PreStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_preStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.blockStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockStmt(self):
            return self.getTypedRuleContext(CSlangParser.BlockStmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_elseStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseStmt" ):
                listener.enterElseStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseStmt" ):
                listener.exitElseStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseStmt" ):
                return visitor.visitElseStmt(self)
            else:
                return visitor.visitChildren(self)




    def elseStmt(self):

        localctx = CSlangParser.ElseStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_elseStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.blockStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CSlangParser.FOR, 0)

        def assignStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.AssignStmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.AssignStmtContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.SEMI)
            else:
                return self.getToken(CSlangParser.SEMI, i)

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def blockStmt(self):
            return self.getTypedRuleContext(CSlangParser.BlockStmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_forStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStmt" ):
                listener.enterForStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStmt" ):
                listener.exitForStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = CSlangParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_forStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.match(CSlangParser.FOR)
            self.state = 481
            self.assignStmt()
            self.state = 482
            self.match(CSlangParser.SEMI)
            self.state = 483
            self.exp(0)
            self.state = 484
            self.match(CSlangParser.SEMI)
            self.state = 485
            self.assignStmt()
            self.state = 486
            self.blockStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(CSlangParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_breakStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStmt" ):
                listener.enterBreakStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStmt" ):
                listener.exitBreakStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)




    def breakStmt(self):

        localctx = CSlangParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.match(CSlangParser.BREAK)
            self.state = 489
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(CSlangParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_continueStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStmt" ):
                listener.enterContinueStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStmt" ):
                listener.exitContinueStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStmt" ):
                return visitor.visitContinueStmt(self)
            else:
                return visitor.visitChildren(self)




    def continueStmt(self):

        localctx = CSlangParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.match(CSlangParser.CONTINUE)
            self.state = 492
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(CSlangParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = CSlangParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.match(CSlangParser.RETURN)
            self.state = 496
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5152417041432527232) != 0):
                self.state = 495
                self.exp(0)


            self.state = 498
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodInvocationStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def staticMethodInvocation(self):
            return self.getTypedRuleContext(CSlangParser.StaticMethodInvocationContext,0)


        def instanceMethodInvocation(self):
            return self.getTypedRuleContext(CSlangParser.InstanceMethodInvocationContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_methodInvocationStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodInvocationStmt" ):
                listener.enterMethodInvocationStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodInvocationStmt" ):
                listener.exitMethodInvocationStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodInvocationStmt" ):
                return visitor.visitMethodInvocationStmt(self)
            else:
                return visitor.visitChildren(self)




    def methodInvocationStmt(self):

        localctx = CSlangParser.MethodInvocationStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_methodInvocationStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 500
                self.staticMethodInvocation()
                pass

            elif la_ == 2:
                self.state = 501
                self.instanceMethodInvocation()
                pass


            self.state = 504
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def stmts(self):
            return self.getTypedRuleContext(CSlangParser.StmtsContext,0)


        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_blockStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStmt" ):
                listener.enterBlockStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStmt" ):
                listener.exitBlockStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStmt" ):
                return visitor.visitBlockStmt(self)
            else:
                return visitor.visitChildren(self)




    def blockStmt(self):

        localctx = CSlangParser.BlockStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_blockStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self.match(CSlangParser.LP)
            self.state = 507
            self.stmts()
            self.state = 508
            self.match(CSlangParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.StmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.StmtContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmts

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmts" ):
                listener.enterStmts(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmts" ):
                listener.exitStmts(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmts" ):
                return visitor.visitStmts(self)
            else:
                return visitor.visitChildren(self)




    def stmts(self):

        localctx = CSlangParser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_stmts)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 5152487409623458268) != 0):
                self.state = 510
                self.stmt()
                self.state = 515
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDeclStmt(self):
            return self.getTypedRuleContext(CSlangParser.VarDeclStmtContext,0)


        def valDeclStmt(self):
            return self.getTypedRuleContext(CSlangParser.ValDeclStmtContext,0)


        def assignStmtSemi(self):
            return self.getTypedRuleContext(CSlangParser.AssignStmtSemiContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(CSlangParser.IfStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(CSlangParser.ForStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(CSlangParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(CSlangParser.ContinueStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(CSlangParser.ReturnStmtContext,0)


        def methodInvocationStmt(self):
            return self.getTypedRuleContext(CSlangParser.MethodInvocationStmtContext,0)


        def blockStmt(self):
            return self.getTypedRuleContext(CSlangParser.BlockStmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = CSlangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_stmt)
        try:
            self.state = 526
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 516
                self.varDeclStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 517
                self.valDeclStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 518
                self.assignStmtSemi()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 519
                self.ifStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 520
                self.forStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 521
                self.breakStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 522
                self.continueStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 523
                self.returnStmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 524
                self.methodInvocationStmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 525
                self.blockStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[23] = self.exp_sempred
        self._predicates[24] = self.exp1_sempred
        self._predicates[25] = self.exp2_sempred
        self._predicates[26] = self.exp3_sempred
        self._predicates[27] = self.exp4_sempred
        self._predicates[29] = self.operand_sempred
        self._predicates[30] = self.operand1_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def operand_sempred(self, localctx:OperandContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def operand1_sempred(self, localctx:Operand1Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




