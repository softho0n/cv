# GrapCut
> `cv2.grapCut` 함수를 적용하면 Background, Foreground 두 가지 요소로 분리할 수 있음. 이를 바탕으로 배경과 객체를 분리하고 마우스 이벤트를 통해 최적의 객체를 찾아내는 프로그램임.

### GrapCut Function
  ```python
  cv2.grabCut(img, mask, rect, bgdModel, fgdModel, iterCount, mode=None)
         -> mask, bgdModel, fgdModel
  ```
  * `img` : 입력 영상
  * `mask` : 입출력 마스크
  * `rect` : ROI 영역
  * `bgdModel` : 임시 배경 모델 행렬
  * `fgdModel` : 임시 전경 모델 행렬
  * `iterCount` : 결과 생성까지의 반복 횟수
  * `mode` : 모드 상수

### Code
1. [`__init__`](https://github.com/softho0n/cv/blob/main/02-grapcut.py#L6) 
3. [`on_mouse`](https://github.com/softho0n/cv/blob/main/02-grapcut.py#L14)
4. [`execute`](https://github.com/softho0n/cv/blob/main/02-grapcut.py#L33)

### Execute
 
