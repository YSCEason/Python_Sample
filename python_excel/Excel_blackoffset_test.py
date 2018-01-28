import re
import xlsxwriter
import random
import operator
import parser

blk_offset = (
             ['in_w'                , 1920],
             ['in_h'                , 1080],
             ['woi_x'               , 5   ],
             ['woi_y'               , 10  ],
             ['woi_w'               , 10  ],
             ['woi_h'               , 5   ],
             ['flyby_in_width'      , 5   ],
             ['flyby_in_height'     , 5   ],
             ['in_up_crop_pixel'    , 5   ],
             ['in_down_crop_pixel'  , 5   ],
             ['in_left_crop_pixel'  , 5   ],
             ['in_right_crop_pixel' , 5   ],
             ['Shd_Tab_in_w'        , 5   ],
             ['Shd_Tab_in_h'        , 5   ],
             ['Shd_Tab_woi_x'       , 5   ],
             ['Shd_Tab_woi_y'       , 5   ],
             ['shd_scl_in_width'    , 5   ],
             ['shd_scl_in_height'   , 5   ],
             ['shd_scl_out_width'   , 5   ],
             ['shd_scl_out_height'  , 5   ],
             ['shade_bypass'        , 5   ],
             ['Black_Offset_Add_00' , 5   ],
             ['Black_Offset_Sbt_00' , 5   ],
             ['Black_Offset_Add_01' , 5   ],
             ['Black_Offset_Sbt_01' , 5   ],
             ['Black_Offset_Add_10' , 5   ],
             ['Black_Offset_Sbt_10' , 5   ],
             ['Black_Offset_Add_11' , 5   ],
             ['Black_Offset_Sbt_11' , 5   ]
             )


# ---------------------------------------------------


blk_offset3 = (
               { 'in_w'                : {'Value' : 1920, 'Minimum' : 4, 'Maximum' : 8192 ,'Condition1' : "*;4"       , 'Condition2' : ""     } },
               { 'in_h'                : {'Value' : 1080, 'Minimum' : 1, 'Maximum' : 8192 ,'Condition1' : "odd"       , 'Condition2' : ""     } },
               { 'woi_x'               : {'Value' : 5   , 'Minimum' : 0, 'Maximum' : 0    ,'Condition1' : ""          , 'Condition2' : ""     } },
               { 'woi_y'               : {'Value' : 10  , 'Minimum' : 0, 'Maximum' : 0    ,'Condition1' : ""          , 'Condition2' : ""     } },
               { 'woi_w'               : {'Value' : 10  , 'Minimum' : 4, 'Maximum' : 8192 ,'Condition1' : "=;in_w"    , 'Condition2' : ""     } },
               { 'woi_h'               : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 8192 ,'Condition1' : "=;in_h"    , 'Condition2' : ""     } },
               { 'flyby_in_width'      : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : "*;4"       , 'Condition2' : ""     } },
               { 'flyby_in_height'     : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : ""          , 'Condition2' : ""     } },
               { 'in_up_crop_pixel'    : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : ""          , 'Condition2' : ""     } },
               { 'in_down_crop_pixel'  : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : ""          , 'Condition2' : ""     } },
               { 'in_left_crop_pixel'  : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : ""          , 'Condition2' : ""     } },
               { 'in_right_crop_pixel' : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : ""          , 'Condition2' : ""     } },
               { 'Shd_Tab_in_w'        : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : ""          , 'Condition2' : ""     } },
               { 'Shd_Tab_in_h'        : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : ""          , 'Condition2' : ""     } },
               { 'Shd_Tab_woi_x'       : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : "0"         , 'Condition2' : ""     } },
               { 'Shd_Tab_woi_y'       : {'Value' : 6   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : "0"         , 'Condition2' : ""     } },
               { 'shd_scl_in_width'    : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : ""          , 'Condition2' : ""     } },
               { 'shd_scl_in_height'   : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : ""          , 'Condition2' : ""     } },
               { 'shd_scl_out_width'   : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : ""          , 'Condition2' : ""     } },
               { 'shd_scl_out_height'  : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : ""          , 'Condition2' : ""     } },
               { 'shade_bypass'        : {'Value' : 1   , 'Minimum' : 0, 'Maximum' : 1    ,'Condition1' : ""          , 'Condition2' : ""     } },
               { 'Black_Offset_Add_00' : {'Value' : 5   , 'Minimum' : 0, 'Maximum' : 1024 ,'Condition1' : "Random"    , 'Condition2' : ""     } },
               { 'Black_Offset_Sbt_00' : {'Value' : 5   , 'Minimum' : 0, 'Maximum' : 1024 ,'Condition1' : "Random"    , 'Condition2' : ""     } },
               { 'Black_Offset_Add_01' : {'Value' : 5   , 'Minimum' : 0, 'Maximum' : 1024 ,'Condition1' : "Random"    , 'Condition2' : ""     } },
               { 'Black_Offset_Sbt_01' : {'Value' : 5   , 'Minimum' : 0, 'Maximum' : 1024 ,'Condition1' : "Random"    , 'Condition2' : ""     } },
               { 'Black_Offset_Add_10' : {'Value' : 5   , 'Minimum' : 0, 'Maximum' : 1024 ,'Condition1' : "Random"    , 'Condition2' : ""     } },
               { 'Black_Offset_Sbt_10' : {'Value' : 5   , 'Minimum' : 0, 'Maximum' : 1024 ,'Condition1' : "Random"    , 'Condition2' : ""     } },
               { 'Black_Offset_Add_11' : {'Value' : 5   , 'Minimum' : 0, 'Maximum' : 1024 ,'Condition1' : "Random"    , 'Condition2' : ""     } },
               { 'Black_Offset_Sbt_11' : {'Value' : 5   , 'Minimum' : 0, 'Maximum' : 1024 ,'Condition1' : "Random"    , 'Condition2' : ""     } }
            )

