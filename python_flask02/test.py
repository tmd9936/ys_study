def solution(info, query):
    answer = []
    for query_str in query:
        count = 0
        query_list = query_str.split(' and ')
        temp = query_list[len(query_list) - 1].split(' ')
        del query_list[len(query_list) - 1]
        query_list.extend(temp)
        
        for info_str in info:
            info_list = info_str.split(' ')
            for idx in range(0, len(info_list)):
                if idx == len(info_list) -1:
                    if int(info_list[idx]) < int(query_list[idx]):
                        break
                else:
                    if query_list[idx] == '-':
                        continue
                    else:
                        if query_list[idx] != info_list[idx]:
                           break
            else:
                count += 1
        answer.append(count)
    
    return answer


ss = [1,2,3]
def solution(info, query):
    answer = []
    for query_str in query:
        count = 0
        query_list = query_str.split(' and ')
        temp = query_list[len(query_list) - 1].split(' ')
        del query_list[len(query_list) - 1]
        query_list.extend(temp)
        
        ' '.join()
        

        for i_str in info:
            b_check = False
            for q_str in query_list:
                if q_str == '-':
                    continue
                else:
                    if not q_str.isnumeric():
                        if q_str not in i_str:
                            b_check = True
                            break
                    else:
                        i_grade = int(i_str.split(' ')[4])

                        if i_grade < int(q_str):
                            b_check = True
                            break

            else:
                count += 1

                
                
                
                
            
        answer.append(count)
    
    return answer