from xlrd import open_workbook






if __name__ == '__main__':


    book = open_workbook('Scenario_TestCase_Sample.xlsx')

    # Get sheet names
    sheet_names = book.sheet_names()
    print sheet_names



    # Get sheet value
    # sheet = book.sheet_by_name(sheet_names[0])
    # keys = [sheet.cell(0, col_index).value for col_index in xrange(sheet.ncols)]

    # for col_index in xrange(sheet.ncols):
    #     for row_index in xrange(sheet.nrows):
    #         print sheet.cell(row_index, col_index).value
    #     print ""





    Pattern_num  = None
    Module_num   = None
    Register_num = None

    Module_idx = None
    Struct_idx = None
    elem_idx   = None
    reg_idx    = None

    Module_name = None

    sheet = book.sheet_by_name(sheet_names[0])
    for row_idx in xrange(sheet.nrows):
        row_list = sheet.row_values(row_idx)
        # print row_list

        if ( (None == Pattern_num) or (None == Module_num) or (None == Register_num) ):
            if "Pattern_num" in row_list:
                Pattern_num = int(row_list[row_list.index("Pattern_num") + 1])
                # print ">> Pattern_num: ", Pattern_num

            if "Module_num" in row_list:
                Module_num = int(row_list[ row_list.index("Module_num") + 1])
                # print ">> Module_num: ", Module_num

            if "Register_num" in row_list:
                Register_num = int(row_list[ row_list.index("Register_num") + 1])
                # print ">> Register_num: ", Register_num

        elif ( (None == Module_idx) or (None == Struct_idx) or (None == elem_idx) or (None == reg_idx) ):
            if "Module" in row_list:
                Module_idx = row_list.index("Module")
            if "Structure" in row_list:
                Struct_idx = row_list.index("Structure")
            if "element" in row_list:
                elem_idx = row_list.index("element")
            if "Registers" in row_list:
                reg_idx = row_list.index("Registers")


            print

            # Get pattern id
            # matching = [s for s in row_list if "Pattern" in s]
            ptnidx_list = [row_list.index(s) for s in row_list if "Pattern" in s]


            print ">>>> Module_idx: ", Module_idx,
            print " Struct_idx: ", Struct_idx,
            print " elem_idx: ", elem_idx,
            print " reg_idx: ", reg_idx,
            print " pattern ID: ", ptnidx_list
            print

        else:

            if row_list[Module_idx]:
                Module_name = row_list[Module_idx]
            if row_list[Struct_idx]:
                Struct_name = row_list[Struct_idx]
            if row_list[elem_idx]:
                elem_name = row_list[elem_idx]

            print " Module :"   , Module_name,
            print ",", Struct_name,
            print ",", elem_name,
            print ",", row_list[reg_idx],


            for ii, ptn_idx in enumerate(ptnidx_list):
                if isinstance(row_list[ptn_idx], unicode) or isinstance(row_list[ptn_idx], str):
                    if "0x" in row_list[ptn_idx]:
                        print (" Pattern_%05d: %s")%(ii+1, int(row_list[ptn_idx],16)),
                    else:
                        print (" Pattern_%05d: %s")%(ii+1, int(row_list[ptn_idx])),
                else:
                    print (" Pattern_%05d: %s")%(ii+1, int(row_list[ptn_idx])),

            print




    print '----------------------------------------------'
    print '----------------------------------------------'

    # for row_idx in xrange(sheet.nrows):
    #     for col_idx in xrange(sheet.ncols):
    #         print sheet.row_values(row_idx)[col_idx]



    pass
