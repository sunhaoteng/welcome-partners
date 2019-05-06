# 导入库
import cv2
# 打开摄像头
capture = cv2.VideoCapture(0)
# 加载人脸模型
face = cv2.CascadeClassifier('./facemodel.xml')
# 获取摄像头的实时画面
while True:
# 读取摄像头的当前这一帧的画面
    ret,image = capture.read()
# 对图片进行灰度处理
    gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
# 检查人脸
    faces = face.detectMultiScale(gray)
# 标记人脸
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x + w,y+h),(0,255,0),2)
# 显示图片
        cv2.imshow('Please look directly at the camera to get the face:',image)
# 暂停窗口
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
# 释放资源
capture.release()
# 销毁窗口
cv2.destroyAllWindows()