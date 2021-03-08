# eeg_authentication

1. server/members/create/ **(POST)**

   회원가입

   > - request (JSON string 형식)
   >
   > ```
   > {
   >     "name": "HyeongGeun Oh",
   >     "username": "hyeonggeun2",
   >     "password": "gudrms12",
   >     "gender": "male",
   >     "age": 26
   > }
   > ```
   >
   > 
   >
   > - response
   >
   > ```
   > {
   >     "user": {
   >         "username": "hyeonggeun2",
   >         "name": "HyeongGeun Oh",
   >         "age": 26,
   >         "gender": "male"
   >     }
   > }
   > ```

   

2. server/members/login/ **(POST)**

   로그인 및 TOKEN 값을 얻습니다.

   > - request
   >
   > ```
   > {
   >     "username": "hyeonggeun21",
   >     "password": "gudrms12"
   > }
   > ```
   >
   > 
   >
   > - response
   >
   > ```
   > {
   >     "token": "e4c0d0daaf2cc4ee2190a033957c1aa8c9eca9a5",
   >     "user": {
   >         "pk": 1,
   >         "username": "hyeonggeun21",
   >         "name": "HyeongGeun Oh",
   >         "age": 26,
   >         "gender": "male"
   >     }
   > }
   > ```

   

3. server/members/logout/ **(POST)**

   로그아웃(토큰 삭제)합니다.

   >- request
   >
   >```
   >{
   >    "token": "e4c0d0daaf2cc4ee2190a033957c1aa8c9eca9a5"
   >}
   >```
   >
   >
   >
   >- response
   >
   >```
   >{
   >    "detail": "로그아웃 되었습니다."
   >}
   >```

   

4. server/authenticate/ **(POST)**

   EEG 데이터를 보내고 인증합니다.

   >- request
   >
   >```
   >{
   >	"token": e4c0d0daaf2cc4ee2190a033957c1aa8c9eca9a5,
   >	"EEG": (FILE)
   >}
   >```
   >
   >
   >
   >- response (현재는 랜덤하게 성공 및 실패)
   >
   >```
   >{
   >    "detail": "인증 실패"
   >}
   >```

   
