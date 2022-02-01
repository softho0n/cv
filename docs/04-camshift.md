# CamShift
> Object Tracking을 CamShift Algorithm을 통해 실습해본다.

## What is CamShift & MeanShift?
refer it: https://docs.opencv.org/4.x/d7/d00/tutorial_meanshift.html

## CamShift API
  ```python
  cv2.CamShift(probImage, window, criteria) -> retval, window
  ```
  * `probImage` : 히스토그램 역투영 영상
  * `window` : 결과 영역
  * `criteria` : 알고리즘 종료 기준. 일반적으로, `term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)` 사용함.
  * `retval` : 추적 객체의 타원 정보

## Core Functions
1. [`selectROI`](https://github.com/softho0n/cv/blob/main/04-camshift.py#L21)
2. [`execute`](https://github.com/softho0n/cv/blob/main/04-camshift.py#L38)

## Execute
* `--videopath` 로 비디오 리소스에 대한 경로값을 전달해야함. Default 값은 None 이므로 설정하지 않을 경우 실행 안됨.
```console
foo@bar:~$ python3 04-camshift.py --videopath="path/to/video"
```

## Result
Try with your resource!
