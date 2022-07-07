import logging
import numbers


def handle(anotherfunc, input_str, tenant_type: str, x_api_key: str, org_id: str, batch_size: numbers = 300):
    response = []
    # if isinstance(tuple, input_str) and len(input_str) < 1:
    #     response = anotherfunc(tenant_type, x_api_key, org_id=org_id, ids=input_str)

    print("inside handle function")
    if input_str is not None:
        input_list = input_str.split(", ")
        for i in range(0, len(input_list), batch_size):
            print("iteration count {}".format(i))
            current_batch = input_list[i:i + batch_size]
            current_batch_str = ','.join(current_batch)
            print("current batch {}".format(current_batch_str))
            temp_resp = anotherfunc(tenant_type, x_api_key, org_id=org_id, ids=current_batch_str)
            print(temp_resp)
            response = response + temp_resp['records']
            print("response {}".format(response))
        return response



# def fun_1(input):
#     resp = list()
#     print(">>>got called")
#     for i in input:
#         resp.append(i * i)
#
#     return resp

# def fun_2(input_1, input_2):
#     return input_1*input_2
#
# input = [1,2,3,4,5,6,7]
#
#
# print(fun_1(input))
#
#
# print(">>>>>>>>>>>>>>>>")
# print(handle(fun_1, input, 2))
