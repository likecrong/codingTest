# Extracting activity from video data
- I rewrite the code I wrote when I was an intern at ETRI due to security issues.
- 한국전자통신연구원 인턴 당시 작성했던 코드를 보안상의 문제로 재작성합니다.
- I downloaded and used the video data from the free video site.
- 영상 데이터는 무료 영상사이트에서 다운받아 활용하였습니다.


```python
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, dump, ElementTree

xml_file = './path.xml'
doc = ET.parse(xml_file)
root = doc.getroot()
p = root.find("path").text
```

### Detail of data
- https://pixabay.com/ko/videos/search/
- I used a traceable video of the pig's movements.
- 돼지의 움직임이 추적가능한 영상을 사용하였습니다.


```python
from IPython.display import Image
```

![little2](https://user-images.githubusercontent.com/112467598/200104783-b36586a0-a236-46aa-9a5d-72aeccd91891.gif)

## 1. dense optical flow by Farneback method
- https://www.geeksforgeeks.org/opencv-the-gunnar-farneback-optical-flow/
- Optical flow is known as the pattern of apparent motion of objects, i.e, it is the motion of objects between every two consecutive frames of the sequence, which is caused by the movement of the object being captured or the camera capturing it.
- 영상 데이터 내 추적되는 물체의 움직임으로 인해 발생하는 과정 중 두 연속된 프레임 사이의 물체의 움직임을 관찰한다.


```python
import cv2
import numpy as np

def start(filePath):
    '''
    입력변수: 영상데이터 파일경로
    영상을 2초씩 이동하며 두 프레임에 대한 dense optical flow를 연산하는 함수
    '''
    
    sig=False #첫 번째 영상프레임을 구분하는 변수
    second = 0 #현재 영상 재생 위치 변수
    increase_width=2 #영상 이동 단위 변수
    
    #영상 프레임 불러오기 위한 변수 설정
    capture = cv2.VideoCapture(filePath)
    
    #처리된 영상을 저장하기 위해 필요한 변수 설정
    width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print("재생할 파일 넓이, 높이 : %d, %d"%(width, height))
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter(p+'/output01.mp4', fourcc, increase_width, (int(width), int(height)))
    
    #dense optical flow의 움직임을 관찰하기 위한 mask 설정
    run, frame = capture.read()
    mask = np.zeros_like(frame)  
    mask[..., 1] = 255
    
    #영상 재생부
    while capture.isOpened():
        
        #영상 프레임 불러오기
        run, frame = capture.read()
        
        #영상 재생이 불가하면
        if not run: 
            print("[프레임 수신 불가] - 종료합니다")
            break #종료
        
        #컬러 설정
        first_frame = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
        #흑백 설정
        fgmask = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
        
        if sig==False: # 두 연속된 프레임을 관찰하기 위해 첫번째 프레임인지 확인
            sig=True
            
        else: #두번째 프레임부터
      
            # Calculates dense optical flow by Farneback method
            flow = cv2.calcOpticalFlowFarneback(prevfgmask, fgmask, 
                                               None,
                                               0.5, 3, 15, 3, 5, 1.2, 0)

            # Computes the magnitude and angle of the 2D vectors
            magnitude, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])

            # Sets image hue according to the optical flow 
            # direction
            mask[..., 0] = angle * 180 / np.pi / 2

            # Sets image value according to the optical flow
            # magnitude (normalized)
            mask[..., 2] = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)

            # Converts HSV to RGB (BGR) color representation
            rgb = cv2.cvtColor(mask, cv2.COLOR_HSV2BGR)            

            # Opens a new window and displays the output frame
            cv2.imshow("dense optical flow", rgb)
            out.write(rgb) #재생되는 영상 저장
      
        #이전 프레임 업데이트
        prevfgmask = fgmask
                
        #사용자가 영상재생을 중단할 때
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
        
        second += increase_width  # 다음 초로 연산
        capture.set(cv2.CAP_PROP_POS_MSEC, second * 1000)  # 영상 시간 이동

    #영상 종료
    capture.release()
    cv2.destroyAllWindows()
```


```python
#파일경로 입력
start(p+'/exampleOfPigMovement3.mp4')
```

    재생할 파일 넓이, 높이 : 1280, 720
    [프레임 수신 불가] - 종료합니다
    

### RESULT

![output01](https://user-images.githubusercontent.com/112467598/200104150-8c8485d0-a419-4977-85a5-f70000161c18.gif)

- It recognizes the borders of objects, but it is difficult to track the entire object. 
- 객체의 테두리를 인식하지만 전체 객체에 대한 추적이 어렵다.
- I needed to find the way which tracks the entire object.
- 새로운 영상처리 기법을 도입해 전체 객체에 대한 추적이 필요하다.

## 2. Removing background + dense optical flow by Farneback method
- the dense optical flow is applied after removing the background excluding the object from the video data.
- 영상 데이터로부터 객체를 제외한 배경을 제거한 뒤 dense optical flow를 적용한다.
- https://www.geeksforgeeks.org/opencv-the-gunnar-farneback-optical-flow/
- Optical flow is known as the pattern of apparent motion of objects, i.e, it is the motion of objects between every two consecutive frames of the sequence, which is caused by the movement of the object being captured or the camera capturing it.
- 영상 데이터 내 추적되는 물체의 움직임으로 인해 발생하는 과정 중 두 연속된 프레임 사이의 물체의 움직임을 관찰한다.


```python
import cv2
import numpy as np

def startNoBackground(filePath):
    '''
    입력변수: 영상데이터 파일경로
    영상을 2초씩 이동하며 두 프레임에 대한 dense optical flow를 연산하는 함수
    '''
    
    sig=False #첫 번째 영상프레임을 구분하는 변수
    second = 0 #현재 영상 재생 위치 변수
    increase_width=2 #영상 이동 단위 변수
    
    #영상 프레임 불러오기 위한 변수 설정
    capture = cv2.VideoCapture(filePath)
    
    #처리된 영상을 저장하기 위해 필요한 변수 설정
    width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print("재생할 파일 넓이, 높이 : %d, %d"%(width, height))
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter(p+'/output02.mp4', fourcc, increase_width, (int(width), int(height)))
    
    #돼지를 제외한 배경 제거를 위한 변수 설정
    fgbg = cv2.createBackgroundSubtractorMOG2()
    
    #dense optical flow의 움직임을 관찰하기 위한 mask 설정
    run, frame = capture.read()
    mask = np.zeros_like(frame)  
    mask[..., 1] = 255
    
    #영상 재생부
    while capture.isOpened():
        
        #영상 프레임 불러오기
        run, frame = capture.read()
        
        #영상 재생이 불가하면
        if not run: 
            print("[프레임 수신 불가] - 종료합니다")
            break #종료
        
        #컬러 설정
        first_frame = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
        #흑백 설정
        prev_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
        
        #배경 제거 하기
        fgmask = fgbg.apply(prev_gray)
        
        if sig==False: # 두 연속된 프레임을 관찰하기 위해 첫번째 프레임인지 확인
            sig=True
            
        else: #두번째 프레임부터

            # Calculates dense optical flow by Farneback method
            flow = cv2.calcOpticalFlowFarneback(prevfgmask, fgmask, 
                                               None,
                                               0.5, 3, 15, 3, 5, 1.2, 0)

            # Computes the magnitude and angle of the 2D vectors
            magnitude, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])

            # Sets image hue according to the optical flow 
            # direction
            mask[..., 0] = angle * 180 / np.pi / 2

            # Sets image value according to the optical flow
            # magnitude (normalized)
            mask[..., 2] = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)

            # Converts HSV to RGB (BGR) color representation
            rgb = cv2.cvtColor(mask, cv2.COLOR_HSV2BGR)
            
            # Opens a new window and displays the output frame
            cv2.imshow("dense optical flow", rgb)
            out.write(rgb)
      
        #이전 프레임 업데이트
        prevfgmask = fgmask
                
        #사용자가 영상재생을 중단할 때
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
        
        second += increase_width  # 다음 초로 연산
        capture.set(cv2.CAP_PROP_POS_MSEC, second * 1000)  # 영상 시간 이동

    #영상 종료
    capture.release()
    cv2.destroyAllWindows()
```


```python
#파일경로 입력
startNoBackground(p+'/exampleOfPigMovement3.mp4')
```

    재생할 파일 넓이, 높이 : 1280, 720
    [프레임 수신 불가] - 종료합니다
    

### RESULT

![output02](https://user-images.githubusercontent.com/112467598/200104181-ec700082-2987-433c-88b6-b13b86f0e92b.gif)

- applying a background-removing code makes it possible to trace the entire object with compared to previous data. 
- 이전 데이터와 비교했을 때, 배경을 제거하는 코드를 적용하면 전체 객체에 대한 추척이 가능해졌다.
- I decided to use this method to track the motion of the object.
- 해당 방법을 최종적으로 이용하여 객체의 움직임을 추적하기로 결정했다.

## 3. Making a DataFrame
- It was consisted of avi and smi files when I used before.
- 회사에서 사용한 영상데이터는 avi와 smi 파일 형식으로 구성되어 있었다.
- The smi file contained the date and time when the video was filmed.
- smi파일에 영상이 촬영된 날짜와 시간에 대한 내용이 담겨있었다.
- The 'increase_width' was set to 2 in the rewritten code, but It set 5 before.
- 재작성한 코드에서 increase_width를 2로 설정하였지만, 회사에서는 5로 설정하였다.

### Result of dataframe

![df](https://user-images.githubusercontent.com/112467598/200104222-c7f1eff2-4e88-4b7a-8426-d4844d2d2f74.jpg)

- variables: Date, result
- Date: The date and time are included. The activity was tracked every 5 seconds by setting the increment_width to 5.
- result: The average value of the magnitude. Missing values are filled with zero.  
### 
- 데이터 프레임 변수: Date, result
- Date: 날짜와 시간이 담겼다. increase_width를 5로 설정하여 5초 마다 활동성을 추적하였다.
- result: magnitude의 평균값이다. 결측치는 0으로 채워넣었다.

### The reason of choosing magnitude, not direction
- The direction was not important to track activity, but how much movement was more important.
- 활동성을 추적하는 데 방향이 중요한 것이 아닌 얼마만큼 움직였는지가 더 중요하다고 판단했다.

### Next
- I will do the data preprocessing using this data frame.
- 해당 데이터 프레임을 활용하여 데이터 전처리를 진행한다.


```python

```
