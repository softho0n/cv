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
* `--imgpath`로 이미지 리소스에 대한 경로값을 전달해주어야 함.
* `cv2.EVENT_LBUTTONDOWN` : Background로 인지한 부분을 다시 Foreground로 업데이트함.
* `cv2.EVENT_RBUTTONDOWN` : Foreground로 인지한 부분을 다시 Background로 업데이트함.
```console
foo@bar:~$ python3 grapcut.py --imgpath="path/to/image"
```

### Result
<p align="center"><img width="55%" src="https://user-images.githubusercontent.com/42256738/147172877-e32a9739-48cc-42fd-9773-bb27618164c8.gif"/></p>
