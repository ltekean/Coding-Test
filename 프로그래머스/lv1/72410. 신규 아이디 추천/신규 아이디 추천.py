def solution(new_id):
    new_id = new_id.lower() #1단계
    checker = "abcdefghijklmnopqrstuvwxyz1234567890-_."
    for i in new_id: #2-1단계
      if not i in checker:#2-2단계
        new_id = new_id.replace(i,"") #2-3단계
    while ".." in new_id: #3-1단계
        new_id = new_id.replace("..",".") #3-2단계
    if new_id and new_id[0] == ".": #4-1단계
      new_id = new_id[1:] #4-2단계
    if new_id and new_id[-1] ==".": #4-1단계
      new_id = new_id[:-1] #4-2단계
    if not new_id: #5-1
      new_id="a" #5-2단계
    if len(new_id) > 15: #6-1단계
      new_id = new_id[:15] #6-2단계
      if new_id[-1] ==".": 
        new_id = new_id[:-1] #6-3단계
    while len(new_id) < 3: #7-1단계
        new_id += new_id[-1] #7-2단계
        
    return new_id