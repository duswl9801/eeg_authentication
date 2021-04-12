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

   

4. server/authenticate/make_model/ **(POST)**

   EEG 데이터를 받아서 모델을 만듭니다.

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
   >- response
   >
   >```
   >{
   >    "detail": "저장완료."
   >}
   >```

   
   
5. server/authenticate/check_user/ **(POST)**

   EEG 데이터를 받아서 해당 유저가 맞는지 검사합니다.

   > - request
   >
   > ```
   > {
   > 	"token": e4c0d0daaf2cc4ee2190a033957c1aa8c9eca9a5,
   > 	"EEG": (FILE)
   > }
   > ```
   >
   > 
   >
   > 
   >
   > - response 
   >
   >   - 인증 성공
   >
   >   ```
   >   {
   >       "전체 Test": 227,
   >       "맞은 Test": 207,
   >       "맞은 비율": 0.9118942731277533,
   >       "detail": "인증 성공"
   >   }
   >   ```
   >
   >   
   >
   >   - 인증 실패
   >
   >   ```
   >   {
   >       "전체 Test": 227,
   >       "맞은 Test": 116,
   >       "맞은 비율": 0.5110132158590308,
   >       "detail": "인증 실패"
   >   }
   >   ```
   >
   >   
