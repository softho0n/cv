# QR Code & Barcode Detector
> 백신 패스가 도입되면서 혹시나 하는 마음에 비슷한 프로그램을 만들수 있을까 호기심이 생겨 제작하게 됨. `pyzbar`와 `zbar`의 라이브러리를 바탕으로 QR 코드 및 바코드를 인식하는 로직을 적용하였고, OpenCV를 통해 유저와 인터랙션 작용을 취한다.

### Prerequisite
* 당연히 `opencv-python`은 설치가 완료된 상태라고 가정함.
* 해당 파이썬 파일을 실행하기 위해선 두 가지 전제조건이 있는데, `zbar` 와 `pyzbar` 가 필요하다는 것이다.
  
    #### Mac OS X
    ```console
    brew install zbar
    ```
    #### Linux
    ```console
    sudo apt-get install libzbar0
    ```
    > `zbar` 설치가 완료 되었다면 Python wrapper 역할을 해주는 `pyzbar`를 최종으로 설치해준다.
    
    #### Python Wrapper
    ```console
    pip install pyzbar
    pip install pyzbar[scripts]
    ```

### Core Function ([`__decoder__`](https://github.com/softho0n/cv/blob/main/03-qr%26barcode.py#L11))
  ```python
  def __decoder__(self, frame):
        gray_img = cv2.cvtColor(frame, 0)
        code_info = decode(gray_img)

        for obj in code_info:
            points = obj.polygon
            (x,y,w,h) = obj.rect
            pts = np.array(points, np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(frame, [pts], True, (0, 255, 0), 3)

            barcodeData = obj.data.decode("utf-8")
            barcodeType = obj.type
            string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)
            
            cv2.putText(frame, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0), 2)
            print("Barcode: "+barcodeData +" | Type: "+barcodeType)
  ```
  * `pyzbar` 에 선언된 `decode` 함수를 호출하면 바코드에 대한 정보를 디코딩하게되고 영상의 위치 좌표 또한 알아낼 수 있다.
  * Full Code : https://github.com/softho0n/cv/blob/main/03-qr%26barcode.py#L11

### Execute
```console
foo@bar:~$ python3 03-qr&barcode.py
```

### Result
<p align="center"><img width="75%" src="https://github.com/softho0n/cv/blob/main/resources/qr%26barcode-result.gif"/></p>
