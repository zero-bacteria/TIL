# algorithm

> 알고리즘 문제정리



### 폴더구조

```
~/
	algorithm/
		0000_문제이름
			input.txt
			sol1.py
		0001_문제이름
			input.txt
			sol1.py
```



### pycharm

#### 터미널 설정 (git bash)

1. `settings` 열기

   - `ctrl` + `alt` + `s`

2. `terminal`검색

3. `Application settings` => `Shell path` => 폴더 아이콘 클릭!

   ![image-20210210100102005](README.assets/image-20210210100102005.png)

4. `C:\Program Files\Git\bin\bash.exe` 선택 (경로 주의!)

   ![image-20210210100200626](README.assets/image-20210210100200626.png)



#### 단축키

- `shift` + `Enter` : 아래줄에 새로운 라인 추가하면서 강제 이동
- `alt` + `ctrl` + `Enter` 윗줄에 새로운 라인 추가하면서 강제 이동
- `alt` + `shift` + :arrow_up: or :arrow_down: : 현재 라인 들고 이동
- `ctrl` + `shift` + `F10` : Run curren File
- `alt` + `F12` 터미널 열고닫기
- `ctrl` + `F4` 탭 닫기



#### 디버깅 

> 라인 숫자가 적힌 왼쪽부분에 break point를 찍어야 디버깅 가능

![image-20210210101027886](README.assets/image-20210210101027886.png)

1. Step Over(`F8`) : 함수는 건너 뛰면서 디버깅 진행
2. Step Into(`F7`) : 현재 실행되는 코드가 함수라면 함수 안으로 들어가면서 디버깅 진행
3. Run to Cursor(`Alt` + `F9`) : 커서를 누른 위치로 디버깅 진행 (for문이 100번 도는 경우 한번에 빠져나올때 사용)



### Tip

> 스크립트 파일로 sol.py 편하게 만들기. 코드입력은 vscode를 이용하여 입력해주세요

1. `~` 경로에 `sol.sh` 파일을 생성한다.

   - `touch ~/sol.sh`

2. `sol.sh` 파일에 아래의 내용을 입력한다.
   
   ```bash
   echo -e "import sys\\nsys.stdin = open(\"input.txt\")\n\nT = int(input())\n\n\nfor tc in range(1, T+1):\n    \n    print(\"#{} \".format(tc, ))\n" >> sol$1.py
   ```
   
3. `~` 경로에 `.bashrc` 파일을 열어서 아래의 내용을 추가한다. (없으면 생성)

   ```bash
   alias sol='~/sol.sh'
   ```

4. 터미널을 한번 껐다 킨다.

5. 파일을 만들고 싶은 위치로 이동 (ex. `cd 4831_전기버스`)

6. 아래의 명령어 입력

   ```bash
   # sol1.py 생성
   $ sol 1
   # sol2.py 생성
   $ sol 2
   ```

   