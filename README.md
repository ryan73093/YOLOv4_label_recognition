"# YOLOv4_label_recognition" 

# 訓練流程
#### 本次將介紹如何透過colab 和 YOLOv4簡單訓練一個辨識模型

step1:下載專案
---
1. 將專案下載至本機電腦
2. darknet資料夾架構如下
3. 原作者github:  https://github.com/AlexeyAB/darknet  

step2:蒐集訓練資料
---
1. 蒐集訓練圖片(自行蒐集)
2. 使用labelimg定義訓練標籤(產出標籤檔yolo.txt)
3. 使用labelimg產出classes.txt
4. 將訓練圖片存放於data/images
5. 將標籤檔存放於data/annotations
6. 將classes.txt附檔名修改為names，並存放於data

step3:切分訓練資料
---
1. 執行data_split.py

step4:修改cfg
---
1. 於cfg資料夾複製一份yolov4.cfg至相同位置，並命名為train.cfg
2. 手動變更以下資訊:
    * batch = 64
    * subdivisions = 16
    * max_batches = 6000
    * steps = 4800, 5400
    * width = 416
    * height = 416
    * 三個 [yolo] 區塊的 classes 改成需辨識的類別數量。可以用搜尋的比較不會遺漏 classes = 3
    * 三個 [yolo] 區塊的前一個 [convolution] 區塊的 filter 改成 (classes + 5) x 3 ，我們有 1 個類別所以是改為 18，記得有三個地方要修改 filters = 18


step5:建立data資料
---
1. 於data新增一個train.txt，並將副檔名修改為data
2. 於文件內編輯以下資料(記得修改物件類別數量n)
    classes=n 
    train=data/train/train.txt
    valid=data/dev/dev.txt
    names=data/classes.names
    backup=backup/
    
step6:上傳資料夾至google drive
---
至目前為止，資料準備工作大致已完成，將資料上傳後打開，透過colab打開train.ipynb開始訓練

step7:執行訓練與預測
---
1. 開啟train.ipynb，並逐步執行儲存格
2. 預測結果如下圖(序號與條碼馬賽克處理)


![](https://i.imgur.com/6XktWof.png)


##參考資料:  
https://mrhandbyhand.medium.com/hand-by-hand-train-your-yolov4-1-5f6a70618500  
https://mrhandbyhand.medium.com/hand-by-hand-train-your-yolov4-kaggle-dataset-ac1456e06604  
  
  
  