# ------------------------------------------------------

blk_offset4 = (
               { 'in_w'                : {'Value' : 1920, 'Minimum' : 4, 'Maximum' : 8192 ,'Condition1' : "in_w%4"                                                   , 'Condition2' : ""     } },
               { 'in_h'                : {'Value' : 1080, 'Minimum' : 1, 'Maximum' : 8192 ,'Condition1' : "odd"                                                      , 'Condition2' : ""     } },
               { 'woi_x'               : {'Value' : 5   , 'Minimum' : 0, 'Maximum' : 0    ,'Condition1' : ""                                                         , 'Condition2' : ""     } },
               { 'woi_y'               : {'Value' : 10  , 'Minimum' : 0, 'Maximum' : 0    ,'Condition1' : ""                                                         , 'Condition2' : ""     } },
               { 'woi_w'               : {'Value' : 10  , 'Minimum' : 4, 'Maximum' : 8192 ,'Condition1' : "=in_w"                                                    , 'Condition2' : ""     } },
               { 'woi_h'               : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 8192 ,'Condition1' : "=in_h"                                                    , 'Condition2' : ""     } },
               { 'flyby_in_width'      : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : "in_w%4"                                                   , 'Condition2' : ""     } },
               { 'flyby_in_height'     : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : "Random"                                                   , 'Condition2' : ""     } },
               { 'in_up_crop_pixel'    : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : "(in_up_crop_pixel+in_down_crop_pixel)<woi_w"              , 'Condition2' : "(woi_w - (in_up_crop_pixel + in_down_crop_pixel)) == even"     } },
               { 'in_down_crop_pixel'  : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : "(in_up_crop_pixel+in_down_crop_pixel)<woi_w"              , 'Condition2' : "(woi_w - (in_up_crop_pixel + in_down_crop_pixel)) == even"     } },
               { 'in_left_crop_pixel'  : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : "<woi_h"                                                   , 'Condition2' : ""     } },
               { 'in_right_crop_pixel' : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : "<woi_h"                                                   , 'Condition2' : ""     } },
               { 'Shd_Tab_in_w'        : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : "Random"                                                   , 'Condition2' : ""     } },
               { 'Shd_Tab_in_h'        : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : "Random"                                                   , 'Condition2' : ""     } },
               { 'Shd_Tab_woi_x'       : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : "0"                                                        , 'Condition2' : ""     } },
               { 'Shd_Tab_woi_y'       : {'Value' : 6   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : "0"                                                        , 'Condition2' : ""     } },
               { 'shd_scl_in_width'    : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : "Random"                                                   , 'Condition2' : ""     } },
               { 'shd_scl_in_height'   : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : "Random"                                                   , 'Condition2' : ""     } },
               { 'shd_scl_out_width'   : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : "( woi_w - in_left_crop_pixel - in_right_crop_pixel ) / 2" , 'Condition2' : ""     } },
               { 'shd_scl_out_height'  : {'Value' : 5   , 'Minimum' : 1, 'Maximum' : 200  ,'Condition1' : "( woi_h - in_up_crop_pixel - in_down_crop_pixel ) / 2"    , 'Condition2' : ""     } },
               { 'shade_bypass'        : {'Value' : 1   , 'Minimum' : 0, 'Maximum' : 1    ,'Condition1' : ""                                                         , 'Condition2' : ""     } },
               { 'Black_Offset_Add_00' : {'Value' : 5   , 'Minimum' : 0, 'Maximum' : 1024 ,'Condition1' : "Random"                                                   , 'Condition2' : ""     } },
               { 'Black_Offset_Sbt_00' : {'Value' : 5   , 'Minimum' : 0, 'Maximum' : 1024 ,'Condition1' : "Random"                                                   , 'Condition2' : ""     } },
               { 'Black_Offset_Add_01' : {'Value' : 5   , 'Minimum' : 0, 'Maximum' : 1024 ,'Condition1' : "Random"                                                   , 'Condition2' : ""     } },
               { 'Black_Offset_Sbt_01' : {'Value' : 5   , 'Minimum' : 0, 'Maximum' : 1024 ,'Condition1' : "Random"                                                   , 'Condition2' : ""     } },
               { 'Black_Offset_Add_10' : {'Value' : 5   , 'Minimum' : 0, 'Maximum' : 1024 ,'Condition1' : "Random"                                                   , 'Condition2' : ""     } },
               { 'Black_Offset_Sbt_10' : {'Value' : 5   , 'Minimum' : 0, 'Maximum' : 1024 ,'Condition1' : "Random"                                                   , 'Condition2' : ""     } },
               { 'Black_Offset_Add_11' : {'Value' : 5   , 'Minimum' : 0, 'Maximum' : 1024 ,'Condition1' : "Random"                                                   , 'Condition2' : ""     } },
               { 'Black_Offset_Sbt_11' : {'Value' : 5   , 'Minimum' : 0, 'Maximum' : 1024 ,'Condition1' : "Random"                                                   , 'Condition2' : ""     } }
            )



