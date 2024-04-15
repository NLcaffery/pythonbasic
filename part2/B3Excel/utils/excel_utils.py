import pandas as pd


def get_excel_case_data(interface_type):
    data = pd.read_excel('./case_data/Excel_case.xlsx')
    interface_type_data = data[data['请求接口类别']==interface_type]
    final_data = []

    staet_index = 0
    for i in interface_type_data.index:
        inner_data = {}
        # for d in interface_type_data.iloc[[i]]:
        #改动
        for d in interface_type_data.iloc[[staet_index]]:
            inner_data[d] = interface_type_data[d][i]
        final_data.append(inner_data)
    return final_data

