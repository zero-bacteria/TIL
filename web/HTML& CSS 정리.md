# HTML& CSS 정리

> 과목평가 대비 교재 참고 하여 간단하게 정리





## HTML

**Hyper Text Markup Language** 



참고 HTTP Hyper Text Transfer Protocol



**Hyper text** 기존의 선형적인 텍스트가 아닌 비선형적 텍스트, HyperLink를 통해 텍스트 이동



**Markup Language**

태그 등을 이용하여 문서나 데이터 구조를 명시하는 언어

프로그래밍 언어와는 다르게 단순하게 데이터를 표현하기만 한다.



* html 요소 : html 문서의 최상위 요소로써 문서의 `root`를 뜻한다.

  * head와 body 부분으로 구분된다.
  * head 문서제목, 문자코드와 같은 문서정보 담고 있음 브라우저에 표시 x  css선언 혹은 외부 로딩파일 지정
  * body 브라우저 화면에 나타나는 정보로 실제 내용에 해당

* DOM(Document Object Model) 트리 부모 관계, 형제 관계

* Element - 태그와 내용으로 이루어져 있음

  * 태그별로 사용할 수 있는 속성(attribute)은 다르다.
  * id, class ,sytle, title

* 시맨틱 태그

  | 종류 | header                  | nav        | aside                 | section              | article                  | footer      |
  | ---- | ----------------------- | ---------- | --------------------- | -------------------- | ------------------------ | ----------- |
  | 역할 | 문서 전체나 섹션의 헤더 | 네비게이션 | 사이드에 위치한 공간, | 컨텐츠의 그룹을 표현 | 독립적으로 구분되는 영역 | 마지막 부분 |

  * 의미있는 정보의 그룹으로 의미를 가지는 태그활용
  * non semantic - div,span
  * semantic - h1, table

* Block, Inline

  * 대부분의 요소는 같은 형태의 다른 요소를 안에 포함할 수 있습니다. (블록 요소 안에 블록 요소, 인라인 요소 안에 인라인 요소)
  * 대부분의 블록 요소는 다른 인라인 요소도 안에 포함할 수 있습니다.
  * 하지만, 인라인 요소는 블록 요소를 포함 할 수 없습니다.

* 태그의 종류

  * `<p>` 하나의 문단만들때 사용 block
  * `<hr>` 수평선 생성할때 사용 block
  * `<ol>`,`<ul>` 순서 있는/없는 리스트 생성 block
  * `<div>` 임의 block 요소
  * `<a>` 링크를 달때 inline
  * `<b>` 단순 프린트적인 강조의 의미 inline
  * `<strong>` 웹에서도 실제로 중요하다는 것을 알려주는 의미 inline
  * `<i>` b와 마찬가지로 단순 이탤릭 프린트 inline
  * `<em>` 시맨틱 태그적의미 strong과 비슷 inline
  * `<span>` 임의 inline 요소
  * `<img>` 이미지 태그는 inline 요소이다.
  * 그외 table 태그 form 태그
  * `<form>`
    * action 폼을 전송할 서버쪽 스크립트 파일 지정
    * method 서버에 전송할 http 메소드 지정
  * `<input>` - label로 해당값의 캡션, 유형에 따른 타입이 달라짐









## CSS

선택자, 선언, 속성 ,값



* css 정의 방법

  1. 인라인 (inline)
  2. 내부참조 ( embedding) - `<style>`
  3. 외부참조 - 분리된 css 파일

  