def get_operator_fn(op):
    return {
        '+'  : operator.add,
        '-'  : operator.sub,
        '*'  : operator.mul,
        '/'  : operator.div,
        '%'  : operator.mod,
        '^'  : operator.xor,
        '< ' : operator.lt,
        '<=' : operator.le,
        '==' : operator.eq,
        '!=' : operator.ne,
        '>=' : operator.ge,
        '> ' : operator.gt,
        }[op]


def eval_binary_expr(op1, operator, op2):
    op1,op2 = int(op1), int(op2)
    return get_operator_fn(operator)(op1, op2)


def GetCondRegName(a_str):
    replaced = re.sub('[\W0-9]+', ' ', a_str)
    # print replaced.split()
    return replaced.split()
    # ----------------------------------
    # from string import maketrans
    # intab  = "';<>=()+-*/%&^~0123456789'"
    # outtab = "                          "
    # trantab = maketrans(intab, outtab)

    # CondStrTmp = a_str.translate(trantab);

    # return CondStrTmp.split()
    # return " ".join(CondStrTmp.split()).split()
    # ----------------------------------------

    # chars_to_remove = [';<>=()+-*/%&^~0123456789']
    # CondStrTmp = a_str.translate(None, ''.join(chars_to_remove))
    # return " ".join(CondStrTmp.split()).split()

def GetCondAns(a_Strformula):
    code = parser.expr(a_Strformula).compile()
    return eval(code)


PATTERN_NUMBER = 10


def GetRegIndex(a_TestGroup, a_regname):
    idx = 0
    for RegName in (a_TestGroup):
        idx += 1
        for key in RegName.keys():
            if( key == a_regname):
                return (idx-1)

    print "It's not find"
    return 0

def GetRegInfo(a_TestGroup, a_regname):
    return a_TestGroup[GetRegIndex(a_TestGroup, a_regname)][a_regname]

def GetRegValue(a_TestGroup, a_regname):
    return a_TestGroup[GetRegIndex(a_TestGroup, a_regname)][a_regname]['Value']

