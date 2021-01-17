# Git

> Git은 분산 버전 관리 시스템(DVCS)이다.
>
> 소스코드의 이력을 추적 & 관리한다. 개인 프로젝트 뿐만 아니라 협업 단계에서도 활용된다.



## 1. 준비

* 윈도우에서 git을 사용하기 위해서는 `git bash`를 설치한다.
* git을 활용하기 위해서 GUI 툴인 `source tree`, `github desktop` 등을 활용할 수도 있다.
* 초기 설치를 완료한 이후에 컴퓨터에 작성자(`author`) 정보를 등록한다.

```bash
# author 정보 등록
$ git config --global user.name {user name}
$ git config --global user.email {user email}

# author 정보 확인
$ git config --global --list
```



## 2. 로컬 저장소(Local Repository) 활용하기

### 2.1 저장소 초기화

```bash
$ git init 
```

* `.git`폴더가 생성되며, 이곳에 git 관련된 모든 정보가 저장된다.
* git bash에 `(master)`라고 표시된다. 이는 현재 `master`라는 branch에 있다는 뜻이다.



### 2.2 ` add`

현재 작업 공간(Working directory)에서 변경된 사항을 커밋으로 기록하기 위해서는 `(staging area)` 를 거쳐야 한다.

```bash
$ git add . # 현재 디렉토리
$ git add images/  # 특정 폴더
$ git add iu.jpg  # 특정 파일
```



### 2.3 `commit`

`commit`은 이력을 확정짓는 명령어다. 해당 시점의 스냅샷을 기록한다.

`commit`시에는 반드시 메시지를 작성 해야하며, 메시지는 변경사항을 알 수 있도록 명확하게 작성한다.

```bash
$ git commit -m "스타트캠프 소스코드 추가"
```

`commit` 이후에는 아래의 명령어를 통해 지금까지 작성된 이력을 확인한다.

```bash
$ git log
```

아래의 명령으를 통해 간편하게 볼 수 있다.

```bash
$ git log --oneline
```





## 3. 원격 저장소(Remote Repository) 활용하기

> 원격 저장소 기능을 제공하는 서비스에는 `Github`,`Gitlab`등이 있다.
>
> 우리는 그 중에서 가장 범용적으로 사용되는 `Github`을 활용한다.

### 3.1 준비

* Github에 새로운 Repository 생성



### 3.2 원격 저장소 등록 

```bash
$ git remote add {origin} {github url}

#[참고] 서로다른 원격 저장소를 사용하고 싶으면 이름을 다르게 연결시킨다.
$ git remote add gitbub {github url}
$ git remote add gitlab {gitlab url}

$ git push github master
$ git push gitlab master
```

* 원격 저장소(`remote`)로 `origin`이라는 이름을 가진 github url을 등록(`add`)한다.
* 등록된 원격 저장소 목록을 보기 위해선 아래 명령어를 입력한다.

``` bash
$ git remote -v
```



### 3.3 `Push`

```bash
$ git push origin master
```

* `origin`이라는 이름으로 설정된 원격 저장소에 `master` 브랜치를 업로드(`push`)
* 이후 변경사항이 생길때마다 `add` - `commit` -`push` 순으로 작업을 수행한다.



`status`, `log`, `remote -v` 틈틈히 체크하는 습관을 들이는 것 중요





*결과값을 같이 저장해보자 사진과 같은 것들로 기록 혹은 같이 뜨는 것들 같이 기록해 보자*  

