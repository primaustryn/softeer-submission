from collections import deque

def solution(customers):
  counsel = deque()
  
  size=len(customers)

  current_time=0
  cur_counselee = None
  next_counsel_end_time=0

  result = [-1] * size

  for i in range(0,size):
    #도착시간, 상담시간, 기대치
    cdd_arr, cdd_dur, cdd_exp = customers[i]
    candidate = customers[i]
    candidate.append(i)
    # print(customers[i])
    
    #현재 시각: 도착 시간으로 간주
    current_time = cdd_arr

    # next_counsel_end_time <= current_time: 
    if(next_counsel_end_time <= current_time):
      
      # 상담자, 대기열 갱신
      if len(counsel) > 0:
        #상담 종료
        completed=counsel.popleft()
        # print('completed:'+str(completed))
        # print('after complete'+str(counsel))

        #result에 index별 종료시간 추가
        result[completed[3]] = next_counsel_end_time
        
        if len(counsel) < 1:
            # 다음 인원 없음
          cur_counselee = None
          
        else:
          # 다음 인원 상담
          cur_counselee = counsel[0]
          next_counsel_end_time += cur_counselee[1]
          
          # 큐가 차 있는 경우
          # 다음 카운셀링 인원 마저도 현재시점에서는 다 끝난 케이스를 잡기 위해.
          while next_counsel_end_time <= current_time:
            #상담 종료
            completed=counsel.popleft()
            #result에 index별 종료시간 추가
            result[completed[3]] = next_counsel_end_time
            if len(counsel) >= 1:
              # 다음 인원 상담
              cur_counselee = counsel[0]
              next_counsel_end_time += cur_counselee[1]

            # 조건문 업데이트
            else: 
            # 다음 인원 없음
              cur_counselee = None
              break
          
        
    # 현재 아무도 미상담이면 -> candidate 무조건 즉시 상담
    if(cur_counselee == None):
      counsel.append(candidate)
      # 다음 상담 종료 타임 갱신
      next_counsel_end_time = current_time + cdd_dur
      cur_counselee = counsel[0]
      continue

    # 현재 누군가 상담중이면 
    # 대기 인원 > 기대치: -1
    if(len(counsel)>cdd_exp):
      result[i]=-1
      continue
    
    # 대기 인원 <= 기대치: 대기 큐에 추가
    if(len(counsel)<=cdd_exp):
      counsel.append(candidate)

  # 모든 input 분석 완료.
  # 대기열에 있는 상담자들 기준으로, 예상 종료시간 누적 계산
  if len(counsel) > 0:
    idx=counsel[0][3]
    result[idx] = next_counsel_end_time    
    for i in range(1,len(counsel)):
      idx=counsel[i][3]
      next_counsel_end_time += counsel[i][1]      
      result[idx] = next_counsel_end_time

  return result
    

c=[[0, 4, 1], [2, 2, 2], [3, 1, 2], [5, 1, 1]]
out=solution(c)
ans=[4, 6, 7, -1]

print(out)
print(ans)


c2=[[3, 5, 2], [6, 4, 1], [7, 5, 1], [8, 4, 1], [10, 3, 3], [11, 2, 3], [12, 1, 3], [16, 2, 2], [100, 1, 1]]
ans2=[8, 12, -1, 16, 19, 21, 22, -1, 101]
out2=solution(c2)

print(out2)
print(ans2)

  