def GetRegMinValue(a_TestGroup, a_regname):
    return a_TestGroup[GetRegIndex(a_TestGroup, a_regname)][a_regname]['Minimum']

def GetRegMaxValue(a_TestGroup, a_regname):
    return a_TestGroup[GetRegIndex(a_TestGroup, a_regname)][a_regname]['Maximum']

def GetRegCondStr(a_TestGroup, a_regname, a_Condition):
    return a_TestGroup[GetRegIndex(a_TestGroup, a_regname)][a_regname][a_Condition]

def SetRegValue(a_TestGroup, a_regname, a_value):
    a_TestGroup[GetRegIndex(a_TestGroup, a_regname)][a_regname]['Value'] = a_value

def CondParse(a_TestGroup, a_regname, a_pattern):
    ErrorCode = 0
    for key in GetRegInfo(a_TestGroup, a_regname):
        if ("Condition" in key):

            CondStringTmp = GetRegCondStr(a_TestGroup, a_regname, key)
            Condlist = CondStringTmp.split(';')

# *********************************************************

            CondRegStrlist = GetCondRegName(CondStringTmp)
            CondExpression = CondStringTmp

            for reg in CondRegStrlist:
                # print reg

                if(reg != 'odd' and reg != 'even' and reg != 'Random'):
                    CondExpression = CondExpression.replace(reg, str(GetRegValue(a_TestGroup, a_regname)) )

            # if (CondExpression != ''):
            #     print '%s:  [%s] = '% (a_regname, CondExpression)
                # print '[%s] = %s'% (CondExpression, GetCondAns(CondExpression))

# *********************************************************



            # if(Condlist[0] == '='):
            #     CondValue = GetRegValue(a_TestGroup, Condlist[1])
            #     SetRegValue(a_TestGroup, a_regname, CondValue)
            #     # print '>>>> assign %s = %s = %d'% (a_regname, Condlist[1], CondValue)


            # elif(Condlist[0] == 'odd'):

            #     if (a_pattern%2 != 0):
            #         SetRegValue(a_TestGroup, a_regname, a_pattern)
            #         # print ">>>> It's odd!!! %s"%GetRegValue(a_TestGroup, a_regname)
            #     else:
            #         # print ">>>> It's not odd!!! %s"%GetRegValue(a_TestGroup, a_regname)
            #         return 0

            # elif(Condlist[0] == 'even'):

            #     if (a_pattern%2 == 0):
            #         SetRegValue(a_TestGroup, a_regname, a_pattern)
            #         # print ">>>> It's even!!! %s"%GetRegValue(a_TestGroup, a_regname)
            #     else:
            #         # print ">>>> It's not even!!! %s"%GetRegValue(a_TestGroup, a_regname)
            #         return 0

            # elif(Condlist[0] == '*'):
            #     CondValue = int(Condlist[1])
            #     if (a_pattern%CondValue == 0):
            #         SetRegValue(a_TestGroup, a_regname, a_pattern)
            #         # print ">>>> It's a multiple of %s!!! %s"%(Condlist[1], GetRegValue(a_TestGroup, a_regname))
            #     else:
            #         # print ">>>> It's not a multiple of %s!!! %s"%(Condlist[1], GetRegValue(a_TestGroup, a_regname))
            #         return 0

            # elif(Condlist[0] == 'Random'):
            #     SetRegValue(a_TestGroup, a_regname, a_pattern)
            #     return 1

            # else:
            #     # print 'no Condition!!'
            #     # pass
            #     return 0
    return 1


def GetTestGroup(a_TestGroup, a_GroupSheet):
    for pattern in range(1, PATTERN_NUMBER+1):
        col = 1
        for RegName in (a_TestGroup):
            for key in RegName.keys():
                # print 'key=%s, Dictionary =%s' % (key, RegName[key])
                # print 'key=%s, Value=%s'       % (key, RegName[key]['Value'])
                # print 'key=%s, Minimum=%s'     % (key, RegName[key]['Minimum'])
                # print 'key=%s, Maximum=%s'     % (key, RegName[key]['Maximum'])
                # print 'key=%s, Condition1=%s'  % (key, RegName[key]['Condition1'])
                # print 'key=%s, Condition2=%s'  % (key, RegName[key]['Condition2'])


                # print '[%s] = %s'% (key, GetRegValue(a_TestGroup, key))

                PatternVal = random.randint(GetRegMinValue(a_TestGroup, key), GetRegMaxValue(a_TestGroup, key))
                while( CondParse(a_TestGroup, key, PatternVal) ):
                    PatternVal = random.randint(GetRegMinValue(a_TestGroup, key), GetRegMaxValue(a_TestGroup, key))
                    # print '[%s] >>> PatternVal = %d'% (key, PatternVal)
                    # SetRegValue(a_TestGroup, key, PatternVal)
                    break

                a_GroupSheet.write(2+pattern, col, RegName[key]['Value'])
                col += 1

            # print ""



    # print a_TestGroup[0]['in_w']

# ---------------------------------------------------




def CreateWorkbook(a_GroupSheet):
    # Create a workbook and add a worksheet.
    # workbook = xlsxwriter.Workbook('Expenses01.xlsx')
    # GroupSheet = workbook.add_worksheet("blk_offset")

    # Start from the first cell. Rows and columns are zero indexed.
    row = 2
    col = 1

    format = workbook.add_format()
    format.set_rotation(-90)
    format.set_bold()

    # Iterate over the data and write it out row by row.
    for RegName in (blk_offset):
        a_GroupSheet.write(row, col, RegName[0], format)
        col += 1


    for CaseNum in range(1, PATTERN_NUMBER+1):
        a_GroupSheet.write(2+CaseNum, 0, "pattern_" + "%05d"%CaseNum)

        col = 1
        for RegName in (blk_offset):
            # if('in_w' == RegName[0]):
            #     a_GroupSheet.write(2+CaseNum, col, RegName[1])
            # if('in_h' == RegName[0]):
            #     a_GroupSheet.write(2+CaseNum, col, RegName[1])
            # if('woi_x' == RegName[0]):
            #     a_GroupSheet.write(2+CaseNum, col, RegName[1])
            # if('woi_y' == RegName[0]):
            #     a_GroupSheet.write(2+CaseNum, col, RegName[1])
            # if('woi_w' == RegName[0]):
            #     a_GroupSheet.write(2+CaseNum, col, RegName[1])
            # if('woi_h' == RegName[0]):
            #     a_GroupSheet.write(2+CaseNum, col, RegName[1])

            col += 1


    # workbook.close()


if __name__ == '__main__':

    workbook = xlsxwriter.Workbook('Expenses01.xlsx')
    GroupSheet = workbook.add_worksheet("blk_offset")

    CreateWorkbook(GroupSheet)
    GetTestGroup(blk_offset4, GroupSheet)


    workbook.close()

# -------------------------------------------

    # print eval_binary_expr(*("1 + 3".split()))
    # print eval_binary_expr(*("1 * 3".split()))
    # print eval_binary_expr(*("1 % 3".split()))
    # print eval_binary_expr(*("1 ^ 3".split()))
    # print eval_binary_expr(*("3 == 3".split()))
    # print eval_binary_expr(*("3 != 3".split()))

# -------------------------------------------

    # formula = "50*2-(1+2*(9+1))"
    # formula = "(100+50)/GetRegValue(blk_offset3, 'shd_scl_in_width')"
    # print 'String formula >>> %s'% GetCondAns(formula)

 # ------------------------------------------


    # print GetCondRegName("( in_up_crop_pixel + in_down_crop_pixel ) < woi_w")
    # print GetCondRegName("( woi_w - in_left_crop_pixel - in_right_crop_pixel ) / 2")
    # print GetCondRegName("(woi_w - (in_up_crop_pixel+in_down_crop_pixel)) == even")
    # print GetCondRegName("Random")
    # print GetCondRegName("(woi_w - (in_up_crop_pixel+in_down_crop_pixel)) == even")


    # from string import maketrans
    # intab  = "';<>=()+-*/%&^~0123456789'"
    # outtab = "                          "
    # trantab = maketrans(intab, outtab)

    # CondStrTmp = "(woi_w - (in_up_crop_pixel+in_down_crop_pixel)) == even";

    # CondStrTmp = CondStrTmp.translate(trantab);
    # print " ".join(CondStrTmp.split()).split()
 # ------------------------------------------

    # str1 = 'AA_$%^BB_hh6_4@566CC_DD_g@#4564g_E&-E+_-FF+*_/a/a-+_+><?bb_vv'

    # replaced = re.sub('[\W0-9]+', ' ', str1)
    # print replaced